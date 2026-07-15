#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: orr_data.csv ===
cat > /app/outputs/orr_data.csv << 'FFEOF'
Model,State_2,State_3,State_4,State_5,Overpotential,Co_Mulliken_charge
undoped Co-gN4,-0.31316,-0.80658,-2.15894,-3.90224,0.73,0.75
BNC-1,-0.33707,-0.85481,-2.4221,-3.98165,0.70,0.82
PNC-1,-0.50,-1.00,-2.50,-4.00,0.48,0.74
FFEOF
