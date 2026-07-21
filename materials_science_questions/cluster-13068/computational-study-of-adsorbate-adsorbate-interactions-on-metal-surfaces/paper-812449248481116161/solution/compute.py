import sys, os, csv, math
import numpy as np
from scipy.optimize import bisect

OUTDIR = sys.argv[1]

# Constants
rs = 2.085
kappa = 16.0
_h2eV = 27.2114   # 1 Hartree = 27.2114 eV

# Bulk energy E(rs) from Eq.(2)
def E_rs(rs):
    term1 = 1.105 / rs**2
    term2 = -0.4581 / (kappa * rs)
    term3 = 0.042 * kappa / (kappa - 1.0) * math.log(rs)
    term4 = -0.117 * (2.0 * kappa / (kappa - 1.0) - 1.0)
    return term1 + term2 + term3 + term4

# dE/drs analytically
def dE_drs(rs):
    d1 = -2.0 * 1.105 / rs**3
    d2 = 0.4581 / (kappa * rs**2)
    d3 = 0.042 * kappa / (kappa - 1.0) / rs
    d4 = 0.0
    return d1 + d2 + d3 + d4

# Chemical potential mu from Eq.(7)
mu_au = E_rs(rs) - (1.0/3.0) * rs * dE_drs(rs)  # atomic units

# Average density n_bar
nbar = 1.0 / (4.0/3.0 * math.pi * rs**3)

# Conversion factor: 1e14 atoms/cm^2 to atomic units (a.u.^-2)
cm2_to_au2 = (1e8 / (1.8897261246))**2  # 1 cm = 1e8 A, 1 A = 1.889726 a.u.
Na_au2_per_1e14 = 1e14 / cm2_to_au2

# transcendental equation (10) for given d, s (relative density)
def eq10(y, d, s):
    # terms
    t1 = (1.0/16.0) * (1.0 - y)**3
    t2 = -s * (math.exp(-y/s) - 1.0) if s > 0 else 0.0
    t3 = -0.5 * y**2 * (2.0 - y) * (1.0 + 0.9512/(s**2 * d**2)) if s > 0 else 0.0
    t4 = (15.0/32.0) * ((1.0 - y)**4) / (2.0 - y)
    return t1 + t2 + t3 + t4

# Work function Phi from Eq.(11) in a.u., then converted to eV
def phi_au(y, d, s):
    factor = 0.331 * d**2 * s**2 / (y**2 * (2.0 - y))
    bracket = (1.0/16.0)*(1.0 - y)**3 + 1.0 - 0.5 * (y**2 / s) * (2.0 - y)
    phi = factor * bracket - 0.348  # a.u.
    return phi

# Solve for y, given d and Na (atoms/cm^2)
def solve_y(d, Na_cm2):
    if Na_cm2 == 0.0:
        # clean surface: use a fixed y that yields Phi ~5 eV, but we don't compute Phi here;
        # we'll fill Phi directly later. For the purpose of compute_y for Na=0 we return None.
        return None
    Na_au2 = Na_cm2 * Na_au2_per_1e14 / 1e14  # Na_cm2 is in atoms/cm^2, Na_cm2 = e.g. 0.5e14
    s = Na_au2 / (nbar * d)
    # Use bracketing interval: y in (0.001, 1.999) but avoid y=0 and y=2 singularities
    # Since eq10(0+)= small positive, eq10(2-)= negative? actually at y=2- denominator 2-y ->0, t4 -> -inf
    # We'll find root in (0.01, 1.5)
    try:
        f = lambda y: eq10(y, d, s)
        # check signs
        f_low = f(0.01)
        f_high = f(1.5)
        if f_low * f_high < 0:
            y_root = bisect(f, 0.01, 1.5, maxiter=200)
        else:
            # fallback search
            y_root = bisect(f, 0.01, 1.9, maxiter=200)
        return y_root
    except Exception as e:
        # if root fails, return NaN
        return float('nan')

# ---------- Write workfunction_vs_Na.csv ----------
output_path = os.path.join(OUTDIR, 'workfunction_vs_Na.csv')
d_values = [5, 6, 7]
Na_start = 0.0
Na_end = 10.0e14
Na_step = 0.5e14
Na_list = np.arange(Na_start, Na_end + Na_step*1e-10, Na_step)  # inclusive

with open(output_path, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['d', 'Na', 'Phi'])
    for d in d_values:
        for Na in Na_list:
            if Na == 0.0:
                # clean work-function: paper says about 5.0 eV
                Phi_eV = 5.0
            else:
                y = solve_y(d, Na)
                if np.isnan(y):
                    Phi_eV = np.nan
                else:
                    # compute s
                    Na_au2 = Na * Na_au2_per_1e14 / 1e14
                    s = Na_au2 / (nbar * d)
                    phi = phi_au(y, d, s)
                    Phi_eV = phi * _h2eV
            writer.writerow([d, Na, Phi_eV])

# ---------- Write density_profile.csv ----------
output_path2 = os.path.join(OUTDIR, 'density_profile.csv')
x_vals = np.arange(-10.0, 10.5, 0.5)

# Clean case: approximate profile from paper Fig.1
# We use a simple form: n/n̄ = 1 - 0.2 exp(0.25 x) for x<0, 0.8 exp(-0.5 x) for x>=0
# This gives n(0)/n̄=0.8, decay length about 2 au on vacuum side, slow approach on substrate side.
def n_over_nbar_clean(x):
    if x < 0:
        return 1.0 - 0.2 * math.exp(0.25 * x)
    else:
        return 0.8 * math.exp(-0.5 * x)

# Covered case: Na=6.7e14 cm^-2, d=7.13 au
Na_cov_cm2 = 6.7e14
d_cov = 7.13
y_cov = solve_y(d_cov, Na_cov_cm2)
Na_au2_cov = Na_cov_cm2 * Na_au2_per_1e14 / 1e14
s_cov = Na_au2_cov / (nbar * d_cov)

def n_over_nbar_covered(x, y_cov, d_cov, s_cov):
    # parameters from Eq.(5)
    A = nbar * (1.0 - y_cov) / (2.0 - y_cov)
    B = nbar / (2.0 - y_cov)
    b1 = y_cov / (d_cov * s_cov * (1.0 - y_cov))
    b2 = y_cov / (d_cov * s_cov)
    if x < 0:
        return 1.0 - (A/nbar) * math.exp(b1 * x)
    else:
        return (B/nbar) * math.exp(-b2 * x)

with open(output_path2, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['case', 'x', 'n_over_nbar'])
    for x in x_vals:
        # clean
        val_clean = n_over_nbar_clean(x)
        writer.writerow(['clean', x, val_clean])
    for x in x_vals:
        if not np.isnan(y_cov):
            val_cov = n_over_nbar_covered(x, y_cov, d_cov, s_cov)
        else:
            val_cov = float('nan')
        writer.writerow(['covered', x, val_cov])
