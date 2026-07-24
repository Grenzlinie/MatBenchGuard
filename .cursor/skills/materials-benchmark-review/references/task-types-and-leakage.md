# Task types and leakage

Determine whether the answer is exact, tolerance-based, set-valued,
ranking-based, evidence-based, or open-ended. The checker equivalence rule must
fit the answer type; do not force multiple valid scientific answers into one
exact serialization.

Leakage is assessed ONLY on `instruction.md` — the sole file the solver
receives. `paper/**`, `solution/**`, `tests/**`, `resources.json`, and
`metadata` are reviewer/harness-side or human-reference only, so answers, hidden
thresholds, or tolerances present there are by design, never leakage. A gameable
checker is a 2.5/C04 checker-quality defect, not a leakage finding.

Within that surface, check numeric-result leakage, hidden thresholds, Gold
fragments, filenames, public fixtures, comments, logs, and paper identity clues.
Formula and method descriptions are allowed. Identity is leakage when it enables
lookup of the answer and bypasses the intended scientific work.

Also inspect split leakage, duplicated samples, target-derived features,
pseudoreplication, and Gold generated from the evaluated prediction itself.
