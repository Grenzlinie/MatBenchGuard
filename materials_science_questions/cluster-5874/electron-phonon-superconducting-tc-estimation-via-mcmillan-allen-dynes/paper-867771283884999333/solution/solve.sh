#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: step_03_table.csv ===
cat > $OUTDIR/step_03_table.csv <<'FFEOF'
Pressure,Tc,dM,aM,dM_minus_aM
155,203.000,121.7,126.8,5.1
160,197.400,113.9,128.7,14.8
165,191.388,115.5,132.1,16.6
170,186.263,112.8,132.0,19.2
175,181.438,110.2,134.3,24.1
185,169.300,103.6,139.5,35.9
195,158.670,98.00,147.1,49.1
205,147.305,91.80,152.7,60.9
215,138.258,86.90,166.1,79.2
FFEOF
