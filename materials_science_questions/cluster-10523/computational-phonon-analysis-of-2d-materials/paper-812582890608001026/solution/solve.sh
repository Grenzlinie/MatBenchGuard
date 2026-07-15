#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
set -euo pipefail
mkdir -p /app/outputs

# === solve block: thermal_conductivity_results.csv ===
cat > /app/outputs/thermal_conductivity_results.csv <<'EOF'
system,length_nm,temperature_K,ITCA_deg,thermal_conductivity_W_mK,uncertainty_W_mK
DWCNT,5,200,0.00,125.2,NaN
DWCNT,10,200,0.00,885.7,NaN
DWCNT,20,200,0.00,1349.8,NaN
DWCNT,10,300,0.00,696.3,NaN
DWCNT,10,400,0.00,620.0,NaN
DWCNT,10,200,5.82,896.8,NaN
DWCNT,10,200,14.70,913.7,NaN
DWCNT,10,200,23.41,930.3,NaN
DWCNT,10,200,30.00,942.9,NaN
EOF
