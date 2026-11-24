# Blueprint: fde-portfolio field record (brownfield, single-file mode)

Project slug: `fde-field-record`. Repository: `mrodgersjs-web/fde-portfolio`. Branch
`aside/tier2-portfolio-20261123`, base commit `15cba0fbc6bf08dfabd060b1ab1e97d0512d22ba` (`15cba0f`,
`origin/main` on 2026-11-23). Template: the-architect `blueprint-template.md`, 20 numbered sections.
Every command runs from the repository root. This file is committed to the repository, so it names no
local machine path and no private document path.

## 1. Project Overview & Non-Goals

### Vision
`fde-portfolio` is a public Forward Deployed Engineering repository: five YAML engagement playbooks,
two JSON Schemas and a CLI that renders a worksheet. It shows a checklist engine and no deployment
evidence. This change adds a labeled field record of confirmed engagements (sector pseudonyms only),
one clearly SYNTHETIC worked engagement whose eval numbers come from running code in the repo, a
failure taxonomy, three ADRs and a runbook, and reorders the README so evidence comes first.

### Current state
- Package `src/fde_portfolio/` (`cli.py`, `loader.py`, `render.py`, `playbooks/*.yaml`,
  `schemas/*.json`); console script `fde-portfolio = fde_portfolio.cli:main`.
- Tests `tests/test_cli.py`, `tests/test_playbooks.py`, `tests/test_render_headings.py`,
  `tests/test_repo_hygiene.py`; `pytest -q` exits 0 with 0 failed on the base commit.
- Docs under `docs/`; `CASE-STUDIES.md` holds six fleet operations; README line 27 carries a stale
  repository census count.
- CI `.github/workflows/ci.yml` (ruff, pytest, `fde-portfolio check`, `scripts/smoke.sh`), `smoke.yml`,
  `rig-lattice.yml`. Runtime deps PyYAML, jsonschema; dev deps pytest, pytest-cov, ruff.

### Target state
- `CLAUDE.md` (commands first) and explicit `blueprints` exclusions in `pyproject.toml`.
- `docs/worked-engagement/`: `README.md`, `eval-set.jsonl`, `scorer.py`, `systems.py`, `run_eval.py`,
  and the runner's outputs `runs/baseline.json`, `runs/improved.json`.
- `docs/field-record.md`, `docs/failure-taxonomy.md`, `docs/runbook.md`,
  `docs/adr/0001-deterministic-offline-eval.md`, `docs/adr/0002-confidence-gate-abstain-to-human.md`,
  `docs/adr/0003-claim-labels-and-pseudonyms.md`.
- README order: field record, worked engagement, checklist CLI; no repository count; no new image
  line beyond the three existing badges (the owner inserts media under the H1 in a later commit).
- New tests `tests/test_scorer.py`, `tests/test_systems.py`, `tests/test_field_record.py`,
  `tests/test_docs.py`.

### Delta
Additive docs and stdlib-only Python under `docs/worked-engagement/`; four new test files; README
reorder; `scripts/smoke.sh` requires three more docs; two config lines in `pyproject.toml`. No change
to `src/`.

### Users
| Persona | What they come to do | Frequency |
|---|---|---|
| Hiring manager for an FDE role | judge field impact and eval discipline in five minutes | once |
| Technical interviewer | rerun the worked engagement and question the ADRs | once |
| Maintainer | update a field-record fact after it is confirmed | monthly |

### Goals — v1 scope
1. A field record whose every public claim is a `[confirmed]` corpus fact, with real gaps listed under "Not yet evidenced".
2. A reproducible synthetic eval: one command regenerates byte-identical baseline and improved runs.
3. Decision, failure and operations docs an interviewer can question.
4. A README that leads with evidence.

### Non-Goals — explicitly out of scope for v1
| Not building | Why not now | Revisit when |
|---|---|---|
| Real customer or employer names, or logos | public boundary: sector pseudonyms only | a client gives written approval |
| Any compensation, rate or dollar figure | never published here | never |
| Any image line or media file | the owner adds media under the H1 in a later commit | that commit |
| Changes to `src/fde_portfolio/`, the CLI, playbooks or schemas | held constant (§5) | a separate blueprint |
| New runtime or dev dependencies | the eval code is stdlib only | an eval needs a model call |
| Edits to `.github/workflows/*`, package metadata, version or dependencies | held constant (§5) | a separate blueprint |
| Sealing the RIG proof packet (four ratios, `.rig/proofs/`) | a separate owner step after Mike confirms | that step |
| Push, remote tag, release or pull request | Gate-D: Mike's exact-text approval | Mike approves |
| An LLM inside the worked engagement | numbers must reproduce offline, byte for byte | a model-backed variant is scoped |
| Any portrait or likeness of Mike Rodgers | standing policy | never |

The builder must not implement anything in this table.

### Success metrics
| Metric | Target | How measured |
|---|---|---|
| Field-record numbers off the allowlist | 0 on 2026-11-23 | `tests/test_field_record.py` |
| Eval reproducibility | both runs byte-identical on rerun | step 5 Verify |
| Suite | 0 failed | `/tmp/fde-py312/bin/python -m pytest -q` |

## 2. Tech Stack
| Layer | Choice | Why |
|---|---|---|
| Language | Python 3.12 in a build venv at `/tmp/fde-py312` (package supports 3.10+); the repo's own `.venv` is never used or modified | existing package |
| Env tool | `uv` 0.13.1 observed on the build machine | creates `/tmp/fde-py312` |
| Eval code | Python standard library (`json`, `re`, `pathlib`) | no new deps |
| Tests | pytest (existing dev dep) | existing suite |
| Lint | ruff (existing dev dep) | existing gate |

## 3. Directory Structure
```
fde-portfolio/
├── AGENTS.md                                   # step 1 (one appended line)
├── CLAUDE.md                                   # step 1
├── pyproject.toml                              # step 1 (two exclusion lines)
├── README.md                                   # step 10
├── scripts/smoke.sh                            # step 10
├── blueprints/fde-field-record-blueprint.md    # input, committed before Bootstrap
├── docs/
│   ├── field-record.md                         # step 7
│   ├── failure-taxonomy.md                     # step 8
│   ├── runbook.md                              # step 8
│   ├── adr/0001-deterministic-offline-eval.md          # step 9
│   ├── adr/0002-confidence-gate-abstain-to-human.md    # step 9
│   ├── adr/0003-claim-labels-and-pseudonyms.md         # step 9
│   └── worked-engagement/
│       ├── eval-set.jsonl                      # step 2
│       ├── scorer.py                           # steps 2-3
│       ├── systems.py                          # step 4
│       ├── run_eval.py                         # step 5
│       ├── runs/baseline.json                  # written by run_eval.py, step 5
│       ├── runs/improved.json                  # written by run_eval.py, step 5
│       └── README.md                           # step 6
└── tests/
    ├── test_scorer.py                          # steps 2-3
    ├── test_systems.py                         # steps 4-5
    ├── test_field_record.py                    # step 7
    └── test_docs.py                            # steps 6, 8, 9, 10
```

### Existing inputs (read, not changed)
`.github/copilot-instructions.md`, `CASE-STUDIES.md`, `tests/test_repo_hygiene.py`,
`tests/test_cli.py`, `tests/test_playbooks.py`, `tests/test_render_headings.py`, and the four original
smoke inputs `docs/implementation-playbook.md`, `docs/architecture.md`,
`docs/evaluation-strategy.md`, `docs/public-boundary.md`.

### Delta
Added: `CLAUDE.md`, every `docs/worked-engagement/` file, `docs/field-record.md`,
`docs/failure-taxonomy.md`, `docs/runbook.md`, the three ADRs and the four test files. Modified:
`README.md`, `scripts/smoke.sh`, `pyproject.toml`, `AGENTS.md` (one appended bridge line). Untouched: `src/`, `.github/`, every other file.

## 4. Data Model
Eval item, one JSON object per line of `eval-set.jsonl`:
`{"id": "T001", "text": "<synthetic ticket>", "label": "<route>"}`; `label` is one of `billing`,
`refund`, `fraud`, `access`, `other`; ids unique.

Prediction: `{"id": str, "route": str | null, "confidence": float}`; `route` null = abstain (sent to
a human).

Score object (from `scorer.score`): keys `system` (str), `n`, `answered`, `abstained`, `correct`,
`wrong_auto_routes` (int), `accuracy`, `answered_accuracy`, `coverage` (float, rounded to 4 places).
`accuracy = correct / n`; `answered_accuracy = correct / answered`, 0.0 when `answered` is 0;
`coverage = answered / n`; a wrong auto route is an answered prediction whose route differs from the
label. Run file `runs/<system>.json` = the score object plus key `predictions` (list of prediction
objects in eval-set order), serialized as the UTF-8 bytes of `json.dumps(obj, indent=2, sort_keys=True) + "\n"` (LF line
endings, one trailing LF).

### Delta
Added: the eval item, prediction, score and run-file contracts above. Existing playbook and schema
data models are unchanged.

## 5. API Design
- `scorer.load_eval(path) -> list[dict]`: raises `ValueError` on an empty file, a missing key, a label outside the
  five routes, or a duplicate id.
- `scorer.score(system, items, preds) -> dict`: raises `ValueError` when `items` is empty, when
  prediction ids contain a duplicate, or when the prediction id sequence is not exactly the item id
  sequence in the same order (no join by id; reordered predictions are rejected).
- `systems.baseline(text) -> tuple[str | None, float]` (always answers) and
  `systems.improved(text) -> tuple[str | None, float]` (may return route `None`).
- `python docs/worked-engagement/run_eval.py`: writes both run files, prints exactly two lines in the
  form `<system> accuracy=<f> answered_accuracy=<f> coverage=<f> wrong_auto_routes=<int>` (floats
  formatted `:.4f`), `baseline` first, and exits 0. `--out DIR` redirects both run files. The input is always `eval-set.jsonl` in the runner's own folder.

### Delta
Added: the `scorer`, `systems` and `run_eval.py` interfaces above. Modified: none of the existing
package interfaces.

### Interfaces held constant
- `fde-portfolio` subcommands `list`, `check`, `checklist`, `build` and their output.
- Playbook YAML ids, both JSON Schemas, `pyproject.toml` dependencies and version `0.2.0`.
- All files under `.github/workflows/`.

## 6. Frontend Architecture
NOT APPLICABLE — documentation and a stdlib script; no UI. No step draws a contract from this section.

## 7. Design System
NOT APPLICABLE — no UI. No step draws a contract from this section.

## 8. Authentication & Authorization
NOT APPLICABLE — no service, no users, no secrets.

## 9. BUILD ORDER

§10 Bootstrap runs once before step 1. Steps run in order; each runs Do, Done when, Verify, then
Checkpoint. Every Verify block exits 0 on a correct step under `set -e`. Before each Checkpoint the builder also runs cumulative gate G below; every line must exit 0. G holds
every non-step-specific check of steps 1-9 (lint, full pytest, installed CLI, both config literals). Each Checkpoint stages only
that step's declared paths, asserts the staged list equals them, commits, and tags locally. Tags are
never pushed. Step rollback is an operator action, never run from the unattended allowlist (§19.3).
Rollback to before step N (N = 1..10; operator sets only `N`). It rolls back steps N..10 together,
refuses to run if any change exists outside the 22 declared paths, and ends on a clean tree:
```bash
set -euo pipefail
test "$(git branch --show-current)" = aside/tier2-portfolio-20261123 || { echo "wrong branch"; exit 1; }
TAGS=(step-01-workspace step-02-eval-set step-03-score step-04-systems step-05-runs step-06-engagement-readme step-07-field-record step-08-ops-docs step-09-adrs step-10-readme)
if [ "$N" -eq 1 ]; then P="$(cat /tmp/fde-build-start)"; else P="refs/tags/${TAGS[$((N-2))]}"; fi
git rev-parse -q --verify "$P^{commit}" >/dev/null || { echo "invalid rollback ref: $P"; exit 1; }
ALL=" AGENTS.md CLAUDE.md pyproject.toml docs/worked-engagement/eval-set.jsonl docs/worked-engagement/scorer.py tests/test_scorer.py docs/worked-engagement/systems.py tests/test_systems.py docs/worked-engagement/run_eval.py docs/worked-engagement/runs/baseline.json docs/worked-engagement/runs/improved.json docs/worked-engagement/README.md tests/test_docs.py docs/field-record.md tests/test_field_record.py docs/failure-taxonomy.md docs/runbook.md docs/adr/0001-deterministic-offline-eval.md docs/adr/0002-confidence-gate-abstain-to-human.md docs/adr/0003-claim-labels-and-pseudonyms.md README.md scripts/smoke.sh "
git status --porcelain=v1 -z --untracked-files=all | tr '\0' '\n' | cut -c4- | while read -r f; do case "$ALL" in *" $f "*) ;; *) echo "change outside declared paths: $f"; exit 1;; esac; done
git log --format=%s "$P..HEAD" | grep -qvE '^step ([1-9]|10): ' && { echo "non-checkpoint commit after $P"; exit 1; } || true
git reset --hard "$P"
for i in $(seq "$N" 10); do case $i in
  1) PATHS="AGENTS.md CLAUDE.md pyproject.toml" ;;
  2) PATHS="docs/worked-engagement/eval-set.jsonl docs/worked-engagement/scorer.py tests/test_scorer.py" ;;
  3) PATHS="docs/worked-engagement/scorer.py tests/test_scorer.py" ;;
  4) PATHS="docs/worked-engagement/systems.py tests/test_systems.py" ;;
  5) PATHS="docs/worked-engagement/run_eval.py docs/worked-engagement/runs/baseline.json docs/worked-engagement/runs/improved.json tests/test_systems.py" ;;
  6) PATHS="docs/worked-engagement/README.md tests/test_docs.py" ;;
  7) PATHS="docs/field-record.md tests/test_field_record.py" ;;
  8) PATHS="docs/failure-taxonomy.md docs/runbook.md tests/test_docs.py" ;;
  9) PATHS="docs/adr/0001-deterministic-offline-eval.md docs/adr/0002-confidence-gate-abstain-to-human.md docs/adr/0003-claim-labels-and-pseudonyms.md tests/test_docs.py" ;;
  10) PATHS="README.md scripts/smoke.sh tests/test_docs.py" ;;
esac; for f in $PATHS; do git cat-file -e "$P:$f" 2>/dev/null || rm -f -- "$f"; done; t="${TAGS[$((i-1))]}"; if git rev-parse -q --verify "refs/tags/$t" >/dev/null; then git tag -d "$t"; fi; done
test -z "$(git status --porcelain)" || { echo "tree not clean after rollback"; exit 1; }
```


