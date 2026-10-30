# Case studies: operating a private AI infrastructure fleet

Six operations from a personal fleet (366 owned repositories at the 2026-10-30
census) running local model inference, agent workloads, and the verification
systems around them. Each case states the environment, my role, what passed,
and what was *not* proven; the limitations are the point. Each names its
evidence tier, because a dated report, a replayed receipt, and a memory
record are three different things and portfolios usually pretend they are one.
All dates are 2026. An independent audit of the whole inventory (2026-10-30)
re-checked sampled claims against original JSON receipts; its six required
corrections are applied in its published artifacts and reflected here, and
the report is cited (by date) rather than linked because these are internal
receipts.

A note on authorship: the fleet is operated with an AI engineering system I
designed and direct. Where a change was executed by agents, my role is stated
as designed-and-verified or directed-and-reviewed, per the receipts; the
ownership framing is confirmed by me, not inferred by an auditor.

## 1. NAS archival with hash-gated deletion (October)

**Problem.** A workstation was disk-pressured while running AI workloads;
application archives had to move to a QNAP NAS before anything was deleted,
with no gap where data existed in exactly one unreliable place.

**Approach.** macOS `bsdtar` archives preserving plist metadata, extended
attributes and symlinks (a metadata warning on one archive was retained in
the manifest and retried, not ignored). Size manifests plus SHA-256 streams;
the deleter rehashed remotely *after* transfer and *before* removal.

**Result.** 47 current application archives verified on the NAS, 10 media
files transferred, 33 of 41 requested application removals executed only
after remote hash confirmation; the 8 skipped targets stayed recorded, not
forgotten.

**Not proven.** Full application *restoration* from the archives (a bounded
metadata/symlink extraction was the tested gate). A candidate intake record
(memory-only evidence) says one incident's offline volume held sole copies of
some batches: an availability-risk lesson; no data loss proven either way,
and that drive was not recovered.

**Role / evidence tier.** Directed and reviewed; executed by the fleet's
operations agents against my retention rules. Replayed receipt tier: dated
cleanup packet with manifests and an independent final verification comparing
sizes.

## 2. External-storage forensics without making it worse (October)

**Problem.** An external Thunderbolt volume dropped offline mid-operation.
The tempting failure mode is "fix it by destroying it": filesystem repair,
reformat, hope.

**Approach.** macOS USB enumeration and accessory-authorization inspection,
the native USB-host device reset as the *only* mutation, gates recorded
independently: reset API result, disk-detection result, drive-recovery result
- scored separately instead of as one "fixed it" claim.

**Result.** Reset passed; the disk stayed undetected; the overall outcome was
recorded `NOT_RECOVERED` on the packet. Original accessory policy restored.
No erase, no filesystem gamble: the volume was left untouched so other
recovery routes stayed open.

**Not proven.** Recovery by this operation: it is logged as a failed
recovery attempt that avoided compounding damage, which is the honest entry.

**Role / evidence tier.** Directed; the diagnostic ladder was my design rule:
each gate independently pass/fail, no aggregate status. Receipt tier.

## 3. Fleet container and scheduler migration (October)

**Problem.** The heaviest workloads needed to move from one Mac to a larger
one: ~66 container images, databases, voice services, vector stores, and ~21
scheduled routines. Rollback had to stay possible; the old machine was to
retire empty.

