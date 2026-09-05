---
id: EP-103
title: Forecast Decision-Quality Benchmark
lane: forecasting
status: OPEN
openness_level: 0
evidence_strength: D
geography: Global
asset_class:
  - load
  - battery_storage
  - flexibility
market_scope:
  - forecasting
  - dispatch
ai_relevance: high
market_integrity_risk: medium
last_updated: 2026-09-05
maintainer: stratnergy
card_completeness: stub
related_contributions:
  []
public_post_url: null
analysis_url: null
interactive_url: null
---

# Forecast Decision-Quality Benchmark

> **Stub.** This card states a label, not yet a problem. It needs a problem statement, a definition of done and a baseline before it can leave `stub`. Start from the [problem-card template](../templates/problem-card-template.md).

## Problem

Evaluate forecasts by downstream trading or dispatch value, not only error metrics.

## Why It Matters

Lower forecast error does not always produce better operational decisions. This
problem asks how forecasts should be judged when the downstream objective is
dispatch quality, trading value, grid relief, or avoided imbalance cost.

## Scope

Decision-quality evaluation should use synthetic or delayed examples and avoid publishing exploitable live strategy.

## Existing Artefacts

Related contribution IDs are listed in front matter. Source URLs and licence details require human verification before claims are upgraded.

## Open Questions

- Which evidence is reproducible from public material?
- Which data can be reused, cited only, or linked only?
- What review would change the status or evidence-strength classification?

## Review Notes

- No card-specific caveats recorded yet. General guardrails: [Market Integrity Policy](../MARKET_INTEGRITY_POLICY.md) and [Data and Licence Policy](../DATA_AND_LICENSE_POLICY.md).
