# AGENTS.md

## Project

This repository is `Open Energy Problems`, a public AI x OSS index of energy-market problems, open-source artefacts, AI-assisted attempts, and reviewed progress.

The project is not a link directory. It is a structured problem and evidence repository.

## Working Principles

- Prefer small, reviewable PRs.
- Do not invent facts about external projects.
- Do not mark a problem as solved unless the status is explicitly requested.
- Keep public problem cards self-contained.
- Separate code licence from data licence.
- Treat public commercial disclosures differently from open-source artefacts.
- Avoid live trading logic, current market positions, confidential optimiser logic, and operational control instructions.
- Every AI-assisted contribution must be labelled.

## Technical Expectations

- Run `python3 scripts/validate_frontmatter.py` after editing problem cards.
- Run `python3 scripts/build_index.py` after editing problems or contributions.
- Run tests before proposing a PR.
- Keep markdown front matter valid YAML.
- Prefer typed schemas and simple generated JSON over ad hoc parsing.
- Keep the site static-first unless instructed otherwise.

## Review Guidelines

Flag as high priority if a change:

- weakens market-integrity safeguards;
- republishes data with unclear licence;
- confuses open-source code with open data;
- presents a public disclosure as reproducible open infrastructure;
- creates an unsupported claim about a project;
- adds agent autonomy without human approval gates.

## Style

- Direct, concise, technical.
- No marketing language.
- No claims of "AI solved X" without evidence.
- Use "solved for scope" rather than "solved" where appropriate.
