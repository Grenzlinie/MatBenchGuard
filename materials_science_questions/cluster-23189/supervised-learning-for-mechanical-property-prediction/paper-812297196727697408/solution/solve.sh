#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p $OUTDIR

# === solve block: step_01_test_predictions.csv ===
cat > "$OUTDIR/step_01_test_predictions.csv" <<'FFEOF'
N,V,R_D,G_D,warp_predicted
2,25,3.5,1.5,0.9802
4,22,2.8,1.5,0.6243
FFEOF

# === solve block: step_02_optimal_parameters.csv ===
cat > "$OUTDIR/step_02_optimal_parameters.csv" <<'FFEOF'
N,V,R_D,G_D,warp_predicted
2,18,2.4,1.82,0.711
FFEOF
