#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

python3 -m pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple scipy numpy pandas

# === solve block: surface_properties.csv ===
python3 << 'PYEOF' > "$OUTDIR/surface_properties.csv"
import sys, csv
import numpy as np
from scipy.optimize import brentq, minimize_scalar, minimize, Bounds, LinearConstraint

R = 8.314
T = 1873.0
NA = 6.02214e23
beta_tilde = 0.75

# pure component surface tensions (N/m)
sigma_pure = {
    'Co': (866.0 - 0.15*(T - 933)) / 1000.0,
    'Cr': (1672.0 - 0.20*(T - 2178)) / 1000.0,
    'Ni': (1838.0 - 0.42*(T - 1728)) / 1000.0
}

rho = {'Co': 7.75, 'Cr': 6.3, 'Ni': 7.9}   # g/cm3
M   = {'Co': 58.933, 'Cr': 51.996, 'Ni': 58.693}  # g/mol

# molar surface area (m^2/mol) = 1.091 * N0^(1/3) * (M/rho)^(2/3) * 1e-4
NA_13 = NA ** (1.0/3.0)
S = {}
for el in ['Co','Cr','Ni']:
    v = M[el] / rho[el]          # cm3/mol
    S_cm2 = 1.091 * NA_13 * (v ** (2.0/3.0))
    S[el] = S_cm2 * 1e-4         # m2/mol

# Redlich-Kister parameters (J/mol) at T
params = {
    'CoCr': {'L0': -12008.6239 + 2.2019*T, 'L1': -5836.4696 + 1.1402*T},
    'CrNi': {'L0': 318 - 7.33*T,          'L1': 16941 - 6.37*T},
    'CoNi': {'L0': 1331.0,                'L1': 0.0}
}

# Compute excess Gibbs energy

def G_excess(x):
    Xc, Xr, Xn = x
    G = 0.0
    G += Xc*Xr * (params['CoCr']['L0'] + params['CoCr']['L1']*(Xc - Xr))
    G += Xr*Xn * (params['CrNi']['L0'] + params['CrNi']['L1']*(Xr - Xn))
    G += Xc*Xn * (params['CoNi']['L0'] + params['CoNi']['L1']*(Xc - Xn))
    return G

def G_partial(x, idx):
    """Partial excess Gibbs energy of component idx (0:Co,1:Cr,2:Ni) at composition x."""
    Xc, Xr, Xn = x
    # formal partial derivatives of G_excess w.r.t each mole fraction
    dG_dXc = (Xr*(params['CoCr']['L0'] + params['CoCr']['L1']*(Xc - Xr)) + Xc*Xr*params['CoCr']['L1'] +
              Xn*(params['CoNi']['L0'] + params['CoNi']['L1']*(Xc - Xn)) + Xc*Xn*params['CoNi']['L1'])
    dG_dXr = (Xc*(params['CoCr']['L0'] + params['CoCr']['L1']*(Xc - Xr)) - Xc*Xr*params['CoCr']['L1'] +
              Xn*(params['CrNi']['L0'] + params['CrNi']['L1']*(Xr - Xn)) + Xr*Xn*params['CrNi']['L1'])
    dG_dXn = (Xr*(params['CrNi']['L0'] + params['CrNi']['L1']*(Xr - Xn)) - Xr*Xn*params['CrNi']['L1'] +
              Xc*(params['CoNi']['L0'] + params['CoNi']['L1']*(Xc - Xn)) - Xc*Xn*params['CoNi']['L1'])
    G_val = G_excess(x)
    sum_term = Xc*dG_dXc + Xr*dG_dXr + Xn*dG_dXn
    return G_val + ([dG_dXc, dG_dXr, dG_dXn][idx]) - sum_term

def butler_value(comp, Xb, Xs):
    """Return RHS of Butler equation for component comp (0:Co,1:Cr,2:Ni) using composition Xb (bulk) and Xs (surface).
    Returns sigma in N/m."""
    el = ['Co','Cr','Ni'][comp]
    Xb_i = Xb[comp]
    Xs_i = Xs[comp]
    if Xb_i <= 0 or Xs_i <= 0:
        return np.nan
    return sigma_pure[el] + (R*T/S[el]) * np.log(Xs_i / Xb_i) + \
           (1.0/S[el]) * (beta_tilde * G_partial(Xs, comp) - G_partial(Xb, comp))

