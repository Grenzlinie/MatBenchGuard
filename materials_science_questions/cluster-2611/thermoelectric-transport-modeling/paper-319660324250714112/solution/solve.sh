#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: hall_magnetoresistance_factors.csv ===
cat > /app/outputs/hall_magnetoresistance_factors.csv <<'EOF'
T,A_N,M_N,A_P,M_P
77,1.11,1.33,1.00,1.01
100,1.19,1.59,1.00,1.01
140,1.36,2.16,1.01,1.03
180,1.57,3.00,1.02,1.06
220,1.78,4.08,1.03,1.09
260,1.93,4.95,1.04,1.11
300,2.17,6.62,1.05,1.14
EOF
