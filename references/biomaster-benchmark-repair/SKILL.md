---
name: biomaster-benchmark-repair
description: repair biomaster biology, biomedical, and bioinformatics benchmark packages using evidence from benchmark_audit. use when a benchmark folder contains audit_report.json, findings.jsonl, resource_checks.json, or checker_tests.json and the user wants safe fixes, regression tests, re-auditing, rollback, or abandonment of an irreparable task. write all repair artifacts to benchmark_repair, never use solution or hidden answers, and abandon tasks whose core data, gold standard, or scientific definition cannot be restored reliably.
---

# BioMaster Benchmark Repair

Repair a benchmark only from its public files and evidence produced by the BioMaster benchmark auditing workflow (`benchmark-biology-auditor`). Prefer abandoning an invalid task over forcing it to pass.

## Required input

Accept a benchmark directory or ZIP containing a benchmark root and:

- `benchmark_audit/audit_report.json`
- `benchmark_audit/findings.jsonl`
- preferably `resource_checks.json`, `checker_tests.json`, and `audit_manifest.json`

Do not read or use `solution/`, `solve.sh`, hidden answers, hidden acceptance criteria, or answer-bearing fixtures that are not public task inputs.

## Operating modes

- `PLAN_ONLY`: generate a repair plan without changing benchmark files.
- `SAFE_AUTO_FIX`: apply low-risk deterministic fixes and test them.
- `ASSISTED_FIX`: apply evidence-supported changes that require interpretation but do not redefine the scientific task.

Do not silently modify Gold standards, biological endpoints, cohort definitions, positive/negative labels, scientific thresholds, or scoring semantics. If such a change lacks explicit support in the paper or public benchmark evidence, abandon the task.

## Workflow

1. **Verify the audit is current.** Compare hashes in `benchmark_audit/audit_manifest.json` with current benchmark files. If the audit is stale, re-run the Auditor before repairing.
2. **Prepare output.** Run `scripts/prepare_repair_output.py <benchmark_root>`. Work only in the returned temporary repair directory until validation succeeds.
3. **Classify findings.** Run `scripts/plan_repairs.py <benchmark_root>` and review the generated plan. Classify each finding as `AUTO_FIX`, `ASSISTED_FIX`, or `ABANDON`.
4. **Apply dependency-ordered fixes.** Use the rules in `references/repair_policy.md` and `references/repair_categories.md`.
5. **Test every change.** Re-run static checks, original failing probes, regression tests, monotonicity tests, and relevant metamorphic tests. For checker changes, read `references/checker_repair.md`.
6. **Re-audit.** Run the BioMaster benchmark auditing workflow (`benchmark-biology-auditor`) on the repaired copy using at least the original paper mode and execution level.
7. **Decide outcome.** Use `REPAIRED`, `PARTIALLY_REPAIRED`, `ABANDONED`, or `ROLLED_BACK` according to `references/abandonment.md`.
8. **Write fixed-format output.** Populate all required files described in `references/report_schema.md`.
9. **Finalize atomically.** Run `scripts/finalize_repair_output.py <benchmark_root> --status <STATUS>`. This validates outputs, archives prior repair reports, and publishes `<benchmark_root>/benchmark_repair/`.

## Repair order

Apply fixes in this order unless evidence requires otherwise:

1. archive safety, parser, and path failures;
2. checker security vulnerabilities;
3. critical resource identity and reachability;
4. missing data or environment dependencies;
5. instruction and output-contract inconsistencies;
6. checker coverage and scoring bugs;
7. leakage and reproducibility failures;
8. paper consistency and Gold provenance;
9. difficulty, usability, and documentation improvements.

Do not patch the checker to accommodate incorrect data. Establish the task definition and resource identity first.

## Automatically repairable issues

Repair when the intended behavior is unambiguous and testable:

