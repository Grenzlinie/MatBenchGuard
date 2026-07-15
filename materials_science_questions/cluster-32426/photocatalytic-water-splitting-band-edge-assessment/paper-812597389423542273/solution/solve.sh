#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: band_gap.txt ===
echo "0.60" > /app/outputs/band_gap.txt

# === solve block: short_circuit_current.txt ===
echo "4.2" > /app/outputs/short_circuit_current.txt

# === solve block: mobility.csv ===
cat > /app/outputs/mobility.csv <<'FFEOF'
type,direction,mobility
electron,x,29.99
electron,y,19.65
hole,x,142.39
hole,y,133.61
FFEOF

# === solve block: power_factor_vs_N.csv ===
python3 /solution/gen_power_factor.py > /app/outputs/power_factor_vs_N.csv
