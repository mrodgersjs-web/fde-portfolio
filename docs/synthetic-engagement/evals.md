# Eval list (synthetic engagement)

Eval set: 200 fixed records, seeded, deterministic. One command regenerates baseline and improved runs byte-identically.

| id | Checks | Type | Metric | Gate |
|---|---|---|---|---|
| E1 | Intake fidelity: typed record fields vs source | Deterministic | Field exact-match rate | >= 0.99 |
| E2 | Pre-screen recall: all must-review cases flagged | Deterministic | Recall on labeled set | >= 0.95 |
| E3 | Pre-screen precision: auto-merge tier purity | Deterministic | Error rate inside tier | <= 0.01 |
| E4 | Gate integrity: partial data never passes | Deterministic | Bypass count | == 0 |
| E5 | Ranker grounding: every rank cites a real field | Deterministic | Grounded-citation rate | == 1.0 |
| E6 | Ranker quality: ordering vs expert labels | Model, fixed seed | Kendall tau | reported, not gated v1 |
| E7 | Corrupt-input behavior: escalates, never silent-pass | Deterministic, planted | Silent-pass count | == 0 |
| E8 | Audit immutability: re-runs write a new pass, never overwrite | Deterministic | Published-pass mutation count | == 0 |
| E9 | Evidence binding: each score row carries the artifact hash | Deterministic | Rows with valid hash | == all |
| E10 | Control: a planted bad run must fail E3 and E4 | Deterministic, negative | Control fails as expected | required |

Baseline and improved runs are reported as a delta table; a metric is only a pass when the control (E10) also behaves. The model call in E6 is the only non-deterministic eval and is seed-pinned and label-pinned.
