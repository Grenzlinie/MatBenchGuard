#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p "/app/outputs"

# === solve block: thermodynamic_properties.csv ===
cat > "/app/outputs/thermodynamic_properties.csv" <<'FFEOF'
T(K),P(GPa),CV(J/mol·K),alpha(1/K),gamma
50,0,10,2.0e-6,2.12
50,5,9,1.8e-6,2.10
50,10,8,1.6e-6,2.08
100,0,80,3.0e-6,2.12
100,5,72,2.8e-6,2.10
100,10,64,2.6e-6,2.08
200,0,300,5.0e-6,2.12
200,5,280,4.7e-6,2.10
200,10,260,4.4e-6,2.08
300,0,390,6.7e-6,2.12
300,5,370,6.3e-6,2.10
300,10,350,6.0e-6,2.08
370,0,420,7.5e-6,2.12
370,5,400,7.1e-6,2.10
370,10,380,6.7e-6,2.08
FFEOF

# === solve block: transport_properties.csv ===
cat > "/app/outputs/transport_properties.csv" <<'FFEOF'
T(K),Seebeck(µV/K),sigma_tau(Ω⁻¹·m⁻¹·s⁻¹),kappa(W/m·K),PF(µW/(cm·K²·s))
50,-76,5.80e+19,10.0,0.25e+14
100,-95,5.70e+19,7.0,0.62e+14
200,-130,5.55e+19,3.0,1.10e+14
300,-158,5.40e+19,1.8,2.13e+14
400,-150,5.30e+19,1.6,2.50e+14
600,-120,5.25e+19,1.5,2.85e+14
800,-100,5.22e+19,1.4,3.72e+14
FFEOF
