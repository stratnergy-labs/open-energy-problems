---
id: EP-004
title: Previsible Battery Revenue Index for Germany
lane: market-benchmarks
status: PUBLIC_DISCLOSURE
openness_level: 3
evidence_strength: C
geography: Germany
asset_class:
  - battery_storage
market_scope:
  - day_ahead
  - intraday
  - FCR
  - aFRR
ai_relevance: high
market_integrity_risk: low
last_updated: 2026-09-05
maintainer: stratnergy
card_completeness: complete
related_contributions:
  - modo-me-bess-de
public_post_url: null
analysis_url: null
interactive_url: null
---

# Previsible Battery Revenue Index for Germany

## Problem

Construct a battery revenue index for Germany that is an index in Andrew Lo's
sense: a portfolio strategy that is transparent, investable, and systematic.
For a battery that means a fully public rule set, run over the standard
reference battery of `EP-005` on public German market prices, in which every
scheduling or bidding decision uses only information available before the
relevant market gate closure. Publish it monthly with versioned rules, beside
its perfect-foresight ceiling (`EP-001`) and realised fleet disclosures
(`EP-002`).

## Why It Matters

German battery benchmarks come in two kinds. Hindsight ceilings optimise
against prices that were only known afterwards; they are useful upper bounds
that nobody can earn. Calibrated simulations scale a modelled revenue by a
factor to match observed fleets; their dispatch logic is not public, so nobody
can check them. Neither is transparent, investable, and systematic at once.
Without such an index there is no checkable yardstick for what a battery
following a known rule would have earned, no honest denominator for "percent
of perfect" claims, and no outcome series against which revenue forecasts can
be scored (`EP-104`).

## Scope

In scope: day-ahead, intraday auction and continuous, and FCR and aFRR
capacity for the reference battery; a previsibility rule per product, stated
at that product's gate closure; monthly publication from redistributable
sources; a versioned methodology with effective dates; the index-to-ceiling
ratio.

Out of scope: any use of post-gate-closure prices, live trading advice,
operational dispatch of real assets, and claims about specific assets or
traders.

Previsibility has to be defined per product. A day-ahead schedule fixed after
the auction clears is close to investable through flexible bid formats; a
schedule optimised against the intraday volume-weighted price or against
activated aFRR energy is not. The rulebook must say, for each product, which
information is admissible and at what time.

## Definition Of Done

1. A public rulebook and code from which an independent party recomputes the
   monthly index from named public sources within a stated tolerance.
2. A previsibility check: a replay harness (`EP-203`) demonstrates that no
   decision uses data published after the relevant gate closure, including
   later revisions of the data (`EP-703`).
3. Redistributable inputs. SMARD publishes day-ahead prices under CC BY 4.0;
   balancing-market sources need a licence review.
4. Three published series per reference configuration: perfect-foresight
   ceiling, previsible index, and realised disclosures where they exist, with
   the index-to-ceiling ratio reported.
5. Change control: rule changes are versioned proposals with effective dates,
   and earlier published values are never recomputed under later rules.
6. Twelve consecutive monthly prints produced by an automated pipeline.

## Baseline

A daily rule fixed at 12:00 on D-1 using only information published before
then: charge in the two lowest-price hours and discharge in the two
highest-price hours of the previous day's day-ahead profile, one cycle per
day, with efficiency and cycle cost from the reference battery. Anything
proposed as the index must beat this baseline out of sample on a rolling basis
while remaining previsible.

## Existing Artefacts

- [Modo Energy ME BESS DE](../contributions/EP-004/modo-me-bess-de.md):
  commercial German benchmark launched in May 2026; a simulated 1h, 2h, and
  4h asset dispatched on real prices with a calibration factor validated on
  GB fleet data; the dispatch logic is not public. Systematic and regular,
  but not transparent and not shown to be previsible.
- ISEA Battery Revenue Index and GigaStorage Battery Trading Benchmark
  (`EP-001`): public and open respectively, but both are hindsight ceilings.

No tracked reference satisfies all three of Lo's properties.

## Open Questions

- Is a post-clearing day-ahead schedule acceptable as previsible, or must
  bids be fixed before the auction?
- How should FCR and aFRR capacity awards be handled when the auction result
  is a price-quantity pair rather than a price?
- What governance keeps the rulebook open to contribution but closed to
  retroactive change?
- What recomputation tolerance is appropriate given source revisions?

## Review Notes

- The definition referenced is Lo, A. W. (2016), "What Is an Index?",
  Journal of Portfolio Management 42(2), 21-36.
- Low market-integrity risk: the rule is simple, public, unoptimised, and
  delayed; it is a yardstick, not a trading signal.
- Do not list a Stratnergy artefact here until it exists publicly.
