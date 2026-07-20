---
name: materials-benchmark-review
description: Audit one materials-science Harbor package at E1 using instruction, tests, an isolated solution Oracle positive mock, and always-read paper evidence for A2/A4/A5, scored on the seven-dimension C01-C07 model.
---

# Materials Benchmark Review

Audit one `paper-{id}/` Harbor 题包 and publish the authoritative
`benchmark_audit/` bundle inside it.

## Quality evidence boundary
Review only:

- `instruction.md`;
- all relevant files under `tests/`;
- `solution/` only to execute its Oracle in isolation and ask whether the
  generated mock passes the real checker;
- `paper/` — always read for `A2`, `A4`, `A5`; `A1`/`A3` may extend to it.

Do not inspect or score `manifest.json`, `resources.json`, `steps.json`,
`task.toml`, `environment/`, cluster names, or other metadata. They may locate
the package but cannot change a quality score, verdict, or Hard Gate.

Oracle outputs are privileged positive mocks. Never include their values in an
audit artifact and never use them as scientific correctness, paper fidelity,
or Gold-provenance evidence. Missing or broken `solution/solve.sh` is a
repairable completeness finding, not evidence that the task science is wrong.

The Stage 0→5 flow, the Agent-adjudicated classification reform (no keyword
prescreen), the D1–D7 and A1–A5 tables with declared input files, the
dimension→check mapping, and the unified terminal fields are in
[references/checks-and-stages.md](references/checks-and-stages.md).

Every authoritative E1 report emits the shared D1–D6 deterministic contract.
Only proven OPEN repairable blockers enter its complete `REQUIRED` queue;
advisory risks never block PASS. A PASS report is eligible for publication only
when the contract is valid and `CLEAN`.

Read [references/harbor-contract.md](references/harbor-contract.md) and
[references/no-paper-e1.md](references/no-paper-e1.md).

## Contract-role mapping
Do not treat every path under `/app/outputs` as a scored answer. Build and
publish this mapping for every workflow requirement:

```text
Instruction requirement
  → Agent work/action
  → declared core output
  → checker actually reads
  → checker actually scores
```

The mapping has three output roles:
- `CORE_OUTPUT` — an explicitly core/scored/final output, or a conservatively
  recognized complete/full model, structure, trajectory, field, or mesh;
- `PROCESS_ONLY` — an explicitly process/intermediate/diagnostic artifact;
- `UNCLASSIFIED` — an uncertain declaration that needs human adjudication.

An instruction may legitimately list process evidence separately from final
submission files. A process artifact missing from the scoring contract is not
`INSTRUCTION_ONLY_OUTPUT` and must not reduce instruction answerability merely
because it has no score weight. Process artifacts remain contract-map-only:
exclude them from all five probe classes and never treat them as weighted
components, deductions, gates, or anti-hacking traces. Complete/full models,
structures, trajectories, fields, and meshes remain core even when mislabeled
process; record the contradiction as `UNCLASSIFIED` while retaining core
checker analysis. Only non-load-bearing logs/intermediates are process-only.
Ignored core output is severe `CHECKER_CORE_TASK_UNASSESSED`.

For every `scored_output`, record whether the checker:

1. loads the file or otherwise reads its contents;
2. binds it to a runtime scoring function;
3. gives it a non-zero effective weight; and
4. uses it in the final reward rather than only checking existence or format.

Missing links are checker/Gold or robustness findings, not generic instruction
omissions. Expose the mapping even when links are unknown; static matches are
only candidates, and missing/unparseable checkers remain unknown/not-run.
Every parsed workflow requirement receives a chain row even when it declares no
recognized output; use an unclassified output and unknown read/score states.

## Checker and Gold audit

The checker audit must combine static contract mapping with isolated dynamic
probes. Inspect for:

- core outputs that are never read;
- file-existence or schema-only checks that ignore the scientific result;
- small hard-coded targets that bypass prediction/model outputs;
- ignored model files, predictions, or load-bearing logs;
- scoring components with zero weight, no runtime binding, or no return value;
- always-pass, always-zero, exception-swallowed, division-by-zero, and
  direction-reversal behavior;
