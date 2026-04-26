---
id: cbc
problem_id: EP-901
title: COIN-OR CBC
type: SOFTWARE_INFRASTRUCTURE
project_url: https://coin-or.github.io/Cbc/intro.html
repository_url: https://github.com/coin-or/Cbc
license_code: EPL-2.0
license_data: null
openness_level: 4
evidence_strength: B
maturity: REFERENCE_AVAILABLE
ai_relevance: medium
review_status: needs_review
last_checked: 2026-04-26
---

# COIN-OR CBC

## Summary

Open-source mixed-integer programming solver from the COIN-OR ecosystem.

## Fit To Problem

This contribution is linked to `EP-901` as a candidate open MIP solver for
energy model cases where mixed-integer formulations need a reproducible solver
path.

## Caveats

- Energy-specific benchmark fit has not yet been reviewed in this repository.
- Packaging and licence details should be checked from the exact distribution
  used in any benchmark.
- This card does not treat CBC as a drop-in substitute for commercial solvers in
  all energy optimisation cases.