- invalid JSON, YAML, TOML, JSONL, or Python syntax;
- broken relative paths and inconsistent filenames;
- missing output directories or deterministic manifest fields;
- weights that do not sum correctly;
- unclear file columns, types, units, coordinate systems, ID types, sorting, duplicate, or missing-value rules;
- official accession or immutable artifact available but only a homepage was declared;
- missing version pins, checksums, package dependencies, or compatible solver declarations;
- checker crashes on missing, empty, duplicate, malformed, NaN, or infinite inputs;
- score direction, boundary, unused-weight, always-pass, or always-zero bugs;
- failure to read a required core output when its validation method is already defined;
- unsafe parsing, path traversal, shell injection, or unbounded file handling.

Every checker fix must add a regression test that failed before and passes after.

## Abandon instead of guessing

Mark the benchmark `ABANDONED` when any blocking condition applies:

- it is not a substantive biology or bioinformatics task;
- irreplaceable core data are permanently unavailable or unauthorized;
- public inputs are insufficient to answer the question;
- the Gold source cannot be verified or contradicts the paper/task;
- unrecoverable manual curation, model files, or historical database snapshots determine the answer;
- fair scoring cannot be defined for multiple valid outputs;
- repair requires inventing biological parameters or redefining the endpoint;
- the checker cannot be fixed without changing the core task;
- the declared compute budget cannot support the task and no valid reduced protocol exists;
- a targeted repair plus one evidence-driven correction still leaves the same FATAL root cause;
- re-audit finds an unresolved or newly introduced FATAL issue.

A transient network failure, replaceable mirror, or simple formatting error is not an abandonment reason.

## Attempt limit

For one root cause, allow:

1. one primary repair attempt;
2. one targeted correction based on test evidence.

If the second attempt fails the relevant Gate, stop and mark the task `ABANDONED`. Do not repeatedly tune thresholds or checker logic to chase a PASS.

## Required tests

At minimum, run:

- syntax, schema, path, and security checks;
- all tests that exposed the original finding;
- missing output, empty file, random answer, duplicate record, NaN/Inf, minimal exploit, and missing core artifact tests;
- a known-valid public fixture when available;
- score monotonicity across quality levels when applicable;
- semantic invariance tests for ordering and irrelevant metadata;
- smoke, reduced, or full scientific execution when required by the original audit level.

Distinguish data, environment, execution, invalid-output, scientific-mismatch, checker, and resource-exceeded failures.

## Outcome rules

- `REPAIRED`: re-audit is `PASS`, no unresolved FATAL/HIGH target findings, and regression tests pass.
- `PARTIALLY_REPAIRED`: re-audit is `CONDITIONAL`, no unresolved FATAL, remaining issues are explicitly recorded, and the package is not represented as fully ready.
- `ABANDONED`: a blocking condition applies or a FATAL remains after the allowed attempts. Set `publishable: false`.
- `ROLLED_BACK`: changes failed validation and the benchmark was restored.

Never report `PARTIALLY_REPAIRED` while a FATAL remains.

## Fixed output location

Write the latest result to:

```text
<benchmark_root>/benchmark_repair/
```

Archive any previous result to:

```text
<benchmark_root>/benchmark_repair_history/<repair_id>/
```

Required files:

```text
benchmark_repair/
├── repair_summary.md
├── repair_report.json
├── repair_plan.md
├── repair_plan.json
├── changes.jsonl
├── unresolved_findings.jsonl
├── regression_tests.json
├── re_audit_comparison.json
├── repair_manifest.json
├── patches/
├── evidence/
└── logs/repair.log
```

For `ABANDONED`, also create `abandoned_findings.jsonl`. Even when no changes are applied, write a complete report explaining the blocking evidence.

## Completion checks

A repair is complete only when:

- every applied change maps to at least one audit finding;
- before/after hashes are recorded;
- automated changes have regression evidence;
- repair outputs pass `scripts/validate_repair_output.py`;
- the Auditor was re-run or the report explicitly states why re-audit was impossible;
- failed changes were rolled back;
- unresolved and abandoned findings are recorded;
- no hidden answer or solution content was used.

In the user-facing response, state only the outcome, the main repaired or blocking issues, and the location of `benchmark_repair/`. The on-disk report is authoritative.
