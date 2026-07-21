#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
set -euo pipefail
mkdir -p /app/outputs
python3 -m pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple numpy

# === solve block: tc_results.csv ===
python3 -m pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple numpy
cat > /tmp/compute_tc.py << 'EOF'
import numpy as np
import csv, sys

def compute_Tc(geometry, Sc, Ss, J1_div_J, delta_s):
    J = 1.0
    J1 = J1_div_J * J
    Js = J * (1.0 + delta_s)
    k = 1.0
    if geometry == 'nanowire':
        C = np.array([
            [2*J, 6*J, 0, 0],
            [J, 4*J, 2*J1, J1],
            [0, 2*J1, 2*Js, 2*Js],
            [0, J1, 2*Js, 2*Js]
        ])
        D_diag = np.array([
            3*Sc*k/(Sc+1),
            3*Sc*k/(Sc+1),
            3*Ss*k/(Ss+1),
            3*Ss*k/(Ss+1)
        ])
    else:  # nanotube
        C = np.array([
            [4*J, 2*J1, J1],
            [2*J1, 2*Js, 2*Js],
            [J1, 2*Js, 2*Js]
        ])
        D_diag = np.array([
            3*Sc*k/(Sc+1),
            3*Ss*k/(Ss+1),
            3*Ss*k/(Ss+1)
        ])
    D_inv = np.diag(1.0 / D_diag)
    M = D_inv @ C
    eigvals = np.linalg.eigvals(M)
    real_pos = eigvals.real[eigvals.real > 0]
    if len(real_pos) == 0:
        return -1.0
    return np.max(real_pos)

param_combos = []
geometries = ['nanowire', 'nanotube']
for g in geometries:
    for delta in [0.0, 0.5, 1.0]:
        param_combos.append((g, 0.5, 1.0, 1.0, delta))
    for delta in [0.0, 0.5, 1.0]:
        param_combos.append((g, 0.5, 0.5, 1.0, delta))
    for delta in [0.0, 0.5, 1.0]:
        param_combos.append((g, 0.5, 1.0, 1.5, delta))

if __name__ == '__main__':
    outpath = sys.argv[1]
    with open(outpath, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['geometry', 'Sc', 'Ss', 'J1_div_J', 'delta_s', 'Tc'])
        for geom, sc, ss, j1_div, delta in param_combos:
            tc = compute_Tc(geom, sc, ss, j1_div, delta)
            writer.writerow([geom, sc, ss, j1_div, delta, tc])
EOF
python3 /tmp/compute_tc.py "$OUTDIR/tc_results.csv"
