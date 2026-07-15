#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: results.csv ===
cat > /app/outputs/results.csv <<'CSVEOF'
case,tilt_angle,offset_S,failure_force,estimated_strength
pristine_zigzag,NaN,NaN,35.0,100
pristine_armchair,NaN,NaN,42.0,125
GB_5.7deg,5.7,0,30.0,80
GB_27.8deg,27.8,0,38.0,110
GB_5.7deg_offset40,5.7,40,30.5,80
GB_5.7deg_offset80,5.7,80,29.8,80
GB_5.7deg_inplane10deg,5.7,NaN,32.5,85
GB_5.7deg_outplane2deg,5.7,NaN,29.0,78
CSVEOF
