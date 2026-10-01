#!/usr/bin/env python3
"""Compute RICE scores from a CSV and write a ranked Markdown table.

SAMPLE DATA ONLY by default. Standard library only (no installs needed).

Usage:
    python scripts/rice.py
    python scripts/rice.py --input data/rice_backlog.csv --output output/rice_ranked.md
"""
import argparse
import csv
from pathlib import Path


def rice(reach: float, impact: float, confidence_pct: float, effort: float) -> float:
    if effort <= 0:
        raise ValueError("effort must be greater than 0")
    return reach * impact * (confidence_pct / 100.0) / effort


def load(path: Path) -> list[dict]:
    rows = []
    with path.open(newline="", encoding="utf-8") as f:
        for r in csv.DictReader(f):
            r["score"] = rice(
                float(r["reach_per_quarter"]),
                float(r["impact"]),
                float(r["confidence_pct"]),
                float(r["effort_person_months"]),
            )
            rows.append(r)
    return sorted(rows, key=lambda r: r["score"], reverse=True)


def to_markdown(rows: list[dict]) -> str:
    out = [
        "# RICE ranking",
        "",
        "> Sample data only. Inputs are fictional estimates.",
        "",
        "| Rank | ID | Item | Reach | Impact | Confidence | Effort (pm) | RICE score |",
        "|---|---|---|---|---|---|---|---|",
    ]
    for i, r in enumerate(rows, 1):
        out.append(
            f"| {i} | {r['id']} | {r['item']} | {r['reach_per_quarter']} | {r['impact']} | "
            f"{r['confidence_pct']}% | {r['effort_person_months']} | {r['score']:.1f} |"
        )
    out += ["", "Score = (Reach x Impact x Confidence) / Effort.", ""]
    return "\n".join(out)


def main() -> None:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--input", default="data/rice_backlog.csv")
    p.add_argument("--output", default="output/rice_ranked.md")
    a = p.parse_args()
    rows = load(Path(a.input))
    out = Path(a.output)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(to_markdown(rows), encoding="utf-8")
    print(f"Scored {len(rows)} items -> {out}")
    for r in rows[:3]:
        print(f"  {r['id']} {r['score']:.1f}  {r['item']}")


if __name__ == "__main__":
    main()
