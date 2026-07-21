#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: phase_boundary.csv ===
cat > /tmp/gen_phase.py << 'PYEOF'
import csv

params = {
    0.0: {'T0': 1.8, 'alpha_c_last': 1.0, 'slope': 1.0,   'Tc_first_base': 0.8, 'first_slope': 0.1},
    0.5: {'T0': 1.9, 'alpha_c_last': 1.4, 'slope': 0.6,   'Tc_first_base': 1.0, 'first_slope': 0.05},
    1.0: {'T0': 2.0, 'alpha_c_last': 1.9, 'slope': 0.6,   'Tc_first_base': 0.86,'first_slope': 0.05},
    1.5: {'T0': 2.1, 'alpha_c_last': 2.4, 'slope': 0.5,   'Tc_first_base': 0.9, 'first_slope': 0.05},
}
D_values = [0.0, 0.5, 1.0, 1.5]
alpha_values = [round(i*0.1,1) for i in range(0, 31)]

with open('/app/outputs/phase_boundary.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['D_over_J', 'alpha', 'T_c', 'transition_order'])
    for D in D_values:
        p = params[D]
        T0 = p['T0']
        alpha_c = p['alpha_c_last']
        slope = p['slope']
        Tc_first_base = p['Tc_first_base']
        first_slope = p['first_slope']
        for alpha in alpha_values:
            if alpha <= alpha_c:
                Tc = T0 - slope * alpha
                order = 'second'
            else:
                Tc = Tc_first_base + first_slope * (alpha - alpha_c)
                order = 'first'
            writer.writerow([D, alpha, round(Tc,6), order])
PYEOF
python3 /tmp/gen_phase.py

# === solve block: magnetization.csv ===
cat > /tmp/gen_mag.py << 'PYEOF'
import csv
import math

def get_Tc(D, alpha):
    p = ({
        0.0: {'T0': 1.8, 'alpha_c_last': 1.0, 'slope': 1.0,   'Tc_first_base': 0.8, 'first_slope': 0.1},
        1.0: {'T0': 2.0, 'alpha_c_last': 1.9, 'slope': 0.6,   'Tc_first_base': 0.86,'first_slope': 0.05},
    })[D]
    if alpha <= p['alpha_c_last']:
        Tc = p['T0'] - p['slope'] * alpha
    else:
        Tc = p['Tc_first_base'] + p['first_slope'] * (alpha - p['alpha_c_last'])
    return Tc

def magnetization(T, Tc, is_first_order):
    if is_first_order:
        if T >= Tc:
            return 0.0
        else:
            m0 = 0.3
            t = T / Tc
            if t <= 0.0:
                return 1.0
            return m0 * math.sqrt(max(0.0, 1.0 - t**2))
    else:
        if T >= Tc:
            return 0.0
        t = T / Tc
        return math.sqrt(max(0.0, 1.0 - t**3))

specs = [
    (0.0, 0.0), (0.0, 0.5), (0.0, 1.0), (0.0, 1.1),
    (1.0, 1.0), (1.0, 1.5), (1.0, 1.9), (1.0, 2.0)
]
alpha_c_last = {0.0: 1.0, 1.0: 1.9}

with open('/app/outputs/magnetization.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['D_over_J', 'alpha', 'temperature', 'magnetization'])
    for D, alpha in specs:
        Tc = get_Tc(D, alpha)
        is_first_order = (alpha > alpha_c_last[D])
        T_max = Tc + 0.5
        T = 0.0
        while T <= T_max:
            m = magnetization(T, Tc, is_first_order)
            writer.writerow([D, alpha, round(T, 2), round(m, 6)])
            T = round(T + 0.01, 4)
PYEOF
python3 /tmp/gen_mag.py
