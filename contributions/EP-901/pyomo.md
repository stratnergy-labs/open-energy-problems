---
id: pyomo
problem_id: EP-901
title: Pyomo
type: SOFTWARE_INFRASTRUCTURE
project_url: https://www.pyomo.org/
repository_url: https://github.com/Pyomo/pyomo
license_code: BSD-3-Clause
license_data: null
openness_level: 4
evidence_strength: B
maturity: REFERENCE_AVAILABLE
ai_relevance: medium
review_status: needs_review
last_checked: 2026-04-26
---

# Pyomo

## Summary

Python-based open-source optimization modelling package for formulating,
solving, and analysing structured optimization models.

## Fit To Problem

This contribution is linked to `EP-901` as a solver-independent modelling layer
that can help energy models run against both open and commercial solvers.

## Caveats

- Energy-specific benchmark fit has not yet been reviewed in this repository.
- Model reproducibility depends on the solver, input data, parameters, and
  environment, not only on the modelling layer.
- Code licence and model-instance/data licences must be reviewed separately.
