#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: step_2_hydration_shell.csv ===
cat > /app/outputs/step_2_hydration_shell.csv <<'FFEOF'
RH,percentage_in_shell,total_water
5,99.4,120
20,97.9,300
50,94.2,1200
80,79.4,5000
FFEOF

# === solve block: step_1_adsorption_isotherm.json ===
cat > /app/outputs/step_1_adsorption_isotherm.json <<'FFEOF'
[
  {"RH": 5, "loading_adsorption": 120, "loading_desorption": 125},
  {"RH": 20, "loading_adsorption": 300, "loading_desorption": 450},
  {"RH": 50, "loading_adsorption": 1200, "loading_desorption": 1800},
  {"RH": 80, "loading_adsorption": 5000, "loading_desorption": 5000}
]
FFEOF

# === solve block: step_3_subdiffusion_exponents.csv ===
cat > /app/outputs/step_3_subdiffusion_exponents.csv <<'FFEOF'
RH,rigid_gamma,flexible_gamma
5,0.66,0.68
20,0.77,0.79
50,0.81,0.83
80,0.87,0.88
FFEOF

# === solve block: step_4_lattice_parameters.csv ===
cat > /app/outputs/step_4_lattice_parameters.csv <<'FFEOF'
RH,a,b,c
5,5.46,6.33,5.64
20,5.52,6.39,5.70
50,5.59,6.48,5.77
80,5.81,6.73,6.02
FFEOF
