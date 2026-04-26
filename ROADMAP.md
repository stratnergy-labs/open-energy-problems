# Roadmap

## Milestone 0: Repository Skeleton

- Repository structure and policies.
- Problem and contribution templates.
- JSON schemas.
- Fifteen seed problem cards.
- Initial contribution cards.
- Front matter validation.
- JSON and CSV index generation.
- Minimal static preview.

Acceptance:

```text
python3 scripts/validate_frontmatter.py
python3 scripts/build_index.py
```

## Milestone 1: Static Problem Explorer

- Problem index page.
- Problem detail page.
- Contribution/project pages.
- Filters for lane, status, openness level, evidence strength, geography, and AI relevance.
- Simple charts from generated JSON.

## Milestone 2: Review And Scoring Layer

- Nullable 0-10 review scores.
- Generated average score.
- Licence and evidence caveats.
- No leaderboard framing.

## Milestone 3: Source Ledger

- Source-ledger examples.
- Source hashing support.
- Licence status fields.
- Evidence-pack template.

## Milestone 4: OpenClaw Automation

- Daily validation job.
- Weekly link check.
- Monthly digest draft.
- Human approval gates for push, merge, status, and evidence changes.

## Initial GitHub Issues

1. Create repository skeleton and policies.
2. Implement problem-card and contribution-card schemas.
3. Add seed problem cards EP-001 to EP-801.
4. Add initial contribution cards for reference projects.
5. Build front matter validation script.
6. Build JSON/CSV index generator.
7. Build minimal static problem explorer.
8. Add source-ledger schema.
9. Add review score model.
10. Configure GitHub Actions validation.
11. Add OpenClaw maintenance-agent instructions.
12. Draft first public launch post.
