# 04 — Direct deterministic publication path

**What to build:** When every operation is narrowly `DIRECT_DETERMINISTIC` — all D1–D6 machine findings, all `AUTO_FIX`, `core_science_change=false`, unique source-bound wiring restoration, mutation allowlist only, no Agent-quality / checker-robustness / paper-grounded instruction / direct-input repairs — Repair may atomically publish after fail-before/pass-after regressions and candidate validation, without invoking equal-depth Review. Record `verification_mode: DIRECT_DETERMINISTIC` and the regression evidence. Any other candidate still requires re-audit; a local regression pass alone never publishes semantic or Agent-lane changes. Direct publish does not consume the two-attempt re-audit budget.

**Blocked by:** 03 — Agent repair assessment and lane-aware plan v2

**Status:** done

**Parent:** `handoff.md` (Materials Repair Redesign)

- [x] Preflight enforces the full narrow eligibility matrix; mixed or non-eligible batches take the re-audit route.
- [x] Eligible D-only unique `AUTO_FIX` publishes after regressions with no Review re-audit invocation.
- [x] Any `ASSISTED_FIX`, Agent finding, checker robustness/semantics fix, paper-grounded instruction change, or indispensable direct-input repair still runs exactly one equal-depth re-audit.
- [x] Direct publication fails closed on stale source audit, package identity drift, mutation outside allowlist, failed regression, malformed plan, or failed atomic swap; original package preserved.
- [x] Re-audit publication keeps PASS / score≥80 / CLEAN / Hard-Gate / severity / two-attempt rules.
- [x] Negative and positive tests cover both routes; Harbor packages never receive generated repair artifacts.
