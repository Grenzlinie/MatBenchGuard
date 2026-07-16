# External review/repair assignment lock

This is a small, stdlib-only orchestration CLI for parent agents that dispatch
the Harbor 题包 review and repair workflows. It does not change the Review or
Repair skill behavior, package contents, scoring, or issue state. Worker
subagents receive one claimed package but must not edit the registry; only the
parent agent claims, heartbeats, completes, releases, or abandons work. This
registry coordinates cooperating parent sessions. It is not a hostile security
boundary, so repository access controls must still protect its credentials.

The default registry is `assign_review_tasks/assignment_lock.json`, resolved
from this script's location. Every command also accepts `--registry PATH`.
The persistent sibling guard is `PATH.lock`; JSON updates are locked and
written through an fsynced temporary file plus atomic replace.

## Claim the next packages

Review candidates in manifest order:

```sh
python assign_review_tasks/assign.py claim-next \
  --manifest future_candidates/manifest.json \
  --operation REVIEW --owner review-parent-01 --count 5
```

Review candidates in a corpus in canonical lexical order:

```sh
python assign_review_tasks/assign.py claim-next \
  --corpus materials_science_questions \
  --operation REVIEW --owner review-parent-01 --count 5
```

The committed whitelist's 100 packages are historical maintainer-accepted
seeds. They are `ACCEPTED`, are intentionally non-assignable, and therefore
produce no claims if used as `claim-next` candidates.

The JSON response contains parent-only claim credentials. The parent retains
`owner` and `token` and uses them for every heartbeat or settlement. Give each
worker only its package identity, operation, source path, and task instructions:

```text
package_id: cluster-123/theme-name/paper-456
operation: REVIEW
source_path: materials_science_questions/cluster-123/theme-name/paper-456
task_instructions: Run the repository Review workflow for this one Harbor package.
```

For a single package:

```sh
python assign_review_tasks/assign.py claim \
  --package-id cluster-123/theme-name/paper-456 \
  --operation REVIEW --owner review-parent-01 --lease-seconds 3600
```

`REPAIR` can only claim a package whose review completed as
`CONDITIONAL` (`REVIEWED_CONDITIONAL`):

```sh
python assign_review_tasks/assign.py claim \
  --package-id cluster-123/theme-name/paper-456 \
  --operation REPAIR --owner repair-parent-01 --lease-seconds 3600
```

## Keep or settle a claim

The parent uses the exact `owner` and `token` returned by `claim` or
`claim-next`; it never passes either credential to the worker:

```sh
python assign_review_tasks/assign.py heartbeat \
  --package-id cluster-123/theme-name/paper-456 \
  --owner review-parent-01 --token "$TOKEN"
```

Review completion outcomes are `PASS`, `CONDITIONAL`, `REJECT`, and
`NOT_ASSESSABLE`:

```sh
python assign_review_tasks/assign.py complete \
  --package-id cluster-123/theme-name/paper-456 \
  --owner review-parent-01 --token "$TOKEN" --outcome PASS
```

Repair completion accepts `PASS` only and returns the package to `ACCEPTED`.
Publication is a separate lifecycle and is not represented by this registry:

```sh
python assign_review_tasks/assign.py complete \
  --package-id cluster-123/theme-name/paper-456 \
  --owner repair-parent-01 --token "$TOKEN" --outcome PASS
```

Release returns the package to the state it had before the claim:

```sh
python assign_review_tasks/assign.py release \
  --package-id cluster-123/theme-name/paper-456 \
  --owner review-parent-01 --token "$TOKEN" --reason "worker stopped cleanly"
```

Abandoning is terminal and is valid only for an active `REPAIR`. An active
`REVIEW` must be completed with its appropriate review outcome or released:

```sh
python assign_review_tasks/assign.py abandon \
  --package-id cluster-123/theme-name/paper-456 \
  --owner repair-parent-01 --token "$TOKEN" \
  --reason "repair evidence cannot support a safe patch"
```

## Stale claims and recovery

An expired lease is not silently stolen. A parent must explicitly reclaim it;
the CLI records an `EXPIRED` history event before making the new claim:

```sh
python assign_review_tasks/assign.py claim \
  --package-id cluster-123/theme-name/paper-456 \
  --operation REVIEW --owner recovery-parent \
  --lease-seconds 3600 --reclaim-expired
```

For deterministic batch recovery in candidate order:

```sh
python assign_review_tasks/assign.py claim-next \
  --manifest future_candidates/manifest.json \
  --operation REVIEW --owner recovery-parent --count 5 --reclaim-expired
```

Without `--reclaim-expired`, `claim-next` skips expired active claims. Direct
`claim` never invents a missing registry entry; only `claim-next` may add a new
identity after reading it from a real, non-symlink corpus or manifest.

If a parent or worker stops unexpectedly, another parent should first run
`list`/`validate`, heartbeat any still-owned live claims, and explicitly
reclaim expired claims. After all workers stop, the parent must settle every
claim with `complete`, `release`, or `abandon`; never dispatch an unclaimed,
foreign-claimed, or completed package.

```sh
python assign_review_tasks/assign.py list
python assign_review_tasks/assign.py validate
```

Terminal states (`ACCEPTED`, `REVIEWED_REJECT`,
`REVIEWED_NOT_ASSESSABLE`, and `ABANDONED`) have no CLI force bypass. Manual
registry policy changes must be deliberate and followed by `validate`.
