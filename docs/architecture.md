# Reference architecture

```text
Customer workflow
   │
   ▼
Context boundary (sources, tools, memory, policy)
   │
   ▼
Deterministic gates ──► Agent / model steps (earned autonomy)
   │
   ▼
Eval harness + human approval (risk-tiered)
   │
   ▼
Audit log / ProofPacket
   │
   ▼
Operable handoff (runbooks, owners, rollback)
```

Principles: local-first when possible, secrets out of prompts, proof before "done".