- positive valid outputs receiving a high score;
- malformed, incomplete, random, or scientifically wrong but
  format-valid outputs receiving a low score.

`largest_weight >= pass_threshold` is only a static risk, not proof of
`SINGLE_COMPONENT_CAN_PASS`; prove it with a component-isolation probe from
source-bound components, verified checker bindings, and an independent public
fixture. The Oracle positive mock is never an isolation fixture; otherwise
record `component_isolation` as required but `NOT_RUN`.
Every reward-derived conclusion uses the shared usable-result predicate. A
finite reward with malformed breakdown or non-empty/malformed `_errors` is
unusable.

If an isolated Oracle producer runs successfully but the checker rejects its
mock, attribute the rejection to checker/Gold alignment or checker runtime
behavior. Only attribute it to solution completeness when the producer failed
to run or failed to generate the declared outputs. Docker paths such as
`/solution` and `/app/outputs` are valid Harbor paths and must not be rewritten
in the package.

## Paper rule and A-layer

There is no paper trigger switch. Paper-grounded E1 is the default path: `A2`,
`A4`, and `A5` always read `paper/`; only a Stage 0 `NON_MAT` Hard Gate
fail-fast skips it. The paper-grounded report binds the authoritative audit ID,
source hashes, and Review implementation hash, and never claims the scientific
workflow ran. Read
[references/paper-grounded-audit.md](references/paper-grounded-audit.md) for the
reproduction-intent classes and the A5 Gold-credibility checklist. Classify
intent as `EXACT_REPRODUCTION`, `METHOD_REIMPLEMENTATION`, or
`SCIENTIFIC_EXTENSION`; default to `METHOD_REIMPLEMENTATION`, never EXACT.
Equivalent software, versions, and solver-selected convergence parameters are
allowed unless instruction fixes them or the checker secretly depends on them.

## Run E1
Write any taxonomy or paper assessment outside the package, then run
paper-grounded E1 (the default path):
```bash
python scripts/run_review.py <Harbor题包目录> \
  --paper-mode paper_grounded \
  --execution-level E1 \
  --agent-assessment <assessment.json> --attestation-output <external.json>
```
The optional attestation output is required before routing an audit into
Repair. It is external, non-overwriting, read-only, and byte-binds audit and
external-input hashes. Review provenance hashes the canonical dependency list
in `references/review-implementation-files.json`.

An independently justified non-Oracle output may additionally be supplied with
`--known-valid-output`. It is used only for discrimination and equivalence
probes and requires an external public `fixture_manifest.json` bound to current
instruction/tests hashes; it never replaces the isolated Oracle positive mock.

Every E1 run records coverage for these probe classes:

- positive — isolated Oracle mock only;
- negative — missing, empty, malformed, random, duplicate, sparse, and
  non-finite attacks;
- discrimination — an independently justified public fixture and scientifically
  worse outputs must not score better;
- equivalence — scientifically equivalent ordering or serialization must not
  change reward, using the same independent public fixture;
- component isolation — independently sourced one-component submissions.

Execute checker cases through `tests/test.sh` in the disposable prebuilt
`qa-checker` Docker sandbox and label runtime provenance as `sandbox`. Build the
image once with
`.cursor/skills/materials-benchmark-review/scripts/sandbox/build_qa_checker.sh`
before running Review or Repair. Docker daemon/image/cache readiness is an
operator precondition: if it is missing, abort the run with the build hint.
Once the sandbox is ready, dependency-install failures and checker crashes are
package findings, not `not-assessable` runtime limitations.

