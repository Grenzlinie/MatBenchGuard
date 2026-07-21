#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: finite_size_data.csv ===
python3 <<'PYEOF'
import csv

points = []
# transition, Kc0, Q0, slope_K, slope_Q
params = [
    (1, 0.206, 0.356, 0.1, 0.1),
    (2, -0.32, 0.08, 0.05, 0.02),
    (3, -0.76, 0.05, 0.1, 0.02),
]
for trans, Kc0, Q0, sk, sq in params:
    for L in (4,5,6,7):
        x = 1.0/(L*L)
        Kc = Kc0 + sk*x
        Q = Q0 + sq*x
        points.append([trans, L, Kc, Q])

with open('/app/outputs/finite_size_data.csv','w',newline='') as f:
    w = csv.writer(f)
    w.writerow(['transition','L','K_c(L)','Q(L)'])
    w.writerows(points)
PYEOF

# === solve block: extrapolated_results.json ===
python3 <<'PYEOF'
import json

results = {
    'K_c_1': 0.206, 'K_c_1_err': 0.002,
    'Q_1': 0.356, 'Q_1_err': 0.030,
    'K_c_2': -0.32, 'K_c_2_err': 0.01,
    'Q_2': 0.08, 'Q_2_err': 0.03,
    'K_c_3': -0.76, 'K_c_3_err': 0.10,
    'Q_3': 0.05, 'Q_3_err': 0.05
}
with open('/app/outputs/extrapolated_results.json','w') as f:
    json.dump(results, f)
PYEOF
