---
name: materials-benchmark-review
description: Audit one materials-science Harbor package on the dual-lane path using deterministic D1-D6 checks plus Agent paper reads for A2/A4/A5, with authoritative C01-C07 scoring.
---

# Materials Benchmark Review

Audit one `paper-{id}/` Harbor package from a main-Agent-created run context.
All artifacts are private to
`.review_records/<cluster>/<theme>/<paper>/runs/<run-id>/`.

## Scope and safety

Read only:

- `instruction.md`;
- all relevant `tests/**`;
- `solution/` only inside an isolated Oracle run to ask whether its generated
  positive mock passes the real checker;
- `paper/` for A2, A4, and A5 (A1/A3 may extend there).

Do not score `manifest.json`, `resources.json`, `steps.json`, `task.toml`,
`environment/`, cluster names, or other metadata. Oracle values, raw output,
and solution content are never audit evidence. A missing or broken
`solution/solve.sh` is a repairable completeness finding, not science evidence.
Review never mutates a Harbor package.

The authoritative stage flow, D1-D6 registry, input-file tables, dimension
mapping, and terminal fields are in
[references/checks-and-stages.md](references/checks-and-stages.md).
The package boundary and output-role contract are in
[references/harbor-contract.md](references/harbor-contract.md).

## Lanes and machine contract

Stage 0 classification is Agent-authoritative from `## Problem background`,
`## Approach`, and `## Reproduction target`; deterministic code validates exact
quotes and legal labels but does not infer the class. Classes are `MAT_CORE`,
`MAT_METHOD`, `MAT_WRAPPER`, `NON_MAT`, and `AMBIGUOUS`. Only authoritative
`NON_MAT` is a C01 Hard Gate and skips paper reading.

The deterministic lane persists D1-D6 under `deterministic_contract` and
`deterministic_core/report.json`, including schema/registry versions, statuses,
finding IDs, complete repair queue, and `contract_digest`. Each check is
`PASS`, `FAIL`, `BLOCKED`, or `NOT_ASSESSABLE`; summary state is `CLEAN`,
`REQUIRED`, or `NOT_APPLICABLE`. Only proven OPEN repairable blockers enter the
complete `REQUIRED` queue; advisory risks do not block PASS.

Repairable Agent-quality / A-lane findings are first-class OPEN queue entries
alongside D1-D6. They keep `lane: agent_quality` and never fabricate a D check.
Each carries stable `finding_id`, severity, C01-C07 `dimension`, repairability,
evidence refs, plus `repair_lane` / `repair_scope`. Allowed scopes include
`DETERMINISTIC_WIRING`, `CHECKER_ROBUSTNESS`, `INSTRUCTION_CONTRACT`,
`SCORING_SEMANTICS`, `DIRECT_INPUT_REFERENCE`, and `SCIENCE_SEMANTICS`.
Normalized `repair_findings` appear on `agent_quality/assessment.json` and the
source audit report (`repair_findings` + complete `repair_queue`); the CLI
validates taxonomy, exact citations, source hashes, package path safety, and
C-dimension mapping. When D1-D6 is `CLEAN` but an OPEN repairable Agent finding
remains, finalization still routes to `REPAIR_QUEUE`. Hard Gates, unrepairable
Agent findings, and evidence gaps keep their existing non-Repair routes.

Publication class (consumed by later Repair tickets): narrow unique D wiring
(`DETERMINISTIC_WIRING` / `UNIQUE_SCORING_WIRING`) may later qualify for direct
deterministic publication; Agent checker-fairness, scoring semantics,
direct-input, science, and paper-grounded instruction repairs require
equal-depth re-audit.

The optional `materials-agent-contract-assessment/1.1` is a separate,
contract-only overlay. It is lane `deterministic_core`, binds machine schema,
registry, and digest, and supplies D1-D6 in order as `PASS` or `NOT_PROVEN`;
`REPAIR_REQUIRED` is additionally legal only for eligible unavailable D6.
Accepted evidence is limited to `instruction.md`,
`tests/**/grading_spec` (and optional extension), deterministic probe artifacts
under `deterministic_core/` or `deterministic_probe_artifacts/`, and—only for
D6 scoring-chain facts—`tests/checker.py`. Scope is `CONTRACT_WIRING` or
`DETERMINISTIC_CONTRACT`.
Conclusive D6 evidence uses one canonical `claim` per cited fact:
`content_read`, `scorer_binding`, `positive_effective_weight`, `finite_return`,
or `final_reward`. PASS covers all five; REPAIR_REQUIRED covers every FAILED
state with an exact quote/excerpt and sha256 binding.

