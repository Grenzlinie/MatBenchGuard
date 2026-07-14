# Repair Output Schema

## Required directory

Write to `<benchmark_root>/benchmark_repair/`. Archive prior results under `benchmark_repair_history/<repair_id>/`.

## repair_summary.md headings

Use exactly:

1. `# Benchmark Repair Report`
2. `## 1. Repair Summary`
3. `## 2. Input Audit`
4. `## 3. Repair Configuration`
5. `## 4. Findings Selected`
6. `## 5. Applied Changes`
7. `## 6. Abandoned or Unrepairable Findings`
8. `## 7. Regression Test Results`
9. `## 8. Re-audit Comparison`
10. `## 9. Unresolved Findings`
11. `## 10. Rollback Status`
12. `## 11. Scope and Limitations`
13. `## 12. Repair Log Summary`

## repair_report.json minimum fields

```json
{
  "schema_version": "1.0",
  "repair_id": "string",
  "parent_audit_id": "string",
  "benchmark": {"name": "string", "root": "string"},
  "configuration": {"mode": "PLAN_ONLY|SAFE_AUTO_FIX|ASSISTED_FIX"},
  "summary": {
    "repair_status": "REPAIRED|PARTIALLY_REPAIRED|ABANDONED|ROLLED_BACK",
    "before_verdict": "string",
    "after_verdict": "string|null",
    "publishable": false,
    "core_reason": "string",
    "rolled_back": false
  },
  "selected_findings": [],
  "resolved_findings": [],
  "unresolved_findings": [],
  "blocking_findings": [],
  "changes": [],
  "regression_tests": [],
  "re_audit": {},
  "scope": {"limitations": [], "assumptions": []}
}
```

## changes.jsonl

Each line must contain `change_id`, `finding_ids`, `path`, `change_type`, `reason`, `before_hash`, `after_hash`, `tests`, and `status`.

Allowed statuses: `PROPOSED`, `APPLIED`, `REVERTED`, `REJECTED`, `REQUIRES_REVIEW`.

## regression_tests.json

Record test ID, linked finding IDs, command, expected behavior, observed behavior, exit code, pass/fail status, and evidence path.

## repair_manifest.json

Record repair ID, parent audit ID, timestamps, repairer version, input hashes, changed-file hashes, output hashes, and rollback state. Do not include secrets.
