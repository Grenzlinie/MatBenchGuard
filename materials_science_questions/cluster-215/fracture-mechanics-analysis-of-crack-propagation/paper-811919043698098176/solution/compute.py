#!/usr/bin/env python3
"""
Compute critical plane predictions for the ±55° filament‑wound specimens.
Uses the paper's closed‑form expressions for Type I and Type II effective stresses.
σ22^max = 1 MPa is used as a reference (the absolute value cancels in the type decision).
"""
import csv
import math

OUTDIR = "/app/outputs"
OUTFILE = f"{OUTDIR}/critical_plane_predictions.csv"

# Static strengths (MPa)
SIGMA_I_F = 980.0
SIGMA_II_F = 48.0
TAU_II_F = 70.0

# Reference stress (common factor)
SIG22_MAX = 1.0

def r1(varsigma, lam):
    """Biaxiality factor r1."""
    num = (1.0 + varsigma) + math.sqrt((1.0 - varsigma)**2 + 4.0 * lam**2)
    den = (1.0 + varsigma) - math.sqrt((1.0 - varsigma)**2 + 4.0 * lam**2)
    if den == 0.0:
        return float('inf')
    return num / den

def r2(varsigma, lam):
    """Biaxiality factor r2."""
    if varsigma == 0.0:
        return float('inf')
    term = math.sqrt(1.0 + (2.0 * lam / varsigma)**2)
    num = 1.0 + term
    den = 1.0 - term
    if den == 0.0:
        return float('inf')
    return num / den

def sigma_I_t_max(varsigma, lam, R22, R12, sig22_max):
    """
    Return maximum tensile normal stress on Type I planes (σ_I,t^max).
    Follows Eqs 8a‑8i for the three loading groups; here σ22 != 0 always.
    """
    # sigma22 != 0 (first group)
    sig22_min = R22 * sig22_max
    
    # term A = (varsigma+1)/2 + sqrt(((varsigma-1)/2)^2 + lam^2)
    A_val = (varsigma + 1.0) / 2.0 + math.sqrt(((varsigma - 1.0) / 2.0)**2 + lam**2)
    # term B = (varsigma+1)/2 - sqrt(...)
    B_val = (varsigma + 1.0) / 2.0 - math.sqrt(((varsigma - 1.0) / 2.0)**2 + lam**2)
    
    r1_val = r1(varsigma, lam)
    
    # cases
    if r1_val <= R22 < 1.0:
        return A_val * sig22_max
    if R22 < r1_val and varsigma > lam**2:
        return A_val * sig22_max
    if R22 < r1_val and varsigma <= lam**2:
        return A_val * sig22_min
    if R22 > 1.0 and varsigma <= lam**2:
        return B_val * sig22_min
    if R22 > 1.0 and varsigma > lam**2:
        return 0.0
    # edge cases: should not reach for given values
    return 0.0

def sigma_I_eq_max(varsigma, lam, R22, R12):
    """Maximum Type I effective stress."""
    sig_t_max = sigma_I_t_max(varsigma, lam, R22, R12, SIG22_MAX)
    return sig_t_max / SIGMA_I_F

