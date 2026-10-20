## What

One paragraph: what this PR ships and why.

## How

The mechanical change in one sentence per file touched. Tests added in
the same commit as the behavior they cover.

## Verification

```
$ python3 -m venv .venv && source .venv/bin/activate
$ pip install -e '.[dev]'
$ ruff check .
$ pytest -q
```

Paste the actual output below.

```
<paste here>
```

## Drift

```
$ fde-portfolio check
```

Must exit 0 — `tests/test_playbooks.py`'s `test_every_playbook_validates[*]`
is the equivalent for CI.

## Checklist

- [ ] Tests added in the same commit as the behavior they cover
- [ ] `ruff check .` clean on application source (`src/fde_portfolio/`, `tests/`)
- [ ] `pytest -q --cov` shows coverage stays at or above 80% on the package
- [ ] `fde-portfolio check` exits 0
- [ ] No customer names in any YAML (the schema + tests enforce this)
- [ ] No invented outcome numbers in any YAML (the test enforces this)
- [ ] No "1000x", "novel", or superlative claims added
- [ ] No prices, client names, or personal data

## Linked issue

Closes #<number>.
