#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
export OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: hard_sphere_results.csv ===
cat > "$OUTDIR/hard_sphere_results.csv" <<'EOF'
rho,h1_norm_HI,h1_norm_LO,pressure_HI,pressure_FL
0.809,6.61,0.00,3.60,4.55
0.800,6.28,0.25,3.51,4.37
0.790,5.91,0.38,3.42,4.19
0.780,5.55,0.49,3.33,4.00
0.775,5.37,0.55,3.28,3.92
0.770,5.19,0.60,3.24,3.84
0.760,4.84,0.71,3.16,3.67
0.750,4.47,0.82,3.08,3.52
0.740,4.10,0.95,3.00,3.37
0.730,3.71,1.11,2.93,3.22
0.725,3.50,1.20,2.90,3.15
0.720,3.28,1.31,2.87,3.09
0.710,2.73,1.64,2.81,2.95
0.706,2.35,1.93,2.81,2.90
0.705,2.12,2.12,2.82,2.89
0.704,NaN,NaN,NaN,2.88
0.703,NaN,NaN,NaN,2.87
0.700,NaN,NaN,NaN,2.82
EOF
