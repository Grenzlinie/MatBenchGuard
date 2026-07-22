# 02 — Dual-lane repair queue with Agent-quality findings

**What to build:** Review’s complete OPEN repair queue includes both machine D1–D6 findings and repairable Agent-quality / A-lane findings as first-class entries. Agent findings keep `lane: agent_quality` (never a fabricated D check), carry stable finding IDs, severity, C01–C07 ownership, repairability, evidence refs, and `repair_lane` / `repair_scope`. When D1–D6 is CLEAN but a repairable Agent finding remains OPEN, finalization still routes to `REPAIR_QUEUE`. Hard Gates, unrepairable Agent findings, and evidence gaps keep their existing non-Repair routes. `AGENT_CONTRACT_PENDING` stays the narrow unavailable-machine-contract overlay only.

**Blocked by:** 01 — Pre-Review paper Agent assessment guard

**Status:** done

**Parent:** `handoff.md` (Materials Repair Redesign)

- [x] Normalized `repair_findings` appear on the Agent quality assessment and source audit report, CLI-validated for taxonomy, exact citations, source hashes, package path safety, and C-dimension mapping.
- [x] Allowed scopes distinguish at least: `DETERMINISTIC_WIRING`, `CHECKER_ROBUSTNESS`, `INSTRUCTION_CONTRACT`, `SCORING_SEMANTICS`, `DIRECT_INPUT_REFERENCE`, `SCIENCE_SEMANTICS`.
- [x] A repairable Agent checker-fairness finding with exact citations routes to `REPAIR_QUEUE` even when D1–D6 is CLEAN.
- [x] Machine D1–D6 statuses, evidence, and source bindings remain authoritative and unchanged by Agent-quality queue entries.
- [x] Skill/docs describe repairable Agent findings and which classes later require re-audit vs direct deterministic publication.
- [x] Fixtures and dual-lane Review tests cover queue emission and routing; no package-local generated audit artifacts.
