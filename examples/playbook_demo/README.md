# Example: a runnable end-to-end check of the FDE playbook bundle

This example exercises the bundled playbook data end-to-end without
the network, without secrets, and without a customer system. It
does the same work the CI tests do, but as a shell command you can
read and copy.

## Run

```sh
cd /Users/rig128gb/Developer/fde-portfolio
python3 -m venv .venv && . .venv/bin/activate
pip install -e '.[dev]'

# 1. List every bundled playbook with the item count
fde-portfolio list

# 2. Validate every playbook against the JSON Schema
fde-portfolio check

# 3. Render one playbook as a Markdown checklist
fde-portfolio checklist discovery --project "Acme AI intake"

# 4. Render the full project worksheet (all five phases)
fde-portfolio build --project "Acme AI intake" --out /tmp/worksheet.md
head -30 /tmp/worksheet.md
```

Every step exits 0. `pytest -q` runs the same validations plus the
no-client-name scan and the no-invented-outcome scan.

## What this proves

- `list` shows the five bundled playbooks with the live item count.
- `check` walks each YAML against `src/fde_portfolio/schemas/file.schema.json`
  and the per-item rules in `loader.py`. A schema failure here
  blocks the build in CI on the same call.
- `checklist` produces a Markdown checklist that any reviewer can
  open without installing anything else. The checkbox row carries
  the item type (`Q` / `T` / `D` / `E` / `O`), the default owner,
  the description, and any cross-references or example shells.
- `build` is the same as `checklist` but prints all five phases in
  canonical order, so a single command produces the worksheet for
  a real engagement.

## When to run it

- After editing any YAML under `src/fde_portfolio/playbooks/`.
- Before any PR that adds or removes a playbook item, a schema
  field, or a CLI subcommand.
- As a fresh-clone check that the bundle still parses after a
  major schema bump.
