# fde-portfolio

> Customer-facing AI implementation: discover the real workflow, design a bounded system, evaluate it, ship with proof, and hand off operable infrastructure.
**Outcome:** Portfolio provides an 8-minute review path linking 9 live studios, each with clone-and-run demo proof.


![status](https://img.shields.io/badge/status-public-studio-blue)
![role](https://img.shields.io/badge/role-Forward%20Deployed%20Engineer-0b3d2e)
![proof](https://img.shields.io/badge/proof-required-orange)

## Resume

[Mike Rodgers — Forward Deployed Engineer](https://github.com/mrodgersjs-web/resume) ([PDF](https://github.com/mrodgersjs-web/resume/blob/main/Mike-Rodgers-Forward-Deployed-Engineer.pdf))

## Employer summary

This repository is the **review path** for hiring managers and technical leaders evaluating Forward Deployed / AI Solutions / Applied AI engineering work.

It is not a dump of experiments. It shows the operating layer that decides whether an AI workflow survives production: requirements, context boundaries, evals, auditability, rollout, and customer handoff.

**Screening question answered here:**  
*Can this person turn an ambiguous AI mandate into a supportable deployment with evidence?*

### 8-minute review path

1. This README  
2. [`docs/implementation-playbook.md`](docs/implementation-playbook.md)  
3. [`docs/architecture.md`](docs/architecture.md)  
4. [`docs/evaluation-strategy.md`](docs/evaluation-strategy.md)  
5. [`docs/customer-discovery.md`](docs/customer-discovery.md)  
6. [`docs/public-boundary.md`](docs/public-boundary.md)  
7. Live studios linked below — clone one and run a demo  

## Why this exists

Most AI projects do not fail because a model cannot produce text.  
They fail because the implementation never becomes trustworthy inside the customer workflow.

This portfolio encodes the implementation layer I care about:

- translating messy business context into usable system boundaries  
- designing agentic workflows with human approval and rollback  
- building eval loops that catch regressions before users do  
- making outputs inspectable with audit logs and provenance  
- turning one-off delivery into reusable templates and tools  

## Reference loop

```text
workflow reality
   → bound context / tools / memory / policy
   → deterministic gates
   → agent steps (earned autonomy)
   → eval harness + human approval
   → ProofPacket / audit log
   → operable handoff
```

## Live system surface (this GitHub)

| Studio | What it proves |
| --- | --- |
| [proof-studio](https://github.com/mrodgersjs-web/proof-studio) | Signed completion claims; false-done catch |
| [jake-studio](https://github.com/mrodgersjs-web/jake-studio) | Operator OS + L10 harness + closed loops |
| [mesh-studio](https://github.com/mrodgersjs-web/mesh-studio) | Multi-node subsystem probe / boot / recover |
| [agency-studio](https://github.com/mrodgersjs-web/agency-studio) | Role contracts — Builder ≠ Verifier |
| [app-factory-studio](https://github.com/mrodgersjs-web/app-factory-studio) | Spec → scaffold with definition-of-done chain |
| [communications-studio](https://github.com/mrodgersjs-web/communications-studio) | Gated communication protocol engine |
| [strategy-studio](https://github.com/mrodgersjs-web/strategy-studio) | Deterministic strategy routing |
| [doctrine](https://github.com/mrodgersjs-web/doctrine) | Rules agents load before they act |
| [openwork](https://github.com/mrodgersjs-web/openwork) | Power-user agent workstation |

## Repository map

| Path | What it shows |
| --- | --- |
| [`docs/implementation-playbook.md`](docs/implementation-playbook.md) | Discovery → go-live phases |
| [`docs/architecture.md`](docs/architecture.md) | Reference architecture for grounded AI workflows |
| [`docs/evaluation-strategy.md`](docs/evaluation-strategy.md) | Contract tests, workflow evals, false-done plants |
| [`docs/customer-discovery.md`](docs/customer-discovery.md) | Questions that turn vague asks into buildable scope |
| [`docs/public-boundary.md`](docs/public-boundary.md) | What is intentionally excluded from public surfaces |
| [`templates/customer-implementation-plan.md`](templates/customer-implementation-plan.md) | Reusable engagement plan skeleton |
| [`templates/go-live-checklist.md`](templates/go-live-checklist.md) | Practical go-live checklist |
| [`examples/audit-log/`](examples/audit-log/) | Audit log pattern notes |
| [`examples/eval-harness/`](examples/eval-harness/) | Eval harness pattern notes |

## 60-second adjacent proof

This repo is documentation-first. The fastest executable proof on the account:

```bash
git clone https://github.com/mrodgersjs-web/proof-studio.git
cd proof-studio/packages/rigforge
python3 -m venv .venv && source .venv/bin/activate
pip install -e .
rigforge demo
```

## Operating principles

1. Outcome first.  
2. Ground everything.  
3. Evals before scale.  
4. Human approval where risk is real.  
5. Auditability is product quality.  
6. Smallest useful loop, then harden.  

## Public boundary

No customer PII, prospect lists, auth cookies, ToS-risk engagement automation, or internal client monorepos.  
See [`docs/public-boundary.md`](docs/public-boundary.md).

## Video walkthrough

- Script: [`docs/video-script.md`](docs/video-script.md)  
- Recording: `assets/demo.mp4` (pending render)  

## Related

- Profile: [mrodgersjs-web](https://github.com/mrodgersjs-web)  
- [proof-studio](https://github.com/mrodgersjs-web/proof-studio) · [jake-studio](https://github.com/mrodgersjs-web/jake-studio) · [doctrine](https://github.com/mrodgersjs-web/doctrine)  

## License

MIT — see [`LICENSE`](LICENSE).


---

## FDE bar (this studio)

| Practice | Here |
| --- | --- |
| Employer summary | top of README |
| 60s / smoke proof |  |
| Public boundary |  |
| Claim under test | '"playbooks + review path present"' |
| Related fleet | [profile](https://github.com/mrodgersjs-web) · [resume](https://github.com/mrodgersjs-web/resume) · [patents teaser](https://github.com/mrodgersjs-web/patents) |

If  fails, the README claim is considered false until fixed.

- Preview: [`assets/demo.gif`](assets/demo.gif)
