#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
set -euo pipefail
mkdir -p /app/outputs

# === solve block: optimal_parameters.csv ===
cat > /app/outputs/optimal_parameters.csv <<'FFEOF'
f,Z1_PCL,Z2_PCL,Tj_PCL,q_PCL,p_net_PCL,p_tot_PCL,Z1_Cu,q_Cu,p_net_Cu,p_tot_Cu,t
0,5900,3207,216.97,33.461,90.461,425.071,8380,45.384,45.384,499.224,26.27
0.2,6200,3321,213.93,29.698,93.620,390.596,8960,38.843,47.896,436.322,23.54
0.4,6460,3420,211.31,26.829,96.336,364.629,9460,34.125,50.033,391.282,21.38
0.6,6700,3506,209.08,24.557,98.729,344.298,9920,30.543,51.900,357.330,19.60
0.8,6900,3588,206.92,22.704,100.872,327.914,10320,27.721,53.566,330.771,18.10
1,7100,3659,205.12,21.160,102.820,314.415,10700,25.433,55.073,309.401,16.80
FFEOF

# === solve block: temperature_profiles.csv ===
python3 /solution/gen_profiles.py > /app/outputs/temperature_profiles.csv
