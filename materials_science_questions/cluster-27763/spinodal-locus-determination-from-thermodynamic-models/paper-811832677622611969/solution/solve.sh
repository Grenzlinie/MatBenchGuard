#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
export OUTDIR="${OUTDIR:-/app/outputs}"
mkdir -p "$OUTDIR"
python3 -m pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple numpy scipy
python3 /solution/compute.py /tmp

# === solve block: phase_boundary_data.csv ===
#!/bin/bash
python3 -m pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple numpy scipy
python3 << 'PYEOF'
import csv, numpy as np
from scipy.optimize import fsolve, minimize_scalar

param_sets = [
    ('Lambda=350_eta_c=-0.05_eta_cc=0.04', 350, -0.05, 0.04),
    ('Lambda=100_eta_c=-0.05_eta_cc=0.04', 100, -0.05, 0.04),
    ('Lambda=100_eta_c=-0.03_eta_cc=0',    100, -0.03, 0.00),
    ('Lambda=100_eta_c=-0.01_eta_cc=-0.04',100, -0.01, -0.04),
]

def eps(c, etac, etacc):
    return etac * c + 0.5 * etacc * c**2

def phi(c, Pi, t, Lam, etac, etacc):
    tiny = 1e-14
    return (t * (c * np.log(np.maximum(c, tiny)) + (1-c) * np.log(np.maximum(1-c, tiny)))
            + 2*c*(1-c) - 4.5*Pi**2 + 3*np.sqrt(Lam) * eps(c, etac, etacc) * Pi)

def dphi_dc(c, Pi, t, Lam, etac, etacc):
    tiny = 1e-14
    return (t * (np.log(np.maximum(c, tiny)) - np.log(np.maximum(1-c, tiny)))
            + 2 - 4*c + 3*np.sqrt(Lam) * (etac + etacc*c) * Pi)

def dphi_dP(c, Pi, t, Lam, etac, etacc):
    return -9*Pi + 3*np.sqrt(Lam) * eps(c, etac, etacc)

def equilibrium_eqs(vars, c_o, Pi_o, t, Lam, etac, etacc):
    ca, cb, Pa, Pb, z = vars
    eq1 = dphi_dc(ca, Pa, t, Lam, etac, etacc) - dphi_dc(cb, Pb, t, Lam, etac, etacc)
    eq2 = dphi_dP(ca, Pa, t, Lam, etac, etacc) - dphi_dP(cb, Pb, t, Lam, etac, etacc)
    eq3 = c_o - (z*cb + (1-z)*ca)
    eq4 = Pi_o - (z*Pb + (1-z)*Pa)
    Gpa = phi(ca, Pa, t, Lam, etac, etacc) - dphi_dc(ca, Pa, t, Lam, etac, etacc)*ca - dphi_dP(ca, Pa, t, Lam, etac, etacc)*Pa
    Gpb = phi(cb, Pb, t, Lam, etac, etacc) - dphi_dc(cb, Pb, t, Lam, etac, etacc)*cb - dphi_dP(cb, Pb, t, Lam, etac, etacc)*Pb
    eq5 = Gpa - Gpb
    return [eq1, eq2, eq3, eq4, eq5]

def solve_tie_line(c_o, Pi_o, t, Lam, etac, etacc, guess=None):
    if guess is None:
        guess = [c_o*0.9, c_o*1.1, Pi_o, Pi_o, 0.5]
    try:
        sol = fsolve(equilibrium_eqs, guess, args=(c_o, Pi_o, t, Lam, etac, etacc),
                     xtol=1e-12, maxfev=2000, full_output=False)
        ca, cb, Pa, Pb, z = sol
        # explicitly check for any None or non-finite in the solution
        if all(v is not None and np.isfinite(float(v)) for v in (ca, cb, Pa, Pb, z)):
            if 0.001 < ca < 0.999 and 0.001 < cb < 0.999 and 0 <= z <= 1:
                return (float(ca), float(cb), float(Pa), float(Pb), float(z))
    except Exception:
        pass
    return None

def t_spinodal(c, Pi, Lam, etac, etacc):
    if c <= 0.0 or c >= 1.0:
        return np.nan
    return c * (1-c) * (4 - Lam * (etac + etacc*c)**2 - 3 * etacc * np.sqrt(Lam) * Pi)

def is_finite_num(val):
    """Return True if value is a finite number (not None, not NaN, not Inf)."""
    try:
        v = float(val)
        return np.isfinite(v)
    except (TypeError, ValueError):
        return False

