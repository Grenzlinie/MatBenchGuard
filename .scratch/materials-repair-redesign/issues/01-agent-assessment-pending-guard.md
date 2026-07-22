# 01 — Pre-Review paper Agent assessment guard

**What to build:** A Review run for a materials Harbor package cannot freeze A0, write a formal audit bundle, enter Repair, or update corpus tracking until a validated paper-grounded Agent assessment is present. Missing or invalid assessment pauses the same run as `AGENT_ASSESSMENT_PENDING`; supplying it resumes at `REVIEWING` without a new assignment. Equal-depth re-audit must inherit that validated assessment through the restricted internal Review context — no silent deterministic-only fallback. Known legacy incomplete audits migrate idempotently to the pending state while preserving diagnostics and tracking.

**Blocked by:** None — can start immediately.

**Status:** implemented (ticket 01)

**Parent:** `handoff.md` (Materials Repair Redesign)

- [x] Run lifecycle includes `ASSIGNED → AGENT_ASSESSMENT_PENDING → REVIEWING → REVIEWED` (and keeps `AGENT_CONTRACT_PENDING` as a separate later overlay).
- [x] Without a valid paper Agent assessment (except Agent-authoritative `NON_MAT` fast reject): no A0, no formal audit, no Repair route, no tracking update.
- [x] After a valid assessment is supplied, the same run completes dual-lane Review.
- [x] Internal re-audit requires the inherited paper assessment; absence/invalid/stale/mismatched binding pauses as assessment-pending and does not consume a semantic attempt.
- [x] Legacy `NOT_SUPPLIED` audits migrate idempotently to `AGENT_ASSESSMENT_PENDING` with an inventory/fixture for the known affected runs; diagnostics preserved; tracking untouched.
- [x] Batch finalization cannot record either pending state as a completed corpus outcome.
- [x] Focused Review tests cover pending → resume and re-audit inheritance; Harbor packages remain free of generated audit artifacts.
