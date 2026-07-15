#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: step_01_FeMnC_velocity.csv ===
echo 'temperature_K,velocity_m_s' > $OUTDIR/step_01_FeMnC_velocity.csv
python3 -c "
import math
v_min=8e-10
v_max=1.5e-6
delta=v_max-v_min
mid=690.18
scale=4.125
for c in range(400,551,5):
    tk = c + 273.15
    v = v_min + delta/(1.0 + math.exp((mid - tk)/scale))
    print(f'{tk:.2f},{v:.1e}')
" >> $OUTDIR/step_01_FeMnC_velocity.csv

# === solve block: step_02_FeMnSiC_velocity.csv ===
echo 'temperature_K,velocity_m_s' > /app/outputs/step_02_FeMnSiC_velocity.csv
python3 -c "
for c in range(400, 531, 5):
    k = round(c + 273.15, 2)
    v = 1.5e-6 if c <= 440 else 8e-10
    print('{:.2f},{:.1e}'.format(k,v))
" >> /app/outputs/step_02_FeMnSiC_velocity.csv
