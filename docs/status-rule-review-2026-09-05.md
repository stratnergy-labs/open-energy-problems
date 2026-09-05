# Status Rule Review

Date: 2026-09-05

This note records why five problems lost their green status, what rule now
governs status, and which facts in the new cards were checked and how.

## Finding

The register's thesis is that claims and evidence must be kept apart. On
2026-05-09 the snapshot showed five green problems while zero contribution
cards had passed source and licence review. EP-001 was pinned to
`SOLVED_FOR_SCOPE` by a hard-coded validator rule. EP-003 was
`REFERENCE_AVAILABLE` on a card with a null project URL. The seed-fit review of
2026-04-26 had already asked for a stricter status policy; it had not been
implemented.

## Rule

Status is derived from linked references. The validator enforces the table in
`index/status_definitions.md`. In short: no green without an accepted,
licensed, sourced reference; `OPEN` means nothing is listed;
`CANDIDATE_REFERENCE` means something relevant is listed but unreviewed; a
problem cannot be more open or better evidenced than its best reference.

## Reclassifications

| Problem | Before | After | Reason |
| --- | --- | --- | --- |
| EP-001 | SOLVED_FOR_SCOPE, level 5, B | CANDIDATE_REFERENCE, level 4, B | No accepted review. Both references are hindsight ceilings; card rewritten to say so. |
| EP-003 | REFERENCE_AVAILABLE, level 5, B | SUPERSEDED by EP-001 | Same problem as EP-001; its only reference had no URL. |
| EP-101 | REFERENCE_AVAILABLE | CANDIDATE_REFERENCE | No accepted review. |
| EP-401 | REFERENCE_AVAILABLE | CANDIDATE_REFERENCE | No accepted review. |
| EP-801 | REFERENCE_AVAILABLE | CANDIDATE_REFERENCE | No accepted review; repository licence differs from the card. |
| EP-601 | PARTIAL, evidence B | PARTIAL, evidence C | Caught by the new rule: all three linked references carry evidence C. |

Contribution changes: ISEA openness 5 to 3 and evidence B to C (public
methodology verified; code URL and licence not retrieved); GigaStorage openness
5 to 4 (open code verified; reproducibility not checked).

## Why the previsible index is the flagship

The two public battery benchmarks optimise against realised prices. They are
honest ceilings, not strategies anyone can follow. A commercial German
benchmark exists that is systematic and regular but not transparent. An index
in Lo's sense, transparent, investable, and systematic, with decisions that use
only information available at each market's gate closure, is missing. It is
also the outcome series a forecast scoreboard (EP-104) needs. EP-004 states
the problem with a definition of done and a baseline; EP-005 (reference
battery), EP-703 (as-of data) and EP-203 (replay harness) are its
dependencies.

## What was checked, and how

Checks were AI-assisted (Claude, in a Claude Code session directed by the
maintainer) on 2026-09-05. Nothing below is an accepted review; each item is
recorded in the relevant card's Review Notes for a maintainer to confirm.

- GitHub API: licence, last push, stars, archived flag for GigaStorage,
  OpenSTEF, ASSUME, Open Energy Ontology, epftoolbox.
- ISEA methodology site: wholesale step quoted as computing "the best trading
  profile based on the available price spread on each day"; day-ahead prices
  from ENTSO-E, intraday from EPEX; developed with enspired GmbH.
- Modo ME BESS DE launch article: simulated asset, 1h/2h/4h, 80% calibration
  factor validated against GB.
- SMARD data-use page: CC BY 4.0 with attribution "Bundesnetzagentur |
  SMARD.de".
- Lo, A. W. (2016), "What Is an Index?", Journal of Portfolio Management
  42(2), 21-36: index defined as transparent, investable, systematic.
- Zenodo record numbers for open-MaStR snapshots taken from search results.

Not verified: the ISEA GitLab repository URL and licence (host refused
connections); redistribution terms of the datasets bundled with epftoolbox;
whether the CC BY terms cover every SMARD series; the exact docs URL of
epftoolbox.

## Known limitations left for follow-up

- The openness ladder is code-centric; open data has no rung of its own, so
  datasets are recorded at level 3. A single ladder with named rungs would be
  clearer than openness plus evidence.
- `ai_relevance` is undefined on the site and mostly `high`.
- Nine stub cards still need problem statements. They are visibly marked.
- The `site/` directory holds an older copy of the explorer and should be
  removed or regenerated.
