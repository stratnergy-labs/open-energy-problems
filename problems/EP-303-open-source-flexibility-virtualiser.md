---
id: EP-303
title: Open Source Flexibility Virtualiser
lane: virtualisation
status: OPEN
openness_level: 0
evidence_strength: D
geography: Germany
asset_class:
  - battery_storage
  - flexibility
  - demand_response
market_scope:
  - virtualisation
  - dispatch
  - contracts
ai_relevance: high
market_integrity_risk: medium
last_updated: 2026-05-09
maintainer: stratnergy
related_contributions: []
public_post_url: null
analysis_url: null
interactive_url: null
---

# Open Source Flexibility Virtualiser

## Problem

Build an open reference virtualiser that turns asset capabilities, constraints,
availability, uncertainty, and fulfilment records into a machine-readable
flexibility representation.

## Why It Matters

Flexibility is often discussed as if it were a simple quantity. In practice, it
depends on physical limits, customer constraints, telemetry, baseline choices,
contract terms, grid location, rebound effects, and confidence intervals. An
open virtualiser would make those assumptions inspectable and comparable.

## Scope

The target artefact is a reference implementation or specification that can
ingest sample asset states and produce a virtual battery or flexibility object.
It should expose inputs, constraints, timestamps, uncertainty, reserved capacity,
fulfilled capacity, unavailable capacity, and caveats.

Supporting subproblems include `EP-301` for the schema, `EP-302` for firm and
interruptible definitions, and `EP-304` for evidence packages.

Out of scope: controlling real assets, publishing customer-sensitive telemetry,
or claiming availability without evidence.

## Existing Artefacts

No accepted reference artefact is listed yet. Related tracked references in
demand response and energy management may provide useful components, but no
tracked contribution currently covers the full virtualiser problem.

## Open Questions

- Which asset classes should the first reference virtualiser support?
- How should availability, uncertainty, baseline error, rebound, and fulfilment
  be represented?
- What is the minimum evidence package needed for a virtualised flexibility
  claim?
- How should location and grid constraints be included without exposing
  sensitive asset data?

## Market-Integrity And Licence Notes

Use synthetic or consented sample data. Do not add operational control
instructions, customer-sensitive telemetry, confidential optimiser logic, or
restricted data copies to this problem card.
