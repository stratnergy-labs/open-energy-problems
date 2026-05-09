---
id: EP-202
title: Open Full-Stack Battery Trading Reference Stack
lane: trading-logic
status: OPEN
openness_level: 0
evidence_strength: D
geography: Germany
asset_class:
  - battery_storage
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

# Open Full-Stack Battery Trading Reference Stack

## Problem

Build a public, non-operational reference stack for battery trading research:
data inputs, forecasts, optimisation model, asset constraints, replay or
backtest harness, accounting, and benchmark reporting.

## Why It Matters

Battery strategy claims are difficult to compare when the forecast inputs,
market data, optimisation assumptions, degradation costs, fees, constraints, and
settlement logic are split across private systems. An open reference stack would
let researchers test ideas against a shared structure without publishing live
trading logic.

## Scope

The target is a delayed, synthetic, or research-grade stack for German and
European market examples. It should be useful for comparison, teaching, and
review, but unsuitable for direct operational deployment. It should separate
market data rights, forecast assumptions, objective functions, asset limits,
transaction costs, degradation assumptions, and reporting metrics.

Out of scope: current bids, live dispatch instructions, proprietary optimiser
logic, customer-specific assets, market coordination, and unrestricted
automation against live markets.

## Existing Artefacts

No accepted reference artefact is listed yet. Relevant partial work may include
open ESS benchmarks, public battery revenue indexes, open optimisation tooling,
and market simulators, but no tracked contribution currently covers the full
stack for this problem.

## Open Questions

- What is the minimum safe reference stack that is useful without becoming
  operational trading guidance?
- Which market data can be redistributed, linked, or used only through a source
  ledger?
- How should forecast uncertainty, battery degradation, grid constraints, fees,
  and balancing-market eligibility be represented?
- What benchmark outputs are informative without encouraging live strategy
  copying?

## Market-Integrity And Licence Notes

Use delayed, synthetic, public, or licence-compatible data only. Do not add live
strategy, current bids, operational dispatch instructions, customer-sensitive
data, or restricted data copies to this problem card.
