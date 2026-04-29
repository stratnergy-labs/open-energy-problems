# Open Energy Problems

A Germany-first public register of open references for energy-market, grid,
forecasting, flexibility, and energy-enabling infrastructure problems.
**[Browse the status explorer](https://stratnergy-labs.github.io/open-energy-problems/)**
for the searchable table.

Find open benchmarks, datasets, schemas, simulators, interfaces, source-ledger
patterns, reproducible methods, and carefully reviewed public disclosures. See
which problem each one helps address, what it proves, and what still needs
review.

The register is organised around problems, not vendors or projects. For each
problem, it tracks how far there is an open reference: what exists, what kind of
openness it provides, what evidence it supports, and what remains missing.

This is early, incomplete, and cautious. It is open for contribution: missing
references, corrected links, licence notes, source checks, and review comments
are all useful.

Energy is different from mathematics. In mathematics, a solved problem is often
a proof. In energy, a useful answer is often a reference object: an open
benchmark, dataset, schema, simulator, source ledger, reproducible method, or
carefully reviewed public disclosure.

## Examples And Seed References

Start with these 23 tracked references. Some cards still need source or licence
review.

| Area | Seed references | What this illustrates |
| --- | --- | --- |
| Battery revenue and trading benchmarks | [ISEA Battery Revenue Index](contributions/EP-001/isea-battery-revenue-index.md), [GigaStorage Battery Trading Benchmark](contributions/EP-003/gigastorage-battery-trading-benchmark.md), [enspired Portfolio Performance](contributions/EP-002/enspired-portfolio-performance.md) | Benchmark, trading benchmark, and public commercial disclosure are related but different. |
| Forecasting | [OpenSTEF](contributions/EP-101/openstef.md) | Reproducible forecasting method. |
| Market simulation | [ASSUME](contributions/EP-401/assume.md) | Agent-based market simulation. |
| Grid modelling | [PyPSA](contributions/EP-501/pypsa.md), [LF Energy Power Grid Model](contributions/EP-501/lf-energy-power-grid-model.md) | Open modelling and grid-analysis infrastructure. |
| Demand response and flexibility | [OpenLEADR](contributions/EP-601/openleadr.md), [FlexMeasures](contributions/EP-601/flexmeasures.md), [OpenEMS](contributions/EP-601/openems.md) | Event, flexibility, and energy-management tooling. |
| MaStR and asset registries | [Official Marktstammdatenregister](contributions/EP-701/official-mastr-register.md), [open-MaStR](contributions/EP-701/open-mastr.md), [MaStR MCP Server](contributions/EP-701/mastr-mcp-server.md), [bundesAPI Marktstammdaten API](contributions/EP-701/bundesapi-marktstammdaten-api.md), [Marktstammdatenregister.dev](contributions/EP-701/marktstammdatenregister-dev.md) | Registry, dataset access, API description, and AI-facing interface. |
| Shared terminology | [Open Energy Ontology](contributions/EP-801/open-energy-ontology.md) | Shared vocabulary and schema work. |
| Open optimisation stack | [HiGHS](contributions/EP-901/highs.md), [Pyomo](contributions/EP-901/pyomo.md), [JuMP](contributions/EP-901/jump.md), [Google OR-Tools](contributions/EP-901/or-tools.md), [COIN-OR CBC](contributions/EP-901/cbc.md), [SCIP](contributions/EP-901/scip.md) | Energy-enabling infrastructure for reproducible optimisation. |
| Tool health and adoption | [Open Energy Modelling Tool Tracker](contributions/EP-902/openmod-tracker.md) | Tool inventory, repository metrics, documentation links, and community-activity signals. |
| Source ledgers | [EP-702](problems/EP-702-energy-source-ledger-schema.md) and the [source-ledger template](templates/source-ledger-template.md) | Source, query, timestamp, licence, result count, hash, and caveats. |

Open code, open data, public methodology, AI interfaces, reproducible
benchmarks, and commercial disclosures can all help the energy transition, but
they are not the same thing.

Know a better source, a missing reference, or a caveat that should be visible?
Open an issue or pull request.

## Purpose

The practical question:

> For the most important problems in modern energy systems, what open references already exist, what do they actually prove, and what remains missing?

It helps readers distinguish:

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

Traffic-light status is conservative:

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

## Stratnergy Context

This repository is part of a wider Stratnergy research programme on
software-defined energy markets. The public cards, references, indexes, and
source notes stay useful without any separate publication.

Separate Stratnergy publications may add interpretation: why a problem matters,
what progress means for market participants, and which open references deserve
deeper review. Basic verification stays in the public repo.

## Status Snapshot

Seed snapshot as of 2026-04-29. The traffic lights describe repository classification, not project quality or commercial usefulness.

| Light | Meaning | Count | Current problem IDs |
| --- | --- | ---: | --- |
| 🟢 | Reference available or solved for a narrow stated scope | 5 | EP-001, EP-003, EP-101, EP-401, EP-801 |
| 🟡 | Partial progress or public disclosure, with important reproducibility gaps | 6 | EP-002, EP-501, EP-601, EP-701, EP-901, EP-902 |
| 🔴 | Open problem with no accepted open reference yet | 6 | EP-103, EP-201, EP-301, EP-302, EP-304, EP-702 |

Current seed map:

- 17 problem cards.
- 23 tracked references.
- 7 project relationship cards.
- 10 problem areas.
- 0 accepted source/licence reviews; seed contribution cards remain `needs_review` until source URLs and licence terms are verified.

For the full status table, filters, open-solution levels, evidence strength, and tracked references, use the [GitHub Pages explorer](https://stratnergy-labs.github.io/open-energy-problems/). Each problem links back to its GitHub card.

## What Is Tracked

- Problem cards in `problems/`.
- Tracked reference cards in `contributions/`.
- Project relationship cards in `relationships/`.
- AI attempt logs, source ledgers, reviews, and benchmark notes.
- Generated indexes in `index/`.
- JSON schemas in `schemas/`.
- A GitHub Pages status explorer in `docs/`.

## Status Page

Public status page:

<https://stratnergy-labs.github.io/open-energy-problems/>

It shows problem status, evidence strength, open-solution level, and tracked
references from the generated data in `docs/data/`.

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
