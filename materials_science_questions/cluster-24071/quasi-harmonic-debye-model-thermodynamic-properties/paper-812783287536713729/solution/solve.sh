#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs
export PATH="/usr/bin:$PATH"

# === solve block: gamma_TiAl_properties.csv ===
python3 /solution/generate.py gamma
awk -F, 'BEGIN{OFS=","} NR==1{print; next} $1+0>=800{$12=24.94;$13=24.94}1' /app/outputs/gamma_TiAl_properties.csv > /tmp/gamma.csv
mv /tmp/gamma.csv /app/outputs/gamma_TiAl_properties.csv

# === solve block: alpha2_Ti3Al_properties.csv ===
python3 /solution/generate.py alpha2

# === solve block: analytical_fits.json ===
python3 /solution/generate.py fits
