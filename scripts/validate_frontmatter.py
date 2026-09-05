#!/usr/bin/env python3
"""Validate card front matter and enforce the register's status rules.

Status is derived from evidence, not asserted. A problem can only carry a
green status when at least one linked reference has passed source and
licence review. See index/status_definitions.md for the rules in prose.
"""
from __future__ import annotations

from collections import Counter
from pathlib import Path
import sys

from frontmatter_lib import iter_markdown, parse_markdown, require_fields

ROOT = Path(__file__).resolve().parents[1]

PROBLEM_REQUIRED = [
    "id", "title", "lane", "status", "openness_level", "evidence_strength",
    "geography", "asset_class", "market_scope", "ai_relevance",
    "market_integrity_risk", "last_updated", "maintainer", "card_completeness",
    "related_contributions",
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
EVIDENCE_RANK = {"A": 5, "B": 4, "C": 3, "D": 2, "E": 1}
VALID_RELEVANCE = {"low", "medium", "high"}
VALID_RISK = {"low", "medium", "high"}
VALID_STATUS = {
    "OPEN",
    "CANDIDATE_REFERENCE",
    "PARTIAL",
    "PUBLIC_DISCLOSURE",
    "REFERENCE_AVAILABLE",
    "SOLVED_FOR_SCOPE",
    "SUPERSEDED",
    "BLOCKED",
    "NEEDS_REVIEW",
    "REJECTED_OUT_OF_SCOPE",
}
GREEN_STATUS = {"REFERENCE_AVAILABLE", "SOLVED_FOR_SCOPE"}
VALID_LANES = {
    "market-benchmarks",
    "forecasting",
    "trading-logic",
    "virtualisation",
    "market-simulation",
    "grid-stress",
    "demand-response",
    "open-data",
    "terminology",
    "computational-infrastructure",
    "ai-assisted-analysis",
}
VALID_COMPLETENESS = {"stub", "draft", "complete"}
COMPLETE_SECTIONS = ("## Definition Of Done", "## Baseline")
VALID_REVIEW_STATUS = {"needs_review", "accepted", "rejected"}
VALID_CONTRIBUTION_TYPES = {
    "AI_ASSISTED_ANALYSIS",
    "BENCHMARK",
    "DATASET",
    "MCP_CONNECTOR",
    "METHODOLOGY",
    "INVENTORY",
    "PARTIAL_PROGRESS",
    "PUBLIC_DISCLOSURE",
    "REFERENCE_SOLUTION",
    "SCHEMA",
    "SOFTWARE_INFRASTRUCTURE",
    "SIMULATOR",
}
VALID_MATURITY = {"NEEDS_REVIEW", "PARTIAL", "PUBLIC_DISCLOSURE", "REFERENCE_AVAILABLE"}
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


def has_source(card: dict) -> bool:
    return bool(card.get("repository_url") or card.get("project_url"))


def has_licence(card: dict) -> bool:
    return bool(card.get("license_code") or card.get("license_data"))


def is_accepted_reference(card: dict) -> bool:
    return card.get("review_status") == "accepted" and has_source(card) and has_licence(card)


def validate_problem(path: Path, data: dict, body: str) -> list[str]:
    errors = require_fields(path, data, PROBLEM_REQUIRED)
    if data.get("status") not in VALID_STATUS:
        errors.append(f"{path}: status `{data.get('status')}` is not defined in index/status_definitions.md")
    if data.get("status") in {"SOLVED", "FULLY_SOLVED"}:
        errors.append(f"{path}: do not use fully solved statuses")
    if data.get("lane") not in VALID_LANES:
        errors.append(f"{path}: lane `{data.get('lane')}` has no lanes/ note")
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
    completeness = data.get("card_completeness")
    if completeness not in VALID_COMPLETENESS:
        errors.append(f"{path}: card_completeness must be stub, draft, or complete")
    has_sections = all(section in body for section in COMPLETE_SECTIONS)
    if completeness == "complete" and not has_sections:
        errors.append(f"{path}: a complete card needs `## Definition Of Done` and `## Baseline` sections")
    if completeness == "stub" and has_sections:
        errors.append(f"{path}: card has a definition of done and a baseline; it is not a stub")
    return errors


def validate_problem_status(problem: dict, contributions: dict[str, dict], problem_ids: set[str]) -> list[str]:
    """Status rules: a status may only claim what the linked references support."""
    errors: list[str] = []
    pid = problem.get("id")
    status = problem.get("status")
    related = [contributions[cid] for cid in problem.get("related_contributions", []) if cid in contributions]
    accepted = [card for card in related if is_accepted_reference(card)]

    if status in GREEN_STATUS and not accepted:
        errors.append(
            f"{pid}: status {status} requires at least one related contribution with "
            "review_status accepted, a source URL, and a licence; none qualifies"
        )
    if status == "OPEN" and related:
        errors.append(f"{pid}: OPEN means no reference is listed; use CANDIDATE_REFERENCE or PARTIAL")
    if status in {"CANDIDATE_REFERENCE", "PARTIAL"} and not related:
        errors.append(f"{pid}: status {status} requires at least one related contribution")
    if status == "PUBLIC_DISCLOSURE" and not any(card.get("type") == "PUBLIC_DISCLOSURE" for card in related):
        errors.append(f"{pid}: status PUBLIC_DISCLOSURE requires a related contribution of type PUBLIC_DISCLOSURE")
    if status == "SUPERSEDED":
        target = problem.get("superseded_by")
        if target not in problem_ids or target == pid:
            errors.append(f"{pid}: SUPERSEDED requires `superseded_by` naming another existing problem")

    max_openness = max((card.get("openness_level", 0) for card in related), default=0)
    if isinstance(problem.get("openness_level"), int) and problem["openness_level"] > max_openness:
        errors.append(
            f"{pid}: openness_level {problem['openness_level']} exceeds the best related "
            f"contribution ({max_openness}); a problem cannot be more open than its references"
        )
    max_evidence = max((EVIDENCE_RANK.get(card.get("evidence_strength"), 0) for card in related), default=EVIDENCE_RANK["D"])
    if EVIDENCE_RANK.get(problem.get("evidence_strength"), 0) > max_evidence:
        errors.append(
            f"{pid}: evidence_strength {problem.get('evidence_strength')} is stronger than any related contribution"
        )
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
    if data.get("type") not in VALID_CONTRIBUTION_TYPES:
        errors.append(f"{path}: type `{data.get('type')}` is not recognized")
    if data.get("maturity") not in VALID_MATURITY:
        errors.append(f"{path}: maturity `{data.get('maturity')}` is not recognized")
    if data.get("review_status") not in VALID_REVIEW_STATUS:
        errors.append(f"{path}: review_status must be needs_review, accepted, or rejected")
    if data.get("review_status") == "accepted":
        if not has_source(data):
            errors.append(f"{path}: an accepted contribution needs a repository_url or project_url")
        if not has_licence(data):
            errors.append(f"{path}: an accepted contribution needs license_code or license_data")
    return errors


def validate_relationship(path: Path, data: dict) -> list[str]:
    errors = require_fields(path, data, RELATIONSHIP_REQUIRED)
    if data.get("evidence_strength") not in VALID_EVIDENCE:
        errors.append(f"{path}: evidence_strength must be A-E")
    if data.get("relationship_type") not in VALID_RELATIONSHIP_TYPES:
        errors.append(f"{path}: relationship_type is not recognized")
    if data.get("review_status") not in VALID_REVIEW_STATUS:
        errors.append(f"{path}: review_status must be needs_review, accepted, or rejected")
    if data.get("source_id") == data.get("target_id"):
        errors.append(f"{path}: source_id and target_id must differ")
    return errors


def main() -> int:
    errors: list[str] = []
    problems: list[dict] = []
    problem_ids: set[str] = set()
    contributions: dict[str, dict] = {}
    relationship_ids: set[str] = set()

    for path in iter_markdown(ROOT / "problems"):
        data, body = parse_markdown(path)
        errors.extend(validate_problem(path, data, body))
        if data.get("id") in problem_ids:
            errors.append(f"{path}: duplicate problem id {data.get('id')}")
        problem_ids.add(data.get("id"))
        problems.append(data)

    for path in iter_markdown(ROOT / "contributions"):
        data, _ = parse_markdown(path)
        errors.extend(validate_contribution(path, data))
        if data.get("id") in contributions:
            errors.append(f"{path}: duplicate contribution id {data.get('id')}")
        contributions[data.get("id")] = data
        if data.get("problem_id") not in problem_ids:
            errors.append(f"{path}: unknown problem_id {data.get('problem_id')}")
        expected_dir = data.get("problem_id")
        if path.parent.name != expected_dir:
            errors.append(f"{path}: card lives under contributions/{path.parent.name}/ but problem_id is {expected_dir}")

    relationships_root = ROOT / "relationships"
    if relationships_root.exists():
        for path in iter_markdown(relationships_root):
            data, _ = parse_markdown(path)
            errors.extend(validate_relationship(path, data))
            if data.get("id") in relationship_ids:
                errors.append(f"{path}: duplicate relationship id {data.get('id')}")
            relationship_ids.add(data.get("id"))
            for field in ("source_id", "target_id"):
                if data.get(field) not in contributions:
                    errors.append(f"{path}: unknown {field} {data.get(field)}")

    for problem in problems:
        for contribution_id in problem.get("related_contributions", []):
            if contribution_id not in contributions:
                errors.append(f"{problem.get('id')}: unknown related_contribution {contribution_id}")
        errors.extend(validate_problem_status(problem, contributions, problem_ids))

    if errors:
        print("Front matter validation failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    status_counts = Counter(problem.get("status") for problem in problems)
    completeness_counts = Counter(problem.get("card_completeness") for problem in problems)
    accepted_count = sum(1 for card in contributions.values() if card.get("review_status") == "accepted")
    print(
        f"Validated {len(problem_ids)} problems, "
        f"{len(contributions)} contributions, and "
        f"{len(relationship_ids)} relationships."
    )
    print("Problem status: " + ", ".join(f"{key}={value}" for key, value in sorted(status_counts.items())))
    print("Card completeness: " + ", ".join(f"{key}={value}" for key, value in sorted(completeness_counts.items())))
    print(f"Accepted contribution reviews: {accepted_count} of {len(contributions)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
