# Materials Benchmark Audit Report

## 1. Audit Summary

- Audit ID: {{AUDIT_ID}}
- Benchmark: {{BENCHMARK_NAME}}
- Paper mode: {{PAPER_MODE}}
- Execution level: {{EXECUTION_LEVEL}}
- Materials class: AMBIGUOUS
- Answer type: OPEN_ENDED
- Final verdict: NOT_ASSESSABLE
- Disposition: NOT_ASSESSABLE
- Publishable: false
- Canonical review_verdict: NOT_ASSESSABLE
- Canonical publishability: EVIDENCE_PENDING
- Canonical repair_decision: NOT_REQUIRED
- Canonical repair_status: NOT_APPLICABLE
- Repair state: NOT_REQUIRED
- Authoritative score (0–100): null
- Scoring version: materials-review-scoring/2.0
- Publication effective D1-D6 status: NOT_APPLICABLE
- Machine deterministic status: NOT_APPLICABLE
- Effective deterministic status: NOT_APPLICABLE
- Agent contract status: NOT_SUPPLIED
- Deterministic repair state: NOT_REQUIRED
- Publication route: EVIDENCE_PENDING
- Core reason: Audit not yet completed.

## 2. Benchmark Identity

## 3. Audit Configuration

## 4. Final Verdict

The verdict is fail-closed under `materials-evidence-contract/2.0`. List every
unresolved evidence gap; a report with any gap cannot be `PASS`.

## 5. Materials Qualification

Record the authoritative classification, rationale, and instruction/tests quote
for each required axis. Prescreen output alone is not authoritative evidence.
Paper is always read for A2/A4/A5 unless materials_qualification establishes
NON_MAT.

## 6. Capability Alignment

## 7. Gate Results

Exactly four Hard Gates are reported with code, status, evidence, and affected
locations.

### 7.1 Deterministic D1-D6 Contract

The authoritative report records every D1-D6 status, proven/blocking finding
IDs, advisory-only findings, the complete deterministic repair queue, and the
source-bound implementation digest. Advisory risks do not block PASS. A
publishable PASS requires effective deterministic `CLEAN`; an OPEN blocking finding at
any severity routes to `CONDITIONAL / REPAIR_QUEUE`.

The machine contract is the authoritative D1-D6 artifact. An optional
contract-only `agent_contract_assessment` is separate and additive; it can
overlay only eligible unavailable (`BLOCKED`/`NOT_ASSESSABLE`) checks. It cannot
override machine `FAIL`, proven facts, runtime contradictions, Hard Gates, or
quality findings. The effective contract preserves machine findings and
records the applied assessment.

New deterministic repair plans use
`materials-deterministic-repair-plan/1.0` and bind the source contract schema,
registry, digest, audit identity, and every `required_finding_id`. Historical
unbound repair plan `0.1` artifacts remain evidence archives.

If preparation is incomplete because the machine summary is
`NOT_APPLICABLE`, Review persists `agent_contract/request.json` under
`materials-agent-contract-request/1.0` with status
`AGENT_CONTRACT_PENDING`. The pending response is
`NOT_ASSESSABLE`, `publishable=false`, and includes `request_path`; resume with
`--agent-contract-assessment` reuses persisted probes and validates the
package, implementation, artifact, and machine-contract bindings. A completed
report records the assessment under `agent_contract_assessment` and the
additive effective artifact under `effective_deterministic_contract`.

## 8. Resource Reachability

Status: NOT_ASSESSED
Reason: Only indispensable direct inputs explicitly required by instruction are eligible for verification.

## 9. Instruction and Task Design

Publish the role-aware contract map:

`Instruction requirement → Agent work → core output → checker read → checker score`

Process artifacts are contract-map-only and never score, gate, or trigger
dynamic probes. Load-bearing scientific artifacts remain core outputs.
Final scored outputs must distinguish static read/scorer candidates from
runtime proof, and show declared weight, effective-weight status, return-path
status, and every required dynamic check that was not run.
Include requirements without recognized outputs as unclassified rows with
explicit unknown read and score states.

## 10. Checker Assessment

## 11. Gold Standard Assessment

Status: NOT_ASSESSED
Reason: Gold provenance must be recorded from independent paper-grounded
evidence; Oracle outputs are not provenance.

## 12. Execution Feasibility

## 13. Reproducibility and Leakage

Oracle values are never scientific evidence and never appear in this report.

First-class QA axes (not weighted dimensions):

- factual_accuracy: status, evidence, locations, limitations
- answer_leakage: status, evidence, locations, limitations
- instruction_completeness: status, evidence, locations, limitations
- checker_instruction_consistency: status, evidence, locations, limitations

Evidence semantics must match status: `supports_pass`, `supports_failure`,
`supports_warning`, or `supports_limitation`.

## 14. Paper Consistency

Status: NOT_ASSESSED
Reason: Paper fidelity has not yet been assessed on the dual-lane path.

## 15. Dimension Scores

The authoritative scoring is the seven-dimension `dimensions_v11` model
(C01–C07). Each dimension reports weight/max points, points earned, normalized
score, key-dimension flag, status, its deductions, and finding IDs; deductions
apply by severity ratio inside that dimension only. `summary.total_score` is the
weighted 0–100 total. Robustness (C07) also records
positive/negative/discrimination/equivalence provenance. C06/solution status
records only solve/positive-mock status and never Oracle values.

`summary.total_score` is a score, not the final verdict or publication route.
The current artifacts do not emit `quality_score` or `pre_gate_score`. The
final verdict is `summary.final_verdict`/top-level `review_verdict`; the
deterministic gate uses the effective contract after Hard Gates and evidence
availability are applied. `summary.publication_route`/top-level
`publishability` are routing fields, not scores.

| dim | title | weight | earned | normalized | key | finding IDs |
| --- | --- | --- | --- | --- | --- | --- |
| C01 | domain_admission | 10 | | | yes | |
| C02 | task_design_and_file_consistency | 20 | | | no | |
| C03 | scientific_validity_and_solvability | 20 | | | yes | |
| C04 | scoring_semantics | 20 | | | yes | |
| C05 | answer_leakage | 10 | | | no | |
| C06 | reproducibility | 10 | | | yes | |
| C07 | difficulty_and_auditability | 10 | | | no | |

### 15.1 Repair Delta

After a repair re-audit, `repair_delta` records before/after normalized scores
and `delta_pp` per C01–C07 from the single equal-depth re-audit.
The re-audit runs exactly once at equal dual-lane depth and is the sole
post-repair authority.
Atomic publication additionally requires no Hard Gate, preserved identity,
allowed mutation scope, and resolution of every target finding.

## 16. Findings

## 17. Required Fixes

## 18. Recommended Improvements

## 19. Audit Scope and Limitations

## 20. Audit Log Summary
