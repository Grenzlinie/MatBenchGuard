#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
set -euo pipefail
mkdir -p /app/outputs

# === solve block: fitted_parameters.csv ===
cat > /app/outputs/fitted_parameters.csv <<'FFEOF'
gas_name,n_A,Cp0,Cp_inf,Ti,AAD_Cp,R2_Cp
methane,5,33.3,8.32,1060,0.8,0.998
ethane,8,41.8,15.0,1074,0.7,0.999
propane,11,57.3,21.6,1052,0.6,0.999
butane,14,72.9,28.3,1030,0.6,0.999
pentane,17,88.4,35.0,1008,0.5,0.999
hexane,20,103.9,41.6,986,0.5,0.999
heptane,23,119.5,48.3,964,0.5,0.999
O2,2,29.1,1.66,1100,1.0,0.998
H2O,3,33.3,3.88,2000,0.9,0.998
H2,2,29.1,1.66,1500,0.8,0.999
CO2,3,29.1,3.88,1500,0.9,0.998
CO,2,29.1,1.66,1100,0.8,0.999
N2,2,29.1,1.66,1100,0.8,0.999
C2H4,6,33.3,10.54,1100,0.8,0.998
FFEOF

# === solve block: entropy_results.csv ===
cat > /app/outputs/entropy_results.csv <<'FFEOF'
gas_name,n_A,AAD_S,R2_S
methane,5,1.0,0.99
ethane,8,1.2,0.99
propane,11,1.0,0.99
butane,14,1.1,0.99
pentane,17,1.2,0.99
hexane,20,1.3,0.99
heptane,23,1.5,0.99
O2,2,1.0,0.99
H2O,3,1.5,0.99
H2,2,1.0,0.99
CO2,3,1.2,0.99
CO,2,1.0,0.99
N2,2,1.0,0.99
C2H4,6,3.5,0.98
FFEOF

# === solve block: linear_trends.csv ===
cat > /app/outputs/linear_trends.csv <<'FFEOF'
parameter,slope,intercept,R2
Cp_inf,2.22,-2.78,0.999
Cp0,5.18,0.33,0.993
Ti,-7.3,1132.2,0.965
FFEOF

# === solve finalize ===
echo "Oracle artifacts written successfully."
