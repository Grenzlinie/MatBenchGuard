#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: optimal_zt_summary.csv ===
cat > /app/outputs/optimal_zt_summary.csv <<'CSVEOF'
monolayer,temperature_K,carrier_type,optimal_carrier_concentration_cm2,Seebeck_uVK,electrical_conductivity_Ohm-1m-1,power_factor_Wm-1K-2,electronic_thermal_conductivity_Wm-1K-1,ZT
gamma-Pb2SSe,300,p,3.6e12,247.1,63276,0.003863,0.232,1.36
gamma-Pb2STe,300,p,1.8e12,289.9,31618,0.002657,0.114,2.96
gamma-Pb2SeTe,300,p,1.5e12,301.6,32865,0.002989,0.116,3.22
gamma-Pb2SSe,800,p,3.4e12,297.2,19693,0.001739,0.157,3.52
gamma-Pb2STe,800,p,2.7e12,339.9,10543,0.001218,0.086,5.33
gamma-Pb2SeTe,800,p,1.4e12,357.3,9828,0.001255,0.084,6.88
CSVEOF
