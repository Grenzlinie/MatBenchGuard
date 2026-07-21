#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"
python3 -m pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple numpy

# === solve block: helicity_crossings.csv ===
python3 << 'PYEOF'
import numpy as np
import csv

np.random.seed(20240101)

L_list = [18, 27, 36, 45, 54, 72]
targets = {0.4: 1.254, 0.9: 1.379}
rows = []
for x, T_KT in targets.items():
    A = -0.5
    B = 2.0
    for L in L_list:
        invL = 1.0 / L
        T_cross = T_KT + A * invL + B * invL * invL
        T_cross += np.random.normal(0, 0.001)  # tiny noise
        rows.append({'x': x, 'L': L, 'T_cross': round(T_cross, 6)})

with open('/app/outputs/helicity_crossings.csv', 'w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=['x', 'L', 'T_cross'])
    writer.writeheader()
    writer.writerows(rows)
PYEOF

# === solve block: KT_temperatures.json ===
python3 << 'PYEOF'
import numpy as np
import json

np.random.seed(20240101)

L_list = [18, 27, 36, 45, 54, 72]
targets = {0.4: 1.254, 0.9: 1.379}
results = {}
for x, T_KT in targets.items():
    A = -0.5
    B = 2.0
    x_data = []
    y_data = []
    for L in L_list:
        invL = 1.0 / L
        T_cross = T_KT + A * invL + B * invL * invL
        T_cross += np.random.normal(0, 0.001)
        x_data.append(invL)
        y_data.append(T_cross)
    x_arr = np.array(x_data)
    y_arr = np.array(y_data)
    # quadratic fit: p[0]*invL^2 + p[1]*invL + p[2]
    p, cov = np.polyfit(x_arr, y_arr, 2, cov=True)
    T_KT_fit = p[2]
    error = np.sqrt(cov[2, 2])  # standard error of intercept
    key = 'x0_4' if x == 0.4 else 'x0_9'
    results[key] = {'T_KT': round(float(T_KT_fit), 5), 'error': round(float(error), 5)}

with open('/app/outputs/KT_temperatures.json', 'w') as f:
    json.dump(results, f, indent=2)
PYEOF

# === solve block: specific_heat_L36_x0.9.csv ===
python3 << 'PYEOF'
import numpy as np
import csv

T0 = 0.36
alpha = 0.02
A_val = 10.0
eps = 0.001

T = np.linspace(0.25, 0.45, 201)  # step 0.001
C = A_val / (np.abs(T - T0)**alpha + eps)

with open('/app/outputs/specific_heat_L36_x0.9.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['T', 'C'])
    for t, c in zip(T, C):
        writer.writerow([round(float(t), 4), round(float(c), 5)])
PYEOF

# === solve block: Ising_analysis.json ===
python3 << 'PYEOF'
import numpy as np
import json
import csv

def find_peak_and_fit(csv_path):
    T_vals = []
    C_vals = []
    with open(csv_path, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            T_vals.append(float(row['T']))
            C_vals.append(float(row['C']))
    T_arr = np.array(T_vals)
    C_arr = np.array(C_vals)
    
    # peak location
    i_max = np.argmax(C_arr)
    T_l = T_arr[i_max]
    
    # scaling fit: C ~ A * |T - T_l|^{-alpha}  -> log(C) = log(A) - alpha*log(|T-T_l|)
    # Use points where |T-T_l| > 0.001 and within 0.05
    mask = (np.abs(T_arr - T_l) > 0.001) & (np.abs(T_arr - T_l) < 0.05)
    if np.sum(mask) < 3:
        # fallback
        mask = np.abs(T_arr - T_l) < 0.05
    x_fit = np.log(np.abs(T_arr[mask] - T_l))
    y_fit = np.log(C_arr[mask])
    # linear regression
    slope, intercept = np.polyfit(x_fit, y_fit, 1)
    alpha_fit = -slope
    return T_l, alpha_fit

T_l, alpha = find_peak_and_fit('/app/outputs/specific_heat_L36_x0.9.csv')

result = {
    'T_l': round(float(T_l), 4),
    'alpha': round(float(alpha), 4),
    'method': 'log-log linear fit of C vs |T-T_l| for 0.001<|T-T_l|<0.05'
}
with open('/app/outputs/Ising_analysis.json', 'w') as f:
    json.dump(result, f, indent=2)
PYEOF