def sigma_II_eq_max(varsigma, lam, R22, R12):
    """
    Maximum Type II effective stress and maximizing γ (radians).
    Follows Eqs 14a‑14j for σ22 != 0.
    """
    sig22_max = SIG22_MAX
    sig22_min = R22 * sig22_max
    
    # Factor
    lam2 = lam**2
    t1 = (TAU_II_F / SIGMA_II_F)**2
    
    # Conditions per Eq 14a,14b, etc.
    # Since σ12_f = 70 > σ22_f = 48, paper says use simplified Eq 17.
    # But for robustness we implement the full piecewise for σ22 != 0.
    
    # thresholds
    thresh1 = 1.0 - 2.0 * t1
    thresh2 = -2.0 * math.sqrt(TAU_II_F**2 + (lam * SIGMA_II_F)**2) / ((1.0 + lam2) * SIGMA_II_F)
    thresh3 = -math.sqrt(1.0 + (TAU_II_F / (lam * SIGMA_II_F))**2) if lam != 0 else float('-inf')
    thresh4 = -math.sqrt(1.0 / (1.0 - t1)) if t1 < 1.0 else float('-inf')
    
    # 14a
    if 0.0 <= R22 < 1.0 and lam2 < thresh1:
        gamma = 0.5 * math.acos((TAU_II_F**2 + (lam * SIGMA_II_F)**2) / (TAU_II_F**2 - SIGMA_II_F**2))
        val = (lam2 + 1.0) * SIGMA_II_F / (2.0 * TAU_II_F * math.sqrt(SIGMA_II_F**2 - TAU_II_F**2)) * sig22_max
        return val, gamma
    # 14b
    if 0.0 <= R22 < 1.0 and lam2 >= thresh1:
        val = math.sqrt(TAU_II_F**2 + (lam * SIGMA_II_F)**2) / (SIGMA_II_F * TAU_II_F) * sig22_max
        return val, math.pi / 2.0
    # 14c
    if R22 > 1.0 and lam2 < 1.0:
        gamma = 0.5 * math.acos(-lam2)
        val = - (lam2 + 1.0) / (2.0 * TAU_II_F) * sig22_min
        return val, gamma
    # 14d
    if R22 > 1.0 and lam2 >= 1.0:
        val = abs(lam * sig22_min) / TAU_II_F
        return val, math.pi / 2.0
    # 14e
    if thresh3 <= R22 < 0.0 and lam2 >= 1.0:
        val = math.sqrt(TAU_II_F**2 + (lam * SIGMA_II_F)**2) / (SIGMA_II_F * TAU_II_F) * sig22_max
        return val, math.pi / 2.0
    # 14f
    if R22 < thresh3 and lam2 >= 1.0:
        val = abs(lam * sig22_min) / TAU_II_F
        return val, math.pi / 2.0
    # 14g
    if thresh2 < R22 < 0.0 and thresh1 <= lam2 < 1.0:
        val = math.sqrt(TAU_II_F**2 + (lam * SIGMA_II_F)**2) / (SIGMA_II_F * TAU_II_F) * sig22_max
        return val, math.pi / 2.0
    # 14h
    if R22 <= thresh2 and thresh1 <= lam2 < 1.0:
        gamma = 0.5 * math.acos(-lam2)
        val = abs(sig22_min) / (2.0 * TAU_II_F) * (1.0 + lam2)
        return val, gamma
    # 14i
    if thresh4 < R22 < 0.0 and lam2 < thresh1:
        gamma = 0.5 * math.acos((TAU_II_F**2 + (lam * SIGMA_II_F)**2) / (TAU_II_F**2 - SIGMA_II_F**2))
        val = (lam2 + 1.0) * SIGMA_II_F / (2.0 * TAU_II_F * math.sqrt(SIGMA_II_F**2 - TAU_II_F**2)) * sig22_max
        return val, gamma
    # 14j
    if R22 <= thresh4 and lam2 < thresh1:
        gamma = 0.5 * math.acos(-lam2)
        val = (lam2 + 1.0) / (2.0 * TAU_II_F) * abs(sig22_min)
        return val, gamma
    # fallback (shouldn't happen)
    return 0.0, 0.0

def beta_from_lam_varsigma(varsigma, lam, sigma12_sign):
    """
    Return β (radians) for the plane maximizing Type I stress,
    according to Eqs 6a‑6c. sigma12_sign is 1 for positive σ12, -1 for negative, 0 for zero.
    """
    if sigma12_sign > 0:
        return (3.0 * math.pi / 4.0) - 0.5 * math.atan2(varsigma - 1.0, 2.0 * lam)
    elif sigma12_sign < 0:
        return (math.pi / 4.0) - 0.5 * math.atan2(varsigma - 1.0, 2.0 * lam)
    else:
        # sigma12 == 0; from paper: β = π/2 if σ11 > σ22, else no specific (but we treat as π/2)
        # We don't need this case for our given values (all have λ != 0 implying σ12 != 0)
        return math.pi / 2.0

