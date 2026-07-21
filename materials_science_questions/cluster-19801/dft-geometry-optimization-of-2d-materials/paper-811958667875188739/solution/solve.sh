#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: structural_parameters.csv ===
cat > /app/outputs/structural_parameters.csv << 'FFEOF'
configuration,charge_state,buckling_angle_deg,bond_length_A
HD1,Ne-1,15.9,2.25
HD1,Ne,14.6,2.26
HD1,Ne+1,3.2,2.33
HD1,Ne+2,-5.7,2.42
HD2,Ne,15.5,2.30
HD2,Ne+1,15.7,2.30
HD2,Ne+2,15.8,2.29
FFEOF
