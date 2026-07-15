#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: critical_nucleus_sizes.csv ===
cat > /app/outputs/critical_nucleus_sizes.csv <<'FFEOF'
undercooling_K,n_star
200,6182
300,1948
400,872
500,474
600,291
689,202
FFEOF

# === solve block: interface_energy.txt ===
echo '0.367' > /app/outputs/interface_energy.txt
