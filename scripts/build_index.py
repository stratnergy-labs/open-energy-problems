#!/usr/bin/env python3
from __future__ import annotations

import csv
import json
import subprocess
import sys
from pathlib import Path

from frontmatter_lib import iter_markdown, parse_markdown, scalar_for_csv

ROOT = Path(__file__).resolve().parents[1]


def run_validation() -> None:
    result = subprocess.run([sys.executable, str(ROOT / "scripts" / "validate_frontmatter.py")], cwd=ROOT)
    if result.returncode != 0:
        raise SystemExit(result.returncode)


def load_cards(directory: str) -> list[dict]:
    cards = []
    for path in iter_markdown(ROOT / directory):
        data, body = parse_markdown(path)
        cards.append({**data, "path": str(path.relative_to(ROOT)), "body": body.strip()})
    return sorted(cards, key=lambda item: item["id"])


def write_json(path: Path, rows: list[dict]) -> None:
    path.write_text(json.dumps(rows, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def write_csv(path: Path, rows: list[dict]) -> None:
    if not rows:
        path.write_text("", encoding="utf-8")
        return
    fieldnames = sorted({key for row in rows for key in row if key != "body"})
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, lineterminator="\n")
        writer.writeheader()
        for row in rows:
            writer.writerow({field: scalar_for_csv(row.get(field)) for field in fieldnames})


def mirror_site_data(problems: list[dict], contributions: list[dict]) -> None:
    data_dir = ROOT / "docs" / "data"
    if not data_dir.exists():
        return
    write_json(data_dir / "problems.json", problems)
    write_json(data_dir / "contributions.json", contributions)


def main() -> int:
    run_validation()
    index_dir = ROOT / "index"
    index_dir.mkdir(exist_ok=True)
    problems = load_cards("problems")
    contributions = load_cards("contributions")
    write_json(index_dir / "problems.json", problems)
    write_json(index_dir / "contributions.json", contributions)
    write_json(index_dir / "artefacts.json", contributions)
    write_json(index_dir / "projects.json", contributions)
    write_json(index_dir / "ai_attempts.json", [])
    write_csv(index_dir / "problems.csv", problems)
    write_csv(index_dir / "contributions.csv", contributions)
    write_csv(index_dir / "artefacts.csv", contributions)
    write_csv(index_dir / "projects.csv", contributions)
    mirror_site_data(problems, contributions)
    print(f"Wrote {len(problems)} problems and {len(contributions)} contributions to index/.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
