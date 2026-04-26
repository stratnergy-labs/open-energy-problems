---
id: scip
problem_id: EP-901
title: SCIP
type: SOFTWARE_INFRASTRUCTURE
project_url: https://scipopt.org/
repository_url: https://github.com/scipopt/scip
license_code: Apache-2.0
license_data: null
openness_level: 4
evidence_strength: B
maturity: REFERENCE_AVAILABLE
ai_relevance: medium
review_status: needs_review
last_checked: 2026-04-26
---

# SCIP

## Summary

Solver and framework for mixed-integer programming, mixed-integer nonlinear
programming, and constraint integer programming.

## Fit To Problem

This contribution is linked to `EP-901` as a candidate open solver stack for
harder energy optimisation cases where integer or nonlinear structure matters.

## Caveats

- SCIP version and dependency licences must be checked for each build.
- Energy-specific benchmark fit has not yet been reviewed in this repository.
- This card does not claim parity with any commercial solver for any given
  energy workload.
