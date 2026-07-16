# Materials Benchmark Audit Report

## 1. Audit Summary

- Audit ID: {{AUDIT_ID}}
- Benchmark: {{BENCHMARK_NAME}}
- Paper mode: {{PAPER_MODE}}
- Execution level: {{EXECUTION_LEVEL}}
- Materials class: AMBIGUOUS
- Answer type: OPEN_ENDED
- Final verdict: NOT_ASSESSABLE
- Authoritative score (0–100): null
- Scoring version: materials-review-scoring/1.0
- Core reason: Audit not yet completed.

## 2. Benchmark Identity

## 3. Audit Configuration

## 4. Final Verdict

The verdict is fail-closed under `materials-evidence-contract/1.0`. List every
unresolved evidence gap; a report with any gap cannot be `PASS`.

## 5. Materials Qualification

Record the authoritative classification, rationale, and instruction/tests quote
for each required axis. Prescreen output alone is not authoritative evidence.
For no-paper review, also record all four paper-trigger adjudications with
package evidence.

## 6. Capability Alignment

## 7. Gate Results

Exactly four Hard Gates are reported with code, status, evidence, and affected
locations.

## 8. Resource Reachability

Status: NOT_ASSESSED
Reason: Only indispensable direct inputs explicitly required by instruction are eligible for verification.

## 9. Instruction and Task Design

Publish the role-aware contract map:

`Instruction requirement → Agent work → core output → checker read → checker score`

Process evidence is verification-only and has no independent rubric weight.
Final scored outputs must distinguish static read/scorer candidates from
runtime proof, and show declared weight, effective-weight status, return-path
status, and every required dynamic check that was not run.
Include requirements without recognized outputs as unclassified rows with
explicit unknown read and score states.

## 10. Checker Assessment

## 11. Gold Standard Assessment

Status: NOT_ASSESSED
Reason: Gold provenance requires paper-grounded review.

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
Reason: No-paper mode does not assess paper fidelity.

## 15. Dimension Scores

Each dimension reports points earned/max points, normalized score, deduction
IDs, finding IDs, and non-empty positive or finding evidence. Robustness also
records positive/negative/discrimination/equivalence provenance. Solution
completeness records only solve/positive-mock status and never Oracle values.

## 16. Findings

## 17. Required Fixes

## 18. Recommended Improvements

## 19. Audit Scope and Limitations

## 20. Audit Log Summary
