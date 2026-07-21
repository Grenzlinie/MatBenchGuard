#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail

python3 -m pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple numpy scipy
mkdir -p /app/outputs
echo 'Environment ready.'

# === solve block: critical_surface.csv ===
python3 << 'BLOCKEOF'
import csv, sys
sys.path.insert(0, '/solution')
from functions import classify_critical

j00_vals = [0.5, 1.0, 1.5, 2.0, 2.5, 3.0]
j01_vals = [-2.0, -1.5, -1.0, -0.5, 0.0, 0.5, 1.0, 1.5, 2.0]
j11_vals = [0.5, 1.0, 1.5, 2.0, 2.5]

with open('/app/outputs/critical_surface.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['J00_div_J', 'J01_div_J', 'J11_div_J', 'is_critical'])
    for J00 in j00_vals:
        for J01 in j01_vals:
            for J11 in j11_vals:
                ic = classify_critical(J00, J01, J11)
                w.writerow([J00, J01, J11, ic])
BLOCKEOF
echo 'critical_surface.csv written.'

# === solve block: T_CS_values.csv ===
python3 << 'BLOCKEOF'
import csv, sys
sys.path.insert(0, '/solution')
from functions import solve_tcs_cubic

points = [
    (0.0, 0.0, 0.0),
    (0.5, 0.0, 0.5),
    (1.0, 0.0, 1.0),
    (1.5, 0.0, 0.5),
    (2.0, 0.0, 1.0),
    (1.29, 0.0, -1.282),
    (1.0, 0.5, 0.8),
    (2.0, 0.5, 0.0),
    (0.5, 0.2, 1.2),
    (0.0, 0.0, -1.0),
    (1.5, 0.0, 0.0),
    (0.8, 0.3, 0.9),
]

with open('/app/outputs/T_CS_values.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['a', 'b', 'c', 'T_CS_div_T_C'])
    for a, b, c in points:
        tcs = solve_tcs_cubic(a, b, c)
        w.writerow([a, b, c, tcs])
BLOCKEOF
echo 'T_CS_values.csv written.'

# === solve block: magnetization_profile.csv ===
python3 << 'BLOCKEOF'
import csv, sys, math
sys.path.insert(0, '/solution')
from functions import bulk_magnetization, layer_magnetization

# Gd parameters
J00 = 1.645
J01 = -1.282
J11 = 1.0
Jb = 1.0

T_min = 1.0           # T_C = 12, so this is ~0.083 T_C
T_max = 14.4          # 1.2 T_C
N = 200

with open('/app/outputs/magnetization_profile.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['T_div_T_C', 'eta_0', 'eta_1', 'eta_2',
                'eta_avg_3layers', 'eta_avg_surface_layer_model'])
    for i in range(N + 1):
        T = T_min + (T_max - T_min) * i / N
        T_div = T / 12.0
        eta_bulk = bulk_magnetization(T)
        etas = layer_magnetization(T, J00, J01, J11, Jb)
        eta0 = etas[0]
        eta1 = etas[1]
        eta2 = etas[2]
        avg3 = eta0 + eta1 + eta2
        avg_surf = eta0 + 2.0 * eta_bulk
        w.writerow([T_div, eta0, eta1, eta2, avg3, avg_surf])
BLOCKEOF
echo 'magnetization_profile.csv written.'
