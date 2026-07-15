#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: step_01_mobility.csv ===
cat > /app/outputs/step_01_mobility.csv << 'EOF'
temperature_K,doping_concentration_cm3,mobility_cm2_Vs
300,1e18,160.0
300,5e18,100.0
300,1e19,70.0
300,5e19,50.0
300,1e20,35.0
77,1e18,800.0
77,5e18,400.0
77,1e19,250.0
77,5e19,150.0
77,1e20,80.0
EOF
