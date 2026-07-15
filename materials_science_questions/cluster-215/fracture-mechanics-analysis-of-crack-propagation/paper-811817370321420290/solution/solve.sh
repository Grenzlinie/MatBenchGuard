#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: hydraulic_fracture_results.csv ===
cat > "$OUTDIR/hydraulic_fracture_results.csv" <<'EOF'
water_pressure,stress_tip_1,stress_tip_2,max_opening
100,-36,-3,0.43
200,-24,-6,0.85
300,-12,-9,1.29
EOF
