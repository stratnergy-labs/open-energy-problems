---
id: EP-001
title: Battery Revenue Ceiling Benchmark for Germany
lane: market-benchmarks
status: CANDIDATE_REFERENCE
openness_level: 4
evidence_strength: B
geography: Germany
asset_class:
  - battery_storage
market_scope:
  - day_ahead
  - intraday
  - FCR
  - aFRR
ai_relevance: medium
market_integrity_risk: low
last_updated: 2026-09-05
maintainer: stratnergy
card_completeness: complete
related_contributions:
  - isea-battery-revenue-index
  - gigastorage-battery-trading-benchmark
public_post_url: null
analysis_url: null
interactive_url: null
---

# Battery Revenue Ceiling Benchmark for Germany

## Problem

Publish a transparent, reproducible perfect-foresight revenue ceiling for a
standard reference battery across German market products: the revenue the
battery would have earned with full knowledge of realised prices. A ceiling is
an upper bound that no real asset can earn. Its value is as a common
denominator for "percent of perfect" claims and as the top line beside a
previsible index (`EP-004`) and realised disclosures (`EP-002`).

## Why It Matters

Hindsight ceilings are the most common battery benchmark in Germany and the
most commonly misread as achievable revenue. Two public ceilings exist, each
with its own battery assumptions, markets, and data sources, so their numbers
are not comparable with each other or with realised performance. Publishing
ceilings for one shared reference battery, with the hindsight assumption
declared per product, makes revenue claims comparable and stops a ceiling
being presented as a forecast.

## Scope

In scope: day-ahead, intraday auction and continuous, FCR and aFRR capacity
and energy for the reference battery of `EP-005`; single-market and
cross-market ceilings; an explicit statement per product of which realised
data the optimisation sees; redistributable sources; monthly publication.

Out of scope: any strategy that must be previsible (`EP-004`), forecasts of
future ceilings, and claims about specific assets or traders.

## Definition Of Done

1. Open code and named public sources from which an independent party
   recomputes each monthly ceiling within a stated tolerance.
2. The reference battery of `EP-005` adopted, or the deviation documented
   parameter by parameter.
3. A hindsight declaration per product: which realised prices, volumes, and
   activation signals the optimiser uses, and at what resolution.
4. Cross-market ceilings that state how product conflicts are resolved,
   rather than summing single-market results.
5. A licence review of every input, with link-only handling for sources that
   cannot be redistributed.
6. Twelve consecutive monthly values published from an automated pipeline.

## Baseline

The single-market day-ahead ceiling for the reference battery with one cycle
per day, computed from SMARD day-ahead prices. Every richer ceiling should be
reported as an increment over this number.

## Existing Artefacts

- [ISEA Battery Revenue Index](../contributions/EP-001/isea-battery-revenue-index.md):
  public methodology; the wholesale step computes the best trading profile per
  day on realised ENTSO-E day-ahead and EPEX intraday prices, so it is a
  ceiling; phase one combines single-market results by weighting; developed
  by ISEA at RWTH Aachen together with enspired GmbH; the site says code is on
  GitLab, but the repository URL and licence have not been retrieved.
- [GigaStorage Battery Trading Benchmark](../contributions/EP-001/gigastorage-battery-trading-benchmark.md):
  open code under Apache-2.0 that computes the optimal value an energy storage
  system can earn on realised prices; Dutch market scope; active repository.

Neither reference has passed source and licence review, and neither uses a
shared reference battery, so the status is `CANDIDATE_REFERENCE`.

## Open Questions

- How should cross-market conflicts be resolved in a ceiling without turning
  it into a strategy?
- How should the quarter-hourly day-ahead auction since October 2025 be
  handled alongside the hourly history?
- Cycle cap or degradation cost: which convention keeps ceilings comparable?

## Review Notes

- Status changed on 2026-09-05 from `SOLVED_FOR_SCOPE` to
  `CANDIDATE_REFERENCE`: no linked reference had an accepted source and
  licence review, so the previous status contradicted the register's own
  rule. See [the status-rule review](../docs/status-rule-review-2026-09-05.md).
- `EP-003` was merged into this card; the GigaStorage reference moved here.
- Low market-integrity risk: a hindsight ceiling is not a trading signal.