The overlay must not use `paper/`, `solution/`, Oracle output, metadata,
Agent-quality evidence, Gold, targets, tolerances, formulas, units, thresholds,
or scoring-direction claims. Checker source is restricted to the five D6
scoring-chain states. It may apply only to an
unavailable (`BLOCKED`/`NOT_ASSESSABLE`) check with no proven or blocking
finding, dependency failure, missing input, Hard Gate, or usable runtime
contradiction. It cannot override machine `FAIL` or any machine fact.
`NOT_PROVEN` leaves the check unavailable.

The additive `materials-effective-deterministic-contract/1.0` is emitted as
`effective_deterministic_contract` and as `effective_contract` in
`deterministic_core/report.json`. It records eligibility, application, and
effective repair state; only an eligible unavailable check may become
effective `PASS`, and all machine findings remain preserved.

## Contract-only pending/resume

`AGENT_ASSESSMENT_PENDING` is the mandatory pre-Review gate. Until a validated
paper-grounded `agent_assessment.json` is present in the run (Stage 0 taxonomy
plus A2/A4/A5 citations, or an Agent-authoritative `NON_MAT` fast reject), Review
must not freeze A0, write a formal audit bundle, enter Repair, or update corpus
tracking. Supply the assessment in the same run and resume:

```bash
python scripts/run_review.py --run-dir <run-dir>
```

`AGENT_CONTRACT_PENDING` is emitted when D6 is an eligible unavailable
scoring-chain gap and there is no machine `FAIL`, proven/blocking D finding,
required machine queue, Hard Gate, usable runtime contradiction, or other
machine defect. An unrelated OPEN Agent-quality finding does not suppress the
D6 request; it remains in the queue and may route the completed Review to
Repair after effective D6 PASS.
Otherwise Review finalizes the authoritative non-PASS verdict (`CONDITIONAL` or
`REJECT` as applicable). A pending result is `NOT_ASSESSABLE`, has
`publishable=false`, and has no final audit bundle. Contract pending is only
reachable after the paper Agent assessment has already validated.

For an eligible contract pause, Review writes run-local
`agent_contract/request.json`; the same Review Agent places its assessment at
`agent_contract/assessment.json` and resumes the same run:

```bash
python scripts/run_review.py --run-dir <run-dir>
```

Resume validates bindings, reuses persisted probes, and does not rerun
deterministic preparation. Equal-depth Repair re-audits must inherit the same
validated paper assessment through the restricted internal Review API; there is
no deterministic-only fallback.

## Output roles and checker audit

Map every workflow requirement from its explicit `Role:` or `Purpose:` as:

```text
instruction requirement → Agent work/action → declared core output
→ checker reads → checker scores in final reward
```

Use `CORE_OUTPUT`, `PROCESS_ONLY`, or `UNCLASSIFIED`. `scored*` (plus compatible
`core*` / `final*` aliases) maps to `CORE_OUTPUT`; `process*` maps to
`PROCESS_ONLY`. Process artifacts remain contract-map-only: they are excluded
from D6, probe classes, weights, deductions, gates, and anti-hacking traces.
Descriptive words such as complete, full, load-bearing, model, structure, or
trajectory never promote a process output. An ignored scored core output is
`CHECKER_CORE_TASK_UNASSESSED`.

For each scored output record content-read, scorer binding, non-zero effective
weight, and final-reward use. Combine static mapping with sandbox probes for
missing/empty/malformed/random/duplicate/sparse/non-finite cases. Positive,
negative, and runtime integration probes belong to `deterministic_core`;
discrimination, equivalence, and component isolation are Agent-quality results.
Malformed reward breakdowns or non-empty/malformed `_errors` are unusable.

