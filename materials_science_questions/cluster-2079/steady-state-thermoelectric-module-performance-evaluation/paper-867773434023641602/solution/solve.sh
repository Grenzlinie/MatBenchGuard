#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: results.json ===
cat > /app/outputs/results.json <<'FFEOF'
{"RTD":{"P_max_MW_per_m2":0.49,"eta_Pmax_percent":44.66,"eta_max_percent":61.5,"PEP_max_MW_per_m2":0.18,"PF_max":2.20,"zT_max":13.37,"zT_range":"1.54-3.08","S_range_mV_per_K":"0.15-0.21"},"FP-I":{"P_max_MW_per_m2":0.90,"eta_Pmax_percent":46.34,"eta_max_percent":64.1,"PEP_max_MW_per_m2":0.37,"PF_max":4.03,"zT_max":14.98,"zT_range":"2.99-4.49","S_range_mV_per_K":"0.2-0.25"},"FP-II":{"P_max_MW_per_m2":1.03,"eta_Pmax_percent":46.42,"eta_max_percent":64.4,"PEP_max_MW_per_m2":0.41,"PF_max":4.62,"zT_max":15.57,"zT_range":"2.92-4.51","S_range_mV_per_K":"0.2-0.25"},"FP-III":{"P_max_MW_per_m2":1.06,"eta_Pmax_percent":46.32,"eta_max_percent":64.4,"PEP_max_MW_per_m2":0.42,"PF_max":4.82,"zT_max":15.09,"zT_range":"2.93-4.51","S_range_mV_per_K":"0.2-0.26"}}
FFEOF
