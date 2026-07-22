---
name: materials-benchmark-repair
description: Repair one audited materials-science Harbor package in one isolated, tested batch and exactly one equal-depth Review re-audit, publishing only a fully verified REPAIRED result.
---

# Materials Benchmark Repair

Repair one Harbor package from its immutable Review run. Review owns evidence
and no mutations; Repair reads the run-local `plan.json`, applies one isolated
candidate, then either atomically publishes a narrowly eligible
`DIRECT_DETERMINISTIC` batch or invokes exactly one equal-depth re-review.
Local regression success alone never publishes semantic or Agent-lane changes.

## Public seam and output policy

Plans, attestations, audit bundles, repair bundles, snapshots, candidates, and
histories stay outside the Harbor package, within the same run:

```sh
python scripts/run_repair.py --run-dir <run-dir>
```

The run owns the source audit, candidate, re-audit and repair evidence. The
package must not receive generated audit or repair-report files. Review
generates all synthetic probes inside the run-local re-audit workspace.

Repair holds the same canonical source-output lock for its full lifecycle, so
Review cannot replace the source audit during pending, resume, re-audit, or
publication. The source bundle's byte digest is recorded and rechecked at
each boundary; any change fails closed and requires a fresh audit.

Repair accepts only a complete dual-lane `REVIEWED` source audit that binds a
validated paper Agent assessment. Incomplete or `NOT_SUPPLIED` paper
assessments are rejected at ingress (legacy runs migrate per the Review
`AGENT_ASSESSMENT_PENDING` path). Plan fields cannot replace that assessment.

If equal-depth Review returns `AGENT_CONTRACT_PENDING`, preserve the candidate
and workspace without consuming an attempt. The same run is resumed by its
main Agent after placing the assessment in `agent_contract/assessment.json`:

```sh
python scripts/run_repair.py --run-dir <run-dir>
```

Pending has `status=AGENT_CONTRACT_PENDING`,
`repair_state=AGENT_CONTRACT_PENDING`, `review_verdict=NOT_ASSESSABLE`,
`publishability=EVIDENCE_PENDING`, `publishable=false`, and
`attempt_consumed=false`. Resume validates package, plan, request, machine
contract, probe, and workspace bindings; it reuses probes and creates no
semantic attempt.

## Canonical run-local repair bundle

Every terminal Repair attempt (direct, partial, abandoned, rollback, or
re-audited repaired) emits this tree under the run's repair output path — never
inside the Harbor package:

```text
repair/benchmark_repair/
├── repair_summary.md
├── repair_report.json
├── repair_plan.md
├── repair_plan.json
├── changes.jsonl
├── unresolved_findings.jsonl
├── regression_tests.json
├── re_audit_comparison.json
├── patches/
├── evidence/
├── logs/
└── repair_manifest.json
```

History archives live at `repair/benchmark_repair_history/<repair_id>/`.
`repair_manifest.json` hashes every member and binds A0, source audit,
assessment, publication record, and history link. Legacy deliverable names
(`changes.json`, `patch.json`, `repair.log`, `history.json`) are not emitted.
For `DIRECT_DETERMINISTIC` (when enabled), `re_audit_comparison.json` keeps the
same schema with `reaudit_performed: false` and an explicit reason.

## Agent repair assessment and plan v2

Before any candidate mutation, place an Agent-authored assessment at:

```text
<run-dir>/repair/agent_repair_assessment.json
```

Schema `materials-agent-repair-assessment/1.0`. It must bind every OPEN queue
finding (D1–D6 and Agent-quality) with `decision`, `agent_verdict`,
`repair_scope`, `core_science_change`, evidence, and
`approved_operation_ids`. Omission is fail-closed. The machine check remains
factual authority: the Agent cannot suppress a machine `FAIL`, delete a
confirmed finding, or invent science from unavailable evidence.

Executable plans use `materials-repair-plan/2.0` and bind:

- audit ID, source audit identity, A0 ContentRoot, package identity, and
  Review implementation digest;
