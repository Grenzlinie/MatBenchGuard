# Checker audit

Map every final core scientific output through checker read, scorer binding,
positive effective weight, finite contribution, and final reward. Ignore
recommended methods, process-only artifacts, traces, training logs, and
intermediates; the checker need not read or authenticate them.

Record these probe classes as `PASS`, `FAIL`, `NOT_APPLICABLE`, or
`NOT_ASSESSABLE`:

- `valid_positive`;
- `missing_output`;
- `empty_output`;
- `malformed_output`;
- `random_or_constant`;
- `duplicate_records`;
- `non_finite_values`;
- `minimal_exploit`;
- `quality_gradient`;
- `semantic_equivalence`;
- `component_isolation`.

Use task-specific attacks for tables, structures, trajectories, images,
rankings, scalar values, models, or other outputs. Test boundary tolerances and
partial correctness when meaningful.

A result is usable only when execution completes, reward is finite, breakdown
is parseable, and checker errors are absent. Mark irrelevant probes
`NOT_APPLICABLE` with a rationale. Criteria 2.4/2.5 cannot pass when an
applicable core probe fails or is unassessed.

Non-finite values, wrong types, missing fields, duplicate identifiers, invalid
formats, and unsafe parsing are checker defects eligible for `AUTO_FIX`; they
are not by themselves grounds for abandonment. Fatal examples are limited to
cases where the final core result cannot be fairly assessed without redefining
the public contract, such as random/minimal final output passing, an ignored
final core output, reversed score direction, non-monotonic final-result quality,
correct-result rejection, or materially different treatment of scientifically
equivalent final results.

Audit paths using the package's declared container layout. A host path mismatch,
failed local path rewrite, or helper that does not support the container layout
is `AUTOMATION_LIMITATION`, not a package defect, unless direct evidence shows
the declared in-container path, mount, or layout is invalid.
