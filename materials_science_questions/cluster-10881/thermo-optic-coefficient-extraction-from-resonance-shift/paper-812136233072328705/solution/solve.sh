#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: reproduced_tolerances.json ===
# Write the reference values directly to the required output file
cat > "$OUTDIR/reproduced_tolerances.json" <<'FFEOF'
{
  "ref_lambda_p0": 1065.0,
  "dlambda_dGaAs": 5.2,
  "dlambda_dAlox": -3.5,
  "dlambda_dT": 0.133
}
FFEOF

# === solve finalize ===
echo 'Oracle solve.sh finished writing artifacts.'
