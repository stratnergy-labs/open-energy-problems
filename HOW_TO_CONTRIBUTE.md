# How To Contribute

Small, sourced improvements are welcome. The register gets better when people
check one link, clarify one licence, add one missing reference, or sharpen one
problem statement.

## Good Contributions

A good contribution is specific:

- it names the problem or reference it relates to;
- it links to the source being checked;
- it says what the source does and does not show;
- it separates code licence, data licence, and reuse rights;
- it avoids unsupported claims about performance or market impact.

## Useful Ways To Help

### Suggest a reference

Use this when you know an open-source project, dataset, benchmark, schema,
simulator, public disclosure, or methodology that belongs in the register.

Open a [new contribution issue](https://github.com/stratnergy-labs/open-energy-problems/issues/new?template=new-contribution.yml)
with the source URL, the problem it may fit, and any licence notes you can find.

### Review an entry

Use this when a tracked reference looks relevant, but its source, licence, fit,
evidence strength, or safety caveat needs checking.

Open a [review note](https://github.com/stratnergy-labs/open-energy-problems/issues/new?template=review-request.yml).
A useful review can be small: one verified source URL, one corrected licence
field, or one caveat that prevents overclaiming.

### Propose a problem

Use this when a recurring energy-market or grid question is important enough to
track, but the open solution landscape is unclear.

Open a [new problem issue](https://github.com/stratnergy-labs/open-energy-problems/issues/new?template=new-problem.yml)
and describe the scope, geography, why it matters, and any known references.

### Improve a card

Use this when you want to edit a problem card or reference card directly. Start
from the templates in `templates/`, keep the YAML front matter valid, and open a
pull request.

After local edits, run:

```bash
python3 scripts/validate_frontmatter.py
python3 scripts/build_index.py
```

## What Not To Submit

Do not submit:

- live trading positions;
- current bids or dispatch instructions;
- confidential optimiser logic;
- inside information;
- customer, asset, or operational data that is not public and reusable;
- copies of restricted datasets;
- claims that cannot be checked from public sources.

AI-assisted contributions are welcome, but disclose the tool used, what it
helped with, and which claims were independently checked.
