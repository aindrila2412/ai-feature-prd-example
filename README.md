# AI Feature PRD Example

A personal practice portfolio piece: a complete product-management document set for a **fictional** AI-assisted feature, plus concise learning notes on LLMs and agentic AI.

> **Personal practice project. Fictional product and sample data only.**
> "CommunityHub" and its "Suggested Answers" feature are invented. All personas, numbers, targets, and timelines are illustrative hypotheses. This is not client or employer work, and it does not claim any real product outcomes or experience. The AI notes are learning notes, not expert guidance.

## Purpose

To show how I structure product thinking for an AI feature: problem framing, PRD, roadmap, RICE prioritisation, user stories with acceptance criteria, metrics and OKRs, risks, and an evaluation plan.

## Structure

```text
ai-feature-prd-example/
├── README.md
├── LICENSE
├── .gitignore
├── .markdownlint.json
├── .github/workflows/ci.yml
├── docs/
│   ├── 01-prd.md
│   ├── 02-roadmap.md                       # Now / Next / Later
│   ├── 03-prioritization-rice.md
│   ├── 04-user-stories-acceptance-criteria.md
│   ├── 05-metrics-and-okrs.md
│   ├── 06-risks-and-dependencies.md
│   └── 07-evaluation-plan.md
├── data/rice_backlog.csv                   # FICTIONAL inputs
├── scripts/rice.py                         # RICE scoring (standard library only)
├── output/rice_ranked.md                   # generated from the sample data
└── learning-notes/
    ├── llm-concepts.md                     # prompting, tool use, RAG, evaluation, risks
    └── mock_agent.py                       # rule-based agent loop; no model, no API keys
```

## How to use it

- Read the docs in numeric order, starting with the [PRD](docs/01-prd.md).
- Copy the structure for your own feature and replace the fictional content.
- Re-run the scoring after editing the backlog:

```bash
python scripts/rice.py
```

- Run the learning example (Python 3.9+, nothing to install):

```bash
python learning-notes/mock_agent.py
```

## Limitations

- Everything is hypothetical: no research, baselines, or results exist.
- The mock agent uses keyword matching and is not a real model or a real agent framework.

## Licence

MIT. See [LICENSE](LICENSE).
