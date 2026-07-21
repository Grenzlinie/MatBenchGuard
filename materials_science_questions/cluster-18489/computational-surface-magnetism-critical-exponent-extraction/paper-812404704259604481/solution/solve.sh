#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: phase_diagram.csv ===
python3 << PYEOF
import math, csv

def a_of_t(t):
    """Transfer function parameter a."""
    disc = 5.0 * (t - 1.0) * (t - 0.2)
    if disc < 0:
        return None
    return -1.5 + 2.5 * t - 0.5 * math.sqrt(disc)

def A_S(t, Delta_S, D_S):
    """Disorder-averaged A_S."""
    d0 = 5.0 * t + 1.0
    u1 = 1.0 + Delta_S + D_S
    u2 = 1.0 + Delta_S - D_S
    d1 = d0 + Delta_S + D_S
    d2 = d0 + Delta_S - D_S
    eps = 1e-12
    return 0.5 * (u1 / (d1 if d1 != 0 else eps) + u2 / (d2 if d2 != 0 else eps))

def A_1(t):
    """For Delta_1 = 0, D_1 = 0."""
    return 1.0 / (5.0 * t + 1.0)

def secular_func(t, Delta_S, D_S):
    a = a_of_t(t)
    if a is None:
        return None
    A_s = A_S(t, Delta_S, D_S)
    A1 = A_1(t)
    term = (4.0 + a) / (5.0 * t + 1.0) - 1.0
    return (4.0 * A_s - 1.0) * term - A1 * A1

def find_tc(Delta_S, D_S):
    """Find reduced surface critical temperature t_c in [0,1]."""
    # Check exact t = 1.
    f1 = secular_func(1.0, Delta_S, D_S)
    if f1 is not None and abs(f1) < 1e-10:
        return 1.0
    # Scan interval [1e-6, 0.2] for sign change.
    t_lo = 1e-6
    f_lo = secular_func(t_lo, Delta_S, D_S)
    # if f_lo is None, enlarge slightly
    if f_lo is None:
        t_lo = 1e-4
        f_lo = secular_func(t_lo, Delta_S, D_S)
    t_hi = 0.2
    f_hi = secular_func(t_hi, Delta_S, D_S)
    # Both ends valid and opposite sign -> root exists.
    def valid(f):
        return f is not None
    if valid(f_lo) and valid(f_hi) and f_lo * f_hi <= 0:
        a = t_lo
        b = t_hi
        fa = f_lo
        fb = f_hi
        for _ in range(80):
            m = (a + b) / 2.0
            fm = secular_func(m, Delta_S, D_S)
            if fm is None:
                break
            if abs(fm) < 1e-14:
                return m
            if fa * fm <= 0:
                b = m
                fb = fm
            else:
                a = m
                fa = fm
        return (a + b) / 2.0
    # No clear root -> surface does not order (t_c = 0).
    return 0.0

rows = []
for i in range(-10, 51):
    Delta_S = round(i / 10.0, 1)
    tc_pure = find_tc(Delta_S, 0.0)
    tc_amorph = find_tc(Delta_S, 2.0)
    rows.append([Delta_S, float(tc_pure), 'pure'])
    rows.append([Delta_S, float(tc_amorph), 'amorphized'])

with open('$OUTDIR/phase_diagram.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Delta_S', 't_c', 'param_label'])
    writer.writerows(rows)
PYEOF

# === solve block: critical_values.csv ===
echo "critical_values.csv already written by compute script"

# === solve block: reentrant_curve.csv ===
echo "reentrant_curve.csv already written by compute script"

# === solve finalize ===
python3 /solution/compute.py
