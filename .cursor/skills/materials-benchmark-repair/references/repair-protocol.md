# Repair protocol details

This reference holds the detailed operational contract for
`materials-benchmark-repair/SKILL.md`.

## Batch integrity

Repair consumes one immutable source audit and one external attestation. The
attestation binds the manifest, report, disposition, assessment hashes, package
identity, and Review implementation hashes. Never trust a package-local
manifest or plan-provided assessment hash. Freeze the source digest over
`instruction.md`, `tests/**`, and `solution/**` (including `tests/test.sh`),
then verify every finding, including `ABANDON`, is still `OPEN`.

The plan schema is `materials-deterministic-repair-plan/1.0`. It binds the
source deterministic schema, registry, digest, audit ID, and complete
`required_finding_ids` queue. Every finding has a decision, operations,
evidence links, and causal regressions. Unknown ownership, omitted findings,
stale bindings, or invalid evidence fail closed before mutation.

## Isolated pass

1. Copy the package to isolated `snapshot/` and `candidate/` directories.
2. Run every causal regression against the snapshot and require fail-before.
3. Apply all valid operations once, recording before/after hashes and evidence.
4. Run every regression against the candidate and require pass-after.
5. Invoke the canonical Review CLI exactly once at equal dual-lane depth.

The Review re-audit is the only post-repair authority. Emit C01–C07
before/after normalized scores and delta in percentage points. A local score,
finding heuristic, or regression result cannot publish a candidate.

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
evidence.

`ASSISTED_FIX` is evidence-backed and every operation references evidence IDs.
Local paper/direct-source evidence must be source-audit-bound and quote the
exact file. Primary-web evidence additionally needs HTTPS URL, retrieval time
and metadata, exact quote, source hash, applicability/derivation, and an
explicit approved-primary record. A missing or type-mismatched source is
`BLOCKED_EVIDENCE`; Repair never guesses. `ABANDON` has no operations, but it
uses the same current batch schema and complete authenticated source queue as
every other decision. Legacy 0.1/0.2 plans are archival-only and never enter
Repair execution.
Agent-quality findings never receive D1–D6 ownership. Oracle/solution values
and metadata cannot support a public contract or science change.

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
