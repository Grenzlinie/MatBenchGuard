# QA Review + Repair Runner Playbook (one package at a time)

You process the exact package id(s) handed to you. NEVER modify anything under
the source corpus (`$QA_SRC`, the read-only Harbor packages). ALL outputs go
under `$QA_ROOT/<pkg-id>/`.

Environment: always run python via `uv run --python 3.12 python ...`.
Paths (set by the orchestrator, exported in your prompt):
- SRC  = `$QA_SRC/<pkg>`             (read-only source package)
- OUT  = `$QA_ROOT/<pkg>`            (your writable output for this package)
- SKILLS = the review + repair skills (read SKILL.md + references once, apply)
- SCRIPTS = this skill's `scripts/` (queue.py) + the review/repair skills' scripts

Read the Review skill's `references/check-responsibility-matrix.md` before
processing the first package. It defines the mandatory MECHANICAL/HYBRID/AGENT
boundary and the escalation condition for paper deep review.

## Delivery contract (leakage scope)
The solver receives ONLY `instruction.md`. `paper/**`, `tests/**`,
`resources.json`, `manifest.json` are NOT delivered — reviewer/harness-side.
So Gold/thresholds/tolerances appearing in the paper or checker are
BY DESIGN, NOT leakage. Judge 2.7 leakage only against `instruction.md`. A
checker a no-computation/fabricated submission can pass is a 2.5/C04 defect
(possibly `CHECKER_CORE_TASK_UNASSESSED`), NOT leakage. Grading runs
`tests/test.sh` in a solver-invisible environment. Still read paper/tests/
IN FULL as the reviewer's grounding. `solution/**` is fully out of scope: never
read, execute, hash, scan, cite, or modify it.

## Network policy
GitHub / HuggingFace / other external hosts being unreachable is a VM egress
restriction, NOT a resource defect. Classify such failures as
`AUTOMATION_LIMITATION` and readiness `NOT_ASSESSABLE`/`READY` per the declared
container layout — never `NOT_READY`/`INDISPENSABLE_DIRECT_INPUT_UNAVAILABLE`
solely because a download failed.

## Self-claim loop (drain the queue)
You are given a unique AGENT_ID. Loop until the queue is empty:
1. Claim ONE package:
   `uv run --python 3.12 python $SCRIPTS/queue.py claim <AGENT_ID> 1`
   - Prints a package id -> process it with the per-package procedure below.
   - Prints nothing (empty) -> STOP, the queue is drained. Report and exit.
2. After finishing a package (including `queue.py done`), go back to step 1.
Process ~8 packages max per invocation, then report progress and exit (the pool
relaunches to continue). Always finish the package you started.

## Per-package procedure
1. `mkdir -p OUT/evidence`.
2. Collect Phase 0–2 mechanical evidence:
   `uv run --python 3.12 python $REVIEW_SCRIPTS/collect_package_evidence.py SRC \
      --output OUT/evidence/mechanical_evidence.json`
3. Complete the Phase 0–2 cheap-screen responsibilities from the responsibility
   matrix. Read the actual instruction, steps, resources, grading, checker,
   `tests/test.sh`, task/manifest fields, and relevant Gold/data flow needed to
   resolve limitations and Hybrid checks; a candidate hit or zero hits is never
   itself a verdict.
4. If the package retains a substantive scientific target and has no confirmed
   non-repairable early Hard Gate, enter Phase 3: read `paper/paper.md` IN FULL
   and re-check the decisive package passages against the paper. Perform every
   mandatory Phase 3 Hybrid check in the responsibility matrix. Do not open
   `solution/`. If a non-repairable early Hard Gate is already confirmed, stop
   before Phase 3 and expensive probes; retain the stop reason and collect an
   explicit `--no-execute` observation file only to record why probe classes
   remain unassessed. Such a stopped package cannot PASS or enter Repair; after
   its Review decision validates as `REJECT`, classify it `SCREENED_OUT`.
5. Write the probe plan, then execute Phase 4 checker probes:
   `uv run --python 3.12 python $REVIEW_SCRIPTS/run_checker_probes.py SRC \
      --output OUT/evidence/checker_observations.json`
   Supply Agent-built --case dirs for valid/gradient/equivalence/component
   outputs built from public task evidence.
6. Adjudicate 2.1–2.8, score C01–C07, five Hard Gates, all scientific risk
   patterns, all probe classes, 5 readiness categories, and parameter assessment.
   Explicitly inspect cross-step numeric conflicts, method/reference mismatch,
   and random/interpolated/fitted/smoke/synthetic Gold provenance. Treat lexical
   hits as candidates only: a reduced smoke system may validly score a
   source-backed trend/order when applicability is justified and no exact paper
   value is claimed. Write
   `OUT/agent_final_decision.json` from the review template. Set `package_id`
   to `<pkg>`.
7. Validate:
   `uv run --python 3.12 python $REVIEW_SCRIPTS/validate_agent_decision.py \
      OUT/agent_final_decision.json`  -> must print `"valid": true`.

### If verdict == PASS
No repair needed. Skip to step 10.

### If terminal early verdict == REJECT / SCREENED_OUT
Do not create a candidate or repair report. Skip to step 10. This terminal state
requires a validated Review decision with a controlling Hard Gate/finding
disposition `ABANDON` and no path by which local repairs could make the package
publishable.

### If verdict == NOT_ASSESSABLE
Do not mark complete. Preserve evidence, release the claim, and wait for the
missing evidence or external state.

### Otherwise (CONDITIONAL / REJECT admitted to Repair)
8. Run repair per the repair SKILL:
   - Confirm at least one finding/Hard Gate has disposition `REPAIR` and no
     controlling non-repairable Hard Gate has disposition `ABANDON`.
   - Copy SRC -> `OUT/snapshot/` (immutable) and `OUT/candidate/` (editable).
   - Re-adjudicate under the final-result-only boundary; drop process/trace/
     host-path-only findings. Classify AUTO_FIX / ASSISTED_FIX / ABANDON.
   - For each target: capture fail-before on snapshot, apply only evidence-backed
     edits to `OUT/candidate/**` (never SRC), capture pass-after.
   - Re-run collector + probes on candidate.
   - Perform ONE equal-depth re-audit; write `OUT/reaudit_agent_final_decision.json`
     and validate it.
9. Write `OUT/repair_report.json` and validate with
   `$REPAIR_SCRIPTS/validate_repair_report.py` -> `"valid": true`.
   Outcomes: REPAIRED (reaudit PASS, publish candidate), PARTIALLY_REPAIRED,
   ABANDONED, ROLLED_BACK. Never publish a non-PASS or unvalidated candidate.
   The candidate must preserve the required Harbor structure. Source never mutated.

10. Completion. DONE when `OUT/agent_final_decision.json` validates AND one of:
   verdict is `PASS`; terminal state is `SCREENED_OUT` under the rule above; or
   `OUT/repair_report.json` validates. `NOT_ASSESSABLE` is never DONE. Then:
   `touch OUT/.done` and `uv run --python 3.12 python $SCRIPTS/queue.py done <pkg>`.

## Rules
- Do the science honestly; never fabricate Gold/parameters/tolerances/probes.
- Record actual probe results honestly. Execution is mandatory after Phase 3;
  only a terminal early `SCREENED_OUT` may retain explicit `--no-execute`
  observations instead.
- Keep every artifact under OUT. The source package is never mutated.
- If genuinely blocked (evidence loss), leave NOT_ASSESSABLE, do NOT touch .done;
  `queue.py release <pkg>` and report the package id + reason for retry.
