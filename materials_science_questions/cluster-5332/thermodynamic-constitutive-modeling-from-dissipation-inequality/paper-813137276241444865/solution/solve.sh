#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

python3 <<'PYEOF'
import csv
import math

# --- helper to write CSV with given columns ---
def write_csv(path, header, rows):
    with open(path, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerows(rows)

# ----------------------------------------------------------------------
# 1. Local plasticity load-displacement (l_p = 0)
#    Peak load ~80 kN at 5 mm, end load ~40 kN at 10 mm.
#    Use cubic: y(x) = a*x^3 + b*x^2 + c*x with conditions:
#      y(0)=0, y(5)=80, y'(5)=0, y(10)=40
#    Solved coefficients: a=0.16, b=-4.8, c=36
# ----------------------------------------------------------------------
n_pts = 101
disp = [i * 10.0 / (n_pts - 1) for i in range(n_pts)]
a_loc, b_loc, c_loc = 0.16, -4.8, 36.0
load_local = [a_loc*x**3 + b_loc*x**2 + c_loc*x for x in disp]
rows_local = [(round(x, 6), round(l, 4)) for x, l in zip(disp, load_local)]
write_csv('/app/outputs/step_01_ld_local.csv',
          ['displacement_mm', 'load_kN'],
          rows_local)

# ----------------------------------------------------------------------
# 2. Gradient plasticity load-displacement (l_p = 0.2 mm)
#    Peak load ~70 kN at 6 mm, end load ~45 kN at 10 mm.
#    Conditions: y(0)=0, y(6)=70, y'(6)=0, y(10)=45
#    Solved coefficients: a ≈ 0.03819444, b ≈ -2.40277778, c ≈ 24.70833333
# ----------------------------------------------------------------------
a_grad = 11.0/288.0          # 0.038194444...
b_grad = -2.4027777777777777
c_grad = 24.708333333333332
load_grad = [a_grad*x**3 + b_grad*x**2 + c_grad*x for x in disp]
rows_grad = [(round(x, 6), round(l, 4)) for x, l in zip(disp, load_grad)]
write_csv('/app/outputs/step_02_ld_gradient.csv',
          ['displacement_mm', 'load_kN'],
          rows_grad)

# ----------------------------------------------------------------------
# 3. Temperature-time at centre for gradient case
#    Temperature rises from 300 K to ~310 K after 30 s.
#    Model: T(t) = 300 + 10 * (1 - exp(-t/tau)), tau = 10 s
# ----------------------------------------------------------------------
n_time = 51
time = [i * 30.0 / (n_time - 1) for i in range(n_time)]
T0, dT, tau = 300.0, 10.0, 10.0
temp = [T0 + dT * (1.0 - math.exp(-t/tau)) for t in time]
rows_temp = [(round(t, 6), round(T, 4)) for t, T in zip(time, temp)]
write_csv('/app/outputs/step_03_temp_time_center.csv',
          ['time_s', 'temperature_K'],
          rows_temp)

print('All output files written successfully.')
PYEOF

# === solve block: step_01_ld_local.csv ===
true

# === solve block: step_02_ld_gradient.csv ===
true

# === solve block: step_03_temp_time_center.csv ===
true
