#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p "/app/outputs"

# === solve block: computed_properties.csv ===
cat > "/app/outputs/computed_properties.csv" <<'CSVEOF'
metal,property,T_K,value,unit
Cu,Theta_D,0.0,349.46,K
Cu,gamma,0.0,1.75,dimensionless
Cu,beta,20.0,0.96,1e-6/K
Cu,beta,50.0,13.42,1e-6/K
Cu,beta,100.0,36.81,1e-6/K
Cu,beta,150.0,46.15,1e-6/K
Cu,beta,200.0,50.30,1e-6/K
Cu,beta,300.0,52.23,1e-6/K
Cu,C_v,20.0,0.46,J/(mol·K)
Cu,C_v,50.0,6.39,J/(mol·K)
Cu,C_v,100.0,17.53,J/(mol·K)
Cu,C_v,150.0,21.91,J/(mol·K)
Cu,C_v,200.0,23.95,J/(mol·K)
Cu,C_v,300.0,24.87,J/(mol·K)
Ag,Theta_D,0.0,228.55,K
Ag,gamma,0.0,2.53,dimensionless
Ag,beta,20.0,3.84,1e-6/K
Ag,beta,50.0,27.77,1e-6/K
Ag,beta,100.0,48.53,1e-6/K
Ag,beta,150.0,57.46,1e-6/K
Ag,beta,200.0,58.52,1e-6/K
Ag,beta,300.0,59.85,1e-6/K
Ag,C_v,20.0,1.60,J/(mol·K)
Ag,C_v,50.0,11.57,J/(mol·K)
Ag,C_v,100.0,20.22,J/(mol·K)
Ag,C_v,150.0,23.94,J/(mol·K)
Ag,C_v,200.0,24.38,J/(mol·K)
Ag,C_v,300.0,24.98,J/(mol·K)
Au,Theta_D,0.0,166.44,K
Au,gamma,0.0,2.15,dimensionless
Au,beta,20.0,9.66,1e-6/K
Au,beta,50.0,35.68,1e-6/K
Au,beta,100.0,55.14,1e-6/K
Au,beta,150.0,57.35,1e-6/K
Au,beta,200.0,57.46,1e-6/K
Au,beta,300.0,57.52,1e-6/K
Au,C_v,20.0,4.20,J/(mol·K)
Au,C_v,50.0,15.52,J/(mol·K)
Au,C_v,100.0,23.97,J/(mol·K)
Au,C_v,150.0,24.93,J/(mol·K)
Au,C_v,200.0,24.98,J/(mol·K)
Au,C_v,300.0,25.00,J/(mol·K)
CSVEOF
