#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
OUTDIR=/app/outputs
mkdir -p $OUTDIR

# === solve block: step_01_gamma_c.json ===
cat > $OUTDIR/step_01_gamma_c.json <<'FFEOF'
{
  "gamma_c": 0.42
}
FFEOF

# === solve block: step_02_thermo_ratios.json ===
cat > $OUTDIR/step_02_thermo_ratios.json <<'FFEOF'
{
  "R_delta": 3.37,
  "R_C": 2.4,
  "R_H": 0.227
}
FFEOF
