import math
import csv
import sys

# Constants
k_B = 1.380648e-23          # J / K
h   = 6.626070e-34           # J s
N_A = 6.02214e23             # mol^-1
M_H2O = 18.0148              # g mol^-1
rho_l = 0.965                # g cm^-3  (fixed liquid density)
Delta_G_sd_h = 0.155 * 1000  # J mol^-1 (0.155 kJ mol^-1 enthalpy difference stacking-disordered / hexagonal)
R_gas = 8.31446              # J mol^-1 K^-1  (universal gas constant)

# Power-law parameters for D(T) (Table V, best estimate)
D_star = 8.3175e-6           # cm^2 s^-1 K^-0.5
T_s = 215.45                 # K
gamma = 1.9188

# Polynomial coefficients for DeltaH_m,h(T) (Table III, best estimate)
# k[i] for (T - Tm)^i, i = 0..6
k = [6.008, 0.03616, -3.9479e-4, -1.6248e-5, -3.2563e-7, 0.0, 0.0]
T_m = 273.15  # K

# Reference for Turnbull correlation
T_ref = 236.0                # K
sigma_ref = 18.505           # mJ m^-2  (fitted at T_ref)

# Pre-compute denominator for Turnbull correlation at T_ref
# DeltaH_m,sd(T_ref) = DeltaH_m,h(T_ref) - 0.155 kJ mol^-1
def compute_Delta_H_m_h(T):
    dT = T - T_m
    val = 0.0
    for i, coeff in enumerate(k):
        val += coeff * (dT ** i)
    return val  # kJ mol^-1

DH_sd_ref = compute_Delta_H_m_h(T_ref) - 0.155  # kJ mol^-1

# Number density of water molecules in liquid (cm^-3)
n_l_cm3 = rho_l * N_A / M_H2O

def D_func(T):
    """Self-diffusion coefficient (cm^2 s^-1) from power-law."""
    if T <= T_s:
        return 0.0
    arg = T / T_s - 1.0
    return D_star * math.sqrt(T) * (arg ** gamma)

def Delta_G_diff_func(T):
    """Diffusion activation energy (J) from derivative of power-law D(T)."""
    if T <= T_s:
        return float('inf')
    return k_B * (T / 2.0 + gamma * T * T / (T - T_s))

def sigma_sd_l(T):
    """Interfacial energy (mJ m^-2) via Turnbull correlation."""
    DH = compute_Delta_H_m_h(T) - 0.155
    return sigma_ref * DH / DH_sd_ref

def saturation_ratio(T):
    """Saturation ratio S = P_l / P_sd for stacking-disordered ice."""
    # Vapour pressure of supercooled water (Pa)
    ln_P_l = (54.842763 - 6763.22 / T - 4.210 * math.log(T) + 0.000367 * T +
              math.tanh(0.0415 * (T - 218.8)) *
              (53.878 - 1331.22 / T - 9.44523 * math.log(T) + 0.014025 * T))
    P_l = math.exp(ln_P_l)
    # Vapour pressure of hexagonal ice (Pa)
    ln_P_h = 9.550426 - 5723.265 / T + 3.53068 * math.log(T) - 0.00728332 * T
    P_h = math.exp(ln_P_h)
    # Correct for stacking-disordered ice: P_sd = P_h * exp(DeltaG_h->sd / (R T))
    P_sd = P_h * math.exp(Delta_G_sd_h / (R_gas * T))
    return P_l / P_sd

def rho_i(T):
    """Density of ice (g cm^-3) from Table I."""
    return (-1.3103e-9 * T**3 + 3.8109e-7 * T**2 -
            9.2592e-5 * T + 0.94040)

writer = csv.writer(sys.stdout)
writer.writerow(["T", "D", "Delta_G_diff", "sigma_sd_l", "J"])

for T in range(225, 251):   # 1 K intervals
    D_val = D_func(T)
    DG_diff = Delta_G_diff_func(T)
    sigma_mJ = sigma_sd_l(T)
    S = saturation_ratio(T)
    v_i_cm3 = M_H2O / (N_A * rho_i(T))    # cm^3 per molecule
    v_i = v_i_cm3 * 1.0e-6               # m^3 per molecule
    sigma_Jm2 = sigma_mJ / 1000.0         # J m^-2
    kT = k_B * T
    lnS = math.log(S) if S > 0 else float('-inf')
    if lnS <= 0:
        J_val = 0.0
    else:
        deltaG_crit = (16.0 * math.pi * v_i**2 * sigma_Jm2**3) / (3.0 * (kT * lnS)**2)
        # guard against exponent overflow
        try:
            term1 = math.exp(-DG_diff / kT)
            term2 = math.exp(-deltaG_crit / kT)
        except OverflowError:
            term2 = 0.0
        prefactor = (k_B * T / h) * n_l_cm3
        J_val = prefactor * term1 * term2
    writer.writerow([f"{T:.1f}",
                     f"{D_val:.6e}",
                     f"{DG_diff:.4e}",
                     f"{sigma_mJ:.4f}",
                     f"{J_val:.4e}"])
