---
name: materials-benchmark-review
description: Audit one materials-science Harbor package on the dual-lane path using deterministic code checks plus Agent paper reads for A2/A4/A5, scored on the seven-dimension C01-C07 model.
---

# Materials Benchmark Review

Audit one `paper-{id}/` Harbor 题包 and publish the authoritative
`benchmark_audit/` bundle under the external sibling root
`<topic>/review_outputs/<paper-id>/`.

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
prescreen), the D1–D6 deterministic-core and Agent-quality tables with declared input files, the
dimension→check mapping, and the unified terminal fields are in
[references/checks-and-stages.md](references/checks-and-stages.md).

Every authoritative dual-lane report emits the shared D1–D6 deterministic
contract. Only proven OPEN repairable blockers enter its complete `REQUIRED`
queue; advisory risks never block PASS. A PASS report is eligible for
publication only when the contract is valid and `CLEAN`.

Review persists two non-interchangeable lanes:

- `deterministic_core` contains static D1–D6 results and code-defined runtime
  probes. Malformed, full-integration, partial, and all-wrong cases are
  generated from the declared output schema and grading steps; they are not
  Agent-authored scientific examples and never bind an external fixture.
- `agent_quality` contains the Agent assessment and separately reported quality
  results. The Agent may justify only Gold, target, unit, formula, tolerance,
  threshold, and scoring-direction claims from the paper or authoritative
  sources. It does not generate probe outputs or judge whether synthetic probe
  values are scientifically meaningful.

## Narrow D1–D6 `AUTO_FIX` boundary
Review classifies repairability against the frozen contract and does not mutate a package. `AUTO_FIX` is limited to unique source-bound restoration of existing D1–D6 contract/scoring wiring: output declaration/path synchronization, scorer registration/binding/return/final-reward connections, a standard Harbor entrypoint around one existing producer, or ratio-preserving normalization of finite positive declared weights.
It must not introduce or choose Gold values, targets, tolerances, thresholds, formulas, scorer algorithms, fields, units, scientific parameters, or science semantics; fabricate a producer; make an ignored core output appear scored; or use Oracle/solution content or metadata as evidence. Semantic selection is `ASSISTED_FIX` only with type-matched evidence, otherwise `ABANDON`/`BLOCKED_EVIDENCE`; Oracle values remain absent from audit evidence.
Read [references/harbor-contract.md](references/harbor-contract.md) and [references/paper-grounded-audit.md](references/paper-grounded-audit.md).

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
probes. Deterministic-core probe failures are limited to objective integration
and explicitly schema/step-implied ordering or malformed-input failures.
Discrimination, equivalence, and component-isolation results remain quality
results and cannot acquire D1–D6 ownership. Inspect for:

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

`largest_weight >= pass_threshold` is only a static risk, not proof of a
scientific quality defect. Component isolation is Agent-quality assessment and
is not executed in the deterministic lane or supplied through a fixture.
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

Dual-lane review is the only path: `A2`, `A4`, and `A5` always read `paper/`;
only a Stage 0 `NON_MAT` Hard Gate fail-fast skips it. The report binds the
authoritative audit ID, source
hashes, and Review implementation hash, and never claims the scientific
workflow ran. Read
[references/paper-grounded-audit.md](references/paper-grounded-audit.md) for the
reproduction-intent classes and the A5 Gold-credibility checklist. Classify
intent as `EXACT_REPRODUCTION`, `METHOD_REIMPLEMENTATION`, or
`SCIENTIFIC_EXTENSION`; default to `METHOD_REIMPLEMENTATION`, never EXACT.
Equivalent software, versions, and solver-selected convergence parameters are
allowed unless instruction fixes them or the checker secretly depends on them.

## Run dual-lane review
Write any taxonomy or paper assessment outside the package, then run:
```bash
python scripts/run_review.py <Harbor题包目录> \
  --audit-output-dir <外部审计目录> \
  --agent-assessment <assessment.json> --attestation-output <external.json>
```
If `--audit-output-dir` is omitted, the CLI defaults to the sibling root
`<topic>/review_outputs/<paper-id>/`. Low-level prepare/finalize APIs still
require an explicit external path and reject package-local outputs.
The optional attestation output is required before routing an audit into
Repair. It is external, non-overwriting, read-only, and byte-binds audit and
external-input hashes. Review provenance hashes the canonical dependency list
in `references/review-implementation-files.json`.

Review accepts no external result directory or fixture-manifest input.
The isolated Oracle is used only to seed code-generated positive, partial, and
all-wrong contract probes. Those temporary case directories are stored only
under the external audit workspace and are never a Harbor role, Gold fixture,
or deterministic input. Legacy audits containing fixture hashes or lineage
must be regenerated before they can be used as current evidence.

Every dual-lane run records coverage for these probe classes:

- positive — isolated Oracle mock only;
- negative — missing, empty, malformed, random, duplicate, sparse, and
  non-finite attacks;
- discrimination — Agent-quality assessment of whether the declared scoring
  direction distinguishes scientifically worse outputs;
- equivalence — Agent-quality assessment of whether equivalent representations
  preserve the declared result;
- component isolation — Agent-quality assessment only; no deterministic fixture
  or external result directory is accepted.

Execute checker cases through `tests/test.sh` in the disposable prebuilt
`qa-checker` Docker sandbox and label runtime provenance as `sandbox`. Build the
image once with
`.cursor/skills/materials-benchmark-review/scripts/sandbox/build_qa_checker.sh`
before running Review or Repair. Docker daemon/image/cache readiness is an
operator precondition: if it is missing, abort the run with the build hint.
Once the sandbox is ready, dependency-install failures and checker crashes are
package findings, not `not-assessable` runtime limitations.

These five classes have explicit status/provenance. Dual-lane review runs
`tests/test.sh` (direct probes forbidden if unavailable). Repair invokes this
CLI once for equal-depth re-audit; only that re-audit can publish.

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
weighted total on a 0–100 scale. Reproduction-intent classes never change
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
only. Discrimination, equivalence, and component isolation are not
deterministic-core inputs; their Agent-quality status is reported separately
and cannot block D1–D6. No findings never substitutes for positive evidence.

For repair publication, overall PASS is necessary but not sufficient. The
atomic invariant is:
`PASS + deterministic CLEAN + no Hard Gate + preserved package identity +
allowed mutation scope + all target findings resolved`. Any residual D1–D6
blocker is terminal and non-publishable.

Preserve the pinned taxonomy labels and exact package evidence from
[references/materials-taxonomy.json](references/materials-taxonomy.json).

## Completion

Complete only when the bundle validates, Oracle values are absent, checker
cases record class/reward/status/exit code, weights sum to 100, exactly four
Hard Gates and unified terminal fields are present, and taxonomy labels remain.
