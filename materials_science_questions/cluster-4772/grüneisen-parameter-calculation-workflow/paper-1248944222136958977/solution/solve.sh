#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
set -euo pipefail
mkdir -p /app/outputs

# === solve block: alpha_results.csv ===
cat > /app/outputs/alpha_results.csv <<'EOF'
temperature_K,alpha_s2
300,1.438e-25
10,8.11e-24
EOF
