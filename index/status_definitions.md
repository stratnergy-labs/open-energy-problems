# Status Definitions

Status is derived from evidence, not asserted. `scripts/validate_frontmatter.py`
enforces the rules below, so a card cannot claim more than its linked references
support.

| Status | Meaning | Rule enforced |
| --- | --- | --- |
| `OPEN` | Problem stated; no reference listed. | `related_contributions` must be empty. |
| `CANDIDATE_REFERENCE` | A relevant open reference is listed but has not passed source and licence review. | At least one related contribution. |
| `PARTIAL` | Listed references cover part of the problem; important gaps remain. | At least one related contribution. |
| `PUBLIC_DISCLOSURE` | A public commercial or institutional disclosure exists; no open reference. | A related contribution of type `PUBLIC_DISCLOSURE`. |
| `REFERENCE_AVAILABLE` | A reviewed open reference exists for the problem. | At least one related contribution with `review_status: accepted`, a source URL, and a licence. |
| `SOLVED_FOR_SCOPE` | A reviewed open reference meets the card's definition of done for its stated scope. | Same as `REFERENCE_AVAILABLE`, plus the card must be `complete`. |
| `SUPERSEDED` | Merged into or replaced by another card. | `superseded_by` names another existing problem. |
| `BLOCKED` | Progress prevented by licence, data rights, or safety constraints. | Explain in the card. |
| `NEEDS_REVIEW` | Classification itself is disputed. | Explain in the card. |
| `REJECTED_OUT_OF_SCOPE` | Not a register problem. | Explain in the card. |

Further rules:

- A problem's `openness_level` cannot exceed the highest `openness_level` among
  its related contributions (0 when none are listed).
- A problem's `evidence_strength` cannot be stronger than the strongest related
  contribution (D when none are listed).
- `card_completeness` is `stub` (a label, not yet a problem), `draft` (problem
  stated, no definition of done), or `complete` (has `## Definition Of Done`
  and `## Baseline`). A card with those sections cannot be a stub.
- Only maintainers change `review_status` to `accepted`, and only after source,
  licence, fit, evidence, and safety checks.

Traffic lights on the public site: green for `REFERENCE_AVAILABLE` and
`SOLVED_FOR_SCOPE`; yellow for `CANDIDATE_REFERENCE`, `PARTIAL`, and
`PUBLIC_DISCLOSURE`; red for `OPEN`; grey for the rest.