```bash
# Cumulative gate G (run before every Checkpoint from step 1 on; covers every prior Verify)
/tmp/fde-py312/bin/ruff check .                     # expect: exit 0
/tmp/fde-py312/bin/python -m pytest -q              # expect: exit 0, 0 failed
/tmp/fde-py312/bin/fde-portfolio check              # expect: exit 0
grep -Fqx 'extend-exclude = ["mcp", ".rig", "blueprints"]' pyproject.toml   # expect: exit 0
grep -Fqx 'norecursedirs = ["blueprints", ".venv", ".git"]' pyproject.toml  # expect: exit 0
test "$(shasum -a 256 CLAUDE.md | cut -d' ' -f1)" = c0c057439f0ee06b9d30cb9666e52580a89189f3b51b60d44c8fe03b18d83373   # expect: exit 0, CLAUDE.md equals §19.1
{ git show 15cba0fbc6bf08dfabd060b1ab1e97d0512d22ba:AGENTS.md; printf '%s\n' 'Build, lint, test and eval commands: see CLAUDE.md (canonical).'; } | cmp - AGENTS.md   # expect: exit 0, base AGENTS.md plus the one bridge line
```
From step 5 on, G also runs the default (no-argument) runner in an isolated copy:
```bash
d="$(mktemp -d)" && mkdir "$d/we" && cp docs/worked-engagement/run_eval.py docs/worked-engagement/scorer.py docs/worked-engagement/systems.py docs/worked-engagement/eval-set.jsonl "$d/we/" && test ! -e "$d/we/runs" && /tmp/fde-py312/bin/python "$d/we/run_eval.py" && cmp "$d/we/runs/baseline.json" docs/worked-engagement/runs/baseline.json && cmp "$d/we/runs/improved.json" docs/worked-engagement/runs/improved.json   # expect: exit 0
```
G also reruns, from the step shown: `bash scripts/smoke.sh` (step 1); the step 6 interpreter probe and
reader command (step 6); the step 8 runbook command (step 8). Every other prior Verify line is a pytest,
ruff, CLI, grep, hash or `cmp` line already in G.

### Step map
| # | Step | Depends on | Touches | Gate | Rollback target |
|---|---|---|---|---|---|
| 1 | workspace | — | `AGENTS.md`, `CLAUDE.md`, `pyproject.toml` | `/tmp/fde-py312/bin/python -m pytest -q` | the recorded start tip in `/tmp/fde-build-start` |
| 2 | eval-set | 1 | `docs/worked-engagement/eval-set.jsonl`, `docs/worked-engagement/scorer.py`, `tests/test_scorer.py` | `/tmp/fde-py312/bin/python -m pytest -q tests/test_scorer.py` | `step-01-workspace` |
| 3 | score | 2 | `docs/worked-engagement/scorer.py`, `tests/test_scorer.py` | `/tmp/fde-py312/bin/python -m pytest -q tests/test_scorer.py` | `step-02-eval-set` |
| 4 | systems | 3 | `docs/worked-engagement/systems.py`, `tests/test_systems.py` | `/tmp/fde-py312/bin/python -m pytest -q tests/test_systems.py` | `step-03-score` |
| 5 | runs | 4 | `docs/worked-engagement/run_eval.py`, `docs/worked-engagement/runs/baseline.json`, `docs/worked-engagement/runs/improved.json`, `tests/test_systems.py` | `/tmp/fde-py312/bin/python -m pytest -q tests/test_systems.py` | `step-04-systems` |
| 6 | engagement-readme | 5 | `docs/worked-engagement/README.md`, `tests/test_docs.py` | `/tmp/fde-py312/bin/python -m pytest -q tests/test_docs.py` | `step-05-runs` |
| 7 | field-record | 6 | `docs/field-record.md`, `tests/test_field_record.py` | `/tmp/fde-py312/bin/python -m pytest -q tests/test_field_record.py` | `step-06-engagement-readme` |
| 8 | ops-docs | 6 | `docs/failure-taxonomy.md`, `docs/runbook.md`, `tests/test_docs.py` | `/tmp/fde-py312/bin/python -m pytest -q tests/test_docs.py` | `step-07-field-record` |
| 9 | adrs | 8 | `docs/adr/0001-deterministic-offline-eval.md`, `docs/adr/0002-confidence-gate-abstain-to-human.md`, `docs/adr/0003-claim-labels-and-pseudonyms.md`, `tests/test_docs.py` | `/tmp/fde-py312/bin/python -m pytest -q tests/test_docs.py` | `step-08-ops-docs` |
| 10 | readme | 7, 9 | `README.md`, `scripts/smoke.sh`, `tests/test_docs.py` | `/tmp/fde-py312/bin/python -m pytest -q` | `step-09-adrs` |

### Step 1 — workspace (`workspace`)
**Do.** Write `CLAUDE.md` with the exact content in §19.1. In `pyproject.toml` change
`extend-exclude = ["mcp", ".rig"]` to `extend-exclude = ["mcp", ".rig", "blueprints"]` and add the line
`norecursedirs = ["blueprints", ".venv", ".git"]` under `[tool.pytest.ini_options]` (final block in
§19.6). Append to `AGENTS.md` exactly one line, `Build, lint, test and eval commands: see CLAUDE.md (canonical).`, keeping every
existing line unchanged. Files: `AGENTS.md`, `CLAUDE.md`, `pyproject.toml`. The blueprint is an input: it is already committed on the
branch before Bootstrap, and §10 verifies it is tracked.

**Done when.**
- WHEN `/tmp/fde-py312/bin/python -m pytest -q` runs THE SYSTEM SHALL exit 0 with 0 failed.
- WHEN `/tmp/fde-py312/bin/ruff check .` runs THE SYSTEM SHALL exit 0.
- WHEN `/tmp/fde-py312/bin/fde-portfolio check` runs THE SYSTEM SHALL exit 0.
- WHEN `AGENTS.md` is compared with the base file plus the bridge line THE SYSTEM SHALL find them byte-identical.
- WHEN `CLAUDE.md` is hashed THE SYSTEM SHALL equal the SHA-256 of the §19.1 block, `c0c057439f0ee06b9d30cb9666e52580a89189f3b51b60d44c8fe03b18d83373`.
- WHEN `pyproject.toml` is read THE SYSTEM SHALL contain the literal `"blueprints"` in both `extend-exclude` and `norecursedirs`.

**Verify.**
```bash
/tmp/fde-py312/bin/python -m pytest -q        # expect: exit 0, 0 failed
/tmp/fde-py312/bin/ruff check .               # expect: exit 0
grep -Fqx 'extend-exclude = ["mcp", ".rig", "blueprints"]' pyproject.toml   # expect: exit 0
grep -Fqx 'norecursedirs = ["blueprints", ".venv", ".git"]' pyproject.toml  # expect: exit 0
/tmp/fde-py312/bin/fde-portfolio check   # expect: exit 0, installed console script works
bash scripts/smoke.sh   # expect: exit 0, prints fde-portfolio smoke PASS
test "$(shasum -a 256 CLAUDE.md | cut -d' ' -f1)" = c0c057439f0ee06b9d30cb9666e52580a89189f3b51b60d44c8fe03b18d83373   # expect: exit 0, CLAUDE.md equals the §19.1 block
{ git show 15cba0fbc6bf08dfabd060b1ab1e97d0512d22ba:AGENTS.md; printf '%s\n' 'Build, lint, test and eval commands: see CLAUDE.md (canonical).'; } | cmp - AGENTS.md   # expect: exit 0, base AGENTS.md plus the one bridge line
```
**Checkpoint.**
```bash
git add AGENTS.md CLAUDE.md pyproject.toml && test "$(git diff --cached --name-only | LC_ALL=C sort | tr '\n' ' ')" = "AGENTS.md CLAUDE.md pyproject.toml " && git commit -m "step 1: workspace" && git tag step-01-workspace
```

### Step 2 — eval set and loader (`eval-set`)
**Do.** Write `docs/worked-engagement/eval-set.jsonl` byte for byte as the frozen fixture in §19.6
(34 SYNTHETIC tickets, ids `T001`..`T034`, all five routes present). Write `docs/worked-engagement/scorer.py`
with `ROUTES` and `load_eval` per §5. Write `tests/test_scorer.py` that inserts
`docs/worked-engagement` at `sys.path[0]` and tests: the shipped file's SHA-256 equals
`dae205e9367083d71fb820a1a68ecb9755c4c2f0b03d7763ed50598714cc62d5` (the §19.6 fixture); the shipped set
loads 34 items with all five labels; an empty file, a duplicate id, a missing key and an unknown label each raise `ValueError` (via `tmp_path`).

**Done when.**
- WHEN `load_eval` reads the shipped set THE SYSTEM SHALL return 34 items carrying 5 distinct labels.
- WHEN a file holds a duplicate id THE SYSTEM SHALL raise `ValueError`.
- WHEN a line has an unknown label, or the file is empty, THE SYSTEM SHALL raise `ValueError`.

**Verify.**
```bash
/tmp/fde-py312/bin/python -m pytest -q tests/test_scorer.py   # expect: exit 0, 0 failed
/tmp/fde-py312/bin/ruff check .                               # expect: exit 0
```
**Checkpoint.**
```bash
git add docs/worked-engagement/eval-set.jsonl docs/worked-engagement/scorer.py tests/test_scorer.py && test "$(git diff --cached --name-only | LC_ALL=C sort | tr '\n' ' ')" = "docs/worked-engagement/eval-set.jsonl docs/worked-engagement/scorer.py tests/test_scorer.py " && git commit -m "step 2: eval-set" && git tag step-02-eval-set
```

### Step 3 — score function (`score`)
**Do.** Add `score` to `docs/worked-engagement/scorer.py` per §4 and §5. Extend `tests/test_scorer.py`
with: all-correct predictions give accuracy 1.0 and coverage 1.0; one abstention lowers coverage and
leaves `wrong_auto_routes` 0; one wrong route counts 1 wrong auto route; zero answered gives
`answered_accuracy` 0.0; mismatched ids, reordered ids, duplicate prediction ids and an empty
`items` list each raise `ValueError`.

**Done when.**
- WHEN all predictions match THE SYSTEM SHALL return `accuracy` 1.0 and `coverage` 1.0.
- WHEN one prediction abstains THE SYSTEM SHALL count it in `abstained` and not in `wrong_auto_routes`.
- WHEN prediction ids differ from, reorder or duplicate the item ids, or `items` is empty, THE SYSTEM SHALL raise `ValueError`.

**Verify.**
```bash
/tmp/fde-py312/bin/python -m pytest -q tests/test_scorer.py   # expect: exit 0, 0 failed
/tmp/fde-py312/bin/ruff check .                               # expect: exit 0
```
**Checkpoint.**
```bash
git add docs/worked-engagement/scorer.py tests/test_scorer.py && test "$(git diff --cached --name-only | LC_ALL=C sort | tr '\n' ' ')" = "docs/worked-engagement/scorer.py tests/test_scorer.py " && git commit -m "step 3: score" && git tag step-03-score
```

### Step 4 — two systems (`systems`)
**Do.** Write `docs/worked-engagement/systems.py` byte for byte as the frozen module in §19.6
(baseline: ordered first-match substring rules, confidence 1.0, fallback `other`; improved: fixed
substring weights, negation regex, abstain when the top score is under 2 or leads by less than 1). Write `tests/test_systems.py` with: the file's SHA-256 equals
`da5cc479476a48ace90d5619297530687145e574c16b762ccc760b983ef2f3a7` (the §19.6 module);
`baseline` never returns `None` on the shipped set; `improved("Someone used my card in another
country, I did not make this purchase")` returns `fraud`; `improved("Hello")` returns route `None`;
`improved("Not a fraud issue, I just need a copy of last month's invoice")` returns `billing`.