def sign_of_sigma12(lam, R22):
    """
    sigma12 = lam * sigma22. Since sigma22_max > 0, sign of sigma12 is sign(lam) when sigma22 is at max.
    For consistent sign across cycle, we use lam sign.
    """
    if lam > 0:
        return 1
    elif lam < 0:
        return -1
    else:
        return 0

# Define the 12 conditions
# For each R_globe in [0, -1], λ_globe in [0.5,1,2], ply (+) or (-)
conditions = [
    # λ_globe=0.5
    {"id": "lambda0.5_plus_R0",   "lam": -1.4, "varsigma": 3.0,  "R22": 0.0, "R12": 0.0, "ply": "+"},
    {"id": "lambda0.5_plus_R-1",  "lam": -1.4, "varsigma": 3.0,  "R22": -1.0,"R12": -1.0,"ply": "+"},
    {"id": "lambda0.5_minus_R0",  "lam": 0.5,  "varsigma": -0.5, "R22": 0.0, "R12": 0.0, "ply": "-"},
    {"id": "lambda0.5_minus_R-1", "lam": 0.5,  "varsigma": -0.5, "R22": -1.0,"R12": -1.0,"ply": "-"},
    # λ_globe=1.0
    {"id": "lambda1.0_plus_R0",   "lam": -2.8, "varsigma": 9.2,  "R22": 0.0, "R12": 0.0, "ply": "+"},
    {"id": "lambda1.0_plus_R-1",  "lam": -2.8, "varsigma": 9.2,  "R22": -1.0,"R12": -1.0,"ply": "+"},
    {"id": "lambda1.0_minus_R0",  "lam": 0.4,  "varsigma": -1.3, "R22": 0.0, "R12": 0.0, "ply": "-"},
    {"id": "lambda1.0_minus_R-1", "lam": 0.4,  "varsigma": -1.3, "R22": -1.0,"R12": -1.0,"ply": "-"},
    # λ_globe=2.0
    {"id": "lambda2.0_plus_R0",   "lam": 5.2,  "varsigma": -25.0,"R22": 0.0, "R12": 0.0, "ply": "+"},
    {"id": "lambda2.0_plus_R-1",  "lam": 5.2,  "varsigma": -25.0,"R22": -1.0,"R12": -1.0,"ply": "+"},
    {"id": "lambda2.0_minus_R0",  "lam": 0.2,  "varsigma": -2.2, "R22": 0.0, "R12": 0.0, "ply": "-"},
    {"id": "lambda2.0_minus_R-1", "lam": 0.2,  "varsigma": -2.2, "R22": -1.0,"R12": -1.0,"ply": "-"},
]

rows = []
for c in conditions:
    lam = c["lam"]
    varsigma = c["varsigma"]
    R22 = c["R22"]
    R12 = c["R12"]
    s12_sign = sign_of_sigma12(lam, R22)
    
    # Type I
    sigmaI_eq = sigma_I_eq_max(varsigma, lam, R22, R12)
    beta_I = beta_from_lam_varsigma(varsigma, lam, s12_sign)
    gamma_I = math.pi / 2.0  # always for Type I max
    
    # Type II
    sigmaII_eq, gamma_II = sigma_II_eq_max(varsigma, lam, R22, R12)
    beta_II = 0.0  # for Type II, β = 0
    
    # Critical plane
    if sigmaI_eq > sigmaII_eq:
        crit_type = "I"
        beta_c = beta_I
        gamma_c = gamma_I
    else:
        crit_type = "II"
        beta_c = beta_II
        gamma_c = gamma_II
    
    rows.append([
        c["id"],
        crit_type,
        f"{beta_c:.6f}",
        f"{gamma_c:.6f}",
        f"{sigmaI_eq:.6f}",
        f"{sigmaII_eq:.6f}",
    ])

# Write CSV
with open(OUTFILE, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["condition_id", "critical_plane_type", "beta_c", "gamma_c", "max_sigma_I_eq", "max_sigma_II_eq"])
    writer.writerows(rows)

print(f"Written {len(rows)} rows to {OUTFILE}")