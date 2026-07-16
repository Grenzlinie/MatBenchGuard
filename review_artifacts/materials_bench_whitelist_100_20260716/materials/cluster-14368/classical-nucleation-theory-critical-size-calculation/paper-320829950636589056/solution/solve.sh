#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

python3 << 'PYEOF' > "$OUTDIR/bubble_calculation.json"
import math, json, sys

sigma = 1.200
n_s0_mol_pct = 2.20e-3
n_s0 = n_s0_mol_pct / 100.0
epsilon_eV = 0.6027
p0 = 1.0   # atm, as required by the paper's formula
T = 300.0
N_total = 2.0e23
rho_bub = 1.0e13
nu = 0.5

kB_J = 1.380649e-23
kB_eV = 8.617333262145e-5

kT_eV = kB_eV * T
kT_J = kB_J * T

# 1. Threshold radius
num = 3.0 * (nu**2) * n_s0 * (kT_eV**nu) * math.exp(-epsilon_eV / kT_eV)
den = 64.0 * math.pi * (p0**nu) * (sigma**(1.0 - nu))
frac = num / den
r_b_star_m = 2.0 * (frac ** (1.0 / (nu + 2.0)))
r_b_star_um = r_b_star_m * 1.0e6

# 2. Threshold molecules per bubble
nb_star = (8.0 * math.pi / 3.0) * (sigma / kT_J) * (r_b_star_m ** 2)

# 3. Threshold concentration per unit volume
nt_star_per_bubble = ((nu + 2.0) / (nu**2)) * nb_star
N_t_star = rho_bub * nt_star_per_bubble

# 4. Supersaturation
Delta = (N_total - N_t_star) / N_t_star

# 5. Solve x = r_eq / r_b_star from Eq. (7)
c1 = nu / (nu + 2.0)
c2 = 2.0 / (nu + 2.0)
def f(x):
    return (Delta + 1.0) - c1 * (x**2) - c2 * (x**(-nu))

# f(1) = Delta + 1 - c1 - c2 = Delta > 0, so we need x>1 where f becomes negative
a = 1.0
b = a * 2.0
while f(b) > 0:
    b *= 2.0
for _ in range(100):
    m = (a + b) / 2.0
    fm = f(m)
    if fm == 0.0:
        break
    if fm > 0:
        a = m
    else:
        b = m
x_eq = (a + b) / 2.0

# 6. Equilibrium radius
r_eq_m = x_eq * r_b_star_m
r_eq_um = r_eq_m * 1.0e6

result = {
    "r_b_star_um": r_b_star_um,
    "ratio_r_eq_over_r_b_star": x_eq,
    "r_eq_um": r_eq_um
}
json.dump(result, sys.stdout, indent=2)
PYEOF
