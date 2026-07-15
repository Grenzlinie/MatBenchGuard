#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: growth_curve.csv ===
# Compute growth_curve.csv by solving the modified Kelvin equation
python3 - << 'PYEOF'
import csv, math, sys

# Constants
M_w = 18.015          # g/mol
M_o = 98.079          # g/mol
R_gas = 8.314         # J/(mol·K)
T_K = 298.15          # K
rho_pure = 1.84       # g/cm^3, pure H2SO4

# Dry radii in µm
dry_radii = [0.001, 0.005, 0.05, 0.1, 0.5]
RH_pcts = [0, 10, 30, 50, 70, 80, 90, 100, 101, 110]

# Table 1 data: X (mass%), rho (g/cm^3), drho_dx (scaled, x10^3), sigma (dyn/cm), dsigma_dx (scaled, x10^2), a_w
table = [
    (0.5, 1.000, 8.1, 72.0, 12.0, 0.998),
    (1.0, 1.004, 7.4, 72.1,  8.6, 0.996),
    (5.0, 1.030, 6.7, 72.3,  5.5, 0.982),
    (10.0, 1.064, 7.0, 72.6,  8.0, 0.958),
    (20.0, 1.136, 7.5, 73.7, 11.4, 0.880),
    (25.0, 1.175, 7.9, 74.3, 11.3, 0.823),
    (40.0, 1.299, 8.8, 75.8, 10.0, 0.555),
    (50.0, 1.391, 9.8, 76.8,  6.4, 0.340),
    (66.0, 1.560, 11.3, 75.2, -30.0, 0.075),
    (85.0, 1.773, 8.7, 68.7, -72.0, 0.001),
]

# Separate arrays for interpolation
X_vals = [r[0] for r in table]
rho_vals = [r[1] for r in table]
drho_dx_scaled = [r[2] for r in table]   # actual = scaled / 1000
sigma_vals = [r[3] for r in table]
dsigma_dx_scaled = [r[4] for r in table]  # actual = scaled / 100
a_w_vals = [r[5] for r in table]

def interp(x, xs, ys):
    # linear interpolation, assume xs sorted
    if x <= xs[0]: return ys[0]
    if x >= xs[-1]: return ys[-1]
    for i in range(len(xs)-1):
        if xs[i] <= x <= xs[i+1]:
            t = (x - xs[i]) / (xs[i+1] - xs[i])
            return ys[i] + t * (ys[i+1] - ys[i])
    return ys[-1]

def compute_radius(r0_um, rh_pct):
    if rh_pct == 0:
        return r0_um
    Sw = rh_pct / 100.0
    # acid mass (g)
    r0_cm = r0_um * 1e-4
    V0_cm3 = (4/3)*math.pi * r0_cm**3
    m_acid = V0_cm3 * rho_pure
    # Search X in [0.5, 85] to solve equation
    # define function F(X) = ln(Sw/a_w) - RHS
    def F(X):
        if X < X_vals[0] or X > X_vals[-1]:
            return None
        a_w = interp(X, X_vals, a_w_vals)
        if a_w <= 0 or Sw <= 0:
            return None
        lhs = math.log(Sw / a_w)
        rho = interp(X, X_vals, rho_vals)
        sigma = interp(X, X_vals, sigma_vals)
        drho_dx = interp(X, X_vals, drho_dx_scaled) / 1000.0
        dsigma_dx = interp(X, X_vals, dsigma_dx_scaled) / 100.0
        # droplet radius from mass conservation
        total_mass = m_acid * (100.0 / X)
        V_cm3 = total_mass / rho
        r_cm = (3*V_cm3/(4*math.pi))**(1/3)
        # correction factor
        corr = 1.0 + (X / rho) * drho_dx - 1.5 * (X / sigma) * dsigma_dx
        rhs = (2 * M_w * sigma) / (R_gas * T_K * rho) * (1.0 / r_cm) * corr
        return lhs - rhs
    # scan for sign change
    best_X = None
    best_val = None
    min_abs = float('inf')
    for X in [x/10.0 for x in range(5, 851)]:   # 0.5 to 85.0 step 0.1
        v = F(X)
        if v is None:
            continue
        if abs(v) < min_abs:
            min_abs = abs(v)
            best_X = X
            best_val = v
        # stop if close to zero
        if abs(v) < 1e-12:
            best_X = X
            break
    # If no zero crossing found (should not happen), use best scan point
    X_eq = best_X
    # compute radius at this X
    rho_eq = interp(X_eq, X_vals, rho_vals)
    total_mass = m_acid * (100.0 / X_eq)
    V_eq = total_mass / rho_eq
    r_eq_cm = (3*V_eq/(4*math.pi))**(1/3)
    return r_eq_cm * 1e4   # convert to µm

# Write CSV
with open('/app/outputs/growth_curve.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['dry_radius_um', 'rh_pct', 'eq_radius_um'])
    for r0 in dry_radii:
        for rh in RH_pcts:
            eq = compute_radius(r0, rh)
            writer.writerow([r0, rh, eq])

print('growth_curve.csv written')
PYEOF
