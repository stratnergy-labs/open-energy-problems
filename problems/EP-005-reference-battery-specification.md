---
id: EP-005
title: Reference Battery Specification
lane: market-benchmarks
status: OPEN
openness_level: 0
evidence_strength: D
geography: Germany
asset_class:
  - battery_storage
market_scope:
  - benchmarks
  - virtualisation
ai_relevance: medium
market_integrity_risk: low
last_updated: 2026-09-05
maintainer: stratnergy
card_completeness: complete
related_contributions: []
public_post_url: null
analysis_url: null
interactive_url: null
---

# Reference Battery Specification

## Problem

Define a standard reference battery in machine-readable form: a small set of
named configurations that fix power, energy, round-trip efficiency, usable
state-of-charge window, cycle limit or degradation cost, availability, market
eligibility and prequalification assumptions, and fees. Every index, ceiling,
forecast, and disclosure that uses it becomes comparable with every other.

## Why It Matters

Each existing benchmark uses its own battery. The ISEA index leaves parameters
user-configurable, Modo publishes 1h, 2h, and 4h configurations without a
public dispatch model, and disclosures describe real fleets. The difference
between their assumptions is often larger than the difference between their
methods, and readers cannot tell which is which. A standard asset is to a
revenue benchmark what a standard grade is to a commodity price.

## Scope

In scope: a schema, named configurations, validation examples, and versioning
with effective dates. Out of scope: virtualised flexibility objects
(`EP-301`), a physical degradation model beyond a stated cost convention, and
any claim about a specific real asset.

## Definition Of Done

1. A JSON schema with validation examples.
2. At least three named configurations, for instance 1 MW with 1, 2, and
   4 MWh, with every parameter stated and its source or convention given.
3. A stated treatment of grid fees, levies, and prequalification per product.
4. Adoption by two independent public benchmarks or indices, or a documented
   mapping from their parameters to the standard.
5. Versioning with effective dates; changes never alter earlier published
   results that cite an earlier version.

## Baseline

The parameter set implied by the defaults of the ISEA and GigaStorage code,
written down explicitly as version zero.

## Existing Artefacts

None tracked. ISEA's configurable parameters and Modo's 1h, 2h, and 4h
configurations are the nearest public precedents, and neither is a standard.

## Open Questions

- Cycle cap or euro-per-MWh degradation cost: which convention keeps ceilings
  and indices comparable?
- How should reserved capacity and prequalification for FCR and aFRR be
  represented?
- DC versus AC ratings, auxiliary consumption, and availability: what is the
  minimum honest set?

## Review Notes

- Low market-integrity risk: a parameter standard carries no strategy.
