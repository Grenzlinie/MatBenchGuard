#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: stress_predictions.csv ===
cat > /app/outputs/stress_predictions.csv <<'FFEOF'
tensile_axis,sigma_y,sigma_f
A,400,420
B,120,145
C,115,130
D,145,180
N,420,650
FFEOF