These are exactly the five top-level classes. Task-family attacks are named
negative/discrimination cases and nested subcoverage, never a sixth class.
Each has explicit status/provenance. E1 executes `tests/test.sh`; if unavailable,
direct probes are forbidden and runtime is `NOT_ASSESSABLE`. Review and repair
re-audit are fixed at E1, with no E2 publication path. Repair invokes this
Review CLI exactly once after mutation. That equal-depth re-audit alone
controls the post-repair verdict and deterministic CLEAN state; local repair
heuristics and regression results cannot publish a package.

## Direct inputs
Read [references/materials-resource-policy.md](references/materials-resource-policy.md).
Probe only a direct input or service that instruction explicitly marks as
indispensable and without an equivalent. Do not probe resources metadata,
solver-generated structures/trajectories/models, ordinary solver parameters,
or replaceable software.

## Score and disposition
Read [references/scoring-rubric.md](references/scoring-rubric.md). The Review
CLI is the sole scoring authority; batch and calibration layers only aggregate
an identity- and source-hash-bound CLI report. Never accept manually supplied
dimension scores, total score, Hard Gates, or verdict.

Scoring is the seven-dimension C01–C07 model with fixed weights: C01 domain
admissibility 10, C02 design completeness & file consistency 20, C03 scientific
validity & solvability 20, C04 scoring semantics 20, C05 answer leakage 10, C06
reproducibility 10, C07 difficulty & auditability 10 (total 100). Each dimension
records max/earned/normalized points, its finding IDs, and exact evidence, and
deducts by severity ratio within that dimension only; a non-key evidence gap
never leaks into another dimension. `summary.total_score` is the C01–C07
weighted total on a 0–100 scale; `legacy_total_score` keeps the old five-
dimension sum as a compatibility field. Reproduction-intent classes never change
points. See [references/scoring-rubric.md](references/scoring-rubric.md) for the
dimension→check mapping.

The four Hard Gates override the score and bind to dimensions: C01 (not a
substantive materials-science task / `NON_MAT`); C03 (scientifically invalid or
an unrecoverable missing necessary definition); C04 (checker does not evaluate
the core task and cannot be repaired without redefining it); C06 (an
indispensable direct input is permanently unavailable with no equivalent).

Disposition uses the verdict directly: `PASS` is at least 80 with no unresolved
repairable HIGH; `CONDITIONAL` is 60–79 or has a repairable HIGH; `REJECT` is
below 60 or hits a Hard Gate; `NOT_ASSESSABLE` is temporary evidence
unavailability, re-audited after evidence is restored. Every report and
disposition also carries the unified terminal fields `disposition`,
`publishable`, and `repair_state` (see
[references/checks-and-stages.md](references/checks-and-stages.md)), plus
`dimensions_v11` and `repair_delta` in the report.

`PASS` additionally requires the fail-closed evidence contract: authoritative
materials qualification, non-empty evidence for every scored dimension, honest
status and provenance for all probe classes, and Oracle-safe solution status
only. Assessed discrimination/equivalence must use an independent non-Oracle
fixture; when no such fixture exists, keep both probes unavailable, deduct the
documented non-critical robustness limitation within C07, and continue scoring.
No findings never substitutes for positive evidence.

For repair publication, overall PASS is necessary but not sufficient. The
atomic invariant is:
`PASS + deterministic CLEAN + no Hard Gate + preserved package identity +
allowed mutation scope + all target findings resolved`. Any residual D1–D6
blocker is terminal and non-publishable.

Preserve the pinned three-axis taxonomy labels and exact package evidence. The
versioned runtime source is
[references/materials-taxonomy.json](references/materials-taxonomy.json).

## Batch
Read [references/fast-e1-batch.md](references/fast-e1-batch.md). The candidate
manifest freezes identities only. Finish and freeze the complete original
review baseline before any repair begins.

## Completion

The run is complete when the fixed bundle validates, Oracle values are absent,
quality files are limited to instruction/tests plus the isolated Oracle role and
the always-read paper for A2/A4/A5, every checker case records
class/reward/status/exit code, the seven C01–C07 weights sum to 100, exactly
four Hard Gates are present, the unified terminal fields are set, and taxonomy
labels remain unchanged.
