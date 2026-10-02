# AI Feature PRD Example

This is a practice project. I wanted to write a full set of product docs for an AI feature, so I made one up: a
community platform called "CommunityHub" with a "Suggested Answers" feature. The product, the personas, the numbers,
the targets and the timelines are all invented. This isn't client or employer work, and it doesn't claim any real
results or experience.

The docs are in `docs/` and are meant to be read in order: a PRD, a Now/Next/Later roadmap, RICE prioritisation, user
stories with acceptance criteria, metrics and OKRs, risks and dependencies, and an evaluation plan.

I also added a couple of learning notes on LLMs and agentic AI in `learning-notes/`. They're notes from my own
learning and not expert advice. There's a tiny rule-based "agent" there too (`mock_agent.py`). It uses keyword matching
only, so there's no model and no API key involved.

## Running the code

The RICE script scores the fictional backlog in `data/rice_backlog.csv` and writes `output/rice_ranked.md`. It only
uses the standard library.

```bash
python scripts/rice.py
python learning-notes/mock_agent.py
```

Python 3.9 or newer is fine and there's nothing to install.

If you want to reuse the structure, copy the docs and swap in your own feature.

## Honest notes

Everything is a hypothesis. There was no user research and there are no baselines or results, so the RICE scores are
my guesses. The mock agent is a toy and not a real agent framework. Next I'd like to write the evaluation plan against
a real (small) dataset instead of an imagined one.

## Licence

MIT, see [LICENSE](LICENSE).
