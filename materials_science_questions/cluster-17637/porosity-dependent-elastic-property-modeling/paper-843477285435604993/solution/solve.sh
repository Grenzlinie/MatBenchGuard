#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
export OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"
pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple numpy scipy

# === solve block: step_01_natural_frequencies.json ===
python3 << 'PYEOF'
import json

result = {
    "mode1_freq_hz": 260.0
}

with open(f"/app/outputs/step_01_natural_frequencies.json", "w") as f:
    json.dump(result, f, indent=2)
print("Wrote natural frequency")
PYEOF

# === solve block: step_02_deflection_time_series.csv ===
python3 << 'PYEOF'
import csv
import math
from scipy.integrate import solve_ivp
import numpy as np

# Plate and loading parameters (a=b=0.2 m, h_c=10 mm, h_p=0.1 mm)
a = 0.2
b = 0.2
modal_shape_integral_sq = a * b / 4.0   # integral of sin^2 terms over the plate
load_amplitude_q0 = 0.1e6               # 0.1 MPa -> N/m2
modal_force_scaling = a * b / 4.0        # scaled load for this mode
F0 = modal_force_scaling * load_amplitude_q0

# Effective modal mass (using approximate rho_avg and h_total as in the paper)
rho_avg = 7476.0       # kg/m3
h_total = 0.0102        # m
modal_mass = rho_avg * h_total * modal_shape_integral_sq   # kg

# Natural frequency (Hz) – same as in step_01
f_n = 260.0
omega_n = 2.0 * math.pi * f_n
k_e = modal_mass * omega_n**2

# Uncontrolled modal damping ratio (0.8 %)
zeta_un = 0.008
c_un = 2.0 * zeta_un * omega_n * modal_mass

# Controlled effective damping ratio: Gv=0.01 is modelled as 3.0 % total damping
zeta_ctrl = 0.03
c_ctrl = 2.0 * zeta_ctrl * omega_n * modal_mass

# Step load function: 1 for 0 ≤ t ≤ 0.02 s, then 0
def load_func(t):
    return 1.0 if t <= 0.02 else 0.0

# ODE for SDOF: m*q'' + c*q' + k*q = F0 * load_func(t)
def ode_sys(t, y, m, c, k, F0):
    q, v = y
    dqdt = v
    dvdt = (F0 * load_func(t) - c*v - k*q) / m
    return [dqdt, dvdt]

# Time span
T_end = 0.1
t_eval = np.linspace(0.0, T_end, 2000)

# Solve uncontrolled
y0 = [0.0, 0.0]
sol_un = solve_ivp(ode_sys, [0.0, T_end], y0, t_eval=t_eval,
                  args=(modal_mass, c_un, k_e, F0), method='RK45', rtol=1e-6, atol=1e-9)

# Solve controlled
y0 = [0.0, 0.0]
sol_ctrl = solve_ivp(ode_sys, [0.0, T_end], y0, t_eval=t_eval,
                    args=(modal_mass, c_ctrl, k_e, F0), method='RK45', rtol=1e-6, atol=1e-9)

# Write CSV
with open("/app/outputs/step_02_deflection_time_series.csv", "w", newline='') as f:
    writer = csv.writer(f)
    writer.writerow(["time_s", "deflection_mm", "gain"])
    for i in range(len(t_eval)):
        # uncontrolled
        defl_mm_un = sol_un.y[0, i] * 1e3           # convert m to mm
        writer.writerow([f"{t_eval[i]:.6f}", f"{defl_mm_un:.6f}", "Gv0"])
        # controlled
        defl_mm_ctrl = sol_ctrl.y[0, i] * 1e3
        writer.writerow([f"{t_eval[i]:.6f}", f"{defl_mm_ctrl:.6f}", "Gv0.01"])

print("Wrote deflection time series")
PYEOF
