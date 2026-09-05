# Changelog

## 2026-09-05

Status rules, acceptance criteria, and the previsible-index problem.

- Statuses are now derived from evidence. The validator rejects
  `REFERENCE_AVAILABLE` and `SOLVED_FOR_SCOPE` unless a linked contribution has
  `review_status: accepted`, a source URL, and a licence. It also rejects a
  problem that is more open or better evidenced than its best reference. The
  hard-coded rule that pinned EP-001 to `SOLVED_FOR_SCOPE` was removed.
- EP-601 evidence corrected from B to C; the new rule found that all three of
  its references carry C.
- New status `CANDIDATE_REFERENCE` for problems whose listed references are
  real but unreviewed. EP-001, EP-101, EP-401, and EP-801 moved there from
  green statuses. EP-003 is `SUPERSEDED` by EP-001.
- Every problem card carries `card_completeness` (`stub`, `draft`,
  `complete`). Nine cards are marked stub and show a notice; `complete`
  requires `## Definition Of Done` and `## Baseline` sections.
- EP-001 rewritten as the battery revenue ceiling benchmark; the GigaStorage
  reference moved under it.
- New problem cards: EP-004 Previsible Battery Revenue Index for Germany,
  EP-005 Reference Battery Specification, EP-006 Cannibalisation Metrics From
  Public Data, EP-102 Open Day-Ahead Price Forecast Benchmark, EP-104 Public
  Forecast Scoreboard, EP-703 As-Of Archive Of German Market Data, EP-704
  Storage Buildout Triangulation.
- New reference cards: Modo Energy ME BESS DE (public disclosure),
  epftoolbox, SMARD.
- AI-assisted source checks recorded in Review Notes for GigaStorage, ISEA,
  ASSUME, OpenSTEF, Open Energy Ontology, epftoolbox, SMARD, and Modo; all
  remain `needs_review` until a maintainer confirms.
- Schemas enumerate status, lane, type, maturity, and review status. Status
  definitions rewritten with the enforced rules. Problem template gains
  definition-of-done and baseline sections. Identical market-integrity
  boilerplate replaced by a policy link on stub cards.
- Explorer: candidate-reference and superseded statuses, stub and draft
  pills, four new headline problems, updated legend and seed references.