**Done when.**
- WHEN `baseline` runs on every shipped item THE SYSTEM SHALL return a non-`None` route each time.
- WHEN `improved` receives the negated-fraud invoice ticket THE SYSTEM SHALL return `billing`.
- WHEN `improved` receives `Hello` THE SYSTEM SHALL return route `None`.

**Verify.**
```bash
/tmp/fde-py312/bin/python -m pytest -q tests/test_systems.py  # expect: exit 0, 0 failed
/tmp/fde-py312/bin/ruff check .                               # expect: exit 0
```
**Checkpoint.**
```bash
git add docs/worked-engagement/systems.py tests/test_systems.py && test "$(git diff --cached --name-only | LC_ALL=C sort | tr '\n' ' ')" = "docs/worked-engagement/systems.py tests/test_systems.py " && git commit -m "step 4: systems" && git tag step-04-systems
```

### Step 5 — runner and saved runs (`runs`)
**Do.** Write `docs/worked-engagement/run_eval.py` per §5 with an optional `--out DIR` (default: the
`runs/` folder beside the script). Run `/tmp/fde-py312/bin/python docs/worked-engagement/run_eval.py` once to
write the two run files. Extend `tests/test_systems.py` with a fixture `fresh_runs(tmp_path)` that runs the CLI into that
test's own `tmp_path` and returns `(stdout, tmp_path)`, and six tests (a)-(f): (a) runs `[sys.executable, "docs/worked-engagement/run_eval.py", "--out", str(tmp_path)]` with
`subprocess.run(capture_output=True, text=True)`, asserts return code 0, and asserts
`stdout.splitlines()` equals exactly `[line(b), line(i)]`, where `b` and `i` are the JSON objects read
from `tmp_path/baseline.json` and `tmp_path/improved.json` and
`line(d) = f"{d['system']} accuracy={d['accuracy']:.4f} answered_accuracy={d['answered_accuracy']:.4f} coverage={d['coverage']:.4f} wrong_auto_routes={d['wrong_auto_routes']}"`
(the runner prints with this same format); (d) for each saved run, the key set is exactly `{system, n, answered, abstained, correct,
wrong_auto_routes, accuracy, answered_accuracy, coverage, predictions}`, `[p["id"] for p in predictions]`
equals the eval-set id order, each prediction has keys exactly `{id, route, confidence}`, and
`path.read_bytes() == (json.dumps(json.loads(path.read_bytes()), indent=2, sort_keys=True) + "\n").encode("utf-8")`; (b) using `fresh_runs`, both files in its `tmp_path` are byte-identical to the working-tree
`docs/worked-engagement/runs/baseline.json` and `docs/worked-engagement/runs/improved.json` written
earlier in this step (the committed-byte check is in §20.1); (c) in the saved runs, improved `wrong_auto_routes` is
lower than baseline's, improved `answered_accuracy` is higher than baseline's, and improved
`coverage` is at least 0.8; and both saved runs equal the §19.6 expected published outcome; (e) for each saved run, `system` is
`baseline` or `improved` respectively, every saved prediction's `(route, confidence)` equals
`systems.<system>(text)` for the eval item with that id, and `scorer.score(system, items, preds)`
recomputed from the fixture and the saved predictions equals the saved score fields; (f) copies `run_eval.py`,
`scorer.py` and `systems.py` into `tmp_path/we/` beside a copy of the fixture with item `T001`
relabelled from `billing` to `other`, runs `subprocess.run([sys.executable, str(tmp_path / "we" / "run_eval.py"), "--out", str(tmp_path / "out")])`, and asserts
exit 0 and baseline `correct == 17`.

**Done when.**
- WHEN the runner runs into a temporary folder THE SYSTEM SHALL exit 0 and print exactly the baseline line then the improved line, each equal to the line built from its JSON file.
- WHEN its two outputs are compared with the saved runs THE SYSTEM SHALL find both byte-identical.
- WHEN the saved runs are compared THE SYSTEM SHALL show improved with fewer wrong auto routes, higher answered accuracy, and coverage at least 0.8.

**Verify.**
```bash
/tmp/fde-py312/bin/python docs/worked-engagement/run_eval.py   # expect: exit 0 (stdout asserted by test (a))
/tmp/fde-py312/bin/python -m pytest -q tests/test_systems.py   # expect: exit 0, 0 failed
/tmp/fde-py312/bin/ruff check .                                # expect: exit 0
```
**Checkpoint.**
```bash
git add docs/worked-engagement/run_eval.py docs/worked-engagement/runs/baseline.json docs/worked-engagement/runs/improved.json tests/test_systems.py && test "$(git diff --cached --name-only | LC_ALL=C sort | tr '\n' ' ')" = "docs/worked-engagement/run_eval.py docs/worked-engagement/runs/baseline.json docs/worked-engagement/runs/improved.json tests/test_systems.py " && git commit -m "step 5: runs" && git tag step-05-runs
```

### Step 6 — worked engagement README (`engagement-readme`)
**Do.** Write `docs/worked-engagement/README.md`. Line 1 `# Worked engagement: payments ticket routing`,
line 2 blank, line 3 exactly the banner literal `> SYNTHETIC. Fictional company, fictional tickets. Every result in the table below is produced by run_eval.py.` (no backticks inside it)
Then sections `## Brief`, `## Constraints`, `## Method`, `## Results`, `## Rerun`. Under `## Rerun`
the line `Requires Python 3.10 or newer, standard library only.` and a fenced bash block holding
exactly `python3 docs/worked-engagement/run_eval.py`. Under `## Results`
a table with header `| system | accuracy | answered_accuracy | coverage | wrong_auto_routes |` and one
row per system in baseline-then-improved order, each equal to `row(d)` below built from that system's saved run file.
Create `tests/test_docs.py` with a test that asserts the `## Rerun` section contains the full lines
`Requires Python 3.10 or newer, standard library only.` and `python3 docs/worked-engagement/run_eval.py`, reads both run files and asserts line 3 equals the
SYNTHETIC banner and that, for `d` in (baseline, improved), the full line
`row(d) = f"| {d['system']} | {d['accuracy']:.4f} | {d['answered_accuracy']:.4f} | {d['coverage']:.4f} | {d['wrong_auto_routes']} |"`
is checked inside the `## Results` section only (lines after `## Results` up to the next `## `
line): its table lines are exactly, in order, the header
`| system | accuracy | answered_accuracy | coverage | wrong_auto_routes |`, the separator
`|---|---|---|---|---|`, `row(baseline)` and `row(improved)`.

**Done when.**
- WHEN the README's line 3 is read THE SYSTEM SHALL equal the SYNTHETIC banner.
- WHEN the `## Rerun` section is read THE SYSTEM SHALL contain the line `python3 docs/worked-engagement/run_eval.py`.
- WHEN the `## Results` section is parsed THE SYSTEM SHALL find exactly the header, separator, baseline row and improved row, in that order.

**Verify.**
```bash
/tmp/fde-py312/bin/python -m pytest -q tests/test_docs.py   # expect: exit 0, 0 failed
/tmp/fde-py312/bin/ruff check .                             # expect: exit 0
PATH=/tmp/fde-py312/bin:$PATH python3 -c 'import sys; assert sys.prefix == "/tmp/fde-py312" and sys.version_info[:2] == (3, 12), (sys.prefix, sys.version)'   # expect: exit 0, the venv's python3 is selected
PATH=/tmp/fde-py312/bin:$PATH python3 docs/worked-engagement/run_eval.py && for f in baseline improved; do git show "HEAD:docs/worked-engagement/runs/$f.json" | cmp - "docs/worked-engagement/runs/$f.json" || exit 1; done   # expect: exit 0, the published reader command reproduces the saved runs
```
**Checkpoint.**
```bash
git add docs/worked-engagement/README.md tests/test_docs.py && test "$(git diff --cached --name-only | LC_ALL=C sort | tr '\n' ' ')" = "docs/worked-engagement/README.md tests/test_docs.py " && git commit -m "step 6: engagement-readme" && git tag step-06-engagement-readme
```

### Step 7 — field record (`field-record`)
**Do.** Write `docs/field-record.md` with exactly this structure and only the literals in §14:
1. Line 1 `# Field record`; line 3 the legend literal from §14.
2. A table with header `| Engagement | Years | Sector |`, separator `|---|---|---|`, then the four
   §14 card rows in §14 order, each written as `| <Engagement> | <Years> | <Sector> |`.
3. One card per row: heading `### <Engagement>`, then the line `**Evidence.**`, then one bullet
   `- <claim> [confirmed]` per §14 claim for that card, in §14 order, then the line
   `**Not yet evidenced.**`, then one bullet `- <gap>` per §14 gap for that card.
No other bullet lines. Unknown facts are never written as claims: a fact the source corpus does not
hold appears only as a §14 gap string, never as text under `**Evidence.**`.
Write `tests/test_field_record.py` holding `CARDS` (a list copied verbatim from §14: engagement,
years, sector, claims, gaps) and asserting: (a) the four table rows equal the §14 rows exactly and in
order; (b) for each card, the bullets under `**Evidence.**` equal exactly `[f"- {c} [confirmed]" for c
in claims]` and the bullets under `**Not yet evidenced.**` equal exactly `[f"- {g}" for g in gaps]`;
(c) the file contains no `[inferred]` and no `[unverified]`, and every bullet line in the file is one
of the bullets in (b); (d) every number token matching `\d[\d,]*(\.\d+)?` is in `ALLOWED_NUMBERS`;
(e) every line starting `### ` is one of the four §14 engagement pseudonyms (the exact pseudonym
allowlist); (f) `path.read_bytes() == render(CARDS).encode("utf-8")`, where `render` builds exactly: `# Field record`, blank, legend, blank,
the table header, separator and four rows, then for each card a blank line, `### <Engagement>`, blank,
`**Evidence.**`, blank, its claim bullets, blank, `**Not yet evidenced.**`, blank, its gap bullets,
and a final newline; (g) both (f) and (g) call one helper `validate(path) -> None` that raises
`AssertionError` unless the file at `path` equals `render(CARDS)`; (f) calls it on
`docs/field-record.md`; (g) copies that file to `tmp_path`, appends the line
`The rollout doubled retention.`, and asserts `validate` raises on the copy; a second copy with every
LF replaced by CRLF also makes `validate` raise. `validate` compares bytes as in (f). The builder writes the file by running
nothing but this layout by hand; test (f) is the gate.

**Done when.**
- WHEN the field record is parsed THE SYSTEM SHALL find the four §14 rows and four cards, each card's claims equal to its §14 claims with label `[confirmed]`.
- WHEN a claim bullet differs from its §14 text or label THE SYSTEM SHALL fail test (b) or (c).
- WHEN a card heading is not a §14 pseudonym THE SYSTEM SHALL fail test (e).
- WHEN any line outside the rendered layout appears, including extra prose, THE SYSTEM SHALL fail test (f), proven by test (g).

**Verify.**
```bash
/tmp/fde-py312/bin/python -m pytest -q tests/test_field_record.py   # expect: exit 0, 0 failed
/tmp/fde-py312/bin/ruff check .                                     # expect: exit 0
```
**Checkpoint.**
```bash
git add docs/field-record.md tests/test_field_record.py && test "$(git diff --cached --name-only | LC_ALL=C sort | tr '\n' ' ')" = "docs/field-record.md tests/test_field_record.py " && git commit -m "step 7: field-record" && git tag step-07-field-record
```

### Step 8 — failure taxonomy and runbook (`ops-docs`)
**Do.** Write `docs/failure-taxonomy.md` with a table headed
`| Class | Seen in | Detection signal | Mitigation |` and at least 6 rows, including the
worked-engagement classes `confident wrong route`, `negation flip` and `empty or vague ticket`.
Write `docs/runbook.md` byte for byte as the runbook literal in §19.6. Extend `tests/test_docs.py`:
the taxonomy has the header and at least 6 data rows and names the three classes; `docs/runbook.md`
equals the §19.6 runbook literal exactly and its SHA-256 is `4cec86df18313cd6ca16bace5265da23124683547589ace4e0afd2a757ddb233`.

**Done when.**
- WHEN the taxonomy is parsed THE SYSTEM SHALL find the header, at least 6 data rows and the three named classes.
- WHEN the runbook is read THE SYSTEM SHALL equal the §19.6 runbook literal byte for byte.

**Verify.**
```bash
/tmp/fde-py312/bin/python -m pytest -q tests/test_docs.py   # expect: exit 0, 0 failed
PATH=/tmp/fde-py312/bin:$PATH python3 docs/worked-engagement/run_eval.py && for f in baseline improved; do git show "HEAD:docs/worked-engagement/runs/$f.json" | cmp - "docs/worked-engagement/runs/$f.json" || exit 1; done   # expect: exit 0, the exact runbook command
```
**Checkpoint.**
```bash
git add docs/failure-taxonomy.md docs/runbook.md tests/test_docs.py && test "$(git diff --cached --name-only | LC_ALL=C sort | tr '\n' ' ')" = "docs/failure-taxonomy.md docs/runbook.md tests/test_docs.py " && git commit -m "step 8: ops-docs" && git tag step-08-ops-docs
```

