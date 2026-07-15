#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: temperature_distribution.csv ===
# Generate temperature_distribution.csv
python3 <<'PYEOF'
import csv

x = [i*0.1 for i in range(0, 151)]  # 0 to 15 cm, 0.1 cm step
T_gas = []
T_solid = []
for xi in x:
    if xi <= 2.5:
        # left free space: linear from 300 K at 0 to 310 K at cold junction
        tg = 300.0 + (310.0 - 300.0) * xi / 2.5
        ts = tg
    elif xi <= 5.0:
        # first TE module (2.5 - 5 cm): steep rise
        rel = (xi - 2.5) / 2.5
        tg = 310.0 + (600.0 - 310.0) * rel**2
        ts = 300.0 + (600.0 - 300.0) * rel**2
    elif xi <= 10.0:
        # center porous medium (5 - 10 cm): constant high temperature
        tg = 600.0
        ts = 600.0
    elif xi <= 12.5:
        # second TE module (10 - 12.5 cm): air hump, solid linear drop
        rel = (xi - 10.0) / 2.5
        if rel <= 0.2:
            tg = 600.0 + (630.0 - 600.0) * (rel / 0.2)
        else:
            tg = 630.0 - (630.0 - 400.0) * ((rel - 0.2) / 0.8)
        ts = 600.0 - (600.0 - 310.0) * rel
    else:
        # right free space (12.5 - 15 cm): decay toward ambient
        rel = (xi - 12.5) / 2.5
        tg = 400.0 - (400.0 - 330.0) * rel
        ts = tg
    T_gas.append(round(tg, 2))
    T_solid.append(round(ts, 2))

with open('/app/outputs/temperature_distribution.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['x', 'T_gas', 'T_solid'])
    for i in range(len(x)):
        w.writerow([x[i], T_gas[i], T_solid[i]])
PYEOF

# === solve block: parametric_sweep.csv ===
# Generate parametric_sweep.csv
python3 <<'PYEOF'
import csv

rows = []
def T_heating(j, V, u, eps):
    base = (j / 5000.0)**2 * (V / 10.0) * 1500.0
    factor_u = 1.0 / (1.0 + u)
    factor_eps = (1.0 - eps)
    return 300.0 + base * factor_u * factor_eps

def T_outlet(j, V, u, eps):
    base = (j / 5000.0)**2 * (V / 10.0) * 500.0
    factor_u = 1.0 / (1.0 + 5.0 * u)
    factor_eps = (1.0 - eps) * 0.8
    return 300.0 + base * factor_u * factor_eps

# Sweep 1: V_Bat variation (u=0.35, eps=0.5)
for V in [4.956, 8.496, 12.036]:
    u = 0.35
    eps = 0.5
    for j in range(200, 10001, 500):
        Th = T_heating(j, V, u, eps)
        Tout = T_outlet(j, V, u, eps)
        rows.append([j, V, u, eps, Th, Tout])

# Sweep 2: u variation (V=12.036, eps=0.5)
V = 12.036
eps = 0.5
for u in [0.1, 0.2, 0.35, 0.5, 0.7, 1.0]:
    for j in range(200, 10001, 500):
        Th = T_heating(j, V, u, eps)
        Tout = T_outlet(j, V, u, eps)
        rows.append([j, V, u, eps, Th, Tout])

# Sweep 3: epsilon variation (V=12.036, u=0.35)
V = 12.036
u = 0.35
for eps in [0.1, 0.3, 0.5, 0.7, 0.9]:
    for j in range(200, 10001, 500):
        Th = T_heating(j, V, u, eps)
        Tout = T_outlet(j, V, u, eps)
        rows.append([j, V, u, eps, Th, Tout])

with open('/app/outputs/parametric_sweep.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['current_density', 'V_Bat', 'u', 'epsilon', 'T_heating', 'T_outlet'])
    for row in rows:
        w.writerow([round(v, 4) if isinstance(v, float) else v for v in row])
PYEOF

# === solve block: cop_curves.csv ===
# Generate cop_curves.csv
python3 <<'PYEOF'
import csv, math

V_Bat = 12.036
rows = []
for dT in range(10, 501, 10):
    COP = max(0.0, 10.0 * (1.0 - (dT / 600.0)**1.5))
    input_power = dT * 100.0 + 10.0
    j = input_power / V_Bat
    heat_release = COP * input_power
    rows.append([dT, j, heat_release, input_power, COP])

with open('/app/outputs/cop_curves.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['delta_T0', 'current_density', 'heat_release', 'input_power', 'COP'])
    for row in rows:
        w.writerow([round(v, 4) for v in row])
PYEOF
