---
id: EP-006
title: Cannibalisation Metrics From Public Data
lane: market-benchmarks
status: OPEN
openness_level: 0
evidence_strength: D
geography: Germany
asset_class:
  - battery_storage
market_scope:
  - day_ahead
  - intraday
  - FCR
  - aFRR
ai_relevance: high
market_integrity_risk: medium
last_updated: 2026-09-05
maintainer: stratnergy
card_completeness: complete
related_contributions: []
public_post_url: null
analysis_url: null
interactive_url: null
---

# Cannibalisation Metrics From Public Data

## Problem

Publish reproducible monthly indicators of how storage growth changes the
opportunities storage earns from: day-ahead and intraday spread compression
relative to fleet size, FCR and aFRR capacity-price saturation, and reserve
merit-order depth from the anonymised balancing bid data. The aim is that
"cannibalisation" claims can be checked against measurement rather than
against model output.

## Why It Matters

The market value of wind and solar falls with penetration, and storage has the
same reflexivity through the spreads and reserve prices it trades. Every
long-horizon battery revenue forecast rests on an assumed cannibalisation
path, yet nobody publishes the measured one. A measured series is the empirical
anchor for structural models and a scoreable primitive for `EP-104`.

## Scope

In scope: the German bidding zone; monthly, delayed, and aggregate; sources
SMARD prices, regelleistung.net results and anonymised bids, and fleet size
from `EP-704`; definitions that use the reference battery of `EP-005`. Out of
scope: attributing behaviour to identifiable bidders, real-time signals, and
any non-public data.

## Definition Of Done

1. A pipeline that recomputes each indicator from named sources with a
   source ledger (`EP-702`).
2. Documented definitions: capturable daily spread for the reference battery,
   capacity price per MW and week, share of aFRR capacity demand met at or
   below stated price points, and bid-ladder depth at those points.
3. A licence review of regelleistung.net terms, with link-only handling if
   the bid data cannot be redistributed.
4. Twelve consecutive monthly values published beside fleet size.

## Baseline

The raw spread and capacity-price time series plotted against MaStR fleet
size, with no modelling.

## Existing Artefacts

None tracked. The inputs are public: SMARD (CC BY 4.0), the regelleistung.net
data centre, and the Marktstammdatenregister via `EP-701`.

## Open Questions

- How should the fleet effect be separated from fuel-price and renewable
  effects? This confound is the whole difficulty.
- Are the anonymised bid data redistributable or link-only?
- How should the quarter-hourly day-ahead auction since October 2025 change
  the spread definition?

## Review Notes

- Medium sensitivity for bid data: aggregate and delayed only, never
  bidder-level.
