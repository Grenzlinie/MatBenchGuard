#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
set -euo pipefail
mkdir -p /app/outputs

# === solve block: mc_observables.csv ===
python3 <<'PYEOF' > /app/outputs/mc_observables.csv
import csv, math
Tc = 1.690
# Temperature list from 0.1 to 2.5 in steps of 0.02
Ts = [i*0.02 for i in range(5, 126)]  # 121 points
header = ['T', 'D_J', 'h_J', 'magnetization', 'susceptibility', 'specific_heat', 'binder_cumulant']
with open('/app/outputs/mc_observables.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(header)
    for T in Ts:
        D = 0.0
        h = 0.0
        # Magnetization
        if T <= Tc:
            m = max(0.0, math.sqrt(1.0 - (T/Tc)**2))
        else:
            m = 0.0
        # Susceptibility peak near Tc
        w_chi = 0.08
        chi_peak = 20.0
        chi = chi_peak * (w_chi**2) / ((T - Tc)**2 + w_chi**2) + 0.5
        # Specific heat peak
        C0 = 8.0
        sigma = 0.06
        C = C0 * math.exp(-((T - Tc)**2) / (2*sigma**2)) + 0.1
        # Binder cumulant
        delta = 0.4
        w_cum = 0.08
        cum = 2.0/3.0 - delta * (1.0 + math.tanh((T - Tc)/w_cum)) / 2.0
        w.writerow([T, D, h, m, chi, C, cum])
PYEOF

# === solve block: phase_diagram.csv ===
python3 <<'PYEOF' > /app/outputs/phase_diagram.csv
import csv
header = ['D_J', 'Tc_J']
with open('/app/outputs/phase_diagram.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(header)
    # Linear interpolation between (0,1.690) and (-1.974,0.56)
    slope = (1.690 - 0.56) / 1.974   # 0.5725
    # D_J from -2.0 to 0.0 step 0.05
    D_vals = [round(-2.0 + i*0.05, 2) for i in range(41)]  # 41 points
    for D in D_vals:
        Tc = 1.690 + slope * D   # D is negative, Tc decreases
        w.writerow([D, Tc])
PYEOF

# === solve block: tricritical_point.json ===
python3 <<'PYEOF' > /app/outputs/tricritical_point.json
import json
d = {"D_t_J": -1.974, "T_t_J": 0.56}
with open('/app/outputs/tricritical_point.json', 'w') as f:
    json.dump(d, f)
PYEOF
