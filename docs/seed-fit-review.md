# Seed Fit Review

Date: 2026-04-26

This note records the first fit review of seed problems and contribution examples.

## Review Principles

- Do not list Stratnergy concepts or future artefacts as reference contributions until they exist publicly.
- Do not use a private concept status in the public taxonomy.
- A contribution can be real and useful while still being only partial progress for a specific problem.
- Public commercial disclosures, open code, reproducible benchmarks, and open data are different evidence types.
- Placeholder source URLs mean the card remains `needs_review`.

## Changes Made

- Removed `Open Virtualiser` as a contribution card.
- Removed `STRATNERGY_CONCEPT` from status definitions.
- Reclassified EP-301 and EP-304 as `OPEN` with no related contributions.
- Reclassified EP-201 as `OPEN` because no accepted baseline artefact is listed.
- Set EP-702 openness to `0` because no source-ledger artefact is listed yet.
- Changed ISEA review status from `accepted` to `needs_review` pending source and licence verification.
- Changed OpenLEADR from `MCP_CONNECTOR` to `METHODOLOGY`.
- Downgraded OpenLEADR, FlexMeasures, and OpenEMS to partial evidence for demand-response event replay, because they are relevant open projects but not accepted replay packages by themselves.
- Removed Open Energy Platform from EP-801 because it does not fit the shared-terminology problem cleanly. It can return later under a better-formulated open-data/platform problem.
- Added validation that every `related_contributions` ID must exist.

## Current Fit Notes

| Problem | Current Fit Assessment |
| --- | --- |
| EP-001 Open BESS Revenue Index for Germany | Strongest seed, but source and licence URLs still need verification. Keep `SOLVED_FOR_SCOPE` only for the narrow public-benchmark scope. |
| EP-002 Public Actual BESS Portfolio Performance | Correctly separated as `PUBLIC_DISCLOSURE`; should not be treated as reproducible open infrastructure. |
| EP-003 Open ESS Trading Benchmark | Good fit if the benchmark artefact is verified as reproducible and open. |
| EP-101 Open Short-Term Load Forecast Benchmark | Good fit for OpenSTEF, pending source/licence review. |
| EP-103 Forecast Decision-Quality Benchmark | Correctly open; no seed artefact listed. |
| EP-201 Transparent Battery Strategy Baseline | Correctly open after cleanup; needs an actual delayed/synthetic baseline artefact. |
| EP-301 Open Virtual Battery Schema | Correctly open after cleanup; no self-reference or future Stratnergy artefact listed. |
| EP-302 Firm vs Interruptible Flexibility | Correctly open; likely needs glossary/schema candidates later. |
| EP-304 Virtual Battery Evidence Package | Correctly open after cleanup; no self-reference or future Stratnergy artefact listed. |
| EP-401 Agent-Based Market Simulation Benchmark | ASSUME is a plausible fit for simulation infrastructure; status should remain reviewable. |
| EP-501 Open Grid Stress Modelling | PyPSA and LF Energy Power Grid Model are plausible partial fits, not complete evidence packages by themselves. |
| EP-601 Demand Response Event Replay | OpenLEADR, FlexMeasures, and OpenEMS are relevant partial building blocks, not accepted replay artefacts. |
| EP-701 AI-Accessible Energy Asset Registries | open-MaStR and MaStR MCP Server are plausible fits, pending source/licence review. |
| EP-702 Energy Source-Ledger Schema | Correctly open; needs a neutral schema/example before raising openness. |
| EP-801 Shared Energy Terminology | Open Energy Ontology is a plausible fit; Open Energy Platform was removed as too broad for this problem. |

## Next Review Work

- Add canonical `project_url` and `repository_url` values only after human verification.
- Add licence fields only from primary source material.
- Consider a new problem card for open energy data platforms before re-adding Open Energy Platform.
- Add a stricter status policy so problems with no accepted contributions default to `OPEN`.
