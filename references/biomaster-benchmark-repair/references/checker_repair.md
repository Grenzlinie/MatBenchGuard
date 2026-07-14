# Checker Repair

## Required properties

A repaired checker must:

- read every declared core artifact;
- fail safely on missing, empty, malformed, oversized, or unsafe files;
- reject NaN, Inf, duplicate conflicts, and invalid identifiers;
- avoid executing submitted code or unsafe deserialization;
- score semantic content rather than incidental ordering or metadata;
- produce low scores for random, constant, minimal, and coverage attacks;
- produce high scores for a valid public fixture;
- be approximately monotonic as answer quality improves;
- distinguish checker errors from scientific mismatch.

## Test set

Include tests for missing output, empty output, malformed format, random baseline, constant baseline, duplicate conflicts, NaN/Inf, minimal exploit, omitted core artifact, threshold boundaries, quality gradients, and metamorphic equivalents.

## Multiple valid answers

Use tolerance, set overlap, ranking metrics, evidence validation, or invariant-based checks according to the task type. Do not compare serialized files byte-for-byte when multiple representations are scientifically equivalent.
