#!/usr/bin/env python3
""" Reference oracle for fracture mechanics paper.
    Generates I_vs_x0.csv and scaling_verification.csv
    using the standard three-point bend geometry factor F(x)
    for S/W=4 and the integral relation Eq.(8)."""
import csv
import numpy as np
from scipy.integrate import quad

# ----------------------------------------------------------------------
# Geometry factor F(x) for three-point bend with S/W=4.
# Derived from the standard SIF formula (Tada et al.):
#   K_I = (P S)/(B W^(3/2)) * f(x)
#   f(x) = 1.5 * sqrt(x) * (1.99 - x*(1-x)*(2.15 - 3.93*x + 2.7*x^2))
#                / ((1+2*x)*(1-x)^(3/2))
# With   K_I = sigma sqrt(pi a) F(x)  and  sigma = alpha P/(B W),
#   alpha = 1.5*S/W = 6  (for S=4W).
# result:  F(x) = (1/sqrt(pi)) * num / den,
#   num = 1.99 - x*(1-x)*(2.15 - 3.93*x + 2.7*x^2)
#   den = (1+2*x)*(1-x)^(3/2)
# ----------------------------------------------------------------------
def F(x):
    if x <= 0.0 or x >= 1.0:
        return np.inf if x == 1.0 else 0.0
    num = 1.99 - x * (1.0 - x) * (2.15 - 3.93*x + 2.7*x*x)
    den = (1.0 + 2.0*x) * (1.0 - x) ** 1.5
    return (1.0 / np.sqrt(np.pi)) * num / den

# ----------------------------------------------------------------------
# Integrand for I(x0,n):  [ sqrt(x0)*F(x0) / ( sqrt(x)*F(x) ) ]^n
# ----------------------------------------------------------------------
def integrand(x, x0, n):
    ratio = np.sqrt(x0) * F(x0) / (np.sqrt(x) * F(x))
    return ratio ** n

# ----------------------------------------------------------------------
# Safe integration from x0 to 1.  Singularity at x=1 is integrable.
# ----------------------------------------------------------------------
def compute_I(x0, n, limit=200):
    # x0 near 0 or 1?  Avoid x0=0 (degenerate) and x0=1 (zero length).
    # Integration: use quad with point at 1 for singularity.
    res, _ = quad(integrand, x0, 1.0, args=(x0, n),
                  points=[1.0], limit=limit)
    return res

OUTDIR = "/app/outputs"

# ======================================================================
# Step 1:  I_vs_x0.csv
# ======================================================================
x0_vals = np.linspace(0.01, 0.90, 90)   # 90 points; safe range
n_vals = [5, 10, 20]

with open(f"{OUTDIR}/I_vs_x0.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["x0", "n", "I_value"])
    for n in n_vals:
        for x0 in x0_vals:
            I = compute_I(x0, n)
            writer.writerow([f"{x0:.6f}", n, f"{I:.12e}"])

# ======================================================================
# Step 2:  scaling_verification.csv
#   Large-crack regime (x0 > 0.05): fix x0 constant, vary W.
#   Small-crack regime (x0 < 0.05): fix W, vary a0.
#   Use K* = K0 = 0.28 MPa sqrt(m), a* = 1.0 mm (arbitrary, only
#   ratios matter), and n = 16 (paper’s experimental exponent).
# ======================================================================
Kstar = 0.28          # MPa * sqrt(m)
astar = 1.0           # mm
n_exp = 16

rows = []

# --- Large cracks: constant x0 and K_Ii, different W ---
x0_large = [0.10, 0.15]   # > 0.05
W_large  = [10.0, 20.0, 40.0]  # mm
K_Ii = 0.5               # MPa * sqrt(m)

for x0 in x0_large:
    I_val = compute_I(x0, n_exp)
    denominator = (K_Ii / Kstar) ** n_exp
    for W in W_large:
        a0 = x0 * W
        T_f = (W * I_val / astar) / denominator
        rows.append((W, a0, K_Ii, T_f))

# --- Small cracks: constant W and K_Ii, different a0 (x0 < 0.05) ---
a0_small = [0.1, 0.2, 0.5, 1.0, 2.0]   # mm
W_small  = 40.0                          # mm
for a0 in a0_small:
    x0 = a0 / W_small
    I_val = compute_I(x0, n_exp)
    T_f = (W_small * I_val / astar) / denominator
    rows.append((W_small, a0, K_Ii, T_f))

with open(f"{OUTDIR}/scaling_verification.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["W", "a0", "K_Ii", "T_f"])
    for W, a0, K, Tf in rows:
        writer.writerow([f"{W:.3f}", f"{a0:.6f}", f"{K:.6f}", f"{Tf:.12e}"])

print("Oracle artifacts written successfully.")
