---
name: materials-benchmark-repair
description: Repair one audited materials-science Harbor 题包 through a fresh, isolated, tested, equal-depth, atomic workflow. Use only after materials-benchmark-review routes a package to REPAIR_QUEUE.
---

# Materials Benchmark Repair

Repair one Harbor 题包 at a time. Review remains evidence-only for core package
roles; this skill owns all mutations.

## SAFE_AUTO_FIX

Prepare a JSON plan outside the 题包 with:

- `schema_version: "0.1"`;
- the authoritative `audit_id` and one open `finding_id`;
- `repair_class: "SAFE_AUTO_FIX"` and a justification;
- exactly one deterministic `json_set` operation that adds exact public
  `access.evidence` to a declared resource in `resources.json`;
- one or more `json_path_equals` regression tests that fail before and pass
  after the operation.

Run:

```bash
python scripts/run_repair.py <Harbor题包目录> --plan <repair-plan.json>
```

The runner rejects stale audit hashes before creating a workspace. It then
copies the complete package into a full snapshot and separate candidate under
`.benchmark_repair_tmp/<repair_id>/`, applies the operation only to the
candidate, records before/after hashes, proves the regression transition, and
reruns Review at the original paper mode and execution level.

Publication requires a `PASS`, resolution of the target finding, and successful
path rebasing. The candidate then atomically replaces the original directory;
both the pre-change snapshot and original package move to
`.benchmark_repair_history/<repair_id>/`. A failed swap restores the original.

## Completion

The repair is complete only when:

- `benchmark_repair/repair_manifest.json` says `PUBLISHED`;
- every change links the source finding and has different before/after hashes;
- every regression is false before and true after;
- re-audit uses equal evidence depth and routes to `PUBLISH_CANDIDATE`;
- the package identity and full `solution/` role remain present;
- the history contains full `snapshot/` and `original/` directories.

Do not infer that arbitrary scientific, Gold, checker, or scoring changes are
safe. Those require an assisted workflow.
