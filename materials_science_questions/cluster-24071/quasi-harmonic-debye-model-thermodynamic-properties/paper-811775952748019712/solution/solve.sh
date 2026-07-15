#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
export OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: step_01_eam_potential_parameters.json ===
cat > "$OUTDIR/step_01_eam_potential_parameters.json" <<'FFEOF'
{
  "p1": 5.5619,
  "p2": 1.3850,
  "rho1": 0.900,
  "rho2": 0.800,
  "rho3": 0.700,
  "rho4": 0.600,
  "rho5": 0.500,
  "rho6": 0.400,
  "rho7": 0.100,
  "rho8": 1.20,
  "rho9": 2.00,
  "a1": -3.5659,
  "c1": 0.2753,
  "c2": -0.100,
  "c3": -0.200,
  "c4": 3.65,
  "c5": -1.850,
  "c6": 0.500,
  "c7": 10.60,
  "c8": 0.050,
  "c9": 1.62,
  "c10": 2.24,
  "m": 1.80,
  "n": 1.71,
  "eps": 0.209,
  "d": 3.3318,
  "alpha": 4.100,
  "cutoff": 12.20
}
FFEOF

# === solve block: step_02_liquid_properties_zero_p.csv ===
cat > "$OUTDIR/step_02_liquid_properties_zero_p.csv" <<'FFEOF'
T_K,density_gcm3,U_pot_kJmol,K_T_GPa,D_cm2s,viscosity_cP
1406,17.226,-486.56,34.4,1.99,6.59
1500,17.06,-483.31,31.7,2.25,6.16
2000,16.18,-465.30,22.8,5.06,3.65
2500,15.33,-446.62,18.7,7.95,2.91
3000,14.53,-427.20,17.3,11.1,2.50
3500,13.76,-407.01,14.8,15.7,2.06
4000,13.03,-386.04,10.1,19.3,1.92
4500,12.3,-364.28,4.9,24.7,1.87
FFEOF

# === solve block: step_03_shock_hugoniot.csv ===
cat > "$OUTDIR/step_03_shock_hugoniot.csv" <<'FFEOF'
Z,T_model_K,P_GPa,U_kJmol
0.900,420,16.8,-515.9
0.800,810,51.3,-462.4
0.700,2540,123.2,-295.6
0.653,4825,197.8,-97.8
0.628,5810,248.9,51.8
0.5834,9045,371.6,454.3
FFEOF

# === solve block: step_04_melting_temperature.txt ===
echo 1455 > "$OUTDIR/step_04_melting_temperature.txt"
