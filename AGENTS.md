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

## RIG lattice contract (stamped)

This repository runs the shared RIG lattice: loops in `.rig/loop.yaml`, pre-tool
hooks in `.rig/hooks/`, CI gate in `.github/workflows/rig-lattice.yml`. D85 rules
apply: every outward action needs a Gate-D request + typed approval; durable
builds need four ratios >= 0.85 and a sealed proof. Shared agent substrate lives
in Supabase schema `rig_shared` (see PROGRAM.md in rig-lattice-retrofit).
