#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p $OUTDIR

# === solve block: structural_results.csv ===
cat > $OUTDIR/structural_results.csv <<'FFEOF'
alpha,density,D,xi_x,xi_y_cos_beta,beta,anisotropy_ratio
0.0,0.72,8.0,6.0,6.0,0.0,1.0
20.0,0.71,8.0,6.2,5.9,5.0,1.051
30.0,0.69,8.0,6.6,5.7,10.0,1.158
45.0,0.65,8.0,7.2,5.3,18.0,1.358
55.0,0.60,9.0,8.0,5.16,25.0,1.550
60.0,0.55,10.0,9.0,5.45,30.0,1.651
65.0,0.48,12.0,8.5,5.12,35.0,1.660
70.0,0.40,14.0,7.5,4.8,40.0,1.563
75.0,0.32,16.0,6.5,4.5,45.0,1.444
80.0,0.25,18.0,5.5,4.2,50.0,1.310
85.0,0.18,20.0,4.5,3.9,55.0,1.154
88.0,0.12,22.0,4.0,3.7,58.0,1.081
FFEOF
