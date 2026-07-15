#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: step_01_equilibrium_properties.csv ===
cat > /app/outputs/step_01_equilibrium_properties.csv << 'EOF'
structure,a,c,E0,V0,K0,K0_prime
CoSn,5.221,2.921,-14.046,22.990,303.6,4.19
WC,2.913,2.862,-13.953,21.035,337.1,4.17
NaCl,4.413,,-13.370,21.481,327.6,4.35
ZnS-B3,4.753,,-13.042,26.845,244.2,4.18
CsCl,2.750,,-12.348,20.797,307.0,4.28
EOF

# === solve block: step_02_ground_state.txt ===
echo 'CoSn' > /app/outputs/step_02_ground_state.txt