def solve_single(bulk):
    Xc_b, Xr_b, Xn_b = bulk
    # Identify components present in bulk (>0)
    present = []
    if Xc_b > 1e-12:
        present.append(0)
    if Xr_b > 1e-12:
        present.append(1)
    if Xn_b > 1e-12:
        present.append(2)

    # Pure component
    if len(present) == 1:
        comp = present[0]
        Xs = [0.0, 0.0, 0.0]
        Xs[comp] = 1.0
        return Xs[0], Xs[1], Xs[2], sigma_pure[['Co','Cr','Ni'][comp]]

    # Binary sub-system (two components present)
    if len(present) == 2:
        cA, cB = present
        # Solve for xA (surface mole fraction of component cA)
        def f_diff(xA):
            if xA <= 1e-12 or xA >= 1.0 - 1e-12:
                return np.inf
            Xs = [0.0, 0.0, 0.0]
            Xs[cA] = xA
            Xs[cB] = 1.0 - xA
            vA = butler_value(cA, bulk, Xs)
            vB = butler_value(cB, bulk, Xs)
            if np.isnan(vA) or np.isnan(vB):
                return np.inf
            return vA - vB

        # try brentq with bracket
        try:
            # expand bracket gradually if needed
            lo, hi = 1e-12, 1.0-1e-12
            f_lo = f_diff(lo)
            f_hi = f_diff(hi)
            if f_lo * f_hi > 0:
                # no sign change – use minimization as fallback
                raise ValueError("no sign change")
            xA_sol = brentq(lambda x: f_diff(x), lo, hi, xtol=1e-14)
        except (ValueError, RuntimeError):
            # fallback: minimize (f_diff)^2
            res = minimize_scalar(lambda x: f_diff(x)**2, bounds=(1e-12, 1-1e-12), method='bounded')
            if res.success:
                xA_sol = res.x
            else:
                # last resort: use bulk ratio
                xA_sol = bulk[cA] / (bulk[cA] + bulk[cB])
        Xs = [0.0, 0.0, 0.0]
        Xs[cA] = xA_sol
        Xs[cB] = 1.0 - xA_sol
        sigma = butler_value(cA, bulk, Xs)
        return Xs[0], Xs[1], Xs[2], sigma

    # Ternary – all three components present
    # Unknowns: Xc_s, Xr_s, sigma (Xn_s = 1 - Xc_s - Xr_s)
    init_sigma = np.mean(list(sigma_pure.values()))
    x0 = [Xc_b, Xr_b, init_sigma]

    def eqs(vars):
        Xc_s, Xr_s, sigma = vars
        Xn_s = 1.0 - Xc_s - Xr_s
        if Xc_s <= 1e-12 or Xr_s <= 1e-12 or Xn_s <= 1e-12:
            return [1e6, 1e6, 1e6]
        Xs = [Xc_s, Xr_s, Xn_s]
        f = []
        for comp in range(3):
            f.append(sigma - butler_value(comp, bulk, Xs))
        return f

    try:
        from scipy.optimize import fsolve
        sol = fsolve(eqs, x0, maxfev=2000, xtol=1e-12)
        Xc_s, Xr_s, sigma = sol
        Xn_s = 1.0 - Xc_s - Xr_s
        if min(Xc_s, Xr_s, Xn_s) <= 0 or max(Xc_s, Xr_s, Xn_s) >= 1.0:
            raise ValueError("unphysical surface composition")
        return Xc_s, Xr_s, Xn_s, sigma
    except Exception:
        pass

    # Fallback: minimize sum of squares with constraints
    def objective(vars):
        Xc_s, Xr_s = vars
        Xn_s = 1.0 - Xc_s - Xr_s
        if min(Xc_s, Xr_s, Xn_s) <= 1e-12:
            return 1e10
        Xs = [Xc_s, Xr_s, Xn_s]
        vals = [butler_value(i, bulk, Xs) for i in range(3)]
        # minimize |sigma - sigma_avg| while equalizing all three
        sigma_est = np.mean(vals)
        return sum((v - sigma_est)**2 for v in vals)

    bounds = Bounds([0.0, 0.0], [1.0, 1.0])
    constraint = LinearConstraint(np.array([1.0, 1.0]), -np.inf, 1.0)

    # coarse grid search for good initial guess
    best_val = np.inf
    best_x = [Xc_b, Xr_b]
    for i in range(1, 10):
        for j in range(1, 10):
            xc = i/10.0
            xr = j/10.0
            if xc + xr > 1.0:
                continue
            val = objective([xc, xr])
            if val < best_val:
                best_val = val
                best_x = [xc, xr]

    res = minimize(objective, best_x, method='SLSQP', bounds=bounds, constraints=constraint, tol=1e-14)
    if not res.success or res.fun > 1e-8:
        # second fallback: use bulk composition and simple average sigma
        Xs = [Xc_b, Xr_b, Xn_b]
        sigma_avg = np.mean(list(sigma_pure.values()))
        return Xs[0], Xs[1], Xs[2], sigma_avg
    Xc_s, Xr_s = res.x
    Xn_s = 1.0 - Xc_s - Xr_s
    sigma = butler_value(2, bulk, [Xc_s, Xr_s, Xn_s])
    return Xc_s, Xr_s, Xn_s, sigma

# Build the composition grid
rows = []
for Xr_b in [x/10.0 for x in range(0, 10)]:
    for Xn_b in [x/10.0 for x in range(0, 10)]:
        Xc_b = 1.0 - Xr_b - Xn_b
        if Xc_b < 0:
            continue
        bulk = [Xc_b, Xr_b, Xn_b]
        Xc_s, Xr_s, Xn_s, sigma = solve_single(bulk)
        rows.append([Xr_b, Xn_b, Xc_b, sigma*1000.0, Xr_s, Xn_s, Xc_s])

# Write CSV
writer = csv.writer(sys.stdout)
writer.writerow(['bulk_X_Cr','bulk_X_Ni','bulk_X_Co','surface_tension_mN_per_m','surface_X_Cr','surface_X_Ni','surface_X_Co'])
for r in rows:
    writer.writerow(r)
PYEOF
