---
id: EP-102
title: Open Day-Ahead Price Forecast Benchmark
lane: forecasting
status: CANDIDATE_REFERENCE
openness_level: 4
evidence_strength: B
geography: Germany
asset_class:
  - market
market_scope:
  - day_ahead
  - forecasting
ai_relevance: high
market_integrity_risk: low
last_updated: 2026-09-05
maintainer: stratnergy
card_completeness: complete
related_contributions:
  - epftoolbox
public_post_url: null
analysis_url: null
interactive_url: null
---

# Open Day-Ahead Price Forecast Benchmark

## Problem

A reproducible open benchmark for day-ahead electricity price forecasting in
the German bidding zone: an open dataset with a documented licence, a declared
test window of at least one year, naive and statistical baselines, proper
scoring rules for point and probabilistic forecasts, and statistical tests of
outperformance, so that new methods are compared under common rules.

## Why It Matters

The price forecasting literature has been shown to test on non-public data,
over short windows, without strong baselines and without significance tests,
which invites cherry-picking. Price forecasts feed every battery revenue
forecast; benchmark discipline for the primitive is a precondition for
scoring the derived quantity in `EP-104`.

## Scope

In scope: DE-LU day-ahead prices, hourly history and quarter-hourly since
October 2025; point and probabilistic forecasts; rolling recalibration;
metrics such as MAE, relative MAE, pinball loss, and CRPS; Diebold-Mariano
tests. Out of scope: intraday order-book replication and live trading.

## Definition Of Done

1. A dataset with documented licence and revision policy, or a link-only
   recipe where redistribution is not permitted.
2. Naive seasonal baselines and at least one published statistical reference
   model implemented and runnable.
3. An out-of-sample window of at least one year with results reproducible by
   continuous integration.
4. A quarter-hourly extension covering the period since October 2025.

## Baseline

Naive seasonal forecasts (same hour yesterday and same hour last week) and
the LEAR model of the epftoolbox.

## Existing Artefacts

- [epftoolbox](../contributions/EP-102/epftoolbox.md): open-access benchmark
  with datasets for five markets including Germany, LEAR and DNN reference
  models, evaluation metrics, and statistical tests; Apache-2.0 code; the
  German dataset predates the quarter-hourly era and the licence of the
  bundled data is unverified.

## Open Questions

- Which source can be redistributed for the benchmark dataset: SMARD rather
  than ENTSO-E?
- How should the 2022 price regime be handled in test windows?
- What is the right probabilistic scoring rule set for a market with
  negative prices?

## Review Notes

- Low market-integrity risk.