**Approach.** Image-ID-level verification (names lie, IDs don't); source
images zeroed before any engine shutdown; cold archives hash-checked;
persistent volumes and bind mounts retained; database counts compared before
and after (auth users and public-table counts matched); TLS overlay
re-validated with hostname-rejection negative tests; a legacy database
forward re-pointed to a new local port and protocol-tested; vector stores
migrated with cold snapshots and raft identity restored.

**Result.** 66/66 destination image IDs verified; engines stopped clean; the
scheduler moved with each routine carrying two actual scheduled clean receipts
on the new host. A later race in a different batch, a destination image vanishing
because an automation pruned it, was caught by the same ID readback; the
automation was paused and source deletion withheld (rollout-summary
evidence, not re-verified).

**Not proven.** Content parity of every collection, whole-estate equivalence
(~300 routines), and the migration report stayed explicitly PARTIAL.

**Role / evidence tier.** Directed and reviewed. Report tier: a dated
migration report plus its verification JSON; subordinate receipts were not
all replayed. The ID-verification and two-receipt rules were designed before
the run.

## 4. Blackwell GPU serving: restore, co-tenancy, and a certified fabric (July–October)

**Problem.** Three RTX PRO 6000 Blackwell GPUs host concurrent model
services; restarts must not evict co-tenants, and a tensor-parallel route
deserves a certification rather than a vibe.

**Approach.** systemd service and timer inspection before touching anything;
restore ordered behind idle gates (scheduler jobs, queues, active chats
checked first); exact-output probes at temperature 0 instead of "model list
loaded"; for the fabric, tensor-parallel-3 over PCIe P2P with the IOMMU
constraint understood, then chat/stream/tool/context/overflow gates plus
quality trials.

**Result.** GLM service restored with scheduler timers preserved and exact
output verified; a second lane's restore preserved its co-tenant while
re-adding the intended service; the TP3 route measured 522.988 tok/s median
and 1446.4 tok/s aggregate at concurrency 8, with client smokes (Jul 18,
stamped historical). Earlier in July, a tool-call failure class on another
route was traced to the *parser template*, fixed, and proven by ten automatic
tool calls (Jul 24, historical, not re-run); after disabling an unstable
speculative-decode setting that was blamed first.

**Not proven.** Endurance and whole-fleet SLOs; the July numbers are stamped
historical, deliberately downgraded when an exact re-probe wasn't run. One
host's tool cycles timed out under load; recorded as unproven-under-load,
not as broken.

**Role / evidence tier.** Designed the gates; directed execution; reviewed
the packets. Report tier for the July certification, receipt tier for the
October restores.

## 5. Model routing truth: six client catalogs and the endpoints that lied (October)

**Problem.** Five agent clients plus a LiteLLM-class gateway and a hand-built
model registry had silently diverged: stale routes selectable in UIs, a
client advertising 32,768 context against a server's 8,192, a proxy
advertising a context value 4x off, and an overlay overriding saved roles.

**Approach.** Treat presence as unproven: every route re-qualified with
behavioral probes (chat, streaming, tool calls, *multi-turn continuation*
(with and without tools), embeddings by dimension, vision by modality), and
client/server context values reconciled from server readback, not client
config. Config repairs kept parsing, file modes and hashes checked, with
private backups and exact diffs; an override traced to one overlay file was
surgically removed instead of resetting the world.

**Result.** Six client config files repaired (native UI acceptance still
pending on some); native catalog checks 15/15 and 12/12; a 100-entry import
(99 custom entries plus one companion) rendered 583 native-parser rows with
no warnings; 43 roles and 31 fallback chains validated offline before live
slots were touched. A documented failure class: one fleet endpoint passed one
tool cycle and *failed normal continuation* days later, while passing
no-tools continuation: the evidence behind the permanent rule that catalog
presence proves nothing.

**Not proven.** Full native acceptance on every client (one UI review timed
out), million-token workloads, long-context *quality*.

**Role / evidence tier.** Owned the verification doctrine; directed and
reviewed the repairs. Receipt tier for the validation runs; the config
repairs themselves are report-backed with pending acceptance.

## 6. Leaky MCP server lifecycle: process leaks and clean exits (October)

**Problem.** A machine was accumulating thousands of orphaned stdio MCP
servers: an unglamorous leak class that kills fleets quietly.

**Approach.** Process/RSS enumeration to size the leak; root cause in Node
timers (a referenced cleanup `setInterval` keeping handles alive, fixed via
`.unref()`); lifecycle tests with EOF/disconnect paths; an upstream LAN
verification route exercising the promoted release end-to-end.

**Result.** Two full lifecycle cycles over the LAN exposed 21 tools,
performed real extraction on the second, exited with code 0 and left no
residual processes. The fleet then moved onto the official upstream release,
which carries the same `.unref()` fix; the crash forensics that surrounded it
deliberately refused to blame this component as sole cause without evidence -
resource exhaustion was supported, single-culprit attribution wasn't.

**Not proven.** That every other MCP server in the estate is leak-free; the
method is the deliverable.

**Role / evidence tier.** Directed the diagnosis; the no-sole-blame rule was
my design. Receipt tier.

---

## The verification layer (why these cases have "Not proven" lines)

Every operation above either produced a ProofPacket (a dated, machine-
readable record with per-gate pass/fail and HMAC-SHA256 signing (with an
optional asymmetric public-attestation path) (or stayed out of this file).
The systems that enforce this are public:
[rigforge](https://github.com/mrodgersjs-web/rigforge) (builds/validates the
packets), [proof-studio](https://github.com/mrodgersjs-web/proof-studio)
(tamper checks), [mesh-studio](https://github.com/mrodgersjs-web/mesh-studio)
(fleet probe/recovery), [jev-route](https://github.com/mrodgersjs-web/jev-route)
(Rust + wasm routing policy), [latency-probe](https://github.com/mrodgersjs-web/latency-probe)
(C++17 histograms for serving measurement).

The audit behind this file also recorded what it could *not* verify: one
doctor check failing in the same window, degraded memory retrieval, and
inventory completeness withheld; those limits are in the private
evidence ledger, available on request.
