#!/usr/bin/env python3
"""A tiny rule-based "agent loop" for learning purposes. No model, no API keys.

It mimics the shape of an agent: observe -> decide -> act (tool) -> observe,
with a step limit, a log, and a "no answer" path. The "retrieval" is plain
keyword overlap over a small FICTIONAL help-centre list.

Run:
    python learning-notes/mock_agent.py
"""
import re

HELP_CENTRE = {  # fictional articles
    "join-channel": "To join a channel, open the channel list and press Join.",
    "find-events": "Events are listed on the Events page, sorted by date.",
    "report-problem": "To report a problem, use the Report button; a human moderator will review it.",
}
CONDUCT_WORDS = {"harass", "harassment", "abuse", "threat"}
STOP_WORDS = {"how", "do", "i", "to", "the", "a", "where", "is", "are", "can", "my", "on"}
MAX_STEPS = 4


def tokens(text: str) -> set[str]:
    return {w for w in re.findall(r"[a-z]+", text.lower()) if w not in STOP_WORDS}


def tool_search(question: str):
    """Tool: return (article_id, overlap) of the best keyword match, or (None, 0)."""
    q = tokens(question)
    best, score = None, 0
    for art_id, body in HELP_CENTRE.items():
        s = len(q & (tokens(body) | tokens(art_id.replace("-", " "))))
        if s > score:
            best, score = art_id, s
    return best, score


def run_agent(question: str, verbose: bool = True) -> dict:
    log, state = [], {"question": question, "hit": None, "result": None}

    def step(msg):
        log.append(msg)
        if verbose:
            print(f"  [{len(log)}] {msg}")

    for _ in range(MAX_STEPS):
        # decide
        if tokens(question) & CONDUCT_WORDS:
            step("decide: conduct-related -> hand off to a human (no draft)")
            state["result"] = "ESCALATE_TO_HUMAN"
            break
        if state["hit"] is None:
            step("decide: need information -> call tool_search")
            art, score = tool_search(question)
            state["hit"] = (art, score)  # observe
            step(f"observe: best match={art}, overlap={score}")
            continue
        art, score = state["hit"]
        if art is None or score < 2:
            step("decide: weak or no match -> 'No suggestion'")
            state["result"] = "NO_SUGGESTION"
        else:
            step(f"decide: draft from [{art}] for moderator approval")
            state["result"] = f"DRAFT: {HELP_CENTRE[art]} (source: {art})"
        break
    else:
        state["result"] = "STOPPED_STEP_LIMIT"
    return {"question": question, "result": state["result"], "steps": len(log)}


# A tiny test set, the same idea as the evaluation plan (expected outcome per question).
TEST_SET = [
    ("How do I join a channel?", "DRAFT", "join-channel"),
    ("Where are events listed?", "DRAFT", "find-events"),
    ("Someone is sending me abuse", "ESCALATE_TO_HUMAN", None),
    ("What is the weather on Mars?", "NO_SUGGESTION", None),
]


def main() -> None:
    passed = 0
    for q, expected, source in TEST_SET:
        print(f"Q: {q}")
        out = run_agent(q)
        ok = out["result"].startswith(expected) and (source is None or f"source: {source}" in out["result"])
        passed += ok
        print(f"  -> {out['result']}  [{'PASS' if ok else 'FAIL'}]\n")
    print(f"{passed}/{len(TEST_SET)} test cases passed")
    raise SystemExit(0 if passed == len(TEST_SET) else 1)


if __name__ == "__main__":
    main()
