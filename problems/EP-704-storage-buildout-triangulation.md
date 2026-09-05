---
id: EP-704
title: Storage Buildout Triangulation
lane: open-data
status: OPEN
openness_level: 0
evidence_strength: D
geography: Germany
asset_class:
  - battery_storage
  - registries
market_scope:
  - open_data
  - forecasting
ai_relevance: high
market_integrity_risk: low
last_updated: 2026-09-05
maintainer: stratnergy
card_completeness: complete
related_contributions: []
public_post_url: null
analysis_url: null
interactive_url: null
---

# Storage Buildout Triangulation

## Problem

A reproducible estimate and a dated forecast of installed large-scale battery
capacity in Germany by quarter, triangulated from Marktstammdatenregister
registrations and planned units, grid-connection request statistics, and the
grid development plan, with a measured slippage rate between planned and
actual commissioning derived from archived registry snapshots.

## Why It Matters

Fleet size drives cannibalisation (`EP-006`) and every long-horizon revenue
forecast. Planned units in the registry are known to be optimistic and of
mixed data quality, connection queues are published unevenly, and no public
method reconciles the sources. No dated buildout forecast is scored anywhere.

## Scope

In scope: Germany, units of one megawatt and above, quarterly; a nowcast of
operating capacity, a pipeline view of planned units with commissioning
dates, a slippage-adjusted forecast, and an entry in the scoreboard of
`EP-104`. Out of scope: project-level commercial information and anything not
derivable from public sources.

## Definition Of Done

1. A pipeline over open-MaStR bulk data and archived snapshots.
2. A documented slippage estimator with its uncertainty.
3. A published quarterly series and a dated forecast, scored each quarter
   against the naive baseline.
4. A data-quality register for the registry fields used.

## Baseline

Registry planned commissioning dates taken at face value.

## Existing Artefacts

None tracked for the triangulation itself. Inputs exist: the
Marktstammdatenregister and open-MaStR (`EP-701`), the open-MaStR snapshot
records on Zenodo (for example records 8225106, 14783581, and 14843222),
and irregular connection-request statistics from the regulator and system
operators that need source review.

## Open Questions

- How should units be matched across snapshots when registrations change?
- How should withdrawn or re-registered units be treated?
- How should co-located storage behind a shared connection be counted?

## Review Notes

- Low market-integrity risk: aggregate public registry data.
