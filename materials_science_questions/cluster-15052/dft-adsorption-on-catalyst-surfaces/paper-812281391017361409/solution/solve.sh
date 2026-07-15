#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
export OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: surface_ratios.csv ===
cat > "$OUTDIR/surface_ratios.csv" <<'EOF'
D_x,condition,theta_FFC_over_HFC,theta_FFC_plus_HFC
0.0,presence,3.7,0.77
0.3,presence,4.5,0.71
0.6,presence,5.1,0.65
0.9,presence,5.7,0.49
0.0,absence,4.2,0.92
0.3,absence,4.2,0.87
0.6,absence,4.6,0.80
0.9,absence,4.8,0.56
EOF
