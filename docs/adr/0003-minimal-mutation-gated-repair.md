# ADR 0003: Minimal mutation with independently gated checks

Status: accepted (2026-11-24)

Context: the repair instincts that destroy data: reformat the dropped volume,
restart the service and evict the co-tenant, delete the source before the
destination hash lands, reindex the world to fix one overlay. A repair that
adds a new failure mode is a loss, not a fix.

Decision: each repair names the smallest mutation, and every gate is scored
independently, never as one aggregate status. The volume repair uses the
device reset as the only mutation. Service restores run behind idle gates.
Deletions are hash-gated. One overlay file is removed, not the config.

Consequences: a failed recovery can be an honest NOT_RECOVERED, the volume
left untouched so other routes stay open, and the original policy restored.
Co-tenants and scheduler timers survive a restore. Costs: the run is slower
and the gate count is high. The deliverable is the gated method, not a
greener result.
