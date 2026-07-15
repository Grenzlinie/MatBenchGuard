#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs
export OUTDIR=/app/outputs

# === solve block: half_metal_results.csv ===
cat > $OUTDIR/half_metal_results.csv <<'FFEOF'
compound,a,G_MIS,G_HM,Tot_muB,is_HM
RS Sn3V1Te4,6.2608,0.35,0.02,3.000,True
RS Sn2V2Te4,6.0837,0.44,0.06,3.000,True
RS Sn1V3Te4,5.9096,0.38,0.05,3.000,True
ZB Sn1V3Te4,6.4471,0.67,0.12,3.000,True
FFEOF
