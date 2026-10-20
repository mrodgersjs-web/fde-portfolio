# Changelog

All notable changes are recorded here. Format follows [Keep a
Changelog](https://keepachangelog.com/en/1.1.0/), and this project
adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

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
