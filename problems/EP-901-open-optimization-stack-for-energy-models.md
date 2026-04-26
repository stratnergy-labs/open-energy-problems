---
id: EP-901
title: Open Optimization Stack for Energy Models
lane: computational-infrastructure
status: PARTIAL
openness_level: 4
evidence_strength: B
geography: Global
asset_class:
  - software
  - energy_models
market_scope:
  - dispatch
  - planning
  - storage_optimization
  - flexibility
ai_relevance: medium
market_integrity_risk: medium
last_updated: 2026-04-26
maintainer: stratnergy
related_contributions:
  - highs
  - scip
  - cbc
  - or-tools
  - pyomo
  - jump
public_post_url: null
analysis_url: null
interactive_url: null
---

# Open Optimization Stack for Energy Models

## Problem

Establish an open, solver-independent optimization stack for energy models so
planning, dispatch, storage, grid, and flexibility studies can be reproduced
without relying by default on proprietary solvers.

## Why It Matters

Many public energy models depend on mathematical optimization. If the model can
only be run with a commercial solver, the code may be open while the result is
still hard to reproduce, audit, teach, or extend.

Open solvers and modelling layers do not need to replace commercial solvers for
every workload. The practical question is narrower: which energy workloads can
already be run credibly on open stacks, and where do important gaps remain?

## Scope

This problem tracks energy-enabling infrastructure: solvers, modelling layers,
interfaces, and benchmark practices that support reproducible energy modelling.
It is not a generic optimization software directory.

Do not treat the existence of an open solver as proof that all energy
optimization workloads are solved. Unit commitment, network-constrained
dispatch, stochastic planning, storage valuation, and flexibility scheduling
may have very different numerical and performance requirements.

## Existing Artefacts

Related contribution IDs are listed in front matter. Source URLs and licence
details require human verification before claims are upgraded.

## Open Questions

- Which representative energy workloads should be used as open solver
  benchmark cases?
- For which LP, MIP, QP, MINLP, and constraint-programming cases are open
  solvers already practical?
- Which modelling layers make it easiest to switch between open and commercial
  solvers without changing the energy model?
- What performance, numerical-stability, and licence caveats should accompany
  solver comparisons?

## Market-Integrity And Licence Notes

Optimization examples should use synthetic, delayed, or public benchmark cases.
Do not add live bidding, operational dispatch instructions, confidential model
parameters, or current asset positions.
