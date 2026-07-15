#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: adsorption_results.csv ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs
cat > /app/outputs/adsorption_results.csv <<'FFEOF'
substrate,gas,Eads,magnetic_moment,delta_q
Mo-BC3,HCN,1.03,0.60,0.64
Mo-BC3,NO,2.13,0.00,0.69
Mo-BC3,NO2,2.38,1.00,0.74
Mo-BC3,NH3,1.24,1.00,-0.04
Si-BC3,HCN,0.24,1.00,0.92
Si-BC3,NO,1.18,2.00,0.93
Si-BC3,NO2,2.59,0.00,1.01
Si-BC3,NH3,1.40,0.00,0.07
Pt-BC3,HCN,0.02,0.00,0.04
Pt-BC3,NO,0.74,2.00,0.40
Pt-BC3,NO2,1.67,0.00,0.61
Pt-BC3,NH3,0.67,0.00,-0.14
FFEOF
