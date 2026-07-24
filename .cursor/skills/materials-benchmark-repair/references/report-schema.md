# Repair report schema

Write `repair_report.json` outside the Harbor package using
`materials-agent-repair-report/1.0` and the bundled template.

Record source and candidate identities, source decision, target findings,
decision per target, evidence, intended and actual paths, before/after hashes,
regression results, patch locations, re-audit decision path/verdict, unresolved
findings, outcome, publishability, and limitations.

Outcome consistency:

- `REPAIRED` requires re-audit `PASS`, all targets resolved, every regression
  fail-before/pass-after, and `publishable=true`;
- `PARTIALLY_REPAIRED` requires `CONDITIONAL`, unresolved findings, false publish;
- `ABANDONED` requires `REJECT` or explicit evidence-backed abandonment;
- `ROLLED_BACK` requires false publish and preserved source.

`REPAIRED` is legal only after the candidate's full Review decision validates
as `PASS`. Docker-only behavior that a local helper cannot reproduce belongs in
limitations and must not be represented as an unresolved package defect without
independent container-layout evidence.

Automation/control failures are operational evidence and cannot manufacture a
science verdict.
