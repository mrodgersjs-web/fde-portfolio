# Security

## Reporting a vulnerability

Email **security@rodgersintelligence.com**. Do not open a public
GitHub issue for suspected vulnerabilities. Reports are acknowledged
within two business days and a fix or a documented mitigation lands
on a published timeline for any in-scope advisory.

## Supported versions

| version | status |
|---|---|
| 0.2.x | supported |
| 0.1.x | supported until 2027-04-19 |
| older | unsupported |

## Threat model

This repository is a documentation-first public FDE playbook
template. Its surface is YAML data plus a tiny read-only Python
CLI. It does not run network requests, never connects to a
customer system, and never reads any environment variable or
secret.

What the CLI does:

- Reads YAML files from the package itself (or from a `--root`
  directory) and validates them against the bundled JSON Schemas.
- Renders the YAML to Markdown and writes the output to a path
  the caller chooses (`--out`) or to `stdout`.

Where the residual risk is:

- `--out <path>` can write anywhere the user can; this is by
  design and the user is expected to pass a path inside their
  working directory. The CLI does not canonicalize or follow
  symlinks for output paths.
- YAML parsing is delegated to PyYAML; the Schemas are bounds
  checks on the parsed document. A schema violation is the only
  failure the package produces for a malformed input.

## Out of scope

- `examples/audit-log/` and `examples/eval-harness/` are stub
  READMEs; nothing in this repo runs or imports them. Their security
  model is whatever future content lands there.
- `mcp/server.py` depends on RIG lattice tooling outside this
  repo and is not exercised by CI here.
- `.rig/hooks/pre-tool` is the RIG lattice hook wrapper; it is
  not used outside the lattice project.

## Known limitations

- The CLI does no I/O outside the path the user specifies with
  `--out`. A `--root` path is read but never executed. A typo
  in either is a footgun, not a security boundary.
- YAML safe-load is on, not full-load; the package never imports
  arbitrary Python from a YAML file.