# Binodal data collection
binodal_rows = []
for pname, Lam, etac, etacc in param_sets:
    # Slice 1: constant Pi_o = 0.1 (t-c plane)
    Pi_o = 0.1
    for t in np.arange(0.05, 0.95, 0.025):
        prev = None
        for c_o in np.arange(0.05, 0.95, 0.05):
            sol = solve_tie_line(c_o, Pi_o, t, Lam, etac, etacc, guess=prev)
            if sol is not None:
                ca, cb, Pa, Pb, z = sol
                if all(is_finite_num(v) for v in (t, Pi_o, ca, cb, Pa, Pb, z)):
                    prev = sol
                    binodal_rows.append([pname, 't_c', round(float(t),6), Pi_o,
                                         round(ca,12), round(cb,12),
                                         round(Pa,12), round(Pb,12),
                                         round(z,12)])
    # Slice 2: constant t = 0.8 (c-P plane)
    t_fixed = 0.8
    for Pi_o in np.arange(0.0, 0.35, 0.01):
        prev = None
        for c_o in np.arange(0.05, 0.95, 0.05):
            sol = solve_tie_line(c_o, Pi_o, t_fixed, Lam, etac, etacc, guess=prev)
            if sol is not None:
                ca, cb, Pa, Pb, z = sol
                if all(is_finite_num(v) for v in (t_fixed, Pi_o, ca, cb, Pa, Pb, z)):
                    prev = sol
                    binodal_rows.append([pname, 'c_P', t_fixed, round(Pi_o,6),
                                         round(ca,12), round(cb,12),
                                         round(Pa,12), round(Pb,12),
                                         round(z,12)])

# Spinodal data collection
spinodal_rows = []
for pname, Lam, etac, etacc in param_sets:
    # Slice 1: constant Pi_o = 0.1
    Pi_o = 0.1
    for c in np.linspace(0.001, 0.999, 200):
        t_val = t_spinodal(c, Pi_o, Lam, etac, etacc)
        if is_finite_num(t_val) and 0 < t_val < 2.0:
            spinodal_rows.append([pname, 't_c', round(float(t_val),6), Pi_o, round(c,12)])
    # Slice 2: constant t = 0.8, solve for Pi_o
    t_fixed = 0.8
    for c in np.linspace(0.01, 0.99, 200):
        A = Lam * (etac + etacc*c)**2
        B = 3 * etacc * np.sqrt(Lam)
        denom = c * (1-c)
        if denom == 0 or np.abs(B) < 1e-14:
            continue
        Pi_o_candidate = (4 - A - t_fixed/denom) / B
        if is_finite_num(Pi_o_candidate) and 0 < Pi_o_candidate < 1.0:
            spinodal_rows.append([pname, 'c_P', t_fixed, round(float(Pi_o_candidate),6), round(c,12)])

# Critical points at Pi_o = 0.1
critical_rows = []
for pname, Lam, etac, etacc in param_sets:
    Pi_o = 0.1
    def obj(c):
        if c <= 0.001 or c >= 0.999:
            return -np.inf
        t_val = t_spinodal(c, Pi_o, Lam, etac, etacc)
        if not is_finite_num(t_val) or t_val <= 0:
            return -np.inf
        return t_val
    res = minimize_scalar(lambda c: -obj(c), bounds=(0.001, 0.999), method='bounded')
    if res.success:
        c_c = res.x
        t_c = t_spinodal(c_c, Pi_o, Lam, etac, etacc)
        if is_finite_num(t_c) and is_finite_num(c_c) and t_c > 0:
            critical_rows.append([pname, round(float(t_c),12), round(float(c_c),12), Pi_o])

# Write all CSV files to /tmp
def write_csv(filename, header, rows):
    with open(f'/tmp/{filename}', 'w', newline='') as f:
        w = csv.writer(f)
        w.writerow(header)
        for row in rows:
            w.writerow(row)

write_csv('phase_boundary_data.csv',
          ['param_set','slice_type','t','P_o','c_alpha','c_beta','P_alpha','P_beta','z'],
          binodal_rows)
write_csv('spinodal_data.csv',
          ['param_set','slice_type','t','P_o','c_spinodal'],
          spinodal_rows)
write_csv('critical_points.csv',
          ['param_set','t_c','c_c','P_o_c'],
          critical_rows)
PYEOF

cp /tmp/phase_boundary_data.csv "$OUTDIR/phase_boundary_data.csv"

# === solve block: spinodal_data.csv ===
#!/bin/bash
cp /tmp/spinodal_data.csv "$OUTDIR/spinodal_data.csv"

# === solve block: critical_points.csv ===
#!/bin/bash
cp /tmp/critical_points.csv "$OUTDIR/critical_points.csv"
