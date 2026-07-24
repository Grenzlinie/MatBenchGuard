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

## Delivery contract (leakage scope)
The solver receives ONLY `instruction.md`. `paper/**`, `solution/**`, `tests/**`,
`resources.json`, `manifest.json` are NOT delivered — reviewer/harness-side.
So Gold/thresholds/tolerances appearing in the paper, solution, or checker are
BY DESIGN, NOT leakage. Judge 2.7 leakage only against `instruction.md`. A
checker a no-computation/fabricated submission can pass is a 2.5/C04 defect
(possibly `CHECKER_CORE_TASK_UNASSESSED`), NOT leakage. Grading runs
`tests/test.sh` in a solver-invisible environment. Still read paper/tests/
solution IN FULL as the reviewer's grounding.

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
2. Read SRC/instruction.md, task.toml, steps.json, manifest.json, resources.json,
   tests/checker.py, tests/grading_spec.json, environment/Dockerfile, and
   paper/paper.md IN FULL. Read solution/ only to test acceptance in isolation —
   never as validity evidence.
3. Mechanical evidence (mandatory):
   `uv run --python 3.12 python $REVIEW_SCRIPTS/collect_package_evidence.py SRC \
      --output OUT/evidence/mechanical_evidence.json`
4. Checker probes (execution mandatory):
   `uv run --python 3.12 python $REVIEW_SCRIPTS/run_checker_probes.py SRC \
      --output OUT/evidence/checker_observations.json`
   Supply Agent-built --case dirs for valid/gradient/equivalence/component
   outputs built from public task evidence (never from solution values).
5. Adjudicate 2.1–2.8, score C01–C07, four Hard Gates, all probe classes, 5
   readiness categories, parameter assessment. Write `OUT/agent_final_decision.json`
   from the review template. Set `package_id` to `<pkg>`.
6. Validate:
   `uv run --python 3.12 python $REVIEW_SCRIPTS/validate_agent_decision.py \
      OUT/agent_final_decision.json`  -> must print `"valid": true`.

### If verdict == PASS
No repair needed. Skip to step 9.

### Otherwise (CONDITIONAL / REJECT with repairable findings)
7. Run repair per the repair SKILL:
   - Copy SRC -> `OUT/snapshot/` (immutable) and `OUT/candidate/` (editable).
   - Re-adjudicate under the final-result-only boundary; drop process/trace/
     host-path-only findings. Classify AUTO_FIX / ASSISTED_FIX / ABANDON.
   - For each target: capture fail-before on snapshot, apply only evidence-backed
     edits to `OUT/candidate/**` (never SRC), capture pass-after.
   - Re-run collector + probes on candidate.
   - Perform ONE equal-depth re-audit; write `OUT/reaudit_agent_final_decision.json`
     and validate it.
8. Write `OUT/repair_report.json` and validate with
   `$REPAIR_SCRIPTS/validate_repair_report.py` -> `"valid": true`.
   Outcomes: REPAIRED (reaudit PASS, publish candidate), PARTIALLY_REPAIRED,
   ABANDONED, ROLLED_BACK. Never publish a non-PASS or unvalidated candidate.
   The candidate must preserve the required Harbor structure. Source never mutated.

9. Completion. DONE when `OUT/agent_final_decision.json` validates AND
   (verdict==PASS OR `OUT/repair_report.json` validates). Then:
   `touch OUT/.done` and `uv run --python 3.12 python $SCRIPTS/queue.py done <pkg>`.

## Rules
- Do the science honestly; never fabricate Gold/parameters/tolerances/probes.
- Record actual probe results honestly (execution mandatory).
- Keep every artifact under OUT. The source package is never mutated.
- If genuinely blocked (evidence loss), leave NOT_ASSESSABLE, do NOT touch .done;
  `queue.py release <pkg>` and report the package id + reason for retry.
