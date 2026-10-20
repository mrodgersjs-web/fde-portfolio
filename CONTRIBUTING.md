# Contributing

Thanks for taking the time to sharpen the FDE playbook data or the
CLI. This document covers both.

## What we accept

- A **new checklist item** for an existing playbook, with a
  matching `id`, a `type`, and prose that's clear in one read.
- A **new playbook** for a phase we don't yet cover (a sixth
  phase has to be added to `PHASES` in `loader.py` and to the
  `phase` enum in `schemas/file.schema.json`).
- A **bug fix** to the loader, validator, renderer, or CLI,
  with a test that fails before the change and passes after.

## What we reject

- A PR whose diff introduces a customer name, a real dollar
  figure, a real person, or a fabricated outcome. The tests
  `test_no_client_names_anywhere_in_playbook_data` and
  `test_no_invented_outcomes` will refuse the build.
- A change that weakens or removes the schema validator, the
  no-client-name scan, or the no-invented-outcome scan.
- A change to the CLI that adds a destructive default; the
  default of every command today is "no I/O unless you ask".

## Local setup

```
git clone https://github.com/mrodgersjs-web/fde-portfolio.git
cd fde-portfolio
python3 -m venv .venv && source .venv/bin/activate
pip install -e '.[dev]'
ruff check .
pytest -q
```

This is the CI bar.

## Process

1. **Open an issue first** for any non-trivial change. Schema
   edits, new playbooks, and CLI behavior changes are easy to
   discuss as text before code lands.
2. **Tests.** Every public function added or changed gets a
   test. Coverage below 80% on `fde_portfolio/` is not accepted.
3. **Lint clean.** `ruff check .` must pass on the application
   source (`src/fde_portfolio/`, `tests/`). The vendored RIG
   lattice hooks under `mcp/` and `.rig/` are excluded.
4. **Generated artifacts are generated.** The README, docs, and
   rendered project worksheet are produced by tools in this
   repo or in adjacent repos. Hand edits to outputs of those
   tools are drift by definition.

## Review

Reviewer focus:

- Does the change preserve the data-as-source-of-truth property?
  The CLI and the tests should never silently materialize a
  playbook that was not in the YAML.
- For an item addition, does the prose explicitly name the
  customer-side owner and the action the operator takes?
- For a schema change, is the migration path clear, and does
  `validate_playbook` still produce a one-line reason on every
  failure?

## License

Your contribution is MIT-licensed under the same terms as the rest
of this project (`LICENSE`).
