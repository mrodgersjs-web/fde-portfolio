# Failure taxonomy

Categorized failure modes observed in the field record (docs/field-record.md,
CASE-STUDIES.md). Facts are [corpus] from Mike's career answers corpus (RIG
section, confirmed 2026-11-10) and the dated operations in the field record.
No client names. No AI portraits.

## A. Data-availability failures
- Sole-copy loss: an offline volume held the only copy of some batches;
  no data loss proven, that drive not recovered. [corpus, op 1]
- Deletion-before-verification: source removed before the destination hash
  confirms. Guard: rehash remotely after transfer, before removal. [corpus, op 1]
- Skipped-target amnesia: 8 of 41 removals skipped; the failure is forgetting
  them, not the skip. Keep the skip on the record. [corpus, op 1]

## B. Repair-that-worsens failures
- Fix-by-destroy: volume drops offline, operator reformats and gambles the
  filesystem. Guard: the device reset is the only mutation. [corpus, op 2]
- Aggregate-status masking: one "fixed" flag hides which gate failed. Guard:
  reset, detection, and recovery scored as separate pass/fail. [corpus, op 2]
- Compounded damage: an honest NOT_RECOVERED beats a repair that closes the
  remaining recovery routes. [corpus, op 2]

## C. Migration and identity failures
- Name-lies: two images share a name, one is stale. Guard: verify at image-ID
  level, not name. [corpus, op 3]
- Automation race: a background pruner deleted a destination image mid-batch.
  Caught by the same ID readback; automation paused, source deletion withheld.
  [corpus, op 3, rollout-summary tier, not re-verified]
- Partial-report inflation: a migration over ~300 routines reported PARTIAL;
  the failure is stamping it DONE. [corpus, op 3]
- Protocol drift: a re-pointed database needs a hostname-rejection negative
  test, not a happy-path connect. [corpus, op 3]

## D. Serving and capability-claim failures
- Blame-the-first-suspect: a tool-call failure class was blamed on a
  speculative-decode setting first; the root cause was the parser template.
  [corpus, op 4, historical Jul, not re-run]
- Vibe-probe: "model list loaded" as proof. Guard: exact-output probe at
  temperature 0. [corpus, op 4]
- Restore-evicts-cotenant: a service restart kills the co-tenant. Guard:
  restore behind idle gates (scheduler, queues, active chats checked).
  [corpus, op 4]
- Stale-number laundering: July throughput figures are stamped historical
  and were deliberately downgraded, not re-labeled as current. [corpus, op 4]
- Unproven-under-load: one host's tool cycles timed out under load; recorded
  as unproven, not as broken. [corpus, op 4]

## E. Routing and catalog-lie failures
- Presence-as-proof: an endpoint in a catalog is not a working route. One
  endpoint passed a tool cycle and failed normal continuation days later.
  [corpus, op 5]
- Advertised-vs-real context: client claims 32,768, server has 8,192; a
  proxy's value was 4x off. Reconcile from server readback, not client config.
  [corpus, op 5]
- Overlay shadow: one overlay file silently overrode saved roles. Surgical
  removal, not a world reset. [corpus, op 5]
- Silent divergence: five clients, a gateway, and a hand-built registry
  drifted with no alarm. Divergence is the default, not the exception.
  [corpus, op 5]

## F. Lifecycle and resource-exhaustion failures
- Referenced-timer leak: a cleanup `setInterval` kept process handles
  alive; thousands of orphaned stdio MCP servers. Fix: `.unref()`. [corpus, op 6]
- Sole-culprit over-attribution: crash forensics supported resource
  exhaustion and refused to name one component as the single cause without
  evidence. [corpus, op 6]
- Exit-without-readback: a release is proven by two full lifecycle cycles,
  exit code 0, and zero residual processes — not by the version bump.
  [corpus, op 6]

## G. Reporting and claim-hygiene failures
- Adjective-as-evidence: "done" with no command output, file, or artifact.
  Guard: every claim binds an evidence tier (receipt, replayed receipt,
  report, rollout-summary, memory-only). [corpus, verification layer]
- Not-proven suppression: a case without a not-proven line is marketing.
  Every operation in the field record carries one. [corpus, all ops]
- Memory-only inflation: an intake record with no receipt is labeled
  memory-only and never promoted. [corpus, op 1]
- Pending-acceptance gap: config repairs are report-backed while native UI
  acceptance is pending; the gap is stated, not hidden. [corpus, op 5]
