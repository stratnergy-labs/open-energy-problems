---
id: epftoolbox
problem_id: EP-102
title: epftoolbox
type: BENCHMARK
project_url: https://epftoolbox.readthedocs.io/
repository_url: https://github.com/jeslago/epftoolbox
license_code: Apache-2.0
license_data: null
openness_level: 4
evidence_strength: B
maturity: REFERENCE_AVAILABLE
ai_relevance: high
review_status: needs_review
last_checked: 2026-09-05
---

# epftoolbox

## Summary

Open-access benchmark for day-ahead electricity price forecasting published
with Lago, Marcjasz, De Schutter, and Weron, Applied Energy 293 (2021). It
ships datasets for five markets including Germany, the LEAR and DNN reference
models, evaluation metrics, and statistical tests for comparing forecasts.

## Fit To Problem

Candidate reference for `EP-102`. The German dataset predates the
quarter-hourly day-ahead auction, and the benchmark would need extending to
cover it.

## Caveats

- Redistribution terms of the bundled datasets are unverified; the underlying
  prices originate from exchanges and the ENTSO-E platform.
- Reproducibility of the published results has not been checked here.

## Review Notes

- AI-assisted source check on 2026-09-05 via the GitHub API: licence
  Apache-2.0, last push 2026-05-18, 387 stars, not archived. Human
  confirmation pending.
