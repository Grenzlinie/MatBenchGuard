# Dual-lane paper-grounded audit

Materials Review has one default path:

1. **Deterministic lane** — static D1–D6 contract checks and schema-derived
   checker probes (`malformed` / `full` / `partial` / `all_wrong`).
2. **Agent lane** — materials qualification, taxonomy, and paper-grounded A2 /
   A4 / A5 fidelity judgments with package quotes.

Paper is always in scope for A2/A4/A5 unless `materials_qualification` has
already established `NON_MAT`. Paper reading has no fallback switch and no two-stage parent binding.

## Reproduction intent

Classify as one of:

- `EXACT_REPRODUCTION`
- `METHOD_REIMPLEMENTATION` (default)
- `SCIENTIFIC_EXTENSION`

Never default to EXACT. Equivalent software, versions, and solver-selected
convergence parameters are allowed unless the instruction fixes them or the
checker secretly depends on them.

## A5 Gold credibility checklist

Against the paper, record whether Gold appears to come from experiment, expert
curation, paper text/supplement, a tool output, figure digitization, or another
source; whether measurement uncertainty is acknowledged; whether Gold is
independent of the evaluated method; and whether tolerances have scientific
basis.

## Run outputs

Persist audit evidence in the main-Agent-created run under
`.review_records/<cluster>/<theme>/<paper>/runs/<run-id>/audit/`. Never write
audit artifacts inside the Harbor package. A0 is the run's single content root
for the frozen snapshot and audit evidence.
