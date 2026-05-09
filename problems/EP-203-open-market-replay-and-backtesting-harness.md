---
id: EP-203
title: Open Market Replay And Backtesting Harness
lane: trading-logic
status: OPEN
openness_level: 0
evidence_strength: D
geography: Europe
asset_class:
  - battery_storage
  - flexibility
market_scope:
  - day_ahead
  - intraday
  - balancing
  - backtesting
ai_relevance: high
market_integrity_risk: high
last_updated: 2026-05-09
maintainer: stratnergy
related_contributions: []
public_post_url: null
analysis_url: null
interactive_url: null
---

# Open Market Replay And Backtesting Harness

## Problem

Create a reusable replay environment for testing storage and flexibility
methods against historical or synthetic market conditions, with clear controls
for data leakage, market timing, fees, asset constraints, and reporting.

## Why It Matters

Many energy trading and dispatch claims are backtests, but backtests are easy to
overstate. A common replay harness would make assumptions visible: what was
known at decision time, what data was delayed, how prices were settled, what
costs were included, and which constraints were enforced.

## Scope

The harness should support delayed public datasets, synthetic examples, and
clearly documented assumptions. It should record decision timestamps, source
versions, market-product definitions, unit conversions, transaction costs,
degradation assumptions, and benchmark metrics.

Out of scope: live trading integration, current order-book replication,
proprietary strategy code, and unrestricted use of restricted market data.

## Existing Artefacts

No accepted reference artefact is listed yet. Related partial areas include
open ESS trading benchmarks, forecast decision-quality benchmarks, agent-based
market simulation, and source-ledger records.

## Open Questions

- Which market products and time resolutions should be covered first?
- How should the harness prevent look-ahead bias and accidental use of revised
  data?
- Which data licences permit replay publication, and which require link-only
  source ledgers?
- What benchmark metrics should be reported besides gross revenue?

## Market-Integrity And Licence Notes

Replay examples should be delayed, synthetic, or licence-compatible. Do not add
live strategy, current bids, operational dispatch instructions, customer-
sensitive data, or restricted data copies to this problem card.
