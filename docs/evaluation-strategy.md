# Evaluation strategy

| Layer | What | Pass means |
|---|---|---|
| Contract tests | schemas, CLI exit codes | exit 0 |
| Workflow evals | golden tasks + edge cases | score ≥ threshold |
| False-done tests | forged success claims | signature/gate fails |
| Human review | high-risk samples | reviewer accepts |
| Soak | limited production cohort | error budget holds |

Never scale a loop that cannot fail a planted false-done case.
