#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: scaling_exponents.csv ===
cat > /app/outputs/scaling_exponents.csv <<'EOF'
neighbor_count,alpha,beta
1,0.26,0.08
2,0.31,0.115
3,0.36,0.15
EOF
