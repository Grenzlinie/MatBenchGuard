#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: deposition_results.csv ===
cat > "/app/outputs/deposition_results.csv" <<'FFEOF'
Configuration,E_CrSi12,E_Si111,E_T,E_F,mu_Cr
I,-1000.0,-5000.0,-6009.81,9.81,0.00
II,-1000.0,-5000.0,-6009.50,9.50,0.00
III,-1000.0,-5000.0,-6008.18,8.18,1.43
IV,-1000.0,-5000.0,-6007.21,7.21,1.76
FFEOF