- the complete cross-lane OPEN queue;
- `agent_repair_assessment` path + schema + content hash;
- each finding's lane, scope, decision, evidence, operations, and regressions;
- per-operation `publication_class`: `DIRECT_DETERMINISTIC` or
  `REAUDIT_REQUIRED`.

Prior `materials-deterministic-repair-plan/1.0` (and 0.1/0.2) plans are
archival-only and cannot enter execution. Missing/stale assessment hashes,
unapproved operations, or skipped Agent findings fail closed before mutation.

When every executable operation is narrowly `DIRECT_DETERMINISTIC` (all D1–D6
`AUTO_FIX`, `core_science_change=false`, unique wiring scopes only, mutation
allowlist, no Agent-quality / checker-robustness / paper-instruction /
direct-input repairs), Repair atomically publishes after fail-before/pass-after
regressions without equal-depth Review, recording
`verification_mode: DIRECT_DETERMINISTIC`. Any other candidate still receives
exactly one equal-depth re-audit that inherits the paper assessment. Direct
publish does not consume the two-attempt re-audit budget.

Place the plan as run-local `plan.json` (or an external path for harnesses)
with:

```json
"agent_repair_assessment": {
  "schema_version": "materials-agent-repair-assessment/1.0",
  "path": "repair/agent_repair_assessment.json",
  "assessment_hash": "sha256:..."
}
```

## Plan, assessment, and AUTO_FIX contract

The machine contract remains authoritative. A contract-only assessment may
overlay only an eligible unavailable (`BLOCKED`/`NOT_ASSESSABLE`) check. It
cannot override machine `FAIL`, proven facts, blockers, missing-input
failures, runtime contradictions, Hard Gates, or Agent-quality findings.
Accepted evidence is only `instruction.md`, `tests/**/grading_spec` (with an
optional extension), and deterministic probe artifacts. It cannot use paper,
solution, Oracle, metadata, Gold, targets, tolerances, formulas, units,
thresholds, or science-quality evidence for AUTO_FIX.

The autonomous decision set is `AUTO_FIX`, `ASSISTED_FIX`, `ABANDON`; there is
no human approval state. `AUTO_FIX` is limited to unique, source-bound
restoration of existing D1-D6 contract/scoring wiring:

- synchronize an existing output declaration/path;
- restore existing scorer registration, binding, return, or final-reward links;
- restore a standard Harbor entrypoint around one existing producer;
- normalize already-declared finite positive weights without changing ratios.

`AUTO_FIX` cannot introduce or choose Gold, targets, tolerances, thresholds,
formulas, scorer algorithms, fields, units, scientific parameters, producers,
or science semantics. It cannot make an ignored core output appear scored.
Each operation requires `core_science_change=false`, source-bound proof, and a
causal fail-before/pass-after regression; a passing regression is not science
evidence.

`ASSISTED_FIX` is available for both deterministic and Agent-quality findings
when type-matched evidence is bound and the assessment approves each
operation. Each item records `source_kind`, `exact_quote`, and `source_hash`.
Local paper/direct-source evidence must bind the source audit. Approved
primary-web evidence additionally needs HTTPS URL, `retrieved_at`,
`retrieval_metadata`, applicability, derivation, and explicit primary approval.
Missing, conflicting, ambiguous, or type-mismatched evidence is
`BLOCKED_EVIDENCE`; never guess. Agent-quality findings never receive D1-D6
ownership. `ABANDON` has no operations. Oracle, solution, and metadata content
cannot support a public contract or science change. Unsupported core science
changes must be `BLOCKED_EVIDENCE` or `ABANDON`.

Lane-aware policy replaces D-only boundary checks while preserving no-leak and
evidence rules: Agent findings cannot become `AUTO_FIX` or claim a fabricated
D check; D findings may take evidence-bound `ASSISTED_FIX`.

Detailed evidence, scope, and lifecycle rules are in
[references/repair-protocol.md](references/repair-protocol.md).

## One-pass isolated flow

1. Validate the run's A0 ContentRoot, source audit identity, paper assessment,
   Agent repair assessment, and live package identity against the frozen
   snapshot.
