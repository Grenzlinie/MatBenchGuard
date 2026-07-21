---
name: materials-benchmark-review
description: Audit one materials-science Harbor package on the dual-lane path using deterministic D1-D6 checks plus Agent paper reads for A2/A4/A5, with authoritative C01-C07 scoring.
---

# Materials Benchmark Review

Audit one `paper-{id}/` Harbor package and write its authoritative
`benchmark_audit/` bundle under the external sibling root
`<topic>/review_outputs/<paper-id>/`.

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

The optional `materials-agent-contract-assessment/1.0` is a separate,
contract-only overlay. It is lane `deterministic_core`, binds machine schema,
registry, and digest, and supplies D1-D6 in order as `PASS` or `NOT_PROVEN`.
Accepted evidence is limited to `instruction.md`,
`tests/**/grading_spec` (and optional extension), and deterministic probe
artifacts under `deterministic_core/` or
`deterministic_probe_artifacts/`. Scope is `CONTRACT_WIRING` or
`DETERMINISTIC_CONTRACT`.

The overlay must not use `paper/`, `solution/`, Oracle output, metadata,
`tests/checker.py`, Agent-quality evidence, Gold, targets, tolerances, formulas,
units, thresholds, or scoring-direction claims. It may apply only to an
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

`AGENT_CONTRACT_PENDING` is emitted only when every D1-D6 status is an eligible
unavailable wiring gap and there is no machine `FAIL`, proven/blocking finding,
required queue, Hard Gate, usable runtime contradiction, or other real defect.
Otherwise Review finalizes the authoritative non-PASS verdict (`CONDITIONAL` or
`REJECT` as applicable). A pending result is `NOT_ASSESSABLE`, has
`publishable=false`, and has no final audit bundle.

For an eligible pause, Review writes the external
`agent_contract/request.json` with schema
`materials-agent-contract-request/1.0`, binding package, implementation,
static/probe artifacts, and machine-contract hashes. Resume the same workspace:

```bash
python scripts/run_review.py <Harbor题包目录> \
  --audit-output-dir <外部审计目录> \
  --agent-contract-assessment <assessment.json>
```

Resume validates bindings, reuses persisted probes, and does not rerun
deterministic preparation.

## Output roles and checker audit

Map every workflow requirement as:

```text
instruction requirement → Agent work/action → declared core output
→ checker reads → checker scores in final reward
```

Use `CORE_OUTPUT`, `PROCESS_ONLY`, or `UNCLASSIFIED`. Process artifacts remain
contract-map-only: they are excluded from probe classes, weights, deductions,
gates, and anti-hacking traces. Complete models, structures, trajectories,
fields, and meshes remain core even when mislabeled process. An ignored core
output is `CHECKER_CORE_TASK_UNASSESSED`.

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

## Run and external-output policy

Write taxonomy and paper assessments outside the package, then run:

```bash
python scripts/run_review.py <Harbor题包目录> \
  --audit-output-dir <外部审计目录> \
  --agent-assessment <assessment.json> \
  --attestation-output <external.json>
```

The default output is `<topic>/review_outputs/<paper-id>/`; explicit output
directories must be external and non-overwriting. No fixture manifest or
independent result directory is accepted. Generated probes and attestations
remain external. Attestations bind the audit and external-input hashes.

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
