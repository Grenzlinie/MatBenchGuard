#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: predictions.csv ===
python3 << 'PYEOF'
import math, csv

dm = 50.0
C = 8 * (1 - 0.3) * (2 * 350.0) / (200.0 * 0.002)
rhs = C / (dm ** 3)

V_m_list = [0.051, 0.121, 0.210, 0.314]

def delta(Vm):
    return dm / ((6 / math.pi) * Vm) ** (1 / 3)

def f(h, D):
    return 1 / h**3 + 1 / (D - h)**3

def solve_h(D, target):
    lo, hi = 1e-9, D / 2
    for _ in range(200):
        mid = (lo + hi) / 2
        fm = f(mid, D)
        if abs(fm - target) < 1e-15:
            return mid
        if fm > target:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2

rows = []
for Vm in V_m_list:
    D = delta(Vm)
    h = solve_h(D, rhs)
    th = math.atan(2 * h / D)
    tn = math.tan(th)
    tnh = math.tan(th / 2)
    num = tnh * tn
    K = math.sqrt(num / (1 + num))
    rows.append([Vm, h, math.degrees(th), K])

with open("/app/outputs/predictions.csv", "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["Vm", "h_um", "theta_deg", "Kcl_Kmax"])
    for r in rows:
        w.writerow([f"{r[0]:.6f}", f"{r[1]:.8f}", f"{r[2]:.6f}", f"{r[3]:.8f}"])
PYEOF
