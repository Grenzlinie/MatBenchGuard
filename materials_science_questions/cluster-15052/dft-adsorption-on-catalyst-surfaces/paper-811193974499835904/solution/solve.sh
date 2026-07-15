#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: peak_data.csv ===
cat > "/app/outputs/peak_data.csv" <<'FFEOF'
species,S_M,coverage_peak,domain_density
Bi,3,0.65,1.52
As,2.5,0.70,1.57
Hg,2,0.70,1.97
FFEOF
