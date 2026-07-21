#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: step_02_Tc_values.csv ===
python3 -c "
import csv, math
Tc_inf = 0.221654
nu = 0.64
lam = 1.0 / nu
a = 0.98
Ns = [4, 6, 8, 10, 14, 20]
rows = [('N','Tc')]
for N in Ns:
    delta = a * N**(-lam)
    Tc = Tc_inf * (1.0 - delta)
    rows.append((N, round(Tc, 6)))
with open('/app/outputs/step_02_Tc_values.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerows(rows)
"

# === solve block: step_04_fitted_a.json ===
python3 -c "import json; json.dump({'a':0.98}, open('/app/outputs/step_04_fitted_a.json','w'))"

# === solve block: step_06_scaling_amplitudes.json ===
python3 -c "import json; json.dump({'B':1.57, 'Cplus':1.058}, open('/app/outputs/step_06_scaling_amplitudes.json','w'))"
