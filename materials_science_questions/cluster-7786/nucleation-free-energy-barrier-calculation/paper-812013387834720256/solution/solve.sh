#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
set -euo pipefail
mkdir -p /app/outputs

# === solve block: extremum_points.csv ===
python3 << 'PYEOF'
import csv, math, sys, os

# -------------------------------
# Parameters (all in SI units)
# -------------------------------
sigma = 1.0                        # J/m^2
vA    = 1.0e-5                     # m^3/mol
T     = 300.0                      # K
R     = 8.314                      # J/(mol K)
nA    = 1.0e-4                     # initial mole number (total)
N     = 1.0e14                     # total number of nuclei
xA_sat = 1.0e-5                    # saturated mole fraction
S_ini  = nA / xA_sat               # 10.0

pi = math.pi

def nAn(r):
    """Total mole number in nuclei for given radius r [m]."""
    return (4.0 * pi * r**3 * N) / (3.0 * vA)

def deltaG(r):
    """Free energy change per nucleus, Eq. (2.25.a)."""
    nA_n = nAn(r)
    term1 = 4.0 * pi * r**2 * sigma
    term2 = -(nA_n * R * T / N) * math.log(S_ini)
    # term3: (nA - nA_n) * (RT/N) * ln((1 - nA_n/nA) / (1 - nA_n))
    denom1 = 1.0 - nA_n / nA
    denom2 = 1.0 - nA_n
    if denom1 <= 0.0 or denom2 <= 0.0:
        # Should not happen for physical radii
        term3 = 0.0
    else:
        term3 = (nA - nA_n) * (R * T / N) * math.log(denom1 / denom2)
    # term4: (1 - nA) * (RT/N) * ln(1 / denom2) = -(1 - nA) * (RT/N) * ln(denom2)
    if denom2 <= 0.0:
        term4 = 0.0
    else:
        term4 = (1.0 - nA) * (R * T / N) * math.log(1.0 / denom2)
    return term1 + term2 + term3 + term4

def dGdr_numeric(r, h=1e-12):
    """Central difference derivative of deltaG wrt r."""
    return (deltaG(r + h) - deltaG(r - h)) / (2.0 * h)

def bisect_root(f, a, b, tol=1e-12, max_iter=100):
    """Find root of f(r) in [a,b] via bisection, assumes opposite sign."""
    fa = f(a)
    fb = f(b)
    if fa * fb > 0:
        # fallback: return midpoint
        return (a + b) / 2.0
    for _ in range(max_iter):
        mid = (a + b) / 2.0
        fmid = f(mid)
        if fmid == 0.0:
            return mid
        if fa * fmid < 0:
            b = mid
            fb = fmid
        else:
            a = mid
            fa = fmid
        if abs(b - a) < tol:
            return (a + b) / 2.0
    return (a + b) / 2.0

# -------------------------------
# Grid evaluation for bracketing
# -------------------------------
num_points = 100000
r_start = 1e-12      # 1 pm
r_end   = 10e-9      # 10 nm
r_vals = [r_start + i * (r_end - r_start) / (num_points - 1) for i in range(num_points)]
G_vals = [deltaG(r) for r in r_vals]

# Derivative using central differences (forward/backward at edges)
dG = []
for i in range(num_points):
    if i == 0:
        dG.append((G_vals[1] - G_vals[0]) / (r_vals[1] - r_vals[0]))
    elif i == num_points - 1:
        dG.append((G_vals[-1] - G_vals[-2]) / (r_vals[-1] - r_vals[-2]))
    else:
        dG.append((G_vals[i+1] - G_vals[i-1]) / (r_vals[i+1] - r_vals[i-1]))

# Identify intervals where derivative changes sign
max_intervals = []
min_intervals = []
for i in range(num_points - 1):
    if dG[i] > 0 and dG[i+1] < 0:
        max_intervals.append((r_vals[i], r_vals[i+1]))
    elif dG[i] < 0 and dG[i+1] > 0:
        min_intervals.append((r_vals[i], r_vals[i+1]))

# If no brackets found (should not happen), fallback to global extremum on interior
if not max_intervals:
    margin = max(1, num_points // 50)
    idx_max = max(range(margin, num_points - margin), key=lambda i: G_vals[i])
    r_max = r_vals[idx_max]
else:
    r_left, r_right = max_intervals[0]
    r_max = bisect_root(dGdr_numeric, r_left, r_right)

if not min_intervals:
    # pick global minimum after the maximum
    max_idx = r_vals.index(r_max) if r_max in r_vals else min(range(num_points), key=lambda i: abs(r_vals[i]-r_max))
    idx_min = min(range(max_idx+1, num_points), key=lambda i: G_vals[i])
    r_min = r_vals[idx_min]
else:
    # first minimum after the first maximum
    for r_left, r_right in min_intervals:
        if r_left > r_max:
            r_min = bisect_root(dGdr_numeric, r_left, r_right)
            break
    else:
        r_left, r_right = min_intervals[0]
        r_min = bisect_root(dGdr_numeric, r_left, r_right)

DeltaG_max = deltaG(r_max)
DeltaG_min = deltaG(r_min)

# Convert to nm and write CSV
outdir = os.environ.get('OUTDIR', '/app/outputs')
path = os.path.join(outdir, 'extremum_points.csv')
with open(path, 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['r_max', 'DeltaG_max', 'r_min', 'DeltaG_min'])
    w.writerow([r_max * 1e9, DeltaG_max, r_min * 1e9, DeltaG_min])
PYEOF
