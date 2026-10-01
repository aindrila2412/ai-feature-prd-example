# Prioritisation with RICE (FICTIONAL SAMPLE)

> Fictional backlog and invented inputs. RICE gives a structured conversation, not an answer. Treat every input as an estimate to challenge.

RICE score = (Reach x Impact x Confidence) / Effort

| Factor | Definition used here |
|---|---|
| Reach | People affected per quarter (estimate) |
| Impact | 0.25 minimal, 0.5 low, 1 medium, 2 high, 3 massive |
| Confidence | How sure we are of the other inputs (percentage) |
| Effort | Person-months (estimate) |

## Backlog and scores

The inputs are in [`data/rice_backlog.csv`](../data/rice_backlog.csv). Generate the ranked table with:

```bash
python scripts/rice.py
```

The output is written to [`output/rice_ranked.md`](../output/rice_ranked.md).

## Reading the result

RICE informs order but does not override dependencies. In this sample, the content audit (F-02) and review screen (F-01) are sequenced first because other items depend on them or because a release is unsafe without them, even where another item scores higher.

## Caveats

- Scores are only as good as their inputs; here they are invented.
- Reach and impact estimates should come from data when available.
- A low score does not always mean "no": compliance or risk items may be required regardless.
- Re-score when new information arrives. Include a sensitivity check (change confidence and see if the order flips).
