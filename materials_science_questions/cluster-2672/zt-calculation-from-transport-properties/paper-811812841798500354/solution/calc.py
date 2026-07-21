import numpy as np
import json
import math
from scipy.optimize import minimize_scalar

# --- Geometry and material parameters (SI units) ---
L  = 0.01                 # m, chip side length
t1 = 250e-6               # m, chip thickness
k1 = 163.0                # W/(m K), chip isotropic conductivity
kz = 5.0                  # W/(m K), spreader thru-plane conductivity
h  = 10000.0              # W/(m^2 K), convective coefficient
w  = 500e-6               # m, hot-spot side length
qpp = 1.4e7               # W/m^2, hot-spot heat flux (1.4 kW/cm^2)
Q  = qpp * w**2           # total power on hot spot

# Default spreader thickness used for peak-temperature calculations
t2_default = 500e-6

# --- phi(zeta) function (Eq. 30) ---
# Uses effective k2 and t2 for the anisotropic layer
def phi(zeta, k2, t2):
    alpha = (1.0 - k2/k1) / (1.0 + k2/k1)
    psi   = (zeta + h/k2) / (zeta - h/k2)
    # exponentials
    e_2z_t1   = math.exp(2.0 * zeta * t1)
    e_2z_t2   = math.exp(2.0 * zeta * t2)
    e_4z_t1   = e_2z_t1 * e_2z_t1
    e_2z_2t1t2 = math.exp(2.0 * zeta * (2.0*t1 + t2))
    e_2z_t1t2  = math.exp(2.0 * zeta * (t1 + t2))
    term1 = alpha * e_4z_t1 - e_2z_t2
    term2 = e_2z_2t1t2 - alpha * e_2z_t1t2
    num = term1 + psi * term2
    den = (alpha * e_4z_t1 + e_2z_t2) + psi * (e_2z_2t1t2 + alpha * e_2z_t1t2)
    return num / den

# --- Compute peak excess temperature at hot-spot centre (x=y=L/2) ---
def peak_excess_temp(k_xy, t2=t2_default):
    # Equivalent isotropic parameters for layer 2 (Eq. 31)
    if abs(k_xy - kz) < 1e-15:
        k2_eq = kz
        t2_eq = t2
    else:
        k2_eq = math.sqrt(k_xy * kz)
        t2_eq = t2 / math.sqrt(kz / k_xy)

    # One-dimensional term A0 (Eq. 28) – uses actual k_z for thru-plane resistance
    A0 = Q / (L*L) * (t1/k1 + t2/kz + 1.0/h)

    # Number of modes in each direction
    Mmax = 200
    Nmax = 200

    # Precompute series sums
    sum1 = 0.0   # sum_{m} Am cos(λ_m L/2)
    sum2 = 0.0   # sum_{n} An cos(δ_n L/2) – symmetric, same as sum1
    sum3 = 0.0   # double sum

    # Single sums (identical because of square symmetry)
    cos_center_m = {}  # cos(m pi/2)
    sin_term_m = {}
    for m in range(1, Mmax+1):
        lam = m * math.pi / L
        cos_center = math.cos(lam * L/2)
        # sin((L+w)/2 * lam) - sin((L-w)/2 * lam)
        sin_term = math.sin((L+w)/2.0 * lam) - math.sin((L-w)/2.0 * lam)
        phi_lam = phi(lam, k2_eq, t2_eq)
        Am = 2.0 * Q * sin_term / (L*L * w * k1 * lam*lam * phi_lam)
        sum1 += Am * cos_center
        # store for double sum
        cos_center_m[m] = cos_center
        sin_term_m[m] = math.sin(w * lam / 2.0)
    sum2 = sum1   # identical to sum over n

    # Double sum
    for m in range(1, Mmax+1):
        lam = m * math.pi / L
        cos_lam = cos_center_m[m]
        sl = sin_term_m[m]   # sin(w * lam / 2)
        for n in range(1, Nmax+1):
            delta = n * math.pi / L
            cos_del = math.cos(delta * L/2)
            sd = math.sin(w * delta / 2.0)
            beta = math.sqrt(lam*lam + delta*delta)
            phi_beta = phi(beta, k2_eq, t2_eq)
            Amn = (16.0 * Q * cos_lam * sl * cos_del * sd) / (
                L*L * w*w * k1 * beta * lam * delta * phi_beta)
            sum3 += Amn * cos_lam * cos_del

    return A0 + sum1 + sum2 + sum3

