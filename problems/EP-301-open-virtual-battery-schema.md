---
id: EP-301
title: Open Virtual Battery Schema
lane: virtualisation
status: OPEN
openness_level: 0
evidence_strength: D
geography: Global
asset_class:
  - battery_storage
  - flexibility
market_scope:
  - virtualisation
ai_relevance: high
market_integrity_risk: medium
last_updated: 2026-05-09
maintainer: stratnergy
related_contributions: []
public_post_url: null
analysis_url: null
interactive_url: null
---

# Open Virtual Battery Schema

## Problem

Define a machine-readable schema for virtual battery state, constraints,
availability, uncertainty, and evidence caveats.

## Why It Matters

Virtual batteries are only useful if other people can inspect what the object
means. A schema should make state of charge, power limits, duration, location,
availability, confidence, reservations, and caveats explicit enough for review.

## Scope

This is the schema layer for the broader open-source virtualiser problem in
`EP-303`. Candidate external schemas should be reviewed for scope, licence,
field definitions, validation examples, interoperability, and operational-safety
implications before being added as contributions.

## Existing Artefacts

No contribution is currently accepted for this problem. Source URLs and licence details require human verification before any candidate artefact is listed.

## Open Questions

- Which fields are required for a minimum useful virtual battery object?
- How should firm, interruptible, uncertain, reserved, and unavailable capacity
  be represented?
- Which validation examples can be public without exposing sensitive asset
  data?

## Market-Integrity And Licence Notes

Do not add live strategy, current bids, operational dispatch instructions, customer-sensitive data, or restricted data copies to this problem card.