2. Confirm every target, including `ABANDON`, remains `OPEN`.
3. Copy isolated `snapshot/` and `candidate/` trees. Run all regressions
   fail-before, apply valid operations once, then run
   all regressions pass-after.
4. If the candidate is not narrowly `DIRECT_DETERMINISTIC`, run Review exactly
   once at the source audit's paper mode and dual-lane depth. Emit C01-C07
   before/after normalized scores and delta (pp). Eligible direct candidates
   skip this step and publish from regression evidence alone.

The equal-depth Review uses its own unique run workspace and atomic publication
lock. It never reuses or deletes another run's temporary workspace. A
source audit is immutable: Repair may read it but may not rewrite or refresh it.

A local regression pass alone cannot publish semantic, Agent-lane, or
`ASSISTED_FIX` candidates — only the narrow direct-deterministic matrix may
skip Review. Retain complete candidate, snapshot, comparison, evidence, and
history data for every non-pending outcome.

## Terminal states and atomic publication

All results use `disposition`, `publishable`, and `repair_state`:

| repair_state | disposition | publishable | package |
|---|---|---|---|
| `REPAIRED` | `PASS` | `true` | atomically published |
| `PARTIALLY_REPAIRED` | `CONDITIONAL` | `false` | original preserved |
| `ABANDONED` | `REJECT` | `false` | original preserved |
| `ROLLED_BACK` | source verdict | `false` | restored unchanged |
| `INFRASTRUCTURE_BLOCKED` | source verdict | `false` | restored unchanged |

Re-audit atomic publication requires PASS, score ≥80, effective deterministic
CLEAN, no Hard Gate, preserved identity, allowed mutation scope, no unresolved
HIGH/FATAL finding, every target resolved, and exactly one equal-depth
re-audit. Direct deterministic publication instead requires the eligibility
matrix, fail-before/pass-after regressions, candidate validation, preserved
identity, and a successful atomic swap — with `reaudit_performed: false`.

The semantic attempt limit is two completed re-audits per `audit_id`.
Setup/Docker/regression/apply/Review control failures do not consume it and
use the circuit breaker in `run_repair.py`. A second unresolved semantic
re-audit or post-repair FATAL converges to `ABANDONED`.

## Allowed package changes and regressions

Only `instruction.md`, `tests/**`, and `solution/**` may change.
`paper/**`, metadata, and environment roles are read-only. Supported
operations are `write_file`, `replace_text`, `json_set`, and `delete_file`;
`write_file` may create an executable `solution/solve.sh`.

Regression types are `file_exists`, `file_absent`, `file_executable`,
`text_contains`, `text_not_contains`, `json_path_equals`, and argv `command`.
Command regressions run through the shared disposable `qa-checker` Docker
sandbox, using the same image and preflight as Review:

```sh
.cursor/skills/materials-benchmark-review/scripts/sandbox/build_qa_checker.sh
```

Docker/image/cache setup failures abort the operation as control failures.
Do not probe or repair solver-generated structures/trajectories/models,
routine DFT/MD parameters, substitutable software, or historical software
versions. C06 resource repair is limited to indispensable direct inputs.

## Completion

A nonexistent claimed source is `BLOCKED_EVIDENCE` before writing. Evidence
paths must be allowed local files without traversal, absolute paths, or
symlinks, and must store source hashes. Quote precision must support the
change's precision: new fields/columns need schemas; Gold/tolerance changes
need value, unit, source or derivation; weights/thresholds need contract value
and proof. Paper evidence binds the exact hashed `paper/**` file. Web content
is not fetched during Repair. Solution/Oracle values cannot enter evidence.

Repair is not entered below source score 60. A re-audit below 60 abandons;
60–79 may remain partial. Unverifiable Gold, conflicting paper evidence,
multiple fair answers without scoring, required core-science changes, or
unresolved severe findings trigger abandon/rollback.

Completion requires terminal fields, exactly one equal-depth re-audit,
before/after C01-C07 delta, preserved identity, allowed scope, and a
self-validating run-local `benchmark_repair` bundle and history archive. Publication happens only in `REPAIRED`. Harbor packages stay free of generated repair artifacts.
