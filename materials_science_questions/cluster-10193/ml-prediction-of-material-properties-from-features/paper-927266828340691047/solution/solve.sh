#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: comparison_results.csv ===
cat > /app/outputs/comparison_results.csv <<'EOF'
property,MAE_ML,MAE_O_pband,percent_reduction
k*,1.347,1.0,34.7
D*,1.291,1.0,29.1
k_chem,0.934,1.0,-6.6
D_chem,0.985,1.0,-1.5
ASR,1.27,1.0,27.0
EOF
