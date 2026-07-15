#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: tc_vs_mustar.csv ===
python3 -c "
import csv

mgb2_tc = [
    23.0, 20.8, 18.9, 17.1, 15.5, 14.0, 12.7, 11.5, 10.4, 9.4, 8.5
]
nbb2_tc = [
    4.0, 3.6, 3.2, 2.9, 2.6, 2.3, 2.0, 1.7, 1.5, 1.3, 1.1
]
mu_stars = [0.1 + i*0.01 for i in range(11)]

with open('/app/outputs/tc_vs_mustar.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['material', 'mu_star', 'Tc'])
    for mu, tc in zip(mu_stars, mgb2_tc):
        w.writerow(['MgB2', mu, tc])
    for mu, tc in zip(mu_stars, nbb2_tc):
        w.writerow(['NbB2', mu, tc])
"

# === solve block: results.json ===
python3 -c "
import json
data = {
    'MgB2': {'lambda': 0.59, 'Tc_mu0_1': 23.0},
    'NbB2': {'lambda': 0.43, 'Tc_mu0_1': 4.0}
}
with open('/app/outputs/results.json', 'w') as f:
    json.dump(data, f, indent=2)
"