# --- Compute total thermal resistance R_T = R1D + Rs for given spreader thickness ---
def total_thermal_resistance(t2, k_xy=350.0):
    # Equivalent parameters
    if abs(k_xy - kz) < 1e-15:
        k2_eq = kz
        t2_eq = t2
    else:
        k2_eq = math.sqrt(k_xy * kz)
        t2_eq = t2 / math.sqrt(kz / k_xy)

    # One-dimensional resistance (Eq. 35) – uses actual k_z
    R1D = t1/(k1 * L*L) + t2/(kz * L*L) + 1.0/(h * L*L)

    # Spreading resistance Rs (Eq. 37)
    Mmax = 150
    Nmax = 150

    term1 = 0.0   # sum_m sin^2(w δ_m/2) / (δ_m^3 φ(δ_m))
    term2 = 0.0   # sum_n sin^2(w λ_n/2) / (λ_n^3 φ(λ_n))
    term3 = 0.0   # double sum

    for m in range(1, Mmax+1):
        delta = m * math.pi / L
        sin2_d = math.sin(w * delta / 2.0) ** 2
        term1 += sin2_d / (delta**3 * phi(delta, k2_eq, t2_eq))

    for n in range(1, Nmax+1):
        lam = n * math.pi / L
        sin2_l = math.sin(w * lam / 2.0) ** 2
        term2 += sin2_l / (lam**3 * phi(lam, k2_eq, t2_eq))

    for m in range(1, Mmax+1):
        delta = m * math.pi / L
        sd2 = math.sin(w * delta / 2.0) ** 2
        for n in range(1, Nmax+1):
            lam = n * math.pi / L
            sl2 = math.sin(w * lam / 2.0) ** 2
            beta = math.sqrt(delta*delta + lam*lam)
            term3 += sd2 * sl2 / (delta*delta * lam*lam * beta * phi(beta, k2_eq, t2_eq))

    # Prefactors
    A_half = (w/2.0)**2
    L_half = (L/2.0)**2
    Rs = (1.0/(2.0 * A_half * L_half * k1)) * (term1 + term2) \
         + (1.0/(A_half*A_half * L_half * k1)) * term3

    return R1D + Rs

# ============================================================
# 1. Peak excess temperatures for three in-plane conductivities
# ============================================================
T5    = peak_excess_temp(5.0)
T350  = peak_excess_temp(350.0)
T1800 = peak_excess_temp(1800.0)

# ============================================================
# 2. Optimum spreader thickness for k_xy = 350 W/mK
# ============================================================
# Coarse sweep
n_points = 300
t_min, t_max = 10e-6, 2000e-6  # in metres
t_vals = np.linspace(t_min, t_max, n_points)
RT_vals = [total_thermal_resistance(tv) for tv in t_vals]
idx_min = int(np.argmin(RT_vals))
# Refine using bounded minimizer
f = lambda t: total_thermal_resistance(t) if t>0 else 1e6
res = minimize_scalar(f, bounds=(t_min, t_max), method='bounded')
opt_t_m = res.x
RT_min = res.fun
# Convert optimum thickness to µm
opt_t_um = opt_t_m * 1e6

# ============================================================
# Write JSON result
# ============================================================
result = {
    "kxy5_excess_temp":    round(T5, 4),
    "kxy350_excess_temp":  round(T350, 4),
    "kxy1800_excess_temp": round(T1800, 4),
    "kxy350_opt_thickness": round(opt_t_um, 2),
    "kxy350_total_thermal_resistance": round(RT_min, 6)
}

print(json.dumps(result, indent=2))
