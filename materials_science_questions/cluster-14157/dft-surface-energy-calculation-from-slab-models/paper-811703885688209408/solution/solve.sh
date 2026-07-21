#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: doping_calibration.csv ===
cat > "${OUTDIR}/doping_calibration.csv" <<'FFEOF'
density (electrons/cm^2),fermi_shift (eV)
0.0,0.0
1.0e13,0.06
3.2e13,0.20
5.5e13,0.35
8.0e13,0.49
FFEOF
