# ADR 0001: Bound every claim to a named evidence tier

Status: accepted (2026-11-24)

Context: the field record mixes replayed receipts, one-pass reports, and
memory-only notes. A table where all rows read "verified" is a table of
adjectives, and the 2026-10-30 inventory audit issued six required
corrections before the case set could publish.

Decision: each case names one of five tiers: replayed receipt, receipt,
report, rollout-summary, memory-only. A claim may not cite a tier it cannot
point to. A tier is a floor on what the claim may assert, not a quality score.

Consequences: the July throughput numbers are stamped historical and
downgraded, not relabeled as current. One UI review timeout keeps native
acceptance on the not-proven list. Memory-only evidence on the op-1 volume
is disclosed as an availability risk with no proven loss. Costs: every claim
needs a tier, and the weakest tier caps the strongest claim.
