# Open Energy Problems

AI x OSS reference problems for software-defined energy markets. **[Browse the status explorer](https://stratnergy-labs.github.io/open-energy-problems/)** for the searchable table.

Open Energy Problems is a public register for important energy-market and grid problems, with a Germany-first focus on flexibility, storage, forecasting, open data, and software-defined operation.

The register is organised around problems, not vendors or projects. For each problem, it tracks how far there is an open solution: a reproducible benchmark, schema, dataset, simulator, replay package, source ledger, validated method, or public disclosure.

Energy markets have many important problems that are partly solved, privately solved, commercially disclosed, academically modelled, or not yet clearly stated. This repository makes that state inspectable, so good open work can be found, credited, challenged, and improved.

The goal is not to make a link directory. The goal is to create a cumulative register for software-defined energy markets, starting with the German grid as a demanding test case for public evidence infrastructure.

In mathematics, a solved problem is often a proof. In energy, a solved problem is often a reference object: an open benchmark, schema, dataset, simulator, replay package, or validated method.

## Purpose

Open Energy Problems exists to answer a practical question:

> For the most important problems in modern energy systems, what open references already exist, what do they actually prove, and what remains missing?

The project is useful when it helps readers distinguish:

- an open-source codebase from an open benchmark;
- a public chart from reusable open data;
- a commercial disclosure from reproducible evidence;
- a promising method from a validated open reference;
- an AI-assisted attempt from a reviewed contribution.

Germany is the first anchor because its power system exposes many of the hard problems at once: large renewable penetration, storage economics, redispatch and grid stress, balancing markets, demand response, asset registries, and the need for transparent flexibility evidence. The register can later expand to other geographies where the same problem structure applies.

## How The Register Works

Each problem card asks:

- What is the problem?
- Why does it matter for the grid, market design, or open energy software?
- Which open references or public disclosures are relevant?
- What is the openness level?
- What is the evidence strength?
- What gaps remain?

## Review Track

`Review wanted` means an entry is relevant enough to track, but its source,
licence, fit, evidence level, or safety caveats still need checking.

Community reviews can be small:

- source review;
- licence review;
- fit review;
- evidence review;
- safety review.

Use the [review request template](https://github.com/stratnergy-labs/open-energy-problems/issues/new?template=review-request.yml)
or open a pull request. Maintainers decide whether a review changes the card's
status, openness level, evidence strength, or problem fit.

Traffic-light status is intentionally conservative:

- 🟢 means a useful open reference exists for a stated scope.
- 🟡 means there is partial progress, public disclosure, or relevant open tooling, but important gaps remain.
- 🔴 means the problem is still open in this register because no accepted reference artefact is listed.

## How To Contribute

Useful contributions can be small: suggest a missing reference, check a source,
clarify a licence, review whether a project fits a problem, or improve a problem
statement.

Start with [How To Contribute](HOW_TO_CONTRIBUTE.md), or use one of the GitHub
forms:

- [Suggest a reference](https://github.com/stratnergy-labs/open-energy-problems/issues/new?template=new-contribution.yml)
- [Submit a review note](https://github.com/stratnergy-labs/open-energy-problems/issues/new?template=review-request.yml)
- [Propose a problem](https://github.com/stratnergy-labs/open-energy-problems/issues/new?template=new-problem.yml)

## Project Context

This repository is the public evidence layer for a wider Stratnergy research programme on software-defined energy markets. The repository should remain useful on its own: problem statements, tracked references, generated indexes, and source notes stay public and reviewable.

Separate Stratnergy publications may add interpretation: why a problem matters,
what progress means for market participants, and which open references deserve
deeper review. That interpretation should not be required to verify the public
register.

## Status Snapshot

Seed snapshot as of 2026-04-26. The traffic lights describe repository classification, not project quality or commercial usefulness.

| Light | Meaning | Count | Current problem IDs |
| --- | --- | ---: | --- |
| 🟢 | Reference available or solved for a narrow stated scope | 5 | EP-001, EP-003, EP-101, EP-401, EP-801 |
| 🟡 | Partial progress or public disclosure, with important reproducibility gaps | 5 | EP-002, EP-501, EP-601, EP-701, EP-901 |
| 🔴 | Open problem with no accepted open reference yet | 6 | EP-103, EP-201, EP-301, EP-302, EP-304, EP-702 |

Current seed map:

- 16 problem cards.
- 22 tracked references.
- 7 project relationship cards.
- 10 problem areas.
- 0 accepted source/licence reviews; seed contribution cards remain `needs_review` until source URLs and licence terms are verified.

For the full status table, filters, open-solution levels, evidence strength, and tracked references, use the [GitHub Pages explorer](https://stratnergy-labs.github.io/open-energy-problems/). Each problem links back to its GitHub card.

## Where This Fits

- GitHub repository: public problem and evidence layer.
- Stratnergy publications: interpretation, commentary, and deeper reviews.
- Stratnergy tooling: interactive exploration and analysis.

The public repository must remain useful on its own. Separate Stratnergy work
may add synthesis, tooling, and interpretation, but not basic verification
access for public sources and open references.

## What Is Tracked

- Problem cards in `problems/`.
- Tracked reference cards in `contributions/`.
- Project relationship cards in `relationships/`.
- AI attempt logs, source ledgers, reviews, and benchmark notes.
- Generated indexes in `index/`.
- JSON schemas in `schemas/`.
- A GitHub Pages status explorer in `docs/`.

## Status Page

The public status page is intended to live at:

<https://stratnergy-labs.github.io/open-energy-problems/>

It reads generated JSON from `docs/data/` and gives a Tao-style public table for problem status, evidence strength, open-solution level, and tracked references.

## Start Here

```bash
python3 scripts/validate_frontmatter.py
python3 scripts/build_index.py
```

Generated files:

- `index/problems.json`
- `index/problems.csv`
- `index/contributions.json`
- `index/contributions.csv`
- `index/relationships.json`
- `index/relationships.csv`

## Relationship Map

The register distinguishes problem-to-project links from project-to-project
relationships.

Problem cards say which references are relevant to a public problem.
Relationship cards say how two tracked references relate to each other, for
example `uses_component`, `uses_data_source`, `wraps_project`, `documents_api`,
`shared_data_source`, or `alternative_implementation`.

Do not mark one project as using another unless the source is verified. When
the relationship is only contextual, use a weaker type such as
`shared_data_source` or `same_problem_context`.

## Energy-Enabling Infrastructure

Some tracked references are not energy-specific projects. They belong here when
they are infrastructure that energy reproducibility depends on: optimization
solvers, modelling layers, source-ledger tools, benchmark runners, or other
software needed to inspect and rerun energy results.

These entries should be tied to a specific energy problem. For example,
`EP-901` tracks open optimization stacks for energy models, not generic solver
popularity.

## Guardrails

This repository does not publish live trading logic, current market positions, confidential optimiser logic, or operational control instructions. Public commercial disclosures are tracked separately from reproducible open infrastructure.

AI-assisted submissions are welcome, but they must be labelled and independently checked before claims are treated as evidence.

## Licence

Code is MIT licensed. Text, templates, and cards are licensed under CC-BY-4.0. Third-party sources and data retain their own source-specific licences and restrictions.
