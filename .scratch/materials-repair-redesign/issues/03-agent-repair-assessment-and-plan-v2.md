# 03 — Agent repair assessment and lane-aware plan v2

**What to build:** Repair only accepts a complete dual-lane `REVIEWED` source audit that binds a validated paper Agent assessment. Before any candidate mutation, an Agent-authored `agent_repair_assessment` binds every OPEN queue finding (D and Agent-quality) with decision, scope, evidence, and approved operations. A new executable plan schema (v2) binds the full cross-lane queue, assessment hash, and per-operation `publication_class` (`DIRECT_DETERMINISTIC` | `REAUDIT_REQUIRED`). Plans that omit Agent findings, lack/stale assessment bindings, or use unapproved operations fail closed. In this slice, every executable candidate still goes through equal-depth re-audit (direct publish is not enabled yet).

**Blocked by:** 02 — Dual-lane repair queue with Agent-quality findings

**Status:** done

**Parent:** `handoff.md` (Materials Repair Redesign)

Schema shape retained from handoff (decision-rich, not a demo):

```json
{
  "schema_version": "materials-agent-repair-assessment/1.0",
  "findings": [
    {
      "finding_id": "...",
      "lane": "deterministic_core | agent_quality",
      "decision": "AUTO_FIX | ASSISTED_FIX | ABANDON",
      "agent_verdict": "APPROVE_REPAIR | BLOCKED_EVIDENCE | ABANDON",
      "repair_scope": "...",
      "core_science_change": false,
      "approved_operation_ids": ["op-..."]
    }
  ]
}
```

- [x] Source audits without a validated paper assessment are rejected (or migrated per ticket 01); plan fields cannot replace the assessment.
- [x] Assessment binds the complete OPEN queue; omission is fail-closed.
- [x] `AUTO_FIX` remains unique source-bound D wiring only; Agent cannot suppress machine `FAIL` or invent science claims from unavailable evidence.
- [x] `ASSISTED_FIX` is available for both lanes when type-matched evidence is bound; otherwise `BLOCKED_EVIDENCE` / `ABANDON` with no mutation.
- [x] Executable plan schema is v2; prior 1.0 is archival-only and cannot enter execution.
- [x] Each operation declares `publication_class`; lane-aware policy replaces D-only boundary checks while preserving no-leak / evidence rules.
- [x] All executable candidates in this slice still require exactly one equal-depth re-audit that inherits the paper assessment.
- [x] Tests: refuse omitted Agent finding / missing assessment / stale hashes / unapproved ops; D finding may take evidence-bound `ASSISTED_FIX`; unsupported science changes block or abandon.
