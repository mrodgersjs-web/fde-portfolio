# How I engineer with agents (and how you can check it)

One operator, 366 owned repositories (118 on GitHub, 248 local and in-flight
at the 2026-10-30 census), a GPU host, one QNAP NAS, and an AI engineering
system that executes under gates. The system, not the operator count, is the
leverage.

**Deterministic before agentic.** Any rule that can be a function gets a
prompt only if it can't. The routing policy that decides which model does
which task is a Rust binary with a checked-in benchmark ([jev-route](https://github.com/mrodgersjs-web/jev-route)),
not a judgment call in a chat window.

**Receipts, not status updates.** Every destructive or stateful operation
emits a ProofPacket: per-gate pass/fail, timestamps, commit SHAs,
HMAC-SHA256-signed, with an optional asymmetric public-attestation path. The
packets are themselves checked for tampering with planted forgeries
([rigforge](https://github.com/mrodgersjs-web/rigforge),
[proof-studio](https://github.com/mrodgersjs-web/proof-studio)). A claim that
outlived its receipt gets downgraded to historical: several have, on purpose.

**Independent verification with adversarial defaults.** Audits of my own
inventory re-open the original JSON, issue required corrections before
publication (six on the last one), and withhold completeness when the
sampling can't support it. A doctor check that was FAILing during the same
audit is reported, not hidden.

**Attribution discipline.** Agents executed much of the work under my design
and review. This portfolio says "designed-and-verified" or
"directed-and-reviewed" where the receipts show agent execution, and
"implemented" where they show hands-on authorship (the Rust and C++ repos
were built and reviewed line by line under my direction in live sessions).
I don't upgrade orchestration into manual craft, and I don't minimize the
engineering judgment the orchestration encodes.

**Honest limits.** No distributed serving claims. No training runs. The
public estate has one red line in its own hygiene audit and it is named
there. Kubernetes is not claimed because the fleet doesn't run it.
