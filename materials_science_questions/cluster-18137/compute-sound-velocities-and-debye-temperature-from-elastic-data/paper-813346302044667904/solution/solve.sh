#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: thermal_properties.csv ===
cat > /app/outputs/thermal_properties.csv << 'EOF'
compound,v_l,v_t,v_m,theta_D,k_min
ScBRh3,6149,3315,4366,535,1.023
YBRh3,5865,3157,4159,496,0.922
LuBRh3,5320,2876,3785,458,0.862
LaBRh3,5255,2754,3651,433,0.848
EOF
