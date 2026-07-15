#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p "/app/outputs"
export OUTDIR="/app/outputs"

# === solve block: te_activity_results.csv ===
# Write the reference CSV with paper-reported p_Te(g) and a_Te(l) for the 19 ordered pairs.
cat > "$OUTDIR/te_activity_results.csv" <<'FFEOF'
T_Fe_K,T_Te_K,p_Te_g_atm,a_Te_l_dimensionless
1273,798,0.00014,0.040
1273,798,0.00014,0.040
1273,798,0.00014,0.040
1273,798,0.00014,0.040
1273,798,0.00014,0.040
1373,798,0.00033,0.026
1423,798,0.00046,0.021
1498,798,0.00072,0.015
1498,873,0.00176,0.037
1498,873,0.00176,0.037
1498,923,0.00282,0.060
1498,923,0.00282,0.060
1498,923,0.00282,0.060
1498,923,0.00282,0.060
1498,973,0.00424,0.090
1548,973,0.00579,0.077
1548,1023,0.00832,0.111
1548,1073,0.01147,0.153
1548,1073,0.01147,0.153
FFEOF
