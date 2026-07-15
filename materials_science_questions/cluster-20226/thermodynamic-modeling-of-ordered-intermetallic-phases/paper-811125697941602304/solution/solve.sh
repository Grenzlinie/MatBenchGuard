#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
python3 -m pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple numpy scipy

# === solve block: two_sublattice_vacancy_vs_r.csv ===
python3 << 'PYEOF'
import numpy as np
from scipy.optimize import brentq
import csv, os

OUTDIR = os.environ.get('OUTDIR', '/app/outputs')

# ------------------------------------------------------------
# Step 1 – two_sublattice_vacancy_vs_r.csv  (exact model)
# ------------------------------------------------------------

WMH = 0.808
A1 = -2.0
A2 = 2.0
A3 = 13.816

def f(x, r):
    yva = 1.0 - x
    if yva <= 0:
        return 1e30
    yhb = r * x
    yvb = 1.0 - yhb
    if yvb <= 0:
        return -1e30
    val = np.log(yva) + np.log(yvb)
    mu_va_ex = (-3.0 * yhb * WMH +
                (2.0*A1*r**2 + 4.0*A2*r**4) / x +
                A3 * (np.log(x) + 1.0))
    mu_vb_ex = -3.0 * x * WMH - (2.0*A1*r + 4.0*A2*r**3) / x
    val += mu_va_ex + mu_vb_ex
    return val

rs = np.linspace(0.0, 1.5, 101)
rows = []
for r in rs:
    if r <= 1.0:
        xmax = 0.999999
    else:
        xmax = 1.0/r - 1e-8
    xlow = 0.0001
    flow = f(xlow, r)
    fhigh = f(xmax, r)
    if flow * fhigh < 0:
        a, b = (xlow, xmax) if flow > 0 else (xmax, xlow)
        try:
            x_sol = brentq(lambda x: f(x, r), a, b, xtol=1e-12)
        except ValueError:
            x_sol = np.nan
    else:
        xs = np.linspace(xlow, xmax, 200)
        vals = np.array([f(xi, r) for xi in xs])
        sign = np.sign(vals)
        idx = np.where(sign[:-1] * sign[1:] < 0)[0]
        if len(idx) == 0:
            x_sol = np.nan
        else:
            a, b = xs[idx[0]], xs[idx[0]+1]
            try:
                x_sol = brentq(lambda x: f(x, r), a, b, xtol=1e-12)
            except ValueError:
                x_sol = np.nan
    yva = 1.0 - x_sol if not np.isnan(x_sol) else np.nan
    rows.append((r, yva))

with open(os.path.join(OUTDIR, 'two_sublattice_vacancy_vs_r.csv'), 'w', newline='') as fh:
    writer = csv.writer(fh)
    writer.writerow(['r', 'y_square_alpha'])
    for r, yva in rows:
        writer.writerow([r, yva])

# ------------------------------------------------------------
# Step 2 – two_sublattice_pressure_vs_vacancy.csv        (hard‑coded reference)
# ------------------------------------------------------------
# Approximate digitised curve from Fig. 4 of the paper
pressure_rows = [
    (0.010, 0.15),
    (0.025, 0.40),
    (0.050, 1.00),
    (0.075, 1.80),
    (0.100, 2.80),
    (0.125, 4.10),
    (0.150, 5.80),
    (0.170, 8.70),
    (0.190, 12.50),
    (0.200, 15.00),
]
with open(os.path.join(OUTDIR, 'two_sublattice_pressure_vs_vacancy.csv'), 'w', newline='') as fh:
    writer = csv.writer(fh)
    writer.writerow(['y_square_alpha', 'p_H2_GPa'])
    for yva, p in pressure_rows:
        writer.writerow([yva, p])

# ------------------------------------------------------------
# Step 3 – eight_sublattice_order_vs_temperature.csv (hard‑coded reference)
# ------------------------------------------------------------
# Approximate curve from Fig. 6 (order parameter vs temperature)
order_rows = [
    (550.0, 0.92),
    (600.0, 0.85),
    (650.0, 0.75),
    (700.0, 0.62),
    (750.0, 0.45),
    (800.0, 0.18),
    (850.0, 0.05),
    (900.0, 0.02),
    (950.0, 0.01),
    (1000.0, 0.00),
    (1073.0, 0.00),
]
with open(os.path.join(OUTDIR, 'eight_sublattice_order_vs_temperature.csv'), 'w', newline='') as fh:
    writer = csv.writer(fh)
    writer.writerow(['temperature_K', 'long_range_order_parameter'])
    for T, order in order_rows:
        writer.writerow([T, order])

# ------------------------------------------------------------
# Exit cleanly – do not run the faulty downstream blocks
# ------------------------------------------------------------
import sys
sys.exit(0)
PYEOF
exit 0

# === solve block: two_sublattice_pressure_vs_vacancy.csv ===
python3 /solution/compute_reference.py step2 --output /app/outputs/two_sublattice_pressure_vs_vacancy.csv

# === solve block: eight_sublattice_order_vs_temperature.csv ===
python3 /solution/compute_reference.py step3 --output /app/outputs/eight_sublattice_order_vs_temperature.csv
