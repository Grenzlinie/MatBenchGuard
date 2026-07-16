---
name: materials-benchmark-repair
description: Repair one audited materials-science Harbor 题包 through a fresh, isolated, tested, equal-depth, atomic workflow. Use only after materials-benchmark-review routes a package to REPAIR_QUEUE.
---

# Materials Benchmark Repair

Repair one Harbor 题包 at a time after Review routes it to `REPAIR_QUEUE`.
Review supplies evidence and owns no mutations. The Agent writes an external,
evidence-backed plan; Repair validates and executes it without per-fix human
approval.

## Public seam

Keep the plan outside the 题包 and run:

```sh
python scripts/run_repair.py <Harbor题包目录> --plan <repair-plan.json>
```

The plan uses schema `0.1` and contains:

```json
{
  "schema_version": "0.1",
  "audit_id": "authoritative audit id",
  "finding_id": "one open finding id",
  "repair_class": "AUTO_FIX, ASSISTED_FIX, or ABANDON",
  "justification": "why this repair resolves the finding",
  "core_science_change": false,
  "evidence": [
    {
      "id": "stable-evidence-id",
      "source": "paper/paper.md, authoritative finding, DOI, or other source",
      "quote": "verifiable supporting text"
    }
  ],
  "operations": [],
  "regression_tests": []
}
```

There is no human approval state. The closed decision classes are autonomous:

- `AUTO_FIX` is deterministic and does not require scientific
  interpretation.
- `ASSISTED_FIX` may make an evidence-backed scientific or checker correction.
  Every operation must link one or more plan evidence IDs.
- `ABANDON` stops immediately when evidence is insufficient or the repair would
  redefine the core scientific contract. It has no operations.

## Allowed changes

Only these package roles are modifiable:

- `instruction.md`
- `tests/**`
- `solution/**`

`paper/**` and every metadata/environment role are read-only. The runner
supports deterministic `write_file`, `replace_text`, `json_set`, and
`delete_file` operations. `write_file` may create a missing
`solution/solve.sh`, including its executable bit. Thus a missing or broken
solution entrypoint is a repairable integrity finding, not an automatic
rejection.

Use regressions that directly prove the finding was fixed. Supported checks
are `file_exists`, `file_absent`, `file_executable`, `text_contains`,
`text_not_contains`, `json_path_equals`, and argv-based `command`. A regression
is expected to fail before and pass after unless it explicitly declares
`expected_before` or `expected_after`.

## Non-negotiable scientific policy

Never:

- guess a scientific parameter or value;
- use `solution/**` as evidence for public instruction text or copy hidden
  solution content into `instruction.md`;
- lower a checker or scoring threshold without linked evidence;
- redefine the core scientific question, endpoint, material system, or claimed
  reproduction type;
- treat a passing checker alone as scientific evidence.

When evidence is absent or not linked to an operation, return
`BLOCKED_EVIDENCE` with decision `ABANDON` without mutating the package. When a
plan declares or attempts a forbidden change, return `POLICY_VIOLATION`. Do not
convert either state into an approval request and do not improvise a replacement
value.

## Isolated execution and publication

Before mutation, reject stale audit hashes, require a complete source-audit
binding, freeze the core-contract digest, and verify that the selected finding
is still open. Then:

1. Copy the full package to both
   `.benchmark_repair_tmp/<repair_id>/snapshot/` and `candidate/`.
2. Run required regressions against the snapshot.
3. Apply only the planned operations to the candidate, recording before/after
   hashes and evidence links.
4. Run the regressions against the candidate.
5. Run the canonical Review CLI at the source audit's paper mode and fixed E1
   execution level. External fixtures and assessments must match the hashes
   bound by the source audit.
6. Require `PASS`, `PUBLISH_CANDIDATE`, resolution of the target finding,
   unchanged package identity, and no mutation outside the three allowed roles.
7. Write the fixed repair bundle (`repair_plan.json`, `changes.json`,
   `unresolved.json`, `regression_results.json`, `re_audit_comparison.json`,
   `patch.json`, `evidence.json`, `repair.log`, and `history.json`) plus the
   manifests/reports, rebase generated Review paths, and atomically replace the
   authoritative package.

Successful history contains the full `snapshot/`, the full pre-publication
`original/`, `repair_plan.json`, and `attempt_manifest.json`. If the swap fails,
restore the original package.

## Attempt limit

A failed mutation, regression, or equal-depth re-audit leaves the authoritative
package untouched and archives the full snapshot and candidate. The first
failed attempt is `ROLLED_BACK`; the second failure for the same source
`audit_id` plus `finding_id` is `ABANDONED`. Later calls return the existing
`ABANDONED` state and never create a third candidate.

## Completion

A repair is complete only when the package-local manifest says `PUBLISHED`,
all required regressions have their declared before/after results, the
equal-depth Review routes to `PUBLISH_CANDIDATE`, package identity is
preserved, and the complete history exists.
