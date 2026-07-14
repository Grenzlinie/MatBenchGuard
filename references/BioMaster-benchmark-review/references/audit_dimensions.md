# Audit dimensions and weights

Hard gates always override weighted scores. Use `NOT_ASSESSED` only when the selected mode cannot support a judgment; exclude it from the denominator and state why.

## No-paper mode

| ID | Dimension | Weight | Critical |
|---|---|---:|:---:|
| N01 | Biological admissibility and capability alignment | 0.15 | yes |
| N02 | Resource identity, reachability, and legal usability | 0.15 | yes |
| N03 | Task answerability and data sufficiency | 0.14 | yes |
| N04 | Checker validity and score semantics | 0.14 | yes |
| N05 | Checker robustness, monotonicity, and anti-gaming | 0.10 | yes |
| N06 | Instruction, workflow, manifest, and output-contract consistency | 0.08 | no |
| N07 | Gold quality, independence, and uncertainty | 0.07 | no |
| N08 | Execution and environment feasibility | 0.06 | no |
| N09 | Reproducibility, versioning, and database drift | 0.04 | no |
| N10 | Biological split integrity and contamination resistance | 0.03 | no |
| N11 | Security, privacy, ethics, and licensing | 0.03 | no |
| N12 | Difficulty, discrimination, and auditability | 0.01 | no |

## Paper-grounded mode

| ID | Dimension | Weight | Critical |
|---|---|---:|:---:|
| P01 | Biological admissibility and capability alignment | 0.10 | yes |
| P02 | Resource identity, reachability, and legal usability | 0.11 | yes |
| P03 | Task answerability and data sufficiency | 0.09 | yes |
| P04 | Instruction-to-paper method fidelity | 0.14 | yes |
| P05 | Data, sample, organism, and condition fidelity | 0.09 | yes |
| P06 | Gold provenance, independence, and uncertainty | 0.11 | yes |
| P07 | Checker validity and paper-faithful scoring | 0.11 | yes |
| P08 | Checker robustness, monotonicity, and anti-gaming | 0.07 | no |
| P09 | Execution and environment feasibility | 0.05 | no |
| P10 | Reproducibility, versions, and database drift | 0.04 | no |
| P11 | Biological split integrity and contamination resistance | 0.03 | no |
| P12 | Security, ethics, difficulty, and auditability | 0.06 | no |

## Scoring scale

- `1.00`: strong evidence and no material defect.
- `0.75`: sound overall; minor repair needed.
- `0.50`: important uncertainty or high-severity repair needed.
- `0.25`: major failure or weak evidence.
- `0.00`: absent, contradicted, invalid, fabricated, or impossible.
- `NOT_ASSESSED`: unavailable in the chosen mode; exclude from denominator.

For every score record evidence, confidence, whether it is a fact or inference, the defect, and the post-fix verification test.
