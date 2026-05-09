---
id: EP-305
title: Open Flexibility Portfolio Accounting
lane: virtualisation
status: OPEN
openness_level: 0
evidence_strength: D
geography: Germany
asset_class:
  - flexibility
  - demand_response
  - battery_storage
market_scope:
  - virtualisation
  - contracts
  - settlement
ai_relevance: medium
market_integrity_risk: medium
last_updated: 2026-05-09
maintainer: stratnergy
related_contributions: []
public_post_url: null
analysis_url: null
interactive_url: null
---

# Open Flexibility Portfolio Accounting

## Problem

Define an open accounting method for flexibility portfolios: availability,
reservation, activation, fulfilment, non-delivery, rebound, overcommitment,
baseline error, and settlement caveats.

## Why It Matters

Flexibility portfolios combine assets with different constraints and evidence
quality. Without shared accounting, it is hard to tell whether a portfolio
claim describes physical capability, contracted capacity, expected availability,
delivered response, or a commercial position.

## Scope

The target artefact is a public accounting schema, worked examples, and review
checklist. It should make portfolio-level claims traceable to asset-level
assumptions while protecting sensitive asset and customer data.

Out of scope: settlement advice for specific contracts, live dispatch
instructions, customer-specific data, or claims that cannot be independently
reviewed from the disclosed evidence.

## Existing Artefacts

No accepted reference artefact is listed yet. Relevant partial areas include
demand-response event replay, virtual battery schemas, source ledgers, and
shared energy terminology.

## Open Questions

- How should firm, interruptible, reserved, unavailable, fulfilled, and
  over-committed flexibility be reconciled at portfolio level?
- What evidence is needed to distinguish claimed flexibility from delivered
  flexibility?
- How should rebound, baseline error, location, and uncertainty be recorded?
- Which fields can be public without disclosing sensitive customer or asset
  information?

## Market-Integrity And Licence Notes

Use aggregated, synthetic, delayed, or consented examples. Do not add customer-
sensitive data, operational control instructions, live positions, or restricted
data copies to this problem card.
