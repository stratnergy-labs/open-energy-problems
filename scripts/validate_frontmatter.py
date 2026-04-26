#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path
import sys

from frontmatter_lib import iter_markdown, parse_markdown, require_fields

ROOT = Path(__file__).resolve().parents[1]

PROBLEM_REQUIRED = [
    "id", "title", "lane", "status", "openness_level", "evidence_strength",
    "geography", "asset_class", "market_scope", "ai_relevance",
    "market_integrity_risk", "last_updated", "maintainer", "related_contributions",
]
CONTRIBUTION_REQUIRED = [
    "id", "problem_id", "title", "type", "openness_level", "evidence_strength",
    "maturity", "ai_relevance", "review_status", "last_checked",
]
RELATIONSHIP_REQUIRED = [
    "id", "source_id", "target_id", "relationship_type", "review_status",
    "evidence_strength", "last_checked",
]

VALID_EVIDENCE = {"A", "B", "C", "D", "E"}
VALID_RELEVANCE = {"low", "medium", "high"}
VALID_RISK = {"low", "medium", "high"}
VALID_RELATIONSHIP_TYPES = {
    "uses_component",
    "uses_data_source",
    "wraps_project",
    "extends_project",
    "documents_api",
    "shared_data_source",
    "shared_standard",
    "same_problem_context",
    "alternative_implementation",
    "integration_candidate",
}


def validate_problem(path: Path, data: dict) -> list[str]:
    errors = require_fields(path, data, PROBLEM_REQUIRED)
    if data.get("evidence_strength") not in VALID_EVIDENCE:
        errors.append(f"{path}: evidence_strength must be A-E")
    if data.get("ai_relevance") not in VALID_RELEVANCE:
        errors.append(f"{path}: ai_relevance must be low, medium, or high")
    if data.get("market_integrity_risk") not in VALID_RISK:
        errors.append(f"{path}: market_integrity_risk must be low, medium, or high")
    openness = data.get("openness_level")
    if not isinstance(openness, int) or not 0 <= openness <= 6:
        errors.append(f"{path}: openness_level must be integer 0-6")
    for list_field in ("asset_class", "market_scope", "related_contributions"):
        if list_field in data and not isinstance(data[list_field], list):
            errors.append(f"{path}: {list_field} must be a list")
    if data.get("id") == "EP-001" and data.get("status") != "SOLVED_FOR_SCOPE":
        errors.append(f"{path}: EP-001 should remain SOLVED_FOR_SCOPE for v0.1 scope")
    if data.get("status") == "SOLVED" or data.get("status") == "FULLY_SOLVED":
        errors.append(f"{path}: do not use fully solved statuses")
    return errors


def validate_contribution(path: Path, data: dict) -> list[str]:
    errors = require_fields(path, data, CONTRIBUTION_REQUIRED)
    openness = data.get("openness_level")
    if not isinstance(openness, int) or not 0 <= openness <= 6:
        errors.append(f"{path}: openness_level must be integer 0-6")
    if data.get("evidence_strength") not in VALID_EVIDENCE:
        errors.append(f"{path}: evidence_strength must be A-E")
    if data.get("ai_relevance") not in VALID_RELEVANCE:
        errors.append(f"{path}: ai_relevance must be low, medium, or high")
    return errors


def validate_relationship(path: Path, data: dict) -> list[str]:
    errors = require_fields(path, data, RELATIONSHIP_REQUIRED)
    if data.get("evidence_strength") not in VALID_EVIDENCE:
        errors.append(f"{path}: evidence_strength must be A-E")
    if data.get("relationship_type") not in VALID_RELATIONSHIP_TYPES:
        errors.append(f"{path}: relationship_type is not recognized")
    if data.get("source_id") == data.get("target_id"):
        errors.append(f"{path}: source_id and target_id must differ")
    return errors


def main() -> int:
    errors: list[str] = []
    problem_ids: set[str] = set()
    contribution_ids: set[str] = set()
    relationship_ids: set[str] = set()
    problem_related: dict[str, list[str]] = {}

    for path in iter_markdown(ROOT / "problems"):
        data, _ = parse_markdown(path)
        errors.extend(validate_problem(path, data))
        problem_related[data.get("id")] = data.get("related_contributions", [])
        if data.get("id") in problem_ids:
            errors.append(f"{path}: duplicate problem id {data.get('id')}")
        problem_ids.add(data.get("id"))

    for path in iter_markdown(ROOT / "contributions"):
        data, _ = parse_markdown(path)
        errors.extend(validate_contribution(path, data))
        if data.get("id") in contribution_ids:
            errors.append(f"{path}: duplicate contribution id {data.get('id')}")
        contribution_ids.add(data.get("id"))

    for path in iter_markdown(ROOT / "contributions"):
        data, _ = parse_markdown(path)
        if data.get("problem_id") not in problem_ids:
            errors.append(f"{path}: unknown problem_id {data.get('problem_id')}")

    relationships_root = ROOT / "relationships"
    if relationships_root.exists():
        for path in iter_markdown(relationships_root):
            data, _ = parse_markdown(path)
            errors.extend(validate_relationship(path, data))
            if data.get("id") in relationship_ids:
                errors.append(f"{path}: duplicate relationship id {data.get('id')}")
            relationship_ids.add(data.get("id"))
            for field in ("source_id", "target_id"):
                if data.get(field) not in contribution_ids:
                    errors.append(f"{path}: unknown {field} {data.get(field)}")

    for problem_id, related_ids in problem_related.items():
        for contribution_id in related_ids:
            if contribution_id not in contribution_ids:
                errors.append(f"{problem_id}: unknown related_contribution {contribution_id}")

    if errors:
        print("Front matter validation failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1
    print(
        f"Validated {len(problem_ids)} problems, "
        f"{len(contribution_ids)} contributions, and "
        f"{len(relationship_ids)} relationships."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
