# Fixed audit output schema

The complete audit must be stored at `<benchmark_root>/benchmark_audit/`. Generate in `<benchmark_root>/.benchmark_audit_tmp/` and finalize atomically.

## Required files

```text
benchmark_audit/
├── audit_report.md
├── audit_report.json
├── findings.jsonl
├── resource_checks.json
├── checker_tests.json
├── audit_manifest.json
├── evidence/
│   ├── static_checks/
│   ├── resource_checks/
│   ├── checker_tests/
│   └── paper_checks/
├── logs/
│   └── audit.log
└── patches/
    └── suggested.patch        # optional
```

## Required Markdown headings

Use these headings in this exact order:

1. `# Benchmark Audit Report`
2. `## 1. Audit Summary`
3. `## 2. Benchmark Identity`
4. `## 3. Audit Configuration`
5. `## 4. Final Verdict`
6. `## 5. Biology Qualification`
7. `## 6. Capability Alignment`
8. `## 7. Gate Results`
9. `## 8. Resource Reachability`
10. `## 9. Instruction and Task Design`
11. `## 10. Checker Assessment`
12. `## 11. Gold Standard Assessment`
13. `## 12. Execution Feasibility`
14. `## 13. Reproducibility and Leakage`
15. `## 14. Paper Consistency`
16. `## 15. Dimension Scores`
17. `## 16. Findings`
18. `## 17. Required Fixes`
19. `## 18. Recommended Improvements`
20. `## 19. Audit Scope and Limitations`
21. `## 20. Audit Log Summary`

If a section was not executed, write `Status: NOT_ASSESSED` and a reason.

## Machine-readable summary

`audit_report.json` must contain:

- `schema_version`
- `audit_id`
- benchmark name, root, input type, and input hash;
- paper mode, execution level, start, and completion time;
- biology class and evidence axes;
- answer type and capability target;
- verdict, weighted score, hard-gate state, and core reason;
- gate results;
- dimension scores;
- resources;
- checker tests;
- findings;
- required fixes and recommendations;
- reviewed and unreviewed scope, tests, limitations, and assumptions.

Allowed verdicts: `PASS`, `CONDITIONAL`, `REJECT`, `NOT_ASSESSABLE`.

Allowed gate states: `PASS`, `FAIL`, `WARNING`, `SKIPPED`, `NOT_ASSESSED`.

Allowed severities: `FATAL`, `HIGH`, `MEDIUM`, `LOW`.

Allowed dimension scores: `1.00`, `0.75`, `0.50`, `0.25`, `0.00`, or `NOT_ASSESSED`.

## Findings JSONL

Each line must contain:

- `finding_id`
- `severity`
- `category`
- `phase`
- `status`
- `title`
- affected files and line ranges;
- observation;
- evidence;
- impact;
- exploit or failure scenario;
- required fix;
- verification after fix;
- confidence;
- judgment type: `FACT` or `INFERENCE`.

Use consecutive IDs such as `FINDING-001`.

## Resource checks

For every declared resource record role, identifier, URLs, required and verified reachability levels, status, identity match, HTTP metadata, checksum, timestamp, environment, attempts, evidence, and failure class.

Allowed statuses include `AVAILABLE`, `PARTIALLY_AVAILABLE`, `TRANSIENT_FAILURE`, `UNAVAILABLE`, `IDENTITY_MISMATCH`, `REQUIRES_AUTH`, and `NOT_TESTED`.

## Checker tests

Record test ID, type, description, expected behavior, observed score or status, exit code, hard-gate effect, and evidence path. Include quality-gradient and monotonicity results when tested.

## Manifest and history

`audit_manifest.json` records schema version, audit ID, parent audit ID when re-auditing, timestamps, auditor version, input hashes, output hashes, resolved findings, and new findings.

Do not hash every large raw-data file. Hash instructions, configurations, resources, checker, grading spec, references, paper, environment files, and all audit outputs.

If `benchmark_audit/` already exists, archive it under `benchmark_audit_history/<previous-audit-id>/` before writing the new audit.

## Completion requirements

The audit is complete only when:

1. `benchmark_audit/` exists in the benchmark root;
2. every required file exists;
3. JSON and JSONL parse;
4. Markdown and JSON agree on verdict, score, biology class, answer type, gate states, and finding counts;
5. all referenced evidence paths exist;
6. output hashes validate;
7. skipped phases and reasons are recorded;
8. the final verdict is explicit.
