#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: case_B_compressibility_n12.csv ===
python3 /solution/generate_data.py --case B --peak_mu 1.75 --peak_height 40 --width 0.2 --mu_min 0.5 --mu_max 3.0 --n_points 200 > /app/outputs/case_B_compressibility_n12.csv

# === solve block: case_C_compressibility_n14.csv ===
python3 /solution/generate_data.py --case C --peak_mu 5.0 --peak_height 40 --width 0.5 --mu_min 2.0 --mu_max 8.0 --n_points 300 > /app/outputs/case_C_compressibility_n14.csv

# === solve block: transition_parameters.csv ===
cat > /app/outputs/transition_parameters.csv <<'FFEOF'
case,mu_kT,p_over_rho0kT,density_gap
B,1.75,1.94,0.75
C,5.0,5.0,0.9
FFEOF
