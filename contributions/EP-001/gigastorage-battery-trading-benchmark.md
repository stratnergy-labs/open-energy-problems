---
id: gigastorage-battery-trading-benchmark
problem_id: EP-001
title: GigaStorage Battery Trading Benchmark
type: BENCHMARK
project_url: https://github.com/GigaStorage/battery-trading-benchmark
repository_url: https://github.com/GigaStorage/battery-trading-benchmark
license_code: Apache-2.0
license_data: null
openness_level: 4
evidence_strength: B
maturity: REFERENCE_AVAILABLE
ai_relevance: medium
review_status: needs_review
last_checked: 2026-09-05
---

# GigaStorage Battery Trading Benchmark

## Summary

Open-source tool maintained by GIGA Storage that, in its own words, determines
"the optimal value an Energy Storage System (ESS) can earn on a specific
electricity market". It optimises against realised prices, so its output is a
hindsight ceiling. Current market coverage is Dutch.

## Fit To Problem

Candidate reference for the ceiling benchmark in `EP-001`. It is not a
previsible strategy and does not use a shared reference battery, so it does
not address `EP-004` or `EP-005`.

## Caveats

- Dutch market scope; German products are not covered.
- Reproducibility of a published number has not been checked; the card
  records open code, not a reproducible benchmark.
- Battery assumptions are tool defaults, not a public standard.

## Review Notes

- AI-assisted source check on 2026-09-05 via the GitHub API: repository
  exists, licence Apache-2.0, last push 2026-08-17, 11 stars, not archived.
  Human confirmation pending before `review_status` changes.
