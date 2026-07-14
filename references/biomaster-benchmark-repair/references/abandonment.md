# Abandonment and Rollback

## Immediate abandonment

Abandon without attempting a scientific patch when core public data are irrecoverable, authorization is unavailable, Gold provenance is unverifiable, the public task is underdetermined, or repair would require inventing the biological definition.

## Abandon after attempts

Allow one primary fix and one targeted correction for the same root cause. If the relevant audit Gate still fails, restore the pre-repair benchmark and mark `ABANDONED`.

## Required abandonment record

Record:

- blocking finding IDs;
- evidence;
- attempts made;
- why further repair would be speculative or invalid;
- whether all changes were rolled back;
- `publishable: false`;
- recommended disposition, normally exclusion from the benchmark suite.

## Partial repair

Use `PARTIALLY_REPAIRED` only when no FATAL remains and the package is clearly marked as not fully release-ready. Do not use partial status to retain a fundamentally broken task.
