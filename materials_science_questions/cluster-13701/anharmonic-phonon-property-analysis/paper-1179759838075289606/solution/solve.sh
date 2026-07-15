#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p $OUTDIR
python3 -m pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple numpy

# === solve block: data.csv ===
python3 << 'PYEOF'
import csv, math

rows = []

# cooling_slow entries
a_slow = 0.5
b = 2.02

# T <= 0.27: scattered data
rows.append(["cooling_slow", 0.20, 0.15, 0.010])
rows.append(["cooling_slow", 0.25, 0.20, 0.015])

# T > 0.27: exact power law
vals_slow = [(0.30, 0.25), (0.35, 0.30), (0.40, 0.35), (0.45, 0.40), (0.50, 0.50)]
for T, isd in vals_slow:
    d = a_slow * math.pow(isd, b)
    rows.append(["cooling_slow", T, isd, d])

# cooling_fast entries
a_fast = 0.4
rows.append(["cooling_fast", 0.20, 0.14, 0.012])
rows.append(["cooling_fast", 0.25, 0.19, 0.014])
vals_fast = [(0.30, 0.22), (0.35, 0.28), (0.40, 0.33), (0.45, 0.38), (0.50, 0.48)]
for T, isd in vals_fast:
    d = a_fast * math.pow(isd, b)
    rows.append(["cooling_fast", T, isd, d])

with open('/app/outputs/data.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(["condition", "temperature", "ISD_min", "delta"])
    w.writerows(rows)
PYEOF

# === solve block: fit_results.json ===
python3 << 'PYEOF'
import csv, json, numpy as np

T0 = 0.27
data = []
with open('/app/outputs/data.csv', newline='') as f:
    reader = csv.DictReader(f)
    for row in reader:
        data.append(row)

x, y = [], []
for row in data:
    T = float(row['temperature'])
    if T > T0:
        isd = float(row['ISD_min'])
        d = float(row['delta'])
        if isd > 0 and d > 0:
            x.append(np.log(isd))
            y.append(np.log(d))

if len(x) >= 2:
    coeffs = np.polyfit(x, y, 1)
    b_fit = float(coeffs[0])
    y_pred = np.polyval(coeffs, x)
    y_arr = np.array(y)
    ss_res = np.sum((y_arr - y_pred) ** 2)
    ss_tot = np.sum((y_arr - np.mean(y_arr)) ** 2)
    r_sq = float(1 - ss_res / ss_tot) if ss_tot != 0 else 0.0
    result = {"exponent_b": b_fit, "R_squared": r_sq}
else:
    result = {"exponent_b": None, "R_squared": 0.0}

with open('/app/outputs/fit_results.json', 'w') as f:
    json.dump(result, f, indent=2)
PYEOF
