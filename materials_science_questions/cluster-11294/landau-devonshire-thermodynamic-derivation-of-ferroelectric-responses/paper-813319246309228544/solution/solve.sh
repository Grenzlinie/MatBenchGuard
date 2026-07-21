#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: step_v.txt ===
python3 -c 'print(0.96)' > /app/outputs/step_v.txt

# === solve block: step_t_SD.txt ===
python3 -c 'print((2e-6)**2 / (6 * 1e-5))' > /app/outputs/step_t_SD.txt

# === solve block: step_V_strength.txt ===
python3 -c 'print(5.0)' > /app/outputs/step_V_strength.txt

# === solve block: step_L_star.txt ===
python3 -c 'print(1/((4e-7)**2 * 6e17))' > /app/outputs/step_L_star.txt

# === solve block: step_L_radial.txt ===
python3 -c 'import math; print(math.sqrt(1e-5 * ((2e-6)**2 / (6*1e-5))))' > /app/outputs/step_L_radial.txt

# === solve block: step_L_dstar.txt ===
python3 -c 'print(1e-7 * (1e-3 / 4e-7)**(1.5) * (32 * 50)**(-0.5))' > /app/outputs/step_L_dstar.txt
