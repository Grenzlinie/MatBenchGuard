# 06 — Integrate, full suite, and assigned-package smoke

**What to build:** After tickets 01–05 land, the materials Review/Repair suites pass as one integrated system, and one explicitly assigned Harbor package is exercised end-to-end. Inspect the external run bundle for the new assessment/plan/publication/bundle contracts; confirm the Harbor package contains only allowed source mutations (instruction/tests/solution) and no generated audit or repair artifacts. Only then is the redesign ready for broader assigned-batch use.

**Blocked by:** 04 — Direct deterministic publication path; 05 — Canonical run-local repair bundle and history

**Status:** done (suites green; live Review→Repair smoke skipped — see notes)

**Parent:** `handoff.md` (Materials Repair Redesign)

- [x] Full acceptance matrix from the handoff is green (Agent queue routing; assessment/plan fail-closed cases; `ASSISTED_FIX` evidence rules; direct vs re-audit routes; atomic fail-closed; re-audit PASS/80/CLEAN/two-attempt; bundle tree + hashes; no package-local generated artifacts; assessment-pending lifecycle; repair rejects incomplete source audits / inherits paper assessment on re-audit).
  - Covered by the focused + ticket-specific suites below (118 tests, all OK). No remaining suite failures.
- [x] Focused then full suite passes:
  - `tests.test_materials_batch_repair`
  - `tests.test_materials_safe_repair`
  - `tests.test_materials_assisted_repair`
  - `tests.test_materials_benchmark_review_core`
  - `tests.test_materials_benchmark_review_dual_lane`
  - Plus ticket-specific: `test_materials_agent_assessment_pending`, `test_materials_agent_quality_repair_queue`, `test_materials_agent_repair_assessment`, `test_materials_direct_deterministic_publication`
  - Result (2026-07-22): **Ran 118 tests in 276.436s — OK**
- [ ] One real assigned package run completes through Review → Repair (direct or re-audit as eligible) with a valid run-local `benchmark_repair` bundle.
  - **Skipped:** All 10 ledger-assigned runs are already `REVIEWED` with `repair_decision=NOT_REQUIRED` / `repair_status=NOT_APPLICABLE` / `review_verdict=NOT_ASSESSABLE` (`EVIDENCE_PENDING`). None have `plan.json` or `agent_repair_assessment.json`. Forcing Repair would be a no-op or fail-closed ingress, not a meaningful end-to-end smoke; creating a fresh assignment + paper assessment + dual-lane Review to manufacture a repairable case would mutate real Harbor packages and is out of safe smoke scope for this ticket.
- [x] Harbor package post-run contains source changes only; audit/repair outputs remain under `.review_records/.../runs/<run-id>/`.
  - Verified for all 10 assigned packages: no `benchmark_audit` / `benchmark_repair` / tmp repair-audit dirs under Harbor roots. Artifacts stay under `.review_records/.../runs/<run-id>/audit/`.
- [x] Corpus tracking updated only after the assigned run(s) reach a terminal state, per existing main-Agent policy.
  - No tracking update performed (smoke did not reach a new terminal Repair). Tracking remains `pending` across the corpus.

## Integration notes

- No code fixes required for 01–05 co-landing: suites passed as-is.
- No git commit (ticket policy).

## Residual risks / open gaps vs handoff matrix

1. **Live Review→Repair smoke still outstanding** — matrix items 4–8 are proven in unit/integration tests, not on a repair-eligible assigned package.
2. Existing assigned sample batch is evidence-pending / not repairable; broader batch use should start from a package with a complete dual-lane Review that yields a non-empty OPEN repair queue.
3. Docker is available locally, but was not exercised for a new end-to-end Review in this ticket because no repair-eligible assigned target existed.
