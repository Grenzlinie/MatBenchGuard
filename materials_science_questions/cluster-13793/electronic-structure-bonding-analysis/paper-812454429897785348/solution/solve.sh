#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: mop_values.csv ===
cat > /app/outputs/mop_values.csv <<'EOF'
site,total_MOP,M_M_MOP,M_P_MOP
M1,2.32,1.01,1.31
M2,2.22,1.27,0.95
M3,2.12,0.99,1.13
M4,2.38,1.29,1.09
M5,2.46,2.00,0.46
M6,2.62,1.79,0.83
EOF