### Step 9 — ADRs (`adrs`)
**Do.** Write `docs/adr/0001-deterministic-offline-eval.md`,
`docs/adr/0002-confidence-gate-abstain-to-human.md`, `docs/adr/0003-claim-labels-and-pseudonyms.md`,
each with the full lines `## Context`, `## Decision`, `## Consequences`, `## Alternatives rejected`,
each followed by non-empty text. Extend `tests/test_docs.py` to assert exactly that for the three
exact paths.

**Done when.**
- WHEN each of the three exact ADR paths is read THE SYSTEM SHALL find the four headings as full lines.
- WHEN a heading is followed only by blank lines THE SYSTEM SHALL fail the test.

**Verify.**
```bash
/tmp/fde-py312/bin/python -m pytest -q tests/test_docs.py   # expect: exit 0, 0 failed
```
**Checkpoint.**
```bash
git add docs/adr/0001-deterministic-offline-eval.md docs/adr/0002-confidence-gate-abstain-to-human.md docs/adr/0003-claim-labels-and-pseudonyms.md tests/test_docs.py && test "$(git diff --cached --name-only | LC_ALL=C sort | tr '\n' ' ')" = "docs/adr/0001-deterministic-offline-eval.md docs/adr/0002-confidence-gate-abstain-to-human.md docs/adr/0003-claim-labels-and-pseudonyms.md tests/test_docs.py " && git commit -m "step 9: adrs" && git tag step-09-adrs
```

### Step 10 — README reorder and smoke (`readme`)
**Do.** In `README.md`: keep the H1 and every existing line above `## Why this exists` unchanged (no
image line is added; the owner inserts media under the H1 in a later commit). Insert, before
`## Why this exists`, the line `## Field record`, a blank line, the field-record section literal in
§19.6, a blank line, the line `## Worked engagement (synthetic)`, a blank line, the engagement section
literal in §19.6, and a blank line.
Rename `## Quick start (5 lines)` to `## Quick start` and keep it after both new sections. Replace the
line `| `pytest -q --cov` | 44 tests pass, package coverage 85% | `pytest -q --cov` |` with
`| `pytest -q --cov` | the full suite passes | `pytest -q --cov` |` and the line
`| `tests/` | 44 tests covering schema, render, CLI, drift scans, repo hygiene |` with
`| `tests/` | tests covering schema, render, CLI, drift scans, repo hygiene, the eval and the docs |`;
test (h) asserts both replacement lines are present and no line matches `\b\d+ tests\b`. Insert before `## License`
the line `## Public Boundary`, a blank line, the one-line literal `The public boundary for this repository is in [docs/public-boundary.md](docs/public-boundary.md). Customers and employers appear only as sector pseudonyms, and every claim is a confirmed fact.`, and a blank line. Replace the
first paragraph of `## The operating record` with the operating-record literal in §19.6, as one line. Keep the
CI badge, the `git clone` line, a test command and the footer that `tests/test_repo_hygiene.py`
requires. In `scripts/smoke.sh` add `docs/field-record.md docs/runbook.md docs/failure-taxonomy.md`
to the `for f in` list. Extend `tests/test_docs.py`: (a) README lines 5-7 equal the constant `BADGES` (the three §19.6 badge lines, written into the test) and no other line contains `![`;
(b) the full lines `## Field record`, `## Worked engagement (synthetic)`, `## Quick start` appear in
that order; (c) the non-blank body between `## Field record` and the next `## ` line equals exactly the
field-record section literal, the body under `## Worked engagement (synthetic)` equals exactly the
engagement section literal, and both link targets exist on disk; (d) the first paragraph under `## The operating record` equals the §19.6 operating-record literal
exactly; and a helper `census(text)` returns the matches of
`re.compile(r"\b\d[\d,]*\s*(?:-|\s)?(?:\w+\s+){0,2}repo(?:s|sitory|sitories)?\b", re.I)` and is
empty for the README, while a negative test asserts it is non-empty for each of
`The fleet contains 367 repositories.`, `a 12-repo fleet` and `366 private repos`;
(i) the body under `## Public Boundary` equals that literal and `docs/public-boundary.md` exists;
(e) for each of the three new docs, a fixture copies `scripts/smoke.sh` to `tmp_path/scripts/smoke.sh` and
copies each of the eight files in its `for f in` list (`README.md`,
`docs/implementation-playbook.md`, `docs/architecture.md`, `docs/evaluation-strategy.md`,
`docs/public-boundary.md`, `docs/field-record.md`, `docs/runbook.md`, `docs/failure-taxonomy.md`) to the same repository-relative path under
`tmp_path` (for example `tmp_path/docs/runbook.md`); with all eight present
`subprocess.run(["bash", str(tmp_path / "scripts" / "smoke.sh")])` exits 0 and prints
`fde-portfolio smoke PASS`; then, per new doc, the test removes that one file, asserts exit 1, and
restores it.

**Done when.**
- WHEN README is scanned THE SYSTEM SHALL find only the three base badge images, the three headings in order, and `census` SHALL return no match.
- WHEN `census` scans each of the three negative census sentences THE SYSTEM SHALL return a match.
- WHEN each new section is read THE SYSTEM SHALL equal its §19.6 section literal and its link target SHALL exist.
- WHEN the `## Public Boundary` section is read THE SYSTEM SHALL equal its literal and its link target SHALL exist.
- WHEN smoke runs with one new doc missing THE SYSTEM SHALL exit 1.
- WHEN the full suite runs THE SYSTEM SHALL exit 0 with 0 failed.

**Verify.**
```bash
/tmp/fde-py312/bin/python -m pytest -q    # expect: exit 0, 0 failed
bash scripts/smoke.sh            # expect: exit 0, prints fde-portfolio smoke PASS
/tmp/fde-py312/bin/ruff check .           # expect: exit 0
```
**Checkpoint.**
```bash
git add README.md scripts/smoke.sh tests/test_docs.py && test "$(git diff --cached --name-only | LC_ALL=C sort | tr '\n' ' ')" = "README.md scripts/smoke.sh tests/test_docs.py " && git commit -m "step 10: readme" && git tag step-10-readme
```

### 9.1 Parity and cutover
NOT APPLICABLE — additive change; nothing is migrated, replaced or cut over. The held-constant CLI
and playbooks keep their existing tests as the parity check.

