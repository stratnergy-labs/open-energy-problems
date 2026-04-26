---
id: or-tools
problem_id: EP-901
title: Google OR-Tools
type: SOFTWARE_INFRASTRUCTURE
project_url: https://developers.google.com/optimization/
repository_url: https://github.com/google/or-tools
license_code: Apache-2.0
license_data: null
openness_level: 4
evidence_strength: B
maturity: REFERENCE_AVAILABLE
ai_relevance: medium
review_status: needs_review
last_checked: 2026-04-26
---

# Google OR-Tools

## Summary

Open-source optimization toolkit for combinatorial optimization, constraint
programming, routing, linear programming, and related problem classes.

## Fit To Problem

This contribution is linked to `EP-901` as candidate infrastructure for energy
scheduling, assignment, routing, and constraint-heavy benchmark cases.

## Caveats

- Energy-specific benchmark fit has not yet been reviewed in this repository.
- Some OR-Tools paths wrap or integrate with other solvers; each benchmark
  should record the backend actually used.
- This card does not imply suitability for all mathematical programming
  formulations used in energy systems.
