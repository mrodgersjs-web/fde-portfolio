# AGENTS.md — fde-portfolio
Public FDE hub. No secrets, no client PII. Keep playbooks actionable and short.

## Repository quick reference

`fde-portfolio` is a documentation-first review path for customer-facing AI discovery, bounded architecture, evaluation, rollout proof, and operable handoff. No dependency bootstrap or application runtime is required.

- `docs/`: discovery, architecture, evaluation, implementation, and public-boundary guidance.
- `examples/`: audit-log and evaluation-harness patterns.
- `templates/`: implementation and go-live checklists.
- `scripts/`: repository smoke entry point.
- `assets/`: public visual demonstrations.
- `graft/`: generated context; read when useful and preserve unchanged.

Test and smoke from the repository root:

```bash
bash scripts/smoke.sh
```

Always run the smoke command before claiming done.
