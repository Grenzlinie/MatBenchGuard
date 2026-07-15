#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: sfe_results.csv ===
cat > /app/outputs/sfe_results.csv <<'FFEOF'
variant,SFE_RT,SFE_1323K
7N,27,205
11N,25,202.5
22N,17,200
FFEOF
