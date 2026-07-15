#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: geometric_params.csv ===
cat > "$OUTDIR/geometric_params.csv" <<'FFEOF'
stress,l1,l2,l3,l4,w1,w2,w3,w4,d1,d2,theta1,theta2
0.0,5.50,5.60,5.70,5.80,88.0,92.0,89.0,91.0,5.80,6.00,42.0,48.0
0.5,5.55,5.65,5.75,5.85,87.5,92.5,88.5,91.5,6.05,6.25,45.0,51.0
1.0,5.60,5.70,5.80,5.90,87.0,93.0,88.0,92.0,6.30,6.50,48.0,54.0
1.5,5.65,5.75,5.85,5.95,86.5,93.5,87.5,92.5,6.55,6.75,51.0,57.0
2.0,5.70,5.80,5.90,6.00,86.0,94.0,87.0,93.0,6.80,7.00,54.0,60.0
FFEOF
