---
id: EP-104
title: Public Forecast Scoreboard
lane: forecasting
status: OPEN
openness_level: 0
evidence_strength: D
geography: Germany
asset_class:
  - battery_storage
  - market
market_scope:
  - forecasting
  - day_ahead
  - FCR
  - aFRR
  - imbalance
ai_relevance: high
market_integrity_risk: low
last_updated: 2026-09-05
maintainer: stratnergy
card_completeness: complete
related_contributions: []
public_post_url: null
analysis_url: null
interactive_url: null
---

# Public Forecast Scoreboard

## Problem

A public register of dated, frozen forecasts of scoreable energy-market
primitives, with scoring rules fixed before the outcomes arrive, a mandatory
naive baseline, results reported by horizon, and a separate ledger for any
decision built on a forecast. Candidate primitives: the day-ahead capture
spread of the reference battery (`EP-005`), FCR and aFRR capacity prices, the
imbalance price distribution, and installed storage capacity (`EP-704`).

## Why It Matters

Forecasting competitions in other fields found the same thing: progress
starts when forecasts are fixed in advance, compared with simple baselines,
and scored as outcomes arrive. Battery revenue forecasting has backtests and
P10 to P90 fans but no public forecast-versus-outturn archive an outsider can
score. The M6 competition adds that forecast accuracy and decision value must
be scored separately: a good forecast is not yet a good decision.

## Scope

In scope: a monthly cadence; horizons from one to thirty-six months; proper
scoring rules such as pinball loss, CRPS or the weighted interval score, and
coverage and clustering tests for bands; immutable vintages; pseudonymous or
delayed participation for providers; a separate decision ledger. Out of
scope: judging investment advice and any live position.

## Definition Of Done

1. A vintage schema: forecast date, data cut-off, model version, target,
   horizon, quantiles, and the baseline used.
2. Open scoring code with the rules fixed before use.
3. A public archive holding at least one forecaster's twelve consecutive
   frozen monthly vintages scored against the baseline, by horizon.
4. Tamper evidence: a hash chain or third-party timestamping so that vintages
   cannot be withdrawn or edited after the fact.
5. A decision ledger format that scores a dispatch, contract, or investment
   rule separately from the forecast it used.

## Baseline

The seasonal empirical distribution of the target from the prior years,
expressed as nearest-rank quantiles.

## Existing Artefacts

None tracked in energy for batteries. Pattern references from other fields:
the COVID-19 Forecast Hub, the M-competition data repositories, and the
Survey of Professional Forecasters archive. `EP-103` covers the decision-
quality side.

## Open Questions

- Which primitives first, and at what resolution after the quarter-hourly
  change of October 2025?
- How can post-hoc withdrawal be prevented without a central authority?
- Is the reference-battery capture spread or the raw price the better primary
  target?

## Review Notes

- Low market-integrity risk: forecasts are of public primitives at monthly
  resolution.
- Do not list a Stratnergy artefact here until it exists publicly.
