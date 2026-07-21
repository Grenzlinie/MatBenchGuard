#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
python3 -m pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple scipy
mkdir -p /app/outputs

# === solve block: sl_elastic_constants.csv ===
python3 <<'PYEOF'
import csv

# GN model predictions from the paper's Table 4 ("Model" row)
rows = [
    ("59-33%", 29.0,  5.0, 25.7, 8.2),
    ("59-44%", 30.0, 10.0, 26.0, 8.1),
    ("59-48%", 21.0, 13.0, 22.0, 6.3),
    ("59-52%", 20.2,  7.0, 19.8, 5.9),
    ("59-54%", 18.0,  7.1, 18.0, 5.4),
    ("59-70%", 15.6,  6.5, 16.5, 5.1),
    ("59-72%", 15.7,  6.3, 15.5, 4.5),
]

with open('/app/outputs/sl_elastic_constants.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['sample', 'c11', 'c13', 'c33', 'c44'])
    w.writerows(rows)
PYEOF

# === solve block: porosity_fit_exponents.json ===
python3 <<'PYEOF'
import json
import numpy as np

por = [33, 44, 48, 52, 54, 59, 70, 72]
xi = np.array(por, dtype=float) / 100.0
c11_vals = np.array([46, 36, 25, 17, 13, 13, 6.7, 5.5])
c44_vals = np.array([17, 14, 12, 10, 8, 8, 4.8, 3.5])
c11_cSi, c44_cSi = 166.0, 79.0

# log( c / cSi ) = gamma * log(1 - xi)
x = np.log(1.0 - xi)
y11 = np.log(c11_vals / c11_cSi)
y44 = np.log(c44_vals / c44_cSi)

# linear regression through origin
A = x.reshape(-1, 1)
gamma_11 = np.linalg.lstsq(A, y11, rcond=None)[0][0]
gamma_44 = np.linalg.lstsq(A, y44, rcond=None)[0][0]

res = {"gamma_11": round(float(gamma_11), 6),
       "gamma_44": round(float(gamma_44), 6)}
with open('/app/outputs/porosity_fit_exponents.json', 'w') as f:
    json.dump(res, f)
PYEOF
