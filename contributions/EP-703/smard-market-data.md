---
id: smard-market-data
problem_id: EP-703
title: SMARD Market Data
type: DATASET
project_url: https://www.smard.de/en
repository_url: null
license_code: null
license_data: CC-BY-4.0
openness_level: 3
evidence_strength: C
maturity: PARTIAL
ai_relevance: high
review_status: needs_review
last_checked: 2026-09-05
---

# SMARD Market Data

## Summary

The Bundesnetzagentur's market data portal for Germany: wholesale prices,
generation, consumption, and balancing series with a download centre. Its
data-use page states that downloads are licensed under Creative Commons
Attribution 4.0 with the attribution "Bundesnetzagentur | SMARD.de", and
notes that data originate from the ENTSO-E platform.

## Fit To Problem

The redistributable source for the as-of archive in `EP-703`, and the input
of choice for `EP-004`, `EP-006`, and `EP-102` where ENTSO-E terms would
prevent redistribution. SMARD itself overwrites values and does not preserve
vintages.

## Caveats

- A licence review should confirm that the CC BY terms apply to every series
  offered for download.
- Publication lag and revision behaviour differ by series and are not
  documented on the portal.

## Review Notes

- AI-assisted source check on 2026-09-05: the data-use page was read and the
  licence sentence quoted. Human confirmation pending.
