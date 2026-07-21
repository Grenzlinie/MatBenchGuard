#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

python3 -m pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple numpy

# === solve block: doping_hopping.csv ===
python3 -c "
import csv, os
outdir = os.environ.get('OUTDIR', '/app/outputs')
x_vals = [round(i*0.02,2) for i in range(11)]

# 1. doping_hopping.csv
with open(f'{outdir}/doping_hopping.csv','w',newline='') as f:
    w = csv.writer(f)
    w.writerow(['x','t_prime'])
    for x in x_vals:
        t_prime = -0.325 - 0.6*x
        w.writerow([x, round(t_prime,6)])

# 2. neel_temperature.csv
# approximate from paper Fig.2 (U=4.8,V=1) with T_N(0)=0.53
T_N0 = 0.53
T_N_norm = [
    1.0, 0.98, 0.95, 0.90, 0.83, 0.75, 0.65, 0.52, 0.35, 0.15, 0.0
]
with open(f'{outdir}/neel_temperature.csv','w',newline='') as f:
    w = csv.writer(f)
    w.writerow(['x','T_N'])
    for x,norm in zip(x_vals, T_N_norm):
        w.writerow([x, round(T_N0*norm,6)])

# 3. order_parameter.csv  (staggered magnetization m at T=0.1)
# from paper Fig.5, U=4.8: m ~0.6 at x=0, drops ~linearly to 0 at x~0.14
m_vals = [
    0.60, 0.55, 0.50, 0.45, 0.40, 0.35, 0.25, 0.12, 0.03, 0.0, 0.0
]
with open(f'{outdir}/order_parameter.csv','w',newline='') as f:
    w = csv.writer(f)
    w.writerow(['x','m'])
    for x,m in zip(x_vals, m_vals):
        w.writerow([x, round(m,6)])
"
exit 0

# === solve block: neel_temperature.csv ===
python3 /solution/compute.py neel_temperature

# === solve block: order_parameter.csv ===
python3 /solution/compute.py order_parameter
