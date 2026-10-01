# Evaluation Plan (FICTIONAL SAMPLE)

> How the team would judge draft quality before and during a beta. Fictional; no results exist.

## Offline evaluation (before any member sees a draft)

1. Build a small **test set** of realistic questions with a known correct source article.
2. For each question, record: was the right article retrieved? Was the draft faithful to it? Was "no suggestion" correctly shown when no source exists?
3. Have two reviewers score drafts on a simple rubric and compare scores to catch inconsistency.

| Criterion | Question | Scale |
|---|---|---|
| Correctness | Is the answer right according to the source? | Pass / Fail |
| Groundedness | Does every claim appear in the cited source? | Pass / Fail |
| Tone | Is it polite and in line with the community voice? | 1 to 3 |
| Safety | Does it avoid advice outside scope? | Pass / Fail |

## Shadow mode

Moderators see drafts but do not post them. Compare the draft to what they would have said.

## Beta monitoring

Weekly review of acceptance, edit, reject, and flag counts, plus a manual sample of approved drafts.

## Stop conditions (examples)

- Any draft posted without approval
- Any privacy incident
- A cluster of flagged drafts on the same topic (pause that topic)

The small [mock agent](../learning-notes/mock_agent.py) in `learning-notes/` shows the idea of a test set in a few lines of runnable code.
