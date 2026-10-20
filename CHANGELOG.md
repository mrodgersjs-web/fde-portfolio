# Changelog

All notable changes are recorded here. Format follows [Keep a
Changelog](https://keepachangelog.com/en/1.1.0/), and this project
adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.2.1] - 2026-10-19

- This commit replaces the four em dashes in README.md with colons or hyphens to match the house style (no em dashes).

### Added

- `tests/test_repo_hygiene.py`: 4 checks read from the files on disk that
  `.github/CODEOWNERS` assigns `*` to `@mrodgersjs-web`, that
  `.github/copilot-instructions.md` is non-empty, at most 8000 bytes and names a
  test command, that `README.md` carries a `github/actions/workflow/status` badge,
  the "Built by Mike Rodgers - rodgersintelligence.com" footer, a test command and
  only clones `mrodgersjs-web/fde-portfolio`, and that every job under
  `.github/workflows/` sets `timeout-minutes` and never sets `continue-on-error: true`.

### Changed

- `README.md`: the CI badge now uses the shields
  `github/actions/workflow/status/mrodgersjs-web/fde-portfolio/ci.yml` form, the
  footer is the plain literal "Built by Mike Rodgers - rodgersintelligence.com",
  and the test counts read 44 (the number `pytest -q` prints after the hygiene
  tests landed) instead of 40.
- `.github/copilot-instructions.md` rewritten to 2413 bytes: what the repository is,
  the layout, the exact commands (`pip install -e '.[dev]'`, `ruff check .`,
  `pytest -q`, `fde-portfolio check`, `bash scripts/smoke.sh`), conventions
  (conventional commits, a test for every change, no secrets, no machine paths) and
  the truth rule that every number in docs comes from a command run in this
  repository.
- `.github/workflows/ci.yml`, `.github/workflows/rig-lattice.yml`,
  `.github/workflows/smoke.yml`: `timeout-minutes: 15` on every job.

### Verified

- Fresh venv `python3.12 -m venv`, `pip install -e '.[dev]'`, `ruff check .` clean,
  `pytest -q --cov=fde_portfolio` 44 passed with 85 percent package coverage,
  `fde-portfolio check` reports every playbook valid.

## [0.2.0] - 2026-10-19

### Added

- **Structured playbook data** in
  `src/fde_portfolio/playbooks/` for the five engagement phases:
  `discovery` (8 items), `evaluation` (7 items), `architecture` (8
  items), `go-live` (8 items), `handoff` (7 items). Every item
  declares a stable `id`, a `type` (`question` / `task` /
  `decision` / `evidence` / `owners`), a default owner, and prose.
- **Two JSON Schemas** (`file.schema.json` and
  `playbook.schema.json`) in `src/fde_portfolio/schemas/`. The
  loader inlines the per-item ref so jsonschema resolves it
  without a `Store`.
- **`fde-portfolio` CLI** with `list`, `check`, `checklist`, and
  `build` subcommands. `check` runs the validator; `checklist`
  renders one playbook as a Markdown checklist; `build` renders
  the full project worksheet (all five phases) to stdout or a
  file the caller chooses.
- **Test suite** at `tests/`: 40 tests pass on Python 3.12,
  package coverage 85%. Includes schema validation, no-client-name
  scan, no-invented-outcome scan, CLI dispatch, golden-output,
  parametrized per phase.
- **Community files**: `CONTRIBUTING.md`, `SECURITY.md`,
  `CODE_OF_CONDUCT.md`, `CHANGELOG.md`, `.github/dependabot.yml`,
  issue + PR templates.
- **docs/architecture.md** with the data contract, lifecycle
  sequence diagram, "how to add or change a checklist item"
  recipe, public-guard section, performance budget.

### Changed

- `pyproject.toml` declares an installable package
  (`pip install -e '.[dev]'`, console script `fde-portfolio`),
  full project URLs, `[project.urls]` block, line-length 110,
  broader lint scope.
- `docs/architecture.md` rewritten from a hand-drawn ASCII flow
  to a data-and-CLI architecture with mermaid diagrams and the
  public-guard rules.

## [0.1.0] - 2026-08-07

First public release as a documentation-only FDE review hub.
`README.md` and the `docs/` set shipped; the CLI and the structured
playbook data came in 0.2.0.
