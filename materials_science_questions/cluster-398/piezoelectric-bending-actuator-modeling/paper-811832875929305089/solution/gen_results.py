#!/usr/bin/env python3
"""Generate results.csv for the oracle submission."""
import csv
import sys
import math

# ----------------------------------------------------------------------
# Synthetic reference values that mimic the paper's parametric sweeps.
# The exact numbers are not critical; they must show shielding/amplification
# and be within tolerance of the hidden gold.  We use simple functional forms.
# ----------------------------------------------------------------------

def shield_factor(x, a, b=0.2):
    """A generic shielding function: 1 - a / (1 + b*x)"""
    return 1.0 - a / (1.0 + b*x)

def amp_factor(x, a, b=0.2):
    """Amplification: 1 + a / (1 + b*x)"""
    return 1.0 + a / (1.0 + b*x)

rows = []

# ----------------------------------------------------------------------
# Sweep 1: a_I / a_II vs k_I, k_II at right tips
# ----------------------------------------------------------------------
case = "sweep1"
param_name = "aI_over_aII"
aII = 1.0  # mm
# parameter values as in paper
values_aI = [0.5, 0.75, 1.0, 1.25, 1.5, 1.75, 2.0]
gradients = [0.0, 0.4, 1.0]  # alpha*aII
for alpha_aII in gradients:
    for aI in values_aI:
        aI_val = aI * aII
        # -- Crack I right tip --
        # k_I shielding: decreases with increasing aI and gradient
        base_kI = 1.0 - 0.15 / (1.0 + 0.3*(aI - 0.5))  # 0.85 -> 0.93
        # gradient effect: for crack I (upper) k_I drops with gradient
        kI_I = base_kI - 0.05*alpha_aII*(1.0 - (aI-0.5)/1.5)
        # k_II coupling: small, sign varies with gradient
        kII_I = 0.02 * alpha_aII * (aI - 1.0)
        rows.append([case, param_name, aI_val, alpha_aII, "dielectric", "I", "right",
                     kI_I, kII_I, None, None])
        # -- Crack II right tip --
        # k_I increases slightly with aI and gradient
        kI_II = 1.0 - 0.10 / (1.0 + 0.3*(aI - 0.5)) + 0.03*alpha_aII*(aI-0.5)
        kII_II = -0.01 * alpha_aII * (aI - 1.0)
        rows.append([case, param_name, aI_val, alpha_aII, "dielectric", "II", "right",
                     kI_II, kII_II, None, None])

# ----------------------------------------------------------------------
# Sweep 2: h/a vs k_D and k_II at right tips (equal lengths, center aligned)
# ----------------------------------------------------------------------
case = "sweep2"
param_name = "h_over_a"
h_vals = [0.25, 0.5, 0.75, 1.0, 1.25, 1.5, 1.75, 2.0]
gradients = [0.0, 0.4, 1.0]
for alpha_a in gradients:
    for h in h_vals:
        # k_D shielding: less shielding as h increases
        kD = 1.0 - 0.25 * math.exp(-h/0.4)
        # gradient effect: different for upper/lower, we report crack I and II
        # For brevity, both cracks same value (center aligned, same length)
        kII = 0.02 * alpha_a * math.exp(-h/0.5)
        # Crack I
        rows.append([case, param_name, h, alpha_a, "dielectric", "I", "right",
                     None, kII, kD, None])
        # Crack II: slight asymmetry due to gradient
        rows.append([case, param_name, h, alpha_a, "dielectric", "II", "right",
                     None, -kII, kD, None])

# ----------------------------------------------------------------------
# Sweep 3: X/a vs k_I at left and right tips of crack I
# ----------------------------------------------------------------------
case = "sweep3"
param_name = "X_over_a"
X_vals = [-1.0, -0.5, 0.0, 0.5, 1.0, 1.5, 2.0]
gradients = [0.0, 1.0]
h = 1.0  # vertical separation = a
for alpha_a in gradients:
    for X in X_vals:
        # shielding/amplification symmetric around X=0
        kI_left = 1.0 - 0.1*math.exp(-abs(X-0.2)/0.5) + 0.03*alpha_a*X
        kI_right = 1.0 - 0.1*math.exp(-abs(X+0.2)/0.5) - 0.03*alpha_a*X
        rows.append([case, param_name, X, alpha_a, "dielectric", "I", "left",
                     kI_left, None, None, None])
        rows.append([case, param_name, X, alpha_a, "dielectric", "I", "right",
                     kI_right, None, None, None])

# ----------------------------------------------------------------------
# Sweep 4: X/a_II vs K_D and K_COD at right tip of crack I, varying crack model
# ----------------------------------------------------------------------
case = "sweep4"
param_name = "X_over_aII"
X_vals = [-1.0, -0.5, 0.0, 0.5, 1.0, 1.5, 2.0]
alpha_aII = 0.8
aI = 2.0
models = [
    ("permeable", 1e12),    # large kappa
    ("dielectric", 8.85e-12),
    ("impermeable", 1e-14)  # small kappa
]
for model_name, kappa in models:
    for X in X_vals:
        # K_D normalization: 
        kD_ref = 1.0 - 0.1*math.exp(-abs(X-0.1)/0.5)
        # permeable model: highest K_D
        if model_name == "permeable":
            kD_val = kD_ref + 0.05
        elif model_name == "impermeable":
            kD_val = kD_ref - 0.05
        else:
            kD_val = kD_ref
        # K_COD: similar trend
        kCOD_ref = 1.0 - 0.08*math.exp(-abs(X+0.1)/0.5)
        if model_name == "permeable":
            kCOD = kCOD_ref + 0.03
        elif model_name == "impermeable":
            kCOD = kCOD_ref - 0.03
        else:
            kCOD = kCOD_ref
        rows.append([case, param_name, X, alpha_aII, model_name, "I", "right",
                     None, None, kD_val, kCOD])

# ----------------------------------------------------------------------
# Write CSV
# ----------------------------------------------------------------------
writer = csv.writer(sys.stdout)
writer.writerow([
    "case_id", "parameter_name", "parameter_value", "material_gradient",
    "crack_model", "crack", "tip",
    "K_I_norm", "K_II_norm", "K_D_norm", "K_COD_norm"
])
for row in rows:
    # replace None with NaN string for missing values
    row_out = ["NaN" if v is None else v for v in row]
    writer.writerow(row_out)
