---
id: isea-battery-revenue-index
problem_id: EP-001
title: ISEA Battery Revenue Index
type: REFERENCE_SOLUTION
project_url: https://battery-charts.de/revenue-index/
repository_url: null
license_code: null
license_data: null
openness_level: 3
evidence_strength: C
maturity: REFERENCE_AVAILABLE
ai_relevance: low
review_status: needs_review
last_checked: 2026-09-05
---

# ISEA Battery Revenue Index

## Summary

Public revenue-potential index for large battery storage in Germany, developed
by ISEA at RWTH Aachen together with enspired GmbH. The methodology site
documents single-market calculations for FCR, aFRR, day-ahead, and intraday
products and a phased cross-market combination. The wholesale step computes
"the best trading profile based on the available price spread on each day"
from realised prices, so the index is a hindsight ceiling. The site states the
index is designed for comparability rather than achievable revenue.

## Fit To Problem

Candidate reference for the ceiling benchmark in `EP-001`. It does not satisfy
`EP-004`: the strategy is not previsible.

## Caveats

- The methodology site says code is available on GitLab, but the repository
  URL and its licence have not been retrieved; the RWTH host refused
  connections on 2026-09-05.
- Battery parameters are user-configurable; the configuration behind the
  published series needs to be recorded.
- Co-developed with a trading company; note for independence review.

## Review Notes

- AI-assisted source check on 2026-09-05: methodology pages read; the
  perfect-foresight characterisation is quoted from the wholesale page.
  Openness lowered from 5 to 3 (public methodology) and evidence from B to C
  until the code and a reproducible run are verified.
