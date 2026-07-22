# 05 — Canonical run-local repair bundle and history

**What to build:** Every terminal Repair attempt (direct, partial, abandoned, rollback, re-audited repaired) emits the human-readable `benchmark_repair` bundle under the run’s repair output path — never inside the Harbor package — with JSONL change/unresolved streams, patches/evidence/logs directories, hashed manifest, and archived history per repair ID. Direct-deterministic attempts use the same comparison schema with `reaudit_performed: false` and an explicit reason. Legacy canonical file names are no longer deliverables.

**Blocked by:** 03 — Agent repair assessment and lane-aware plan v2

**Status:** done

**Parent:** `handoff.md` (Materials Repair Redesign)

Required public tree (run-local only):

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

History: `repair/benchmark_repair_history/<repair_id>/`

- [x] Writers/manifest constants emit exactly the new tree; legacy `changes.json`, `patch.json`, `repair.log`, and `history.json` are not canonical deliverables.
- [x] Manifest hashes every bundle member and binds A0, source audit, assessment, publication record, and history link.
- [x] Terminal direct, partial, abandoned, rollback, and re-audited repaired attempts each produce a validating bundle; JSONL and hashes verify.
- [x] Every integration test asserts no generated repair artifact under the Harbor package.
- [x] Skill/docs describe the run-local layout and that Harbor packages stay clean.
- [x] `.gitignore` / run-context helpers updated only if new run-local paths need exclusion; corpus tracking unchanged until a real run goes terminal.
