# Runbook

Operational sequence for the FDE loop, from the six field operations.
[corpus] facts from Mike's career answers corpus (RIG section, confirmed
2026-11-10). Run read-mostly; every mutation has a gate and a not-proven line.

1. Size the leak before the fix. Enumerate processes and RSS; a fleet dies
   quietly from a leak you have not measured. (op 6)
2. Inspect, do not touch. Read service and timer state, scheduler jobs,
   queues, and active chats before any mutation. (op 4)
3. Choose the minimal mutation. Name the one change: a device reset, an
   overlay removal, a service restore. (op 2, op 5)

4. Gate each check independently. Score the reset, the detection, and the
   recovery as separate pass/fail; never one "fixed" flag. (op 2)
5. Verify at identity level. Move images by image-ID readback, not name, and
   rehash remotely after transfer, before deletion. (op 1, op 3)
6. Re-qualify by behavior. Probe chat, streaming, tool calls, and multi-turn
   continuation with and without tools; read context from the server. (op 5)

7. Validate offline, then touch live. Repair config with parsing, file-mode,
   and hash checks, private backups, and exact diffs; validate roles and
   fallback chains before opening a live slot. (op 5)
8. Run full lifecycle cycles. Prove a release with two complete cycles, a
   clean exit code, and zero residual processes. (op 6)
9. Record the not-proven line. Log NOT_RECOVERED, PARTIAL, and
   unproven-under-load as the honest entry, and never as a pass. (op 2, op 3, op 4)
10. Bind the claim to a tier. Stamp receipt, report, or memory-only, and cap
    the claim at the tier. Relabel stale numbers as historical, not current. (all ops)
