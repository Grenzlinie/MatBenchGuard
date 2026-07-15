#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs
export OUTDIR=/app/outputs

# === solve block: dd_seebeck_predictions.csv ===
cat > "$OUTDIR/dd_seebeck_predictions.csv" <<'FFEOF'
element,Seebeck_coefficient_muV_per_K
Sc,7
Ti,11
V,21
Cr,22
Mn,24
Fe,26
Co,25
Ni,14
Cu,17
Zn,16
FFEOF