## 10. Environment Setup
Environment variables: none to configure. Inherited `PATH`: steps 6 and 8 and gate G prefix it as
`PATH=/tmp/fde-py312/bin:$PATH`, so `python3` must resolve to `/tmp/fde-py312/bin/python3`
(the venv's 3.12 interpreter); the step 6 Verify asserts this. `LC_ALL=C` is set command-locally on every Checkpoint's
`sort` so the staged-path order is byte-deterministic; it needs no user configuration. Prerequisites: `git`, `uv` (checked with `uv --version`; 0.13.1
observed), Python 3.12 available to `uv` (checked with `uv python find 3.12`). Bootstrap has two
blocks: 10a runs once before step 1; 10b is repeatable and exits 0 on every line on any rerun:
```bash
# 10a. One-time preflight (run once, before step 1); any failure exits before the start tip is written
set -euo pipefail
git show-ref -q --verify refs/heads/aside/tier2-portfolio-20261123   # expect: exit 0; the prepared branch exists
git switch aside/tier2-portfolio-20261123 || exit 1
test "$(git branch --show-current)" = aside/tier2-portfolio-20261123 || exit 1
git merge-base --is-ancestor 15cba0fbc6bf08dfabd060b1ab1e97d0512d22ba HEAD || exit 1   # expect: exit 0
git cat-file -e HEAD:blueprints/fde-field-record-blueprint.md || exit 1   # expect: exit 0, HEAD contains the blueprint
test -z "$(git status --porcelain)" || exit 1   # expect: exit 0, index and worktree clean
for t in step-01-workspace step-02-eval-set step-03-score step-04-systems step-05-runs step-06-engagement-readme step-07-field-record step-08-ops-docs step-09-adrs step-10-readme; do if git rev-parse -q --verify "refs/tags/$t" >/dev/null; then echo "tag conflict: $t -> $(git rev-parse "refs/tags/$t")"; exit 1; fi; done   # expect: exit 0; a pre-existing step tag stops the build, nothing is deleted
git rev-parse HEAD > /tmp/fde-build-start   # records the pre-build tip
```
```bash
# 10b. Repeatable environment setup (safe to rerun at any time; every line exits 0)
test -x /tmp/fde-py312/bin/python || uv venv -p 3.12 /tmp/fde-py312
/tmp/fde-py312/bin/python -c 'import sys; assert sys.version_info[:2] == (3, 12), sys.version'   # expect: exit 0. On failure, stop and report; the operator recreates `/tmp/fde-py312`
uv pip install --python /tmp/fde-py312/bin/python -e '.[dev]'
/tmp/fde-py312/bin/python -m pytest -q   # expect: exit 0, 0 failed (45 passed on the pre-build tip)
```
The build venv lives outside the repository, so nothing it writes can be staged. The repo's existing `.venv/` (Python 3.14) is ignored by `.gitignore` on the base commit and is never read, used or modified. Files that must
be committed: every path in the step map Touches column. None of them matches a `.gitignore` pattern
(`.venv/`, `.coverage`, `.pytest_cache/`, `.ruff_cache/`, `*.egg-info/`, `build/`, `__pycache__/`,
`*.pyc`, `/graft/`).

## 11. Dependencies
No new dependencies. `pyproject.toml` declares minimum constraints, not pins (`PyYAML>=6.0`,
`jsonschema>=4.20`, `pytest>=8`, `pytest-cov>=4`, `ruff>=0.5`); all are installed by §10's
`uv pip install --python /tmp/fde-py312/bin/python -e '.[dev]'`. Session evidence, 2026-11-23, from
`uv pip list`: PyYAML 6.0.4, jsonschema 4.26.0, pytest 9.2.0, pytest-cov 7.1.0, ruff 0.17.6.

## 12. Deployment Strategy
No deploy. Work stays on the local branch. Step rollback: the step map's Rollback target column.
Whole-change rollback (operator action, not allowlisted): the rollback above with `N=1`, then
`git switch main`. The branch, and any tag that existed before §10a recorded the start, are kept. Push is
Gate-D.

## 13. Testing Strategy
Unit tests for loader and scorer (steps 2-3), behavior tests for both systems (step 4), byte-level
reproducibility of the runs (step 5), content gates for every new doc (steps 6-10), existing suite
held green at every step.

## 14. Security & Secrets
No secrets. Source rule: every career number and deployment fact comes only from the maintainer's
private career answers corpus, confirmed section; its never-claim list is never used. Public-claim
rule: only `[confirmed]` facts appear as claims in public copy (the field record and README). Facts
the corpus holds only as on-record but unverified, and facts it does not hold at all, are never
written as claims; each real gap is named once as a gap string below. `[inferred]` and `[unverified]`
never appear in public copy. The literals are copied here so the blueprint is self-contained.

Legend literal (line 3 of `docs/field-record.md`):
`Every claim below is [confirmed] against the maintainer's private career record. Employers and clients appear as sector pseudonyms. Gaps are listed, not filled.`

| Engagement | Years | Sector |
|---|---|---|
| Independent AI practice | 2025 to now | Banking and payments |
| Health IT vendor, AI portfolio | 2021 to 2026 | Health IT |
| Regional health system, digital and AI innovation | 2013 to 2020 | Health system |
| Telehealth startup, product roadmap | 2020 to 2021 | Telehealth |

Claims (each written publicly as `- <claim> [confirmed]`):

| Engagement | Claim (exact text) |
|---|---|
| Independent AI practice | 8 client engagements since 2025 |
| Independent AI practice | 6 client AI applications live under a written reference architecture, each with a roadmap, service level and health metrics |
| Independent AI practice | Up to 80% adoption of client AI applications through walkthroughs, training and super-user networks |
| Independent AI practice | 8 activate, buy or build feasibility reviews with client IT before spend |
| Independent AI practice | 6 third-party AI vendors vetted for model risk |
| Independent AI practice | A measured cut of about 20% in run cost, incidents, manual handling or review cycle time |
| Independent AI practice | Confidence-gated AI actions with a tamper-evident audit trail, guardrails and eval harnesses |
| Independent AI practice | About 30% of practice time on self-learning systems that improve from usage feedback |
| Health IT vendor, AI portfolio | AI and analytics intake of 12 use cases, top 4 funded |
| Health IT vendor, AI portfolio | 8 AI business cases built with Finance |
| Health IT vendor, AI portfolio | 3 AI and analytics vendor evaluations with Procurement, Risk and Legal |
| Health IT vendor, AI portfolio | An AI capability taken through formal security, privacy, HIPAA and compliance review |
| Regional health system, digital and AI innovation | AI and ML work since 2019, including radiology read prioritization about 15% faster |
| Regional health system, digital and AI innovation | 6 digital-health projects run through an innovation center of excellence |
| Telehealth startup, product roadmap | 6 end-user focus groups and roadmap sessions with health-system partners |

Gaps (each written publicly as `- <gap>`):

| Engagement | Gap (exact text) |
|---|---|
| Independent AI practice | Client-attributable before and after metrics per engagement |
| Health IT vendor, AI portfolio | Market-signal volume for the competitive intelligence capability |
| Regional health system, digital and AI innovation | Teletriage scale and emergency wait-time figures |
| Telehealth startup, product roadmap | Deployment and outcome facts for the platform |

`ALLOWED_NUMBERS` (verbatim for `tests/test_field_record.py`): `{"2013", "2019", "2020", "2021",
"2025", "2026", "3", "4", "6", "8", "12", "15", "20", "30", "80"}`.

Real-name redaction inputs (employer and client names, the never-claim list) stay outside the
repository and are never written into any committed file, test or this blueprint; the committed test
enforces the positive pseudonym allowlist plus test (f) whole-document equality instead. Scope of the
contact rule: `docs/field-record.md` and `docs/worked-engagement/` hold no IP, hostname, email or real
name. The README keeps its existing footer (`rodgersintelligence.com`, required by
`tests/test_repo_hygiene.py`); that is the maintainer's public site, not a customer detail.

## 15. Accessibility
No new images are added; the three existing badges keep their alt text. All tables have header rows.

## 16. Observability & Cost
Zero runtime cost. The two run files are the eval's observable output.

## 17. Model Routing
Builder: one Aside subagent. No model call inside repository code.

## 18. Skills to Use During Build
None. No step invokes a skill.

## 19. Agent Workspace
Single-file mode. The repository keeps its existing `AGENTS.md` (plus one bridge line, §19.2) and `.github/copilot-instructions.md`
unchanged; step 1 adds `CLAUDE.md` (§19.1). §19.3 is for the builder session only and is not
committed.

### 19.1 `CLAUDE.md`
Destination `CLAUDE.md`, written verbatim in step 1:
```markdown
# CLAUDE.md — fde-portfolio

## Commands (run from the repo root)
- Environment install (the first three lines of §10b; §10b's fourth line is the test run below): `test -x /tmp/fde-py312/bin/python || uv venv -p 3.12 /tmp/fde-py312`, then
  `/tmp/fde-py312/bin/python -c 'import sys; assert sys.version_info[:2] == (3, 12), sys.version'`, then
  `uv pip install --python /tmp/fde-py312/bin/python -e '.[dev]'`
- Lint: `/tmp/fde-py312/bin/ruff check .`
- Tests: `/tmp/fde-py312/bin/python -m pytest -q`
- Playbook gate: `/tmp/fde-py312/bin/fde-portfolio check`
- Eval: `/tmp/fde-py312/bin/python docs/worked-engagement/run_eval.py`
- Smoke: `bash scripts/smoke.sh`

## How it connects
- `src/fde_portfolio/` renders the YAML playbooks; it is held constant by the field-record blueprint.
- `docs/worked-engagement/` is a SYNTHETIC eval: `eval-set.jsonl` -> `systems.py` -> `scorer.py`
  -> `runs/*.json`, driven by `run_eval.py`. Saved runs must equal a fresh run byte for byte.
- `docs/field-record.md` numbers are gated by `tests/test_field_record.py`.

## Rules
- Public claims in `docs/field-record.md` are `[confirmed]` only; real gaps go under "Not yet evidenced".
- Customers and employers appear as sector pseudonyms only. No compensation figures.
- No new dependencies. No push without the owner's written approval.
- `AGENTS.md` stays the bridge file; keep both in agreement.
```

### 19.2 `AGENTS.md`
Existing bridge file; its lines stay unchanged. Step 1 appends one line, `Build, lint, test and eval commands: see CLAUDE.md (canonical).`, verified by `cmp`
against the base file plus that line.

### 19.3 `.claude/settings.json`
Builder-session allowlist, not committed. Activation, before §10 Bootstrap: an unattended
Claude Code builder writes this block to `/tmp/fde-claude-settings.json` (outside the checkout,
so `git status --porcelain` stays clean) and starts with `claude --settings /tmp/fde-claude-settings.json`; an Aside or Codex builder runs
under its own session approval and needs no file. Each subcommand of every Verify, Checkpoint,
Bootstrap, gate G and §20.1 line has an exact or command-scoped entry, including the ten exact
`git tag` commands. Destructive commands (`git reset --hard`, `git tag -d`, `rm -f`, `rm -rf`) are
denied: rollback and venv recreation are operator actions approved per run.
```json
{
  "permissions": {
    "allow": [
      "Bash(/tmp/fde-py312/bin/python -m pytest -q)",
      "Bash(/tmp/fde-py312/bin/python -m pytest -q tests/test_scorer.py)",
      "Bash(/tmp/fde-py312/bin/python -m pytest -q tests/test_systems.py)",
      "Bash(/tmp/fde-py312/bin/python -m pytest -q tests/test_docs.py)",
      "Bash(/tmp/fde-py312/bin/python -m pytest -q tests/test_field_record.py)",
      "Bash(/tmp/fde-py312/bin/python docs/worked-engagement/run_eval.py)",
      "Bash(/tmp/fde-py312/bin/ruff check .)",
      "Bash(/tmp/fde-py312/bin/fde-portfolio check)",
      "Bash(bash scripts/smoke.sh)",
      "Bash(uv --version)",
      "Bash(uv python find 3.12)",
      "Bash(uv venv -p 3.12 /tmp/fde-py312)",
      "Bash(uv pip install --python /tmp/fde-py312/bin/python -e '.[dev]')",
      "Bash(git add:*)",
      "Bash(git show 15cba0fbc6bf08dfabd060b1ab1e97d0512d22ba:AGENTS.md)",
      "Bash(printf:*)",
      "Bash(cmp:*)",
      "Bash(git commit -m:*)",
      "Bash(git tag step-01-workspace)",
      "Bash(git tag step-02-eval-set)",
      "Bash(git tag step-03-score)",
      "Bash(git tag step-04-systems)",
      "Bash(git tag step-05-runs)",
      "Bash(git tag step-06-engagement-readme)",
      "Bash(git tag step-07-field-record)",
      "Bash(git tag step-08-ops-docs)",
      "Bash(git tag step-09-adrs)",
      "Bash(git tag step-10-readme)",
      "Bash(cat /tmp/fde-build-start)",
      "Bash(/tmp/fde-py312/bin/python -c 'import sys; assert sys.version_info[:2] == (3, 12), sys.version')",
      "Bash(git ls-files --error-unmatch:*)",
      "Bash(git check-ignore --no-index -q --:*)",
      "Bash(git merge-base --is-ancestor 15cba0fbc6bf08dfabd060b1ab1e97d0512d22ba HEAD)",
      "Bash(grep -Fqx 'extend-exclude = [\"mcp\", \".rig\", \"blueprints\"]' pyproject.toml)",
      "Bash(grep -Fqx 'norecursedirs = [\"blueprints\", \".venv\", \".git\"]' pyproject.toml)",
      "Bash(git diff --cached --name-only)",
      "Bash(git rev-parse HEAD)",
      "Bash(shasum -a 256 CLAUDE.md)",
      "Bash(cut -d' ' -f1)",
      "Bash(mktemp -d)",
      "Bash(mkdir:*)",
      "Bash(cp docs/worked-engagement/run_eval.py docs/worked-engagement/scorer.py docs/worked-engagement/systems.py docs/worked-engagement/eval-set.jsonl:*)",
      "Bash(test ! -e:*)",
      "Bash(/tmp/fde-py312/bin/python \"$d/we/run_eval.py\")",
      "Bash(cmp \"$d/we/runs/baseline.json\" docs/worked-engagement/runs/baseline.json)",
      "Bash(cmp \"$d/we/runs/improved.json\" docs/worked-engagement/runs/improved.json)",
      "Bash(test -x /tmp/fde-py312/bin/python)",
      "Bash(test:*)",
      "Bash(test -z:*)",
      "Bash(test \"$(git diff --cached --name-only:*)",
      "Bash(test \"$rc\" -eq 1)",
      "Bash(git show HEAD:docs/worked-engagement/runs/*)",
      "Bash(git diff --exit-code HEAD -- pyproject.toml)",
      "Bash(python3 docs/worked-engagement/run_eval.py)",
      "Bash(PATH=/tmp/fde-py312/bin:$PATH python3 -c 'import sys; assert sys.prefix == \"/tmp/fde-py312\" and sys.version_info[:2] == (3, 12), (sys.prefix, sys.version)')",
      "Bash(PATH=/tmp/fde-py312/bin:$PATH python3 docs/worked-engagement/run_eval.py)",
      "Bash(echo:*)",
      "Bash(set -euo pipefail)",
      "Bash(exit 1)",
      "Bash(git switch:*)",
      "Bash(git show-ref:*)",
      "Bash(git cat-file:*)",
      "Bash(git status --porcelain)",
      "Bash(test ! -e .rig/proofs)",
      "Bash(/tmp/fde-py312/bin/fde-portfolio list)",
      "Bash(uv venv -q --allow-existing -p 3.10 /tmp/fde-py310)",
      "Bash(uv pip install -q --python /tmp/fde-py310/bin/python -e '.[dev]')",
      "Bash(/tmp/fde-py310/bin/ruff check .)",
      "Bash(/tmp/fde-py310/bin/python -m pytest -q)",
      "Bash(/tmp/fde-py310/bin/python docs/worked-engagement/run_eval.py --out:*)",
      "Bash(git rev-parse:*)",
      "Bash(LC_ALL=C sort)",
      "Bash(tr:*)"
    ],
    "deny": ["Bash(git push:*)", "Read(.env)", "Bash(git reset --hard:*)", "Bash(git branch -D:*)", "Bash(git tag -d:*)", "Bash(rm -f:*)", "Bash(rm -rf:*)"]
  }
}
```

### 19.4 Project skills — `.claude/skills/<name>/SKILL.md`
NOT APPLICABLE — no project skill is needed; no step references one.

### 19.5 `.claude/rules/*.md`
NOT APPLICABLE — the rules live in §19.1; no step references a rules file.

### 19.6 Verify-critical config and local infrastructure
Destination `pyproject.toml`: the two governing blocks after step 1, complete (every other block in
the file is unchanged):
```toml
[tool.ruff]
line-length = 110
target-version = "py310"
extend-exclude = ["mcp", ".rig", "blueprints"]

[tool.pytest.ini_options]
testpaths = ["tests"]
addopts = "-ra --strict-markers"
pythonpath = ["src"]
norecursedirs = ["blueprints", ".venv", ".git"]
```
The `[tool.ruff.lint]` and `[tool.ruff.lint.per-file-ignores]` blocks stay as on the base commit
(`select = ["E", "F", "W", "I", "B", "UP"]`, `"tests/*" = ["E501"]`). No services are needed.

Every file a Verify or §20.1 command names is created by a step: `CLAUDE.md`, `pyproject.toml` (1);
`tests/test_scorer.py` (2); `tests/test_systems.py` (4); `docs/worked-engagement/run_eval.py` and both
run files (5); `tests/test_docs.py` (6); `tests/test_field_record.py` (7); `scripts/smoke.sh` edited (10,
exists on base).

Field-record section literal (README, one line, exact):
```text
Every claim in [docs/field-record.md](docs/field-record.md) is confirmed against the maintainer's private career record, employers appear as sector pseudonyms, and the gaps are listed rather than filled.
```

Engagement section literal (README, one line, exact):
```text
[docs/worked-engagement/README.md](docs/worked-engagement/README.md) is a synthetic ticket-routing engagement: a frozen 34-item eval set, a baseline and an improved router, and results that one command reproduces byte for byte.
```

Runbook literal (`docs/runbook.md`, exact bytes, one trailing LF):
````markdown
# Runbook

## Rerun the eval

Requires Python 3.10 or newer, standard library only.

```bash
python3 docs/worked-engagement/run_eval.py && for f in baseline improved; do git show "HEAD:docs/worked-engagement/runs/$f.json" | cmp - "docs/worked-engagement/runs/$f.json" || exit 1; done
```

The command exits 0 only when the eval succeeds and the rerun reproduces the results committed at `HEAD` byte for byte.

## Change the eval set or a field-record fact

The eval set, the routers and the field record are frozen. Their bytes are pinned by
SHA-256 digests and exact-text tests, so any edit fails the suite on purpose. A change
needs a new blueprint that states the new fixture, the new digests and the new expected
results, and the owner's approval of it.
````

Operating-record literal (step 10, one line, exact):
```text
The playbooks above are the method; [CASE-STUDIES.md](CASE-STUDIES.md) holds six dated operations on a private AI fleet (storage integrity with hash-gated deletion, a container migration with preserved rollback, GPU serving restores behind idle gates, model-routing reconciliation, an MCP process-leak lifecycle fix). Every case names its evidence tier and carries a not-proven line. The case set was gated by an independent 2026-10-30 inventory audit that issued six required corrections before publication.
```

Frozen fixture `docs/worked-engagement/eval-set.jsonl` (exact bytes):
```jsonl
{"id": "T001", "text": "I was charged twice for my monthly plan this morning", "label": "billing"}
{"id": "T002", "text": "Why is my invoice higher than last month", "label": "billing"}
{"id": "T003", "text": "Please update the card on file for my subscription", "label": "billing"}
{"id": "T004", "text": "The billing statement shows a fee I do not recognise from your company", "label": "billing"}
{"id": "T005", "text": "Can I switch to annual invoicing", "label": "billing"}
{"id": "T006", "text": "My payment to the merchant failed but the charge still shows as pending", "label": "billing"}
{"id": "T007", "text": "I want my money back for the order that never arrived", "label": "refund"}
{"id": "T008", "text": "Please refund the duplicate payment", "label": "refund"}
{"id": "T009", "text": "Return started last week, when does the refund post", "label": "refund"}
{"id": "T010", "text": "The merchant agreed to a refund but I have not received it", "label": "refund"}
{"id": "T011", "text": "Cancel the order and give me a refund", "label": "refund"}
{"id": "T012", "text": "I did not refund anyone, why does my account show a refund issued", "label": "fraud"}
{"id": "T013", "text": "Someone used my card in another country, I did not make this purchase", "label": "fraud"}
{"id": "T014", "text": "There are three transactions I never authorised", "label": "fraud"}
{"id": "T015", "text": "I got a text asking for my PIN that claimed to be from you", "label": "fraud"}
{"id": "T016", "text": "My account was opened without my knowledge", "label": "fraud"}
{"id": "T017", "text": "Unrecognised login and then a transfer I did not make", "label": "fraud"}
{"id": "T018", "text": "I cannot log in, the reset link expired", "label": "access"}
{"id": "T019", "text": "Locked out after too many password attempts", "label": "access"}
{"id": "T020", "text": "Two factor code never arrives on my phone", "label": "access"}
{"id": "T021", "text": "How do I add a teammate to our merchant dashboard", "label": "access"}
{"id": "T022", "text": "My login works on mobile but not on the web", "label": "access"}
{"id": "T023", "text": "Need to remove access for an employee who left", "label": "access"}
{"id": "T024", "text": "What are your support hours", "label": "other"}
{"id": "T025", "text": "Do you have an API for exporting reports", "label": "other"}
{"id": "T026", "text": "Where is your office located", "label": "other"}
{"id": "T027", "text": "I want to give feedback on the new app design", "label": "other"}
{"id": "T028", "text": "Is there a partner program for agencies", "label": "other"}
{"id": "T029", "text": "Not a fraud issue, I just need a copy of last month's invoice", "label": "billing"}
{"id": "T030", "text": "This is not about access, I was charged a late fee by mistake", "label": "billing"}
{"id": "T031", "text": "I can log in fine but the refund I was promised is missing", "label": "refund"}
{"id": "T032", "text": "Not asking for a refund, someone stole my card details and bought things", "label": "fraud"}
{"id": "T033", "text": "Hello", "label": "other"}
{"id": "T034", "text": "Question about my account", "label": "other"}
```

Frozen module `docs/worked-engagement/systems.py` (exact bytes):
```python
"""Two SYNTHETIC routing systems for the worked engagement. No model calls."""

from __future__ import annotations

import re

# Baseline: the first keyword that matches wins; it always answers.
BASELINE_RULES = [
    ("refund", "refund"),
    ("fraud", "fraud"),
    ("charged", "billing"),
    ("invoice", "billing"),
    ("login", "access"),
    ("log in", "access"),
    ("password", "access"),
]

# Improved: weighted evidence per route, negation-aware, abstains below a margin.
WEIGHTS = {
    "billing": {"charged": 2, "invoice": 2, "invoicing": 2, "billing": 2, "fee": 1, "card on file": 2,
                "payment": 1, "subscription": 1, "plan": 1, "pending": 1},
    "refund": {"refund": 2, "money back": 3, "return": 2, "cancel the order": 2},
    "fraud": {"fraud": 2, "never authorised": 3, "did not make": 3, "stole": 3, "without my knowledge": 3,
              "pin": 2, "unrecognised login": 3, "another country": 2},
    "access": {"log in": 2, "login": 2, "password": 2, "locked out": 3, "reset link": 2,
               "two factor": 3, "access": 1, "teammate": 2, "dashboard": 1},
    "other": {"support hours": 3, "api": 2, "office": 2, "feedback": 2, "partner program": 3},
}
NEGATION = re.compile(r"\bnot (?:a |about |asking for a )?([a-z ]+?)(?: issue| request)?[,.]")
THRESHOLD = 2


def baseline(text: str) -> tuple[str | None, float]:
    low = text.lower()
    for word, route in BASELINE_RULES:
        if word in low:
            return route, 1.0
    return "other", 1.0


def improved(text: str) -> tuple[str | None, float]:
    low = text.lower()
    negated = {m.group(1).strip() for m in NEGATION.finditer(low)}
    scores = {}
    for route, words in WEIGHTS.items():
        total = 0
        for word, weight in words.items():
            if word in low and not any(word in neg for neg in negated):
                total += weight
        scores[route] = total
    ranked = sorted(scores.items(), key=lambda kv: (-kv[1], kv[0]))
    (top, top_score), (_, second) = ranked[0], ranked[1]
    if top_score < THRESHOLD or top_score - second < 1:
        return None, round(top_score / (top_score + second + 1), 4)
    return top, round(top_score / (top_score + second + 1), 4)
```

Expected published outcome (produced by the frozen fixture and module; step 5 test (c) gates it):
baseline `accuracy=0.5294 answered_accuracy=0.5294 coverage=1.0000 wrong_auto_routes=16`;
improved `accuracy=0.8529 answered_accuracy=1.0000 coverage=0.8529 wrong_auto_routes=0`.

| Authored literal | Governing rule | First comparison (comparator) | Both confirmed |
|---|---|---|---|
| `eval-set.jsonl` bytes | §19.6 frozen fixture | step 2 test, SHA-256 equals `dae205e9367083d71fb820a1a68ecb9755c4c2f0b03d7763ed50598714cc62d5` | yes, digest computed from the fixture source |
| `systems.py` bytes | §19.6 frozen module | step 4 test, SHA-256 equals `da5cc479476a48ace90d5619297530687145e574c16b762ccc760b983ef2f3a7` | yes, digest computed from the module source |
| `CLAUDE.md` bytes | §19.1 block, UTF-8, one trailing LF | step 1 Verify, SHA-256 equals `c0c057439f0ee06b9d30cb9666e52580a89189f3b51b60d44c8fe03b18d83373` | yes |
| `AGENTS.md` bytes | base-commit `AGENTS.md` plus the line `Build, lint, test and eval commands: see CLAUDE.md (canonical).` and one LF | step 1 Verify, `cmp` | yes |
| SYNTHETIC banner | step 6 literal | step 6 test, line 3 string equality | yes |
| `docs/field-record.md` bytes | `render(CARDS)` from §14 literals | step 7 test (f), byte equality incl. CRLF mutation | yes |
| operating-record paragraph | §19.6 literal | step 10 test (d), string equality | yes |
| README section bodies | §19.6 section literals | step 10 test (c), string equality | yes |
| `docs/runbook.md` bytes | §19.6 runbook literal | step 8 test, byte equality and SHA-256 `4cec86df18313cd6ca16bace5265da23124683547589ace4e0afd2a757ddb233` | yes |
| expected published outcome | §4 formulas, `round(x, 4)`; §5 `:.4f` print format. Property (producing code does not exist before the build): baseline `n=34, correct=18, answered=34, wrong_auto_routes=16`, `round(18/34,4)=0.5294`; improved `n=34, correct=29, answered=29, wrong_auto_routes=0`, `round(29/34,4)=0.8529`, `round(29/29,4)=1.0` | chain: step 5 test (a) stdout equals lines built from the JSON, (b) fresh JSON equals saved, (c) saved equals these values | property checked 2026-11-23 with `/tmp/fde-py312/bin/python3 -c` in /tmp; byte lines confirmed only after the build |
| saved run bytes | §4 UTF-8 canonical JSON | step 5 test (d), bytes equality | yes |

Runtime confirmation of these rows is recorded only after the builder runs those tests.

Byte-exact artifact reconciliation: the two run files are never hand-written; `run_eval.py` produces
them with the §4 serialization and step 5 test (b) compares a fresh run against them. The results rows
in the engagement README are compared against the run files by step 6's test.

| Resolution convention matrix: loader | How `scorer` and `systems` resolve |
|---|---|
| direct script: `python docs/worked-engagement/run_eval.py` (Verify and step 5 test (a) subprocess) | Python puts the script's folder at `sys.path[0]`, so `import scorer` and `import systems` resolve there |
| pytest: `tests/test_scorer.py`, `tests/test_systems.py`, `tests/test_docs.py` | `sys.path.insert(0, str(ROOT / "docs" / "worked-engagement"))` at module top; `src` via `pythonpath = ["src"]` |
| installed console script: `/tmp/fde-py312/bin/fde-portfolio check` | `[project.scripts] fde-portfolio = "fde_portfolio.cli:main"` in `pyproject.toml` (base commit), installed by §10's editable `uv pip install -e '.[dev]'`; unaffected by this change |

| Bundle-path exclusion | Literal exclusion |
|---|---|
| ruff | `extend-exclude = ["mcp", ".rig", "blueprints"]` |
| pytest | `norecursedirs = ["blueprints", ".venv", ".git"]` and `testpaths = ["tests"]` |

| Cross-artifact value | Literal | Source (authoritative) | Other occurrences | Compared |
|---|---|---|---|---|
| blueprint path | `blueprints/fde-field-record-blueprint.md` | §3 | §10, §19.6 exclusions | yes |
| `CLAUDE.md` | `CLAUDE.md` | §19.1 | §3, step map, step 1 | yes |
| ruff exclusion line | `extend-exclude = ["mcp", ".rig", "blueprints"]` | §19.6 block | step 1 Do, step 1 Verify, exclusion table | yes |
| pytest exclusion line | `norecursedirs = ["blueprints", ".venv", ".git"]` | §19.6 block | step 1 Do, step 1 Verify, exclusion table | yes |
| root README | `README.md` | §3 | step map, step 10, §19.1 | yes |
| engagement README | `docs/worked-engagement/README.md` | §3 | step map, step 6, step 10 link | yes |
| eval set | `docs/worked-engagement/eval-set.jsonl` (bytes: §19.6 fixture) | §3 | §4, step map, step 2, §19.1 | yes |
| scorer module | `docs/worked-engagement/scorer.py` | §3 | §5, step map, steps 2-3, §19.1 | yes |
| systems module | `docs/worked-engagement/systems.py` (bytes: §19.6 module) | §3 | §5, step map, step 4, §19.1 | yes |
| eval runner | `docs/worked-engagement/run_eval.py` | §5 | §3, step map, step 5, §19.1, §19.3, §20.1 | yes |
| baseline run | `docs/worked-engagement/runs/baseline.json` | §3 | §4, step map, step 5, §20.1 | yes |
| improved run | `docs/worked-engagement/runs/improved.json` | §3 | §4, step map, step 5, §20.1 | yes |
| field record | `docs/field-record.md` | §3 | step map, step 7, step 10, §19.1 | yes |
| failure taxonomy | `docs/failure-taxonomy.md` | §3 | step map, step 8, step 10 | yes |
| runbook | `docs/runbook.md` | §3 | step map, step 8, step 10 | yes |
| ADR 1 | `docs/adr/0001-deterministic-offline-eval.md` | §3 | step map, step 9 | yes |
| ADR 2 | `docs/adr/0002-confidence-gate-abstain-to-human.md` | §3 | step map, step 9 | yes |
| ADR 3 | `docs/adr/0003-claim-labels-and-pseudonyms.md` | §3 | step map, step 9 | yes |
| scorer test | `tests/test_scorer.py` | §3 | step map, steps 2-3, §19.3 | yes |
| systems test | `tests/test_systems.py` | §3 | step map, steps 4-5, §19.3 | yes |
| docs test | `tests/test_docs.py` | §3 | step map, steps 6, 8, 9, 10, §19.3 | yes |
| field record test | `tests/test_field_record.py` | §3 | step map, step 7, §19.3 | yes |
| smoke script | `scripts/smoke.sh` | §3 | step 10, §19.1, §19.3, §20.1 | yes |
| run output line | `f"{d['system']} accuracy={d['accuracy']:.4f} answered_accuracy={d['answered_accuracy']:.4f} coverage={d['coverage']:.4f} wrong_auto_routes={d['wrong_auto_routes']}"` | §5 | step 5 | yes |
| results row | `f"\| {d['system']} \| {d['accuracy']:.4f} \| {d['answered_accuracy']:.4f} \| {d['coverage']:.4f} \| {d['wrong_auto_routes']} \|"` | step 6 Do | step 6 test (Results-section check) | yes |
| SYNTHETIC banner | `> SYNTHETIC. Fictional company, fictional tickets. Every result in the table below is produced by run_eval.py.` | step 6 | none | yes |
| README headings | `## Field record`, `## Worked engagement (synthetic)`, `## Quick start` | step 10 | §1 target | yes |
| README links | `[docs/field-record.md](docs/field-record.md)`, `[docs/worked-engagement/README.md](docs/worked-engagement/README.md)` | §19.6 field-record and engagement section literals | step 10 Do, step 10 test (c) | yes |
| prediction keys | `id`, `route`, `confidence` | §4 | step 5 test (d) | yes |
| run keys | `system`, `n`, `answered`, `abstained`, `correct`, `wrong_auto_routes`, `accuracy`, `answered_accuracy`, `coverage`, `predictions` | §4 | step 5 test (d) | yes |
| run serialization | `json.dumps(obj, indent=2, sort_keys=True) + "\n"`, UTF-8 | §4 | step 5 Do, step 5 test (d) | yes |
| badge lines | `[![CI](https://img.shields.io/github/actions/workflow/status/mrodgersjs-web/fde-portfolio/ci.yml?branch=main&label=CI)](https://github.com/mrodgersjs-web/fde-portfolio/actions/workflows/ci.yml)`; `[![license MIT](https://img.shields.io/badge/license-MIT-0b3d2e)](LICENSE)`; `[![python 3.10+](https://img.shields.io/badge/python-3.10%2B-2c5f5f)](pyproject.toml)` | base `README.md:5-7` at `15cba0f` | step 10 test (a) `BADGES` constant, string equality | yes |
| no-new-image rule | only the three base badge lines contain `![` | step 10 test (a) | §1 target, Non-Goals, §15 | yes |
| runner output flag | `--out DIR` | §5 | step 5 Do, step 5 test (a) argv `"--out"` | yes |
| public rerun command | `python3 docs/worked-engagement/run_eval.py` | step 6 Do | step 6 test, §19.6 runbook literal | yes |
| pytest src path | `pythonpath = ["src"]` | §19.6 block | §19.6 resolution matrix | yes |
| field-record section literal | `Every claim in [docs/field-record.md](docs/field-record.md) is confirmed against the maintainer's private career record, employers appear as sector pseudonyms, and the gaps are listed rather than filled.` | §19.6 | step 10 Do, step 10 test (c) | yes |
| engagement section literal | `[docs/worked-engagement/README.md](docs/worked-engagement/README.md) is a synthetic ticket-routing engagement: a frozen 34-item eval set, a baseline and an improved router, and results that one command reproduces byte for byte.` | §19.6 | step 10 Do, step 10 test (c) | yes |
| runbook bytes | SHA-256 `4cec86df18313cd6ca16bace5265da23124683547589ace4e0afd2a757ddb233` of the §19.6 runbook body plus one LF | §19.6 | step 8 test | yes |
| runbook command | `python3 docs/worked-engagement/run_eval.py && for f in baseline improved; do git show "HEAD:docs/worked-engagement/runs/$f.json" \| cmp - "docs/worked-engagement/runs/$f.json" \|\| exit 1; done` | §19.6 runbook literal | step 8 Verify, gate G | yes |
| reader runtime requirement | `Requires Python 3.10 or newer, standard library only.` | step 6 Do (`## Rerun`) | §19.6 runbook literal, step 6 test | yes |
| AGENTS.md bridge line | `Build, lint, test and eval commands: see CLAUDE.md (canonical).` | step 1 Do | step 1 Verify, gate G, §19.2 | yes |
| census pattern | `\b\d[\d,]*\s*(?:-\|\s)?(?:\w+\s+){0,2}repo(?:s\|sitory\|sitories)?\b` | step 10 test (d) | none | yes |
| build python | `/tmp/fde-py312/bin/python` | §10b | every Verify, §19.1, §19.3, §20.1 | yes |
| build ruff | `/tmp/fde-py312/bin/ruff` | §19.1 | every Verify, §19.3, §20.1 | yes |
| console-script target | `fde_portfolio.cli:main` | `pyproject.toml` `[project.scripts]` | §1 current state, §19.6 resolution matrix | yes |
| build CLI | `/tmp/fde-py312/bin/fde-portfolio` | §19.1 | §19.3, §20.1, §19.6 matrix | yes |
| config file | `pyproject.toml` | §19.6 block | §3, step map, step 1, §11 | yes |
| build venv | `/tmp/fde-py312` | §10 | §2, §19.1, §19.3, every Verify | yes |
| build start record | `/tmp/fde-build-start` | §10 | §12 | yes |
| branch | `aside/tier2-portfolio-20261123` | header | §10, §12, §19.3 | yes |
| base commit | `15cba0fbc6bf08dfabd060b1ab1e97d0512d22ba` | header | §9, step map, §10 | yes |
| worked-engagement folder | `docs/worked-engagement/` | §3 | §1 target, §19.1, step 2, step 5 fixture path | yes |
| editable install extra | `.[dev]` | §10b | §11, §19.1, §19.3 | yes |
| case studies | `CASE-STUDIES.md` | §3 existing inputs | operating-record literal | yes |
| smoke input 1 | `docs/implementation-playbook.md` | `scripts/smoke.sh` (base) | §3 existing inputs, step 10 fixture | yes |
| smoke input 2 | `docs/architecture.md` | `scripts/smoke.sh` (base) | §3 existing inputs, step 10 fixture | yes |
| smoke input 3 | `docs/evaluation-strategy.md` | `scripts/smoke.sh` (base) | §3 existing inputs, step 10 fixture | yes |
| smoke input 4 | `docs/public-boundary.md` | `scripts/smoke.sh` (base) | §3 existing inputs, step 10 fixture | yes |
| hygiene test | `tests/test_repo_hygiene.py` | §3 existing inputs | step 10 Do | yes |
| isolated runner | `"$d/we/run_eval.py"` | gate G (step 5 on) | §20.1, §19.3 | yes |
| isolated baseline run | `"$d/we/runs/baseline.json"` | gate G (step 5 on) | §20.1 | yes |
| isolated improved run | `"$d/we/runs/improved.json"` | gate G (step 5 on) | §20.1 | yes |
| environment install | `test -x /tmp/fde-py312/bin/python \|\| uv venv -p 3.12 /tmp/fde-py312`; `/tmp/fde-py312/bin/python -c 'import sys; assert sys.version_info[:2] == (3, 12), sys.version'`; `uv pip install --python /tmp/fde-py312/bin/python -e '.[dev]'` | §10b lines 1-3 | §19.1, §20.1 (both copies), §19.3 | yes |
| §10b test line | `/tmp/fde-py312/bin/python -m pytest -q` | §10b line 4 | §20.1 bootstrap rerun | yes |
| distribution name | `fde-portfolio` (`[project] name`) | `pyproject.toml` (base) | §1, §5 | yes |
| console script | `fde-portfolio = "fde_portfolio.cli:main"` | `pyproject.toml` `[project.scripts]` (base) | §19.6 matrix, `/tmp/fde-py312/bin/fde-portfolio` | yes |
| public boundary literal | `The public boundary for this repository is in [docs/public-boundary.md](docs/public-boundary.md). Customers and employers appear only as sector pseudonyms, and every claim is a confirmed fact.` | step 10 Do | step 10 test (i) | yes |
| rerun heading | `## Rerun` | step 6 Do | step 6 test | yes |
| results heading | `## Results` | step 6 Do | step 6 test | yes |
| results header | `\| system \| accuracy \| answered_accuracy \| coverage \| wrong_auto_routes \|` | step 6 Do | step 6 test | yes |
| results separator | `\|---\|---\|---\|---\|---\|` | step 6 Do | step 6 test | yes |
| field-record title | `# Field record` | step 7 `render` | step 7 test (f) | yes |
| taxonomy header | `\| Class \| Seen in \| Detection signal \| Mitigation \|` | step 8 Do | step 8 test | yes |
| ADR headings | `## Context`, `## Decision`, `## Consequences`, `## Alternatives rejected` | step 9 Do | step 9 test | yes |
| README pytest row | `\| \`pytest -q --cov\` \| the full suite passes \| \`pytest -q --cov\` \|` | step 10 Do | step 10 test (h) | yes |
| README tests row | `\| \`tests/\` \| tests covering schema, render, CLI, drift scans, repo hygiene, the eval and the docs \|` | step 10 Do | step 10 test (h) | yes |
| public boundary heading | `## Public Boundary` | step 10 Do | step 10 test (i) | yes |
| bridge file | `AGENTS.md` | §19.2 | §19 intro, §19.1 rules | yes |
| field-record legend | `Every claim below is [confirmed] against the maintainer's private career record. Employers and clients appear as sector pseudonyms. Gaps are listed, not filled.` | §14 | step 7 `CARDS`/`render` | yes |
| field-record table header | `\| Engagement \| Years \| Sector \|` | step 7 | §14 table | yes |
| field-record card labels | `**Evidence.**`, `**Not yet evidenced.**` | step 7 | none | yes |
| claim 1 (Independent AI practice) | `8 client engagements since 2025` | §14 claims table | step 7 `CARDS`, rendered `docs/field-record.md` | yes |
| claim 2 (Independent AI practice) | `6 client AI applications live under a written reference architecture, each with a roadmap, service level and health metrics` | §14 claims table | step 7 `CARDS`, rendered `docs/field-record.md` | yes |
| claim 3 (Independent AI practice) | `Up to 80% adoption of client AI applications through walkthroughs, training and super-user networks` | §14 claims table | step 7 `CARDS`, rendered `docs/field-record.md` | yes |
| claim 4 (Independent AI practice) | `8 activate, buy or build feasibility reviews with client IT before spend` | §14 claims table | step 7 `CARDS`, rendered `docs/field-record.md` | yes |
| claim 5 (Independent AI practice) | `6 third-party AI vendors vetted for model risk` | §14 claims table | step 7 `CARDS`, rendered `docs/field-record.md` | yes |
| claim 6 (Independent AI practice) | `A measured cut of about 20% in run cost, incidents, manual handling or review cycle time` | §14 claims table | step 7 `CARDS`, rendered `docs/field-record.md` | yes |
| claim 7 (Independent AI practice) | `Confidence-gated AI actions with a tamper-evident audit trail, guardrails and eval harnesses` | §14 claims table | step 7 `CARDS`, rendered `docs/field-record.md` | yes |
| claim 8 (Independent AI practice) | `About 30% of practice time on self-learning systems that improve from usage feedback` | §14 claims table | step 7 `CARDS`, rendered `docs/field-record.md` | yes |
| claim 9 (Health IT vendor, AI portfolio) | `AI and analytics intake of 12 use cases, top 4 funded` | §14 claims table | step 7 `CARDS`, rendered `docs/field-record.md` | yes |
| claim 10 (Health IT vendor, AI portfolio) | `8 AI business cases built with Finance` | §14 claims table | step 7 `CARDS`, rendered `docs/field-record.md` | yes |
| claim 11 (Health IT vendor, AI portfolio) | `3 AI and analytics vendor evaluations with Procurement, Risk and Legal` | §14 claims table | step 7 `CARDS`, rendered `docs/field-record.md` | yes |
| claim 12 (Health IT vendor, AI portfolio) | `An AI capability taken through formal security, privacy, HIPAA and compliance review` | §14 claims table | step 7 `CARDS`, rendered `docs/field-record.md` | yes |
| claim 13 (Regional health system, digital and AI innovation) | `AI and ML work since 2019, including radiology read prioritization about 15% faster` | §14 claims table | step 7 `CARDS`, rendered `docs/field-record.md` | yes |
| claim 14 (Regional health system, digital and AI innovation) | `6 digital-health projects run through an innovation center of excellence` | §14 claims table | step 7 `CARDS`, rendered `docs/field-record.md` | yes |
| claim 15 (Telehealth startup, product roadmap) | `6 end-user focus groups and roadmap sessions with health-system partners` | §14 claims table | step 7 `CARDS`, rendered `docs/field-record.md` | yes |
| gap 1 (Independent AI practice) | `Client-attributable before and after metrics per engagement` | §14 gaps table | step 7 `CARDS`, rendered `docs/field-record.md` | yes |
| gap 2 (Health IT vendor, AI portfolio) | `Market-signal volume for the competitive intelligence capability` | §14 gaps table | step 7 `CARDS`, rendered `docs/field-record.md` | yes |
| gap 3 (Regional health system, digital and AI innovation) | `Teletriage scale and emergency wait-time figures` | §14 gaps table | step 7 `CARDS`, rendered `docs/field-record.md` | yes |
| gap 4 (Telehealth startup, product roadmap) | `Deployment and outcome facts for the platform` | §14 gaps table | step 7 `CARDS`, rendered `docs/field-record.md` | yes |
| runs folder | `docs/worked-engagement/runs` | §3 | §20.1 diff, §19.6 runbook literal, gate G | yes |
| package folder | `src/fde_portfolio/` | §1 Current state | §1 Non-Goals, §19.1 `CLAUDE.md` | yes |
| `ALLOWED_NUMBERS` | `{"2013", "2019", "2020", "2021", "2025", "2026", "3", "4", "6", "8", "12", "15", "20", "30", "80"}` | §14 | step 7 test (d) | yes |
| operating-record body | `The playbooks above are the method; [CASE-STUDIES.md](CASE-STUDIES.md) holds six dated operations on a private AI fleet (storage integrity with hash-gated deletion, a container migration with preserved rollback, GPU serving restores behind idle gates, model-routing reconciliation, an MCP process-leak lifecycle fix). Every case names its evidence tier and carries a not-proven line. The case set was gated by an independent 2026-10-30 inventory audit that issued six required corrections before publication.` | §19.6 | step 10 Do, step 10 test (d) | yes |
| step tag 1 | `step-01-workspace` | §20.1 | step 1 Checkpoint, §10, §12, §19.3 | yes |
| step tag 2 | `step-02-eval-set` | §20.1 | step 2 Checkpoint, §10, §12, §19.3 | yes |
| step tag 3 | `step-03-score` | §20.1 | step 3 Checkpoint, §10, §12, §19.3 | yes |
| step tag 4 | `step-04-systems` | §20.1 | step 4 Checkpoint, §10, §12, §19.3 | yes |
| step tag 5 | `step-05-runs` | §20.1 | step 5 Checkpoint, §10, §12, §19.3 | yes |
| step tag 6 | `step-06-engagement-readme` | §20.1 | step 6 Checkpoint, §10, §12, §19.3 | yes |
| step tag 7 | `step-07-field-record` | §20.1 | step 7 Checkpoint, §10, §12, §19.3 | yes |
| step tag 8 | `step-08-ops-docs` | §20.1 | step 8 Checkpoint, §10, §12, §19.3 | yes |
| step tag 9 | `step-09-adrs` | §20.1 | step 9 Checkpoint, §10, §12, §19.3 | yes |
| step tag 10 | `step-10-readme` | §20.1 | step 10 Checkpoint, §10, §12, §19.3 | yes |

## 20. Acceptance Gate, Risks & Decision Log

### 20.1 Global acceptance gate
Run as one script under `set -euo pipefail`; the first nonzero status fails the gate. It checks each
of the 22 unique Touches paths individually for tracking and, with `git check-ignore --no-index`,
requires exit status exactly 1 (no `.gitignore` rule matches).
```bash
set -euo pipefail
# environment install for this checkout (§10b lines 1-3), before any tool runs
test -x /tmp/fde-py312/bin/python || uv venv -p 3.12 /tmp/fde-py312
/tmp/fde-py312/bin/python -c 'import sys; assert sys.version_info[:2] == (3, 12), sys.version'
uv pip install --python /tmp/fde-py312/bin/python -e '.[dev]'
/tmp/fde-py312/bin/ruff check .                                            # expect: exit 0
/tmp/fde-py312/bin/python -m pytest -q                                     # expect: exit 0, 0 failed
/tmp/fde-py312/bin/fde-portfolio check                                     # expect: exit 0
/tmp/fde-py312/bin/fde-portfolio list                                      # expect: exit 0 (existing CI step)
uv venv -q --allow-existing -p 3.10 /tmp/fde-py310 && uv pip install -q --python /tmp/fde-py310/bin/python -e '.[dev]'
/tmp/fde-py310/bin/ruff check . && /tmp/fde-py310/bin/python -m pytest -q   # expect: exit 0, CI's 3.10 matrix leg
d310="$(mktemp -d)"; /tmp/fde-py310/bin/python docs/worked-engagement/run_eval.py --out "$d310" && cmp "$d310/baseline.json" docs/worked-engagement/runs/baseline.json && cmp "$d310/improved.json" docs/worked-engagement/runs/improved.json   # expect: exit 0, reader minimum 3.10 reproduces the runs
bash scripts/smoke.sh                                             # expect: exit 0
test -z "$(git status --porcelain)"   # expect: exit 0, clean checkout
git ls-files --error-unmatch AGENTS.md   # expect: exit 0
rc=0; git check-ignore --no-index -q -- AGENTS.md || rc=$?; test "$rc" -eq 1   # expect: exit 0, no ignore rule matches
git ls-files --error-unmatch CLAUDE.md   # expect: exit 0
rc=0; git check-ignore --no-index -q -- CLAUDE.md || rc=$?; test "$rc" -eq 1   # expect: exit 0, no ignore rule matches
git ls-files --error-unmatch pyproject.toml   # expect: exit 0
rc=0; git check-ignore --no-index -q -- pyproject.toml || rc=$?; test "$rc" -eq 1   # expect: exit 0, no ignore rule matches
git ls-files --error-unmatch docs/worked-engagement/eval-set.jsonl   # expect: exit 0
rc=0; git check-ignore --no-index -q -- docs/worked-engagement/eval-set.jsonl || rc=$?; test "$rc" -eq 1   # expect: exit 0, no ignore rule matches
git ls-files --error-unmatch docs/worked-engagement/scorer.py   # expect: exit 0
rc=0; git check-ignore --no-index -q -- docs/worked-engagement/scorer.py || rc=$?; test "$rc" -eq 1   # expect: exit 0, no ignore rule matches
git ls-files --error-unmatch tests/test_scorer.py   # expect: exit 0
rc=0; git check-ignore --no-index -q -- tests/test_scorer.py || rc=$?; test "$rc" -eq 1   # expect: exit 0, no ignore rule matches
git ls-files --error-unmatch docs/worked-engagement/systems.py   # expect: exit 0
rc=0; git check-ignore --no-index -q -- docs/worked-engagement/systems.py || rc=$?; test "$rc" -eq 1   # expect: exit 0, no ignore rule matches
git ls-files --error-unmatch tests/test_systems.py   # expect: exit 0
rc=0; git check-ignore --no-index -q -- tests/test_systems.py || rc=$?; test "$rc" -eq 1   # expect: exit 0, no ignore rule matches
git ls-files --error-unmatch docs/worked-engagement/run_eval.py   # expect: exit 0
rc=0; git check-ignore --no-index -q -- docs/worked-engagement/run_eval.py || rc=$?; test "$rc" -eq 1   # expect: exit 0, no ignore rule matches
git ls-files --error-unmatch docs/worked-engagement/runs/baseline.json   # expect: exit 0
rc=0; git check-ignore --no-index -q -- docs/worked-engagement/runs/baseline.json || rc=$?; test "$rc" -eq 1   # expect: exit 0, no ignore rule matches
git ls-files --error-unmatch docs/worked-engagement/runs/improved.json   # expect: exit 0
rc=0; git check-ignore --no-index -q -- docs/worked-engagement/runs/improved.json || rc=$?; test "$rc" -eq 1   # expect: exit 0, no ignore rule matches
git ls-files --error-unmatch docs/worked-engagement/README.md   # expect: exit 0
rc=0; git check-ignore --no-index -q -- docs/worked-engagement/README.md || rc=$?; test "$rc" -eq 1   # expect: exit 0, no ignore rule matches
git ls-files --error-unmatch tests/test_docs.py   # expect: exit 0
rc=0; git check-ignore --no-index -q -- tests/test_docs.py || rc=$?; test "$rc" -eq 1   # expect: exit 0, no ignore rule matches
git ls-files --error-unmatch docs/field-record.md   # expect: exit 0
rc=0; git check-ignore --no-index -q -- docs/field-record.md || rc=$?; test "$rc" -eq 1   # expect: exit 0, no ignore rule matches
git ls-files --error-unmatch tests/test_field_record.py   # expect: exit 0
rc=0; git check-ignore --no-index -q -- tests/test_field_record.py || rc=$?; test "$rc" -eq 1   # expect: exit 0, no ignore rule matches
git ls-files --error-unmatch docs/failure-taxonomy.md   # expect: exit 0
rc=0; git check-ignore --no-index -q -- docs/failure-taxonomy.md || rc=$?; test "$rc" -eq 1   # expect: exit 0, no ignore rule matches
git ls-files --error-unmatch docs/runbook.md   # expect: exit 0
rc=0; git check-ignore --no-index -q -- docs/runbook.md || rc=$?; test "$rc" -eq 1   # expect: exit 0, no ignore rule matches
git ls-files --error-unmatch docs/adr/0001-deterministic-offline-eval.md   # expect: exit 0
rc=0; git check-ignore --no-index -q -- docs/adr/0001-deterministic-offline-eval.md || rc=$?; test "$rc" -eq 1   # expect: exit 0, no ignore rule matches
git ls-files --error-unmatch docs/adr/0002-confidence-gate-abstain-to-human.md   # expect: exit 0
rc=0; git check-ignore --no-index -q -- docs/adr/0002-confidence-gate-abstain-to-human.md || rc=$?; test "$rc" -eq 1   # expect: exit 0, no ignore rule matches
git ls-files --error-unmatch docs/adr/0003-claim-labels-and-pseudonyms.md   # expect: exit 0
rc=0; git check-ignore --no-index -q -- docs/adr/0003-claim-labels-and-pseudonyms.md || rc=$?; test "$rc" -eq 1   # expect: exit 0, no ignore rule matches
git ls-files --error-unmatch README.md   # expect: exit 0
rc=0; git check-ignore --no-index -q -- README.md || rc=$?; test "$rc" -eq 1   # expect: exit 0, no ignore rule matches
git ls-files --error-unmatch scripts/smoke.sh   # expect: exit 0
rc=0; git check-ignore --no-index -q -- scripts/smoke.sh || rc=$?; test "$rc" -eq 1   # expect: exit 0, no ignore rule matches
d="$(mktemp -d)"; mkdir "$d/we"; cp docs/worked-engagement/run_eval.py docs/worked-engagement/scorer.py docs/worked-engagement/systems.py docs/worked-engagement/eval-set.jsonl "$d/we/"
/tmp/fde-py312/bin/python "$d/we/run_eval.py"   # expect: exit 0, default invocation into a copy with no runs/
cmp "$d/we/runs/baseline.json" docs/worked-engagement/runs/baseline.json   # expect: exit 0, file created and equal
cmp "$d/we/runs/improved.json" docs/worked-engagement/runs/improved.json   # expect: exit 0, file created and equal
for f in baseline improved; do git show "HEAD:docs/worked-engagement/runs/$f.json" | cmp - "docs/worked-engagement/runs/$f.json" || exit 1; done   # expect: exit 0, each rerun file equals its HEAD blob
for t in step-01-workspace step-02-eval-set step-03-score step-04-systems step-05-runs step-06-engagement-readme step-07-field-record step-08-ops-docs step-09-adrs step-10-readme; do git rev-parse -q --verify "refs/tags/$t^{commit}" >/dev/null || exit 1; done   # expect: exit 0, all ten tags resolve
# Bootstrap rerun (§10b, executable)
test -x /tmp/fde-py312/bin/python || uv venv -p 3.12 /tmp/fde-py312
/tmp/fde-py312/bin/python -c 'import sys; assert sys.version_info[:2] == (3, 12), sys.version'
uv pip install --python /tmp/fde-py312/bin/python -e '.[dev]'
/tmp/fde-py312/bin/python -m pytest -q   # expect: exit 0, 0 failed
git diff --exit-code HEAD -- pyproject.toml   # expect: exit 0, manifest unchanged by the rerun
/tmp/fde-py312/bin/fde-portfolio check   # expect: exit 0, installed CLI works after the rerun
test ! -e .rig/proofs   # expect: exit 0, no proof file added by this build
```


Completion proof: the sealed proof (`AGENTS.md`: four ratios >= 0.85) is out of scope for this local
build (Non-Goals) and is not a §20.1 gate; this build writes nothing under `.rig/`, checked by
`test ! -e .rig/proofs` above, so CI's proof step stays skipped. "Done" for this blueprint means §20.1
exits 0; durable-build sealing is a separate owner step after Mike confirms the architecture.

Post-build launch checklist (not gates, per `docs/public-boundary.md`): `flag-gate.sh` PASS (the
maintainer's approved copy, outside this repository); a human review of history and large blobs; the
README keeps its `## Public Boundary` section (step 10); no deploy keys or webhooks copied; the owner adds hero media
under the H1 in a later commit;
Mike approves the push of the branch.

### 20.2 Risk register
| Risk | Mitigation |
|---|---|
| A field-record number not in the corpus | `ALLOWED_NUMBERS` test plus label test |
| Synthetic engagement read as real | banner on line 3, fictional company |
| Unknown fact written as a claim | public-claim rule (§14) plus step 7 exact-claim test |
| README hygiene test breaks | full suite runs in step 10 |

### 20.3 Decision log
| Decision | Because |
|---|---|
| Rule-based systems, no LLM | numbers reproduce offline, byte for byte |
| Wrong auto routes scored apart from accuracy | a confident wrong action costs more than a handoff to a human |
| Employers shown as sector pseudonyms | the public boundary rule extends cleanly; facts stay checkable privately |
| Per-step explicit staging | the blueprint and private notes never enter history by accident |

### 20.4 What to build next
A model-backed third system behind the same scorer; a short demo video; a second engagement.
