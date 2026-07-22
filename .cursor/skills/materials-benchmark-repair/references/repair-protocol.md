# Repair protocol details

This reference holds the detailed operational contract for
`materials-benchmark-repair/SKILL.md`.

## Batch integrity

Repair consumes one immutable A0 source audit within the same run. The A0
ContentRoot binds the snapshot and audit evidence; Review implementation and
leaf hashes are provenance only, not freshness gates. Never trust a
package-local manifest or plan-provided assessment hash. Freeze the source
snapshot over
`instruction.md`, `tests/**`, and `solution/**` (including `tests/test.sh`),
then verify every finding, including `ABANDON`, is still `OPEN`.

The executable plan schema is `materials-repair-plan/2.0`. It binds the source
deterministic schema, registry, digest, audit ID, complete dual-lane OPEN
queue (D1–D6 + Agent-quality), and the hash/schema/path of
`repair/agent_repair_assessment.json`. Every finding has a decision,
operations, evidence links, and causal regressions. Every operation declares
`publication_class` (`DIRECT_DETERMINISTIC` | `REAUDIT_REQUIRED`). Unknown
ownership, omitted findings, stale bindings, missing assessment, unapproved
operations, or invalid evidence fail closed before mutation.

Prior `materials-deterministic-repair-plan/1.0` (and 0.1/0.2) plans are
archival-only history evidence and never enter Repair execution.

## Agent repair assessment

Create `repair/agent_repair_assessment.json` before mutation
(`materials-agent-repair-assessment/1.0`). The Agent must read
`instruction.md`, applicable `tests/**`, source audit evidence, and
`paper/**` whenever the finding is scientific or paper-grounded.

Each OPEN queue finding receives one assessment record with `decision`
(`AUTO_FIX` | `ASSISTED_FIX` | `ABANDON`), `agent_verdict`
(`APPROVE_REPAIR` | `BLOCKED_EVIDENCE` | `ABANDON`), `repair_scope`,
`core_science_change`, rationale, type-matched evidence, and
`approved_operation_ids`. Omission of any OPEN finding is fail-closed.

## Isolated pass

1. Validate paper Agent assessment inheritance on the source audit, then load
   and hash-check `agent_repair_assessment.json`.
2. Copy the package to isolated `snapshot/` and `candidate/` directories.
3. Run every causal regression against the snapshot and require fail-before.
4. Apply all valid, assessment-approved operations once, recording evidence
   and deterministic fail-before/pass-after regressions.
5. Run every regression against the candidate and require pass-after.
6. If every operation is narrowly `DIRECT_DETERMINISTIC` and the eligibility
   matrix holds, atomically publish with `verification_mode:
   DIRECT_DETERMINISTIC` and regression evidence (no Review re-audit).
   Otherwise invoke the internal Review engine exactly once at equal dual-lane
   depth, inheriting the validated paper assessment.

Direct publication eligibility (all must hold): D1–D6 machine findings only;
all `AUTO_FIX`; `core_science_change=false`; unique source-bound wiring
scopes (`DETERMINISTIC_WIRING` / `UNIQUE_SCORING_WIRING`); mutation allowlist
only; no Agent-quality, checker robustness/semantics, paper-grounded
instruction, or direct-input repairs; fail-before/pass-after + identity /
source-audit / mutation checks pass. Mixed or non-eligible batches take the
re-audit route. Direct publish does not consume the two-attempt re-audit
budget.

For re-audit-required candidates the Review re-audit remains the sole
post-repair authority. Emit C01–C07 before/after normalized scores and delta
in percentage points. A local regression pass alone cannot publish semantic or
Agent-lane changes.

## Decisions and evidence

The closed decision set is `AUTO_FIX`, `ASSISTED_FIX`, and `ABANDON`; there is
no human approval state. `AUTO_FIX` is limited to unique source-bound
restoration of existing D1–D6 wiring: output declaration/path sync, scorer
registration/binding/return/final-reward connections, a standard Harbor
entrypoint around one existing producer, or ratio-preserving normalization of
already-declared finite positive weights.

`AUTO_FIX` cannot select or introduce Gold, targets, tolerances, thresholds,
formulas, scorer algorithms, fields, units, scientific parameters, producers,
or science semantics; it cannot make an ignored core output appear scored.
Each operation needs `core_science_change=false`, source-bound proof, and one
causal fail-before/pass-after regression. A passing regression is not science
evidence. Agent-quality findings never receive `AUTO_FIX`.

`ASSISTED_FIX` is available for both lanes when type-matched evidence is bound
and every operation is listed in the assessment's `approved_operation_ids`.
Local paper/direct-source evidence must be source-audit-bound and quote the
exact file. Primary-web evidence additionally needs HTTPS URL, retrieval time
and metadata, exact quote, source hash, applicability/derivation, and an
explicit approved-primary record. A missing or type-mismatched source is
`BLOCKED_EVIDENCE`; Repair never guesses. Unsupported core science changes
must be `BLOCKED_EVIDENCE` or `ABANDON` with no mutation. `ABANDON` has no
operations, but it uses the same current batch schema and complete
authenticated source queue as every other decision.

Lane-aware policy replaces D-only plan binding while preserving no-leak rules:
Agent findings cannot claim D1–D6 ownership; machine `FAIL` facts cannot be
suppressed by assessment text alone.

## Scope and regression interface

Only `instruction.md`, `tests/**`, and `solution/**` may be mutated.
`paper/**`, metadata, and environment roles are read-only. Supported
operations are `write_file`, `replace_text`, `json_set`, and `delete_file`;
`write_file` may create an executable `solution/solve.sh`.

Regression types are `file_exists`, `file_absent`, `file_executable`,
`text_contains`, `text_not_contains`, `json_path_equals`, and argv `command`.
Command regressions use the disposable `qa-checker` Docker sandbox and the
same image/preflight as Review. Setup or image failures are control failures,
not package regression results.

## Terminal and publication rules

The batch states map to canonical fields as follows:

- `REPAIRED` → `PASS`, publishable, and atomic publication.
- `PARTIALLY_REPAIRED` → `CONDITIONAL`, not publishable, original preserved.
- `ABANDONED` → `REJECT`, not publishable, original preserved.
- `ROLLED_BACK` → source verdict, not publishable, restored unchanged.
- `INFRASTRUCTURE_BLOCKED` → source verdict, not publishable, restored unchanged.

Publication requires `PASS`, score at least 80, effective deterministic
`CLEAN`, no Hard Gate, preserved identity, allowed mutation scope, no
unresolved HIGH/FATAL finding, every target finding resolved, and exactly one
re-audit. Preserve a complete external history/bundle for every non-pending
outcome. A pending `AGENT_CONTRACT_PENDING` workspace is retained for resume
and is not a terminal repair bundle.

The semantic attempt limit is two completed re-audits per `audit_id`; setup,
Docker, regression, apply, and Review control failures do not consume it.
Repeated control fingerprints use the circuit breaker in `run_repair.py`.
After two unresolved semantic attempts, or a post-repair FATAL, converge to
`ABANDONED`.

## Canonical repair bundle

Terminal attempts write the human-readable run-local tree under
`repair/benchmark_repair/` with JSONL change/unresolved streams, `patches/`,
`evidence/`, `logs/`, and a hashed `repair_manifest.json`. Archives go to
`repair/benchmark_repair_history/<repair_id>/`. Harbor packages never receive
these generated artifacts.

