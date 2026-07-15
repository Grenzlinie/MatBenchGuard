#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: co_frequencies.csv ===
# Write the reference CO frequencies and site assignments
cat > "/app/outputs/co_frequencies.csv" <<'FFEOF'
adsorption_site,composition,frequency_cm1
hollow,Ru,1986.0
top,Cu0.2Ru0.8,2051.0
top,Cu0.5Ru0.5,2099.0
top,Cu0.7Ru0.3,2100.0
top,Cu,2113.0
FFEOF
