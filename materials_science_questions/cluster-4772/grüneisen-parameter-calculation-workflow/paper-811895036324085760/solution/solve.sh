#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
OUTDIR=/app/outputs
mkdir -p $OUTDIR

# === solve block: disorder_model_numbers.json ===
cat > "$OUTDIR/disorder_model_numbers.json" <<'EEOF'
{
  "beta_thermal_expansion": 0.94,
  "beta_lambda_point": [0.52, 0.64, 0.82, 1.08, 1.43, 1.35],
  "gamma_compressibility": 0.63,
  "Cv_l_ratio": 0.2
}
EEOF
