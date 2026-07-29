# Repair report schema

Write `repair_report.json` outside the Harbor package using
`materials-agent-repair-report/1.2` and the bundled template. Version 1.1 and
older records must be re-audited or migrated before publication.

Record source and candidate identities, source decision, target findings,
decision per target, evidence, intended and actual paths, before/after hashes,
regression results, patch locations, re-audit decision path/verdict, unresolved
findings, outcome, publishability, and limitations.

Also retain and reference:

- the independent pre-repair fresh-defect pass;
- the cross-file impact matrix for every mutation;
- snapshot and candidate builtin plus task-specific probe observations.

Do not include any `solution/` evidence, self-check status, hashes, paths, or
findings. That directory is outside Repair.

Outcome consistency:

- `REPAIRED` requires re-audit `PASS`, all targets resolved, every regression
  fail-before/pass-after, and `publishable=true`;
- `PARTIALLY_REPAIRED` requires `CONDITIONAL`, unresolved findings, false publish;
- `ABANDONED` requires `REJECT` or explicit evidence-backed abandonment;
- `ROLLED_BACK` requires false publish and preserved source.

`REPAIRED` is legal only after the candidate's full Review decision validates
as `PASS` against the candidate's raw observation files, all fresh findings are
closed, and all affected package files are synchronized. Docker-only behavior
that a local helper cannot reproduce belongs in limitations and must not be
represented as an unresolved package defect without independent container-layout
evidence.

Do not create a repair report for a terminal early-screen `REJECT` whose
controlling Hard Gate/finding disposition is `ABANDON`. That package never
entered Repair; its validated Review decision is the terminal evidence.
`ABANDONED` is reserved for a package that passed the Repair entry gate but
became unsafe or impossible to repair during mutation or equal-depth re-audit.

Automation/control failures are operational evidence and cannot manufacture a
science verdict.
