#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: predicted_tbc.csv ===
cat > /app/outputs/predicted_tbc.csv <<'FFEOF'
temperature_K,Al_TBC_MW_m2K,Co_TBC_MW_m2K,Ru_TBC_MW_m2K
80,90,100,80
100,140,160,120
150,250,270,200
200,310,330,280
250,330,360,320
300,350,370,340
350,360,390,355
400,370,400,365
450,380,410,375
500,390,420,385
FFEOF
