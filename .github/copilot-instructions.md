# Copilot instructions

## What this repo is

`fde-portfolio` is a Forward Deployed Engineering playbook repository: five
engagement-phase checklists (`discovery`, `evaluation`, `architecture`,
`go-live`, `handoff`) shipped as structured YAML, validated against JSON
Schemas, and rendered to Markdown worksheets by the `fde-portfolio` CLI. The
checklists are templates with no customer names, no invented outcomes and no
dollar figures.

## Layout

- `src/fde_portfolio/playbooks/` - the five YAML playbooks, the source of truth.
- `src/fde_portfolio/schemas/` - `file.schema.json` and `playbook.schema.json`.
- `src/fde_portfolio/` - package: `loader.py`, `render.py`, `cli.py`.
- `tests/` - pytest suite: schema, render, CLI, drift scans, repo hygiene.
- `examples/` - `playbook_demo/run.sh` plus audit-log and eval-harness notes.
- `docs/` - architecture, customer discovery, evaluation, implementation,
  public boundary.
- `scripts/smoke.sh` - legacy file-existence smoke for the docs surface.
- `.github/workflows/` - `ci.yml` (lint, tests, gate), `smoke.yml`, `rig-lattice.yml`.

## Commands

Run from the repository root in a virtual environment:

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -e '.[dev]'   # installs pytest, pytest-cov, ruff, jsonschema
ruff check .              # lint
pytest -q                 # full test suite
pytest -q --cov           # tests with coverage
fde-portfolio check       # every playbook validates against its schema
bash scripts/smoke.sh     # smoke
```

## Conventions

- Conventional commit messages: `feat:`, `fix:`, `test:`, `docs:`, `ci:`, `chore:`.
- Every behavior change lands with a test that exercises it and passes on a clean install.
- A new checklist item means editing the matching YAML under
  `src/fde_portfolio/playbooks/`; the schemas refuse duplicate ids and items that
  miss `title`, `description`, or `type`.
- No secrets, client PII, prospect lists, auth material or private monorepo content
  in any tracked file. No machine paths such as `/Users/...` or `~/Developer/...`.
- Keep human approval at real risk boundaries, as `docs/public-boundary.md` states.

## Truth rule

Any number in docs, comments, or commit messages must come from a command run in
this repository, for example a test count from `pytest -q` or an item count from
`fde-portfolio list`. Quote the command and its output rather than a memory of it.
