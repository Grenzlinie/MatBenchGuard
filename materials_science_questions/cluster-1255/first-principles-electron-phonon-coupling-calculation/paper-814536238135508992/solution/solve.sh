#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: lambda_and_Tc.csv ===
python3 << 'PYEOF'
import csv, math

m1 = 1.8
m2 = 3.5
m3 = 6.0
xC1 = 6.1
xC2 = 20.0
alpha = m2 / m1
gamma = m3 / m1

# Dense grid covering the whole relevant range
N = 1000
x_min = 0.5
x_max = 35.0
dx = (x_max - x_min) / (N - 1)

with open('/app/outputs/lambda_and_Tc.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['x', 'n_s', 'lambda1', 'lambda2', 'lambda3', 'Q1', 'Q2', 'Q3'])
    for i in range(N):
        x = x_min + i * dx
        # Carrier concentration n_s (cm^-3)
        if x <= xC1:
            n_s = (x / 5.74) ** 3 * 1e18
        elif x <= xC2:
            n_s = (x**3 + alpha**1.5 * (x**2 - xC1**2)**1.5) / 195.0 * 1e18
        else:
            n_s = (x**3 + alpha**1.5 * (x**2 - xC1**2)**1.5 + gamma**1.5 * (x**2 - xC2**2)**1.5) / 195.0 * 1e18

        # Band 1
        lam1 = (1.0 / x) * math.log(1.0 + x)
        Q1 = (x**2 / m1) * math.exp(-1.0 / lam1)

        # Band 2
        if x <= xC1:
            lam2 = 0.0
            Q2 = 0.0
        else:
            x2 = math.sqrt(alpha) * math.sqrt(max(0, x**2 - xC1**2))
            if x2 == 0.0:
                lam2 = 0.0
            else:
                denom2 = x + alpha * x2
                lam2 = (alpha / x2) * math.log(1.0 + x2**2 / denom2)
            Q2 = (x**2 / m2) * math.exp(-1.0 / lam2) if lam2 > 0 else 0.0

        # Band 3
        if x <= xC2:
            lam3 = 0.0
            Q3 = 0.0
        else:
            x3 = math.sqrt(gamma) * math.sqrt(max(0, x**2 - xC2**2))
            # x2 already computed above if needed, but we recompute safely
            x2 = math.sqrt(alpha) * math.sqrt(max(0, x**2 - xC1**2))
            if x3 == 0.0:
                lam3 = 0.0
            else:
                denom3 = x + alpha * x2 + gamma * x3
                lam3 = (gamma / x3) * math.log(1.0 + x3**2 / denom3)
            Q3 = (x**2 / m3) * math.exp(-1.0 / lam3) if lam3 > 0 else 0.0

        w.writerow([x, n_s, lam1, lam2, lam3, Q1, Q2, Q3])
PYEOF

# === solve block: maxima.csv ===
python3 << 'PYEOF'
import csv

x_vals = []
n_s_vals = []
Q = {1: [], 2: [], 3: []}

with open('/app/outputs/lambda_and_Tc.csv', 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        x_vals.append(float(row['x']))
        n_s_vals.append(float(row['n_s']))
        Q[1].append(float(row['Q1']))
        Q[2].append(float(row['Q2']))
        Q[3].append(float(row['Q3']))

maxima = []
for band in [1, 2, 3]:
    qlist = Q[band]
    max_val = max(qlist)
    idx = qlist.index(max_val)
    x_max = x_vals[idx]
    n_s_max = n_s_vals[idx]
    maxima.append((band, x_max, n_s_max, max_val))

with open('/app/outputs/maxima.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['band', 'x_max', 'n_s_max', 'Q_max'])
    for row in maxima:
        w.writerow(row)
PYEOF
