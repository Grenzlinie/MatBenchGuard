#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: results_table.csv ===
cat > "$OUTDIR/results_table.csv" <<'CSVEOF'
system,E_ads,E_g,charge_transfer
isomer1_CO_A,-0.265,0.703,0.168
isomer1_CO_B,-0.138,0.677,-0.088
isomer1_NO_A,-0.721,0.306,-0.546
isomer1_NO_B,-0.666,0.253,-0.087
isomer1_NO_C,-0.447,0.332,-0.606
isomer1_HCN_A,-0.854,0.587,-0.189
isomer1_HCN_B,-0.390,0.755,0.311
isomer2_NO_A,-0.717,0.254,-0.386
isomer2_NO_B,-0.356,0.416,0.042
isomer2_CO_A,-0.365,1.031,0.364
isomer2_HCN_B,-0.090,1.088,0.042
CSVEOF