## Narrow `AUTO_FIX` boundary

Review classifies but does not apply repair. D1-D6 `AUTO_FIX` may only restore
unique, source-bound existing contract/scoring wiring: output declaration/path synchronization,
scorer registration/binding/return/final-reward connections, a standard Harbor
entrypoint around one existing producer, or ratio-preserving normalization of
finite positive declared weights.

It must not introduce or choose Gold, targets, tolerances, thresholds, formulas,
scorer algorithms, fields, units, scientific parameters, producers, or science
semantics; it cannot make an ignored core output appear scored or use Oracle,
solution, or metadata as evidence. Semantic changes require type-matched
`ASSISTED_FIX`; otherwise use `ABANDON`/`BLOCKED_EVIDENCE`.
See [references/scoring-rubric.md](references/scoring-rubric.md).

## Run policy

The main Agent creates a run for an explicit `package_id`; Review receives only
that directory. Put Agent assessments inside the run (`agent_assessment.json`
or `agent_contract/assessment.json`) and run:

```bash
python scripts/run_review.py --run-dir <run-dir>
```

The run owns `snapshot/`, `audit/`, `agent_contract/`, `status.json` and
`roots/A0.json`; no independent output directory is accepted. Generated probes
and attestations remain inside the run, and the main Agent alone updates
tracking after all assigned runs finish.

Each Review acquires an atomic owner lock for the canonical output root before
preflight or probes. The lock records an immutable run ID, PID, and
process-start token; live or identity-ambiguous owners fail closed. Only a
demonstrably dead or PID-reused owner may be reclaimed. Temporary workspaces
are unique `<output>/.benchmark_audit_tmp/<audit-id>` directories and are
never shared or deleted by another run.

Run checker cases through `tests/test.sh` in the disposable prebuilt
`qa-checker` Docker sandbox:

```bash
.cursor/skills/materials-benchmark-review/scripts/sandbox/build_qa_checker.sh
```

Docker daemon/image/cache readiness is an operator precondition. Once ready,
dependency-install failures and checker crashes are package findings, not
evidence unavailability.

## Scoring and publication

The Review CLI is the sole scoring authority. C01-C07 weights are
`10,20,20,20,10,10,10`; `summary.total_score` is the weighted 0–100 score,
not a verdict. Do not emit or consume `quality_score` or `pre_gate_score`.
The verdict is `summary.final_verdict` and top-level `review_verdict`; the route
is `summary.publication_route` and top-level `publishability`.

Hard Gates are C01 non-material task, C03 invalid science/unrecoverable
definition, C04 checker not assessing the core task and not repairable, and C06
unavailable indispensable direct input. `PASS` requires score ≥80, no unresolved
repairable HIGH, all evidence contracts, and effective D1-D6 `CLEAN`.
`CONDITIONAL` is 60–79 or a repairable HIGH; `REJECT` is below 60 or a Hard
Gate; `NOT_ASSESSABLE` is temporary evidence unavailability.

Every report and disposition carries `disposition`, `publishable`, and
`repair_state`, plus `dimensions_v11` and `repair_delta`. Publication additionally
requires preserved identity, allowed mutation scope, and all target findings
resolved. Paper intent is `EXACT_REPRODUCTION`, `METHOD_REIMPLEMENTATION`
(default), or `SCIENTIFIC_EXTENSION`; see
[references/paper-grounded-audit.md](references/paper-grounded-audit.md).
Taxonomy labels come from
[references/materials-taxonomy.json](references/materials-taxonomy.json).

Finalization validates the exact output-file set, recomputed output hashes,
implementation-file aggregate, and report/manifest/disposition bindings before
atomically replacing `benchmark_audit`. When an attestation is requested, it
is written while the lock is held and the finalized bundle is then made
application-immutable and read-only where portable. An attested bundle cannot
be hash-refreshed; a new implementation requires a fresh Review.

## Completion

Complete only when the external bundle validates, Oracle values are absent,
checker cases record class/reward/status/exit code, weights sum to 100, exactly
four Hard Gates and unified terminal fields are present, and taxonomy labels
remain source-bound.
