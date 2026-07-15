#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: step_01_properties.csv ===
cat > "$OUTDIR/step_01_properties.csv" <<'CSVEOF'
geometry,ZT_max,sigma_ph_300K,band_gap
monolayer,0.91,1.0,1.69
zigzag_10_0,0.47,0.5,0.36
armchair_6_6,0.33,1.5,0.24
CSVEOF
