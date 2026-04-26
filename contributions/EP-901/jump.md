---
id: jump
problem_id: EP-901
title: JuMP
type: SOFTWARE_INFRASTRUCTURE
project_url: https://jump.dev/
repository_url: https://github.com/jump-dev/JuMP.jl
license_code: MPL-2.0
license_data: null
openness_level: 4
evidence_strength: B
maturity: REFERENCE_AVAILABLE
ai_relevance: medium
review_status: needs_review
last_checked: 2026-04-26
---

# JuMP

## Summary

Julia modelling language and supporting package ecosystem for mathematical
optimization.

## Fit To Problem

This contribution is linked to `EP-901` as a solver-independent modelling layer
used by several optimization-heavy energy modelling projects.

## Caveats

- Energy-specific benchmark fit has not yet been reviewed in this repository.
- Model reproducibility depends on solver choice, solver version, inputs, and
  execution environment.
- Code licence and model-instance/data licences must be reviewed separately.
