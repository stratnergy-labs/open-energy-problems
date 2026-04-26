# Open Energy Problems

AI x OSS reference problems for software-defined energy markets.

Energy markets have many important problems that are partly solved, privately solved, commercially disclosed, academically modelled, or not yet clearly stated.

This repository tracks those problems.

It records open-source projects, public methodologies, benchmark artefacts, AI-assisted attempts, replications, critiques, and remaining gaps.

The goal is not to make a link directory. The goal is to create a cumulative problem map for software-defined energy markets.

In mathematics, a solved problem is often a proof. In energy, a solved problem is often a reference artefact: an open benchmark, schema, dataset, simulator, replay package, or validated method.

## Surfaces

- GitHub repository: public problem and evidence layer.
- Stratnergy.com: editorial interpretation layer.
- Stratnergy.online: interactive terminal and analysis layer.

The public repository must remain useful without a subscription. Paid surfaces may add synthesis, tooling, and interpretation, but not basic verification access for public artefacts.

## What Is Tracked

- Problem cards in `problems/`.
- Contribution cards in `contributions/`.
- AI attempt logs, source ledgers, reviews, and benchmark notes.
- Generated indexes in `index/`.
- JSON schemas in `schemas/`.
- A GitHub Pages status explorer in `docs/`.

## Status Page

The public status page is intended to live at:

<https://stratnergy-labs.github.io/open-energy-problems/>

It reads generated JSON from `docs/data/` and gives a Tao-style public table for problem status, evidence strength, openness, and related artefacts.

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

## Guardrails

This repository does not publish live trading logic, current market positions, confidential optimiser logic, or operational control instructions. Public commercial disclosures are tracked separately from reproducible open infrastructure.

AI-assisted contributions are welcome, but they must be labelled and independently checked before claims are treated as evidence.

## Licence

Code is MIT licensed. Text, templates, and cards are licensed under CC-BY-4.0. Third-party sources and data retain their own source-specific licences and restrictions.
