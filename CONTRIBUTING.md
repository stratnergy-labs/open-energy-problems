# Contributing

Contributions should add inspectable problem statements, reproducible artefacts,
careful source notes, review comments, or clearly labelled AI-assisted attempts.

Small contributions are useful. A good first contribution is often one checked
source URL, one licence clarification, one missing reference, or one correction
to a problem card.

## Ways To Help

- Suggest a reference with the [new contribution form](https://github.com/stratnergy-labs/open-energy-problems/issues/new?template=new-contribution.yml).
- Review an entry with the [review note form](https://github.com/stratnergy-labs/open-energy-problems/issues/new?template=review-request.yml).
- Propose a problem with the [new problem form](https://github.com/stratnergy-labs/open-energy-problems/issues/new?template=new-problem.yml).
- Improve a card directly using the templates in `templates/`.

See [How To Contribute](HOW_TO_CONTRIBUTE.md) for the short workflow and guardrails.

## Local Checks

After editing problem cards, contribution cards, or relationship cards, run:

```bash
python3 scripts/validate_frontmatter.py
python3 scripts/build_index.py
```

## Guardrails

Do not add live trading logic, current positions, confidential data, restricted
datasets, or unsupported claims. Separate code licence, data licence, and reuse
rights. Label AI-assisted contributions and note what was independently checked.
