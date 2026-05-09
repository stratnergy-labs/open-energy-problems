---
id: EP-201
title: Transparent Battery Strategy Baseline
lane: trading-logic
status: OPEN
openness_level: 0
evidence_strength: D
geography: Europe
asset_class:
  - battery_storage
market_scope:
  - day_ahead
  - intraday
ai_relevance: medium
market_integrity_risk: high
last_updated: 2026-05-09
maintainer: stratnergy
related_contributions:
  []
public_post_url: null
analysis_url: null
interactive_url: null
---

# Transparent Battery Strategy Baseline

## Problem

Define simple reproducible DA/ID battery arbitrage baselines that are useful
for comparison, teaching, and sanity checks, without becoming live trading
guidance.

## Why It Matters

Battery revenue claims need humble baselines. Before comparing complex
optimisers, reviewers need to know how a simple rule, perfect-foresight toy
model, or constrained arbitrage baseline performs under the same data,
efficiency, degradation, and fee assumptions.

## Scope

Candidate baselines should be simplified, documented, delayed, and unsuitable
for operational trading replication. This card covers baseline strategy logic,
not the full stack for forecasts, replay, accounting, and reporting; that
larger problem is tracked in `EP-202`.

## Existing Artefacts

No accepted artefact is listed yet. Related benchmark work may inform this
problem, but a baseline should not be upgraded until source, licence, timing,
and market-integrity caveats are reviewed.

## Open Questions

- Which baseline is simple enough to inspect but still useful for comparison?
- Which public or synthetic data can be used without licence problems?
- How should degradation, efficiency, fees, and market-product eligibility be
  represented?

## Market-Integrity And Licence Notes

Do not add live strategy, current bids, operational dispatch instructions, customer-sensitive data, or restricted data copies to this problem card.
