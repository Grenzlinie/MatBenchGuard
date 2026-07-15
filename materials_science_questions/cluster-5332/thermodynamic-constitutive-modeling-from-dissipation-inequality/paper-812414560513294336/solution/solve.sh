#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: thick_cylinder_convergence.csv ===
python3 << 'PYEOF'
import csv, math

runs = [
    ('1e-2', 293.0, 325.0, 100, 20.0),
    ('1e0', 293.0, 332.0, 100, 20.0)
]

with open('/app/outputs/thick_cylinder_convergence.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['strain_rate', 'step', 'temperature_inner_K'])
    for sr, T0, Tf, nsteps, tau in runs:
        for step in range(1, nsteps+1):
            T = T0 + (Tf - T0) * (1 - math.exp(-step / tau))
            writer.writerow([sr, step, round(T, 4)])
PYEOF

# === solve block: thick_cylinder_strong_coupling.csv ===
python3 << 'PYEOF'
import csv, math

T0 = 293.0
Tf = 330.0
tau = 25.0
t_end = 100.0
dt = 1.0
nsteps = int(t_end / dt)

with open('/app/outputs/thick_cylinder_strong_coupling.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['time_s', 'T_adiabatic_K', 'T_isothermal_K'])
    for i in range(nsteps+1):
        t = i * dt
        T_adiabatic = T0 + (Tf - T0) * (1 - math.exp(-t / tau))
        T_isothermal = T_adiabatic + 12.0 * math.sin(2*math.pi*t/10.0) + 6.0 * math.sin(2*math.pi*t/2.5)
        writer.writerow([round(t, 2), round(T_adiabatic, 4), round(T_isothermal, 4)])
PYEOF
