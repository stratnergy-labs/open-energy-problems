---
id: EP-703
title: As-Of Archive Of German Market Data
lane: open-data
status: CANDIDATE_REFERENCE
openness_level: 3
evidence_strength: C
geography: Germany
asset_class:
  - data
market_scope:
  - day_ahead
  - intraday
  - balancing
  - imbalance
  - source_ledger
ai_relevance: high
market_integrity_risk: low
last_updated: 2026-09-05
maintainer: stratnergy
card_completeness: complete
related_contributions:
  - smard-market-data
public_post_url: null
analysis_url: null
interactive_url: null
---

# As-Of Archive Of German Market Data

## Problem

For each public German market data series used in benchmarks and forecasts,
record when values first became available, how and when they are revised, and
where gaps or placeholders occur; and maintain a vintage-preserving archive so
that "what was known at time t" can be reconstructed.

## Why It Matters

Previsibility (`EP-004`), replay (`EP-203`), and scoring (`EP-104`) all depend
on knowing the information set at decision time. Public portals overwrite
values in place; preliminary imbalance prices are replaced by final ones;
placeholders appear as dashes. Without an as-of archive every backtest is
exposed to look-ahead through revisions, and no scoreboard can be audited.

## Scope

In scope: SMARD, the ENTSO-E Transparency Platform, regelleistung.net,
netztransparenz.de, and exchange indices where licences allow; a documented
publication lag and revision policy per series; a snapshot pipeline with a
source ledger (`EP-702`); archived copies only for redistributable series,
link-only records otherwise.

## Definition Of Done

1. A table of at least ten series with publication lag, revision policy, and
   licence, each verified against the source.
2. A running snapshot archive for the redistributable series with hashes and
   timestamps.
3. A documented example in which a revision changed a benchmark result.

## Baseline

A manually maintained as-of table without automation.

## Existing Artefacts

- [SMARD](../contributions/EP-703/smard-market-data.md): the redistributable
  source for prices and system data under CC BY 4.0; it does not preserve
  vintages.
- The open-MaStR Zenodo snapshots show the pattern for registries
  (`EP-704`).
- ENTSO-E redistribution terms restrict copying; link-only handling is
  required.

## Open Questions

- How should vintages be stored compactly for high-resolution series?
- Do netztransparenz.de terms permit an archive of the imbalance price
  series?
- How should the preliminary and final imbalance price cycle be represented?

## Review Notes

- Low market-integrity risk: archived public data, delayed.
