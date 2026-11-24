# Synthetic engagement: AI review queue for a document operations team

Sector-pseudonymized, fully synthetic. No client name, no real data, no AI portrait.

## Worked example: the pipeline under test

| Stage | What it does | Failure mode | Control |
|---|---|---|---|
| Intake parser | Normalizes incoming docs to typed records | Field loss on multi-page forms | Schema validation, reject with reason code |
| Pre-screen model | Flags records needing human review | Silent pass on corrupt input | Confidence floor, corrupt input escalates |
| LLM ranker | Ranks flagged records by review urgency | Confident-sounding wrong ranking | Constrained output, rank must cite a field |
| Rules gate | Blocks release of a review packet | Gate bypass on partial data | All checks run, missing check is a fail |
| Escalation lane | Routes hard cases to the operator | Queue growth, operator ignored | Bounded auto-merge tier, KPI on queue age |
| Audit log | Records every decision and its inputs | Log overwritten by re-runs | Per-pass evidence dir, published pass is immutable |

## The scenario
A document operations team reviews vendor intake packets. Today: manual read, manual sort, no record of why. Constraint: the team keeps final say; the system may only auto-merge a bounded tier.

## Deployment sequence (this is the contract an interviewer can question)
| 1 | Instrument the queue: log every decision and input, read-only | Queue age and touch time measured, no behavior change |
| 2 | Baseline run: parse, score, rank, gate on a fixed 200-record fixture | Scores recorded, immutably, as the pass record |
| 3 | Deploy pre-screen in shadow: model proposes, human decides | Agreement rate, model disagreements studied |
| 4 | Add rules gate: releases require all checks, a missing check fails | Gate fired count, blocked-release count |
| 5 | Open the bounded auto-merge tier | Auto-merge share, error rate inside the tier, recall into the human lane |
| 6 | Retest on the same fixture, report as a delta on the baseline | Every metric, baseline and after, side by side |

Adoption metric: review time per packet and queue age, reported as a measured percentage change, not an absolute business claim. Rollback: the gate is a pass-through flag; the queue predates the system and stays warm.
