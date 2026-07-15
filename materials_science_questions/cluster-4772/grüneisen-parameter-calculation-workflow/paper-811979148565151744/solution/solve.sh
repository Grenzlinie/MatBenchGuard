#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: gp_table.csv ===
cat > "$OUTDIR/gp_table.csv" <<'EOF'
theta,X1,gamma1_prime,gamma1_doubleprime,X2,gamma2_prime,gamma2_doubleprime,X3,gamma3_prime,gamma3_doubleprime
5,63.80,1.87,6.50,16.16,1.10,5.83,16.02,1.03,5.94
15,62.26,1.87,6.50,17.34,1.78,4.65,16.13,1.25,5.51
25,59.59,1.87,6.45,19.34,2.75,2.98,16.36,1.65,4.71
35,56.64,2.00,6.14,21.38,3.53,1.65,16.66,2.17,3.66
45,54.57,2.43,5.24,22.43,3.72,1.36,17.00,2.75,2.50
55,54.25,3.19,3.69,21.72,3.21,2.31,17.34,3.31,1.38
65,55.38,3.98,2.09,19.70,2.31,3.90,17.64,3.79,0.43
75,56.89,4.55,0.96,17.87,4.13,-0.26,17.52,1.45,5.42
85,57.87,4.84,0.41,17.98,4.31,-0.62,16.18,0.83,6.37
EOF
