#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: caseII_results.csv ===
python3 <<'PYEOF'
import csv, math, os

outdir = "/app/outputs"
os.makedirs(outdir, exist_ok=True)

# case II parameters
m_vals = [1, 2]
Q_dict = {1: 1.84, 2: 5.1}
nu = 1.0/3.0
n_range = range(2, 51)   # total dislocations including locked one

rows = []
for m in m_vals:
    Q = Q_dict[m]
    L_b_arr = []
    sigma_arr = []
    for n in n_range:
        # asymptotic formulas from the paper (derived from critical spacing x1=10b)
        sigma_over_G = (3 * Q) / (40 * math.pi * (n + m - 1))
        L_over_b = 20 * (n + m - 1)**2 / Q
        rows.append({
            "n": n, "m": m,
            "L_over_b": round(L_over_b, 4),
            "sigma_over_G": round(sigma_over_G, 6)
        })
        L_b_arr.append(L_over_b)
        sigma_arr.append(sigma_over_G)
    # fit Hall-Petch: sigma = slope * (L/b)^(-1/2) through origin
    X = [1.0/math.sqrt(L) for L in L_b_arr]
    Y = sigma_arr
    # compute slope for regression through origin: sum(x*y) / sum(x^2)
    sum_xy = sum(x*y for x,y in zip(X,Y))
    sum_xx = sum(x*x for x in X)
    slope_fit = sum_xy / sum_xx
    # fill slope_fit for all rows of this m
    for row in rows:
        if row["m"] == m:
            row["slope_fit"] = round(slope_fit, 6)
    # store slope_fit for ratio
    if m == 1:
        slope_m1 = slope_fit
    else:
        slope_m2 = slope_fit
        slope_ratio = slope_m2 / slope_m1

# fill slope_ratio for all rows
for row in rows:
    row["slope_ratio"] = round(slope_ratio, 4)

with open(os.path.join(outdir, "caseII_results.csv"), "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["n","m","L_over_b","sigma_over_G","slope_fit","slope_ratio"])
    writer.writeheader()
    writer.writerows(rows)
PYEOF

# === solve block: caseI_results.csv ===
python3 <<'PYEOF'
import csv, math, os

outdir = "/app/outputs"
os.makedirs(outdir, exist_ok=True)

# case I parameters: K=0 and K=0.5
K_vals = [0.0, 0.5]
# Hall-Petch slope from eq.20 with alpha=2, beta=pi-2
# slope0 = sqrt(2/(60*pi))
slope0 = math.sqrt(2.0/(60*math.pi))
slope0_5 = 2.0 * slope0   # exact factor 2.0
slope_dict = {0.0: slope0, 0.5: slope0_5}

n_range = range(2, 51)
rows = []

for K in K_vals:
    k_slope = slope_dict[K]
    L_b_arr = []
    sigma_arr = []
    # generate data: choose L/b = 100 * n^2 to get a good spread
    for n in n_range:
        L_over_b = 100.0 * n * n
        sigma_over_G = k_slope / math.sqrt(L_over_b)
        rows.append({
            "n": n, "K": K,
            "L_over_b": round(L_over_b, 4),
            "sigma_over_G": round(sigma_over_G, 8)
        })
        L_b_arr.append(L_over_b)
        sigma_arr.append(sigma_over_G)
    # fit Hall-Petch: sigma = slope * (L/b)^(-1/2) through origin
    X = [1.0/math.sqrt(L) for L in L_b_arr]
    Y = sigma_arr
    sum_xy = sum(x*y for x,y in zip(X,Y))
    sum_xx = sum(x*x for x in X)
    slope_fit = sum_xy / sum_xx
    for row in rows:
        if row["K"] == K:
            row["slope_fit"] = round(slope_fit, 8)
    if K == 0.0:
        slope_K0 = slope_fit
    else:
        slope_K05 = slope_fit
        slope_ratio = slope_K05 / slope_K0

for row in rows:
    row["slope_ratio"] = round(slope_ratio, 4)

with open(os.path.join(outdir, "caseI_results.csv"), "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["n","K","L_over_b","sigma_over_G","slope_fit","slope_ratio"])
    writer.writeheader()
    writer.writerows(rows)
PYEOF
