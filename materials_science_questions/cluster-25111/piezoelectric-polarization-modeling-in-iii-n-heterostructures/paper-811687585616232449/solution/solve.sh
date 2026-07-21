#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: corrected_delta_EV.csv ===
cat > "$OUTDIR/corrected_delta_EV.csv" <<'FFEOF'
In_molar_fraction,delta_EV
0.17,0.2
0.25,0.1
0.30,0.0
FFEOF
