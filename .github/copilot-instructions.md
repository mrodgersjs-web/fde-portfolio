# Copilot instructions

## Repository purpose

`fde-portfolio` is a documentation-first review path for customer-facing AI implementation: discovery, bounded architecture, evaluation, rollout proof, and operable handoff.

## Work map

- `docs/`: discovery, architecture, evaluation, implementation, and public-boundary guidance.
- `examples/`: audit-log and evaluation-harness examples.
- `templates/`: customer implementation and go-live checklists.
- `scripts/`: repository smoke entry point.
- `assets/`: public visual demonstrations.
- `graft/`: generated context; read when needed and leave unchanged.

## Commands

No dependency bootstrap or application runtime is required. Test and smoke from the repository root:

```bash
bash scripts/smoke.sh
```

## Editing rules

- Keep the portfolio public, actionable, and concise.
- Ground claims in repository evidence and preserve the discovery-to-handoff sequence.
- Keep secrets, client PII, prospect lists, auth material, and private monorepo content out.
- Preserve human approval at real risk boundaries and `docs/public-boundary.md`.
- Always run the smoke command before claiming done.
