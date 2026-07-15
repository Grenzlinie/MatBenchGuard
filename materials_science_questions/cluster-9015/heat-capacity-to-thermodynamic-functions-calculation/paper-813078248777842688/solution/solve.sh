#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: step_01_cellI_results.json ===
cat > /app/outputs/step_01_cellI_results.json <<'FFEOF'
{
  "dfG_intercept": -286.989,
  "dfG_slope": 0.098,
  "drG_intercept": -379.022,
  "drG_slope": -0.153,
  "emf_intercept": 654.717,
  "emf_slope": 0.265
}
FFEOF

# === solve block: step_02_cellII_results.json ===
cat > /app/outputs/step_02_cellII_results.json <<'FFEOF'
{
  "dfG_intercept": -287.756,
  "dfG_slope": 0.102,
  "drG_intercept": -296.487,
  "drG_slope": -0.094,
  "emf_intercept": 512.147,
  "emf_slope": 0.162
}
FFEOF

# === solve block: step_03_enthalpy_fit.json ===
cat > /app/outputs/step_03_enthalpy_fit.json <<'FFEOF'
{
  "T2_coefficient": 0.029713,
  "T_coefficient": 124.236,
  "T_inv_coefficient": 4020100,
  "constant": -53166
}
FFEOF

# === solve block: step_04_thermo_functions.csv ===
cat > /app/outputs/step_04_thermo_functions.csv <<'FFEOF'
T(K),H_T_H298 (kJ/mol),Cp (J/K·mol),S (J/K·mol),GEF (J/K·mol)
300,0.18,97.40,113.82,113.22
400,11.33,122.88,145.73,117.40
500,24.42,137.87,174.87,126.03
600,38.77,148.73,201.01,136.39
700,54.10,157.63,224.62,147.34
800,70.27,165.50,246.19,158.36
900,87.18,172.76,266.11,169.24
1000,104.80,179.64,284.67,179.87
1100,123.10,186.28,302.11,190.20
1200,142.06,192.76,318.59,200.21
1300,161.65,199.11,334.27,209.93
1400,181.87,205.38,349.26,219.35
1500,202.72,211.59,363.64,228.49
1600,224.19,217.75,377.49,237.37
FFEOF

# === solve block: step_05_third_law_results.json ===
cat > /app/outputs/step_05_third_law_results.json <<'FFEOF'
{
  "cell_II_mean_delta_f_H298": -180.2,
  "cell_I_mean_delta_f_H298": -173.2
}
FFEOF
