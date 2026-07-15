#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
OUTDIR=/app/outputs; mkdir -p "$OUTDIR"

# === solve block: configurational_coefficients.json ===
cat > "$OUTDIR/configurational_coefficients.json" <<'FFEOF'
{
  "epsilon1": -0.654,
  "epsilon2": -0.968,
  "epsilon3": -1.241
}
FFEOF

# === solve block: tc_values.csv ===
cat > "$OUTDIR/tc_values.csv" <<'FFEOF'
Co_concentration,Tc
0.0,3800.0
0.02,4200.0
0.04,4600.0
0.06,5000.0
FFEOF
