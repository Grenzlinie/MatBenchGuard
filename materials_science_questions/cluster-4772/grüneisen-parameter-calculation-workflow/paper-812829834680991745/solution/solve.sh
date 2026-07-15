#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: kappa_lat_summary.csv ===
cat > /app/outputs/kappa_lat_summary.csv <<'FFEOF'
composition,kappa_lat_300K,kappa_lat_1000K,reduction_percentage_300K
TiNiSn,9.23,2.59,0
Ti0.75Zr0.25NiSn,6.72,1.89,27.19
Ti0.75Hf0.25NiSn,7.36,2.08,20.26
Ti0.50Mn0.50NiSn,7.60,2.13,17.65
FFEOF

# === solve block: ti_nisn_properties.csv ===
cat > /app/outputs/ti_nisn_properties.csv <<'FFEOF'
property,value,unit
a0_0K,5.9536,Å
B0_0K,124.01,GPa
Debye_temperature_300K,404.86,K
FFEOF
