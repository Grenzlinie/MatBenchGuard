#!/usr/bin/env python3
import math, json

# Physical constants (cgs)
E_CHARGE = 4.803e-10   # esu

# Data from Table 1 and Table 3 for NaCl, KF, NaF
compounds = {
    "NaCl": {
        "r0_cm": 2.820e-8,          # nearest-neighbour distance (cm)
        "Z": 0.91,
        "b": 29.8,                  # 10^{-10} erg/bond -> converted to erg below
        "rho_cm": 0.293e-8,         # 10^{-8} cm -> cm
        "epsilon_0": 442,           # 10^{-16} erg/bond -> converted below
        "r_m_cm": 3.89e-8,          # 10^{-8} cm -> cm
        # static-lattice quantities (kb) from Table 3
        "P_tilde": -5.9,
        "K_tilde": 239,
        "C44_tilde": 131,
        "Cs_tilde": 195,
        # experimental (Table 1) to get thermal offsets
        "K_exp": 240,
        "C44_exp": 126
    },
    "KF": {
        "r0_cm": 2.674e-8,
        "Z": 0.92,
        "b": 84.8,
        "rho_cm": 0.251e-8,
        "epsilon_0": 457,
        "r_m_cm": 3.16e-8,
        "P_tilde": -6.4,
        "K_tilde": 307,
        "C44_tilde": 133,
        "Cs_tilde": 274,
        "K_exp": 305,
        "C44_exp": 125
    },
    "NaF": {
        "r0_cm": 2.317e-8,
        "Z": 0.87,
        "b": 68.3,
        "rho_cm": 0.218e-8,
        "epsilon_0": 311,
        "r_m_cm": 2.99e-8,          # Table 4 gives (2.99) for NaF
        "P_tilde": -7.8,
        "K_tilde": 463,
        "C44_tilde": 290,
        "Cs_tilde": 334,
        "K_exp": 465,
        "C44_exp": 281
    }
}

# Convert parameter units to cgs (erg, cm)
for name, c in compounds.items():
    c["b_erg"] = c["b"] * 1e-10
    c["epsilon_0_erg"] = c["epsilon_0"] * 1e-16

# Static-lattice formulas (return kb)
def P_tilde(r, params):
    r0 = params["r0_cm"]
    rp = math.sqrt(2) * r
    coul = params["Z"]**2 * E_CHARGE**2 / r0
    factor = 1.0 / (2 * r0**3 * 1e9)   # cgs -> kbar
    return factor * (
        -0.58252 * coul * (r0/r)**4
        + 2 * params["b_erg"] * (r0/params["rho_cm"]) * (r0/r)**2 * math.exp(-r/params["rho_cm"])
        + math.sqrt(2) * params["epsilon_0_erg"] * (r0/params["r_m_cm"])**3
          * (48 * (params["r_m_cm"]/rp)**15 - 48 * (params["r_m_cm"]/rp)**9)
    )

def K_tilde(r, params):
    r0 = params["r0_cm"]
    rp = math.sqrt(2) * r
    coul = params["Z"]**2 * E_CHARGE**2 / r0
    factor = 1.0 / (2 * r0**3 * 1e9)
    return factor * (
        -0.77669 * coul * (r0/r)**4
        + (2/3) * params["b_erg"] * (r0/params["rho_cm"]) * (2*(r0/r)**2 + (r0/params["rho_cm"])*(r0/r)) * math.exp(-r/params["rho_cm"])
        + math.sqrt(2) * params["epsilon_0_erg"] * (r0/params["r_m_cm"])**3
          * (240 * (params["r_m_cm"]/rp)**15 - 144 * (params["r_m_cm"]/rp)**9)
    )

def C44_tilde(r, params):
    r0 = params["r0_cm"]
    rp = math.sqrt(2) * r
    coul = params["Z"]**2 * E_CHARGE**2 / r0
    factor = 1.0 / (2 * r0**3 * 1e9)
    return factor * (
        1.27802 * coul * (r0/r)**4
        - 2 * params["b_erg"] * (r0/params["rho_cm"]) * (r0/r)**2 * math.exp(-r/params["rho_cm"])
        + math.sqrt(2) * params["epsilon_0_erg"] * (r0/params["r_m_cm"])**3
          * (120 * (params["r_m_cm"]/rp)**15 - 48 * (params["r_m_cm"]/rp)**9)
    )

def Cs_tilde(r, params):
    r0 = params["r0_cm"]
    rp = math.sqrt(2) * r
    coul = params["Z"]**2 * E_CHARGE**2 / r0
    factor = 1.0 / (2 * r0**3 * 1e9)
    return factor * (
        -1.22153 * coul * (r0/r)**4
        + params["b_erg"] * (r0/params["rho_cm"]) * ((r0/params["rho_cm"])*(r0/r) - (r0/r)**2) * math.exp(-r/params["rho_cm"])
        + math.sqrt(2) * params["epsilon_0_erg"] * (r0/params["r_m_cm"])**3
          * (36 * (params["r_m_cm"]/rp)**15)
    )

# Pressure derivatives at r0 (equations 6-8)  (dimensionless)
def K_prime(r0, params):
    r = r0   # equilibrium
    rp = math.sqrt(2) * r
    coul = params["Z"]**2 * E_CHARGE**2 / r
    factor = 1.0 / (2 * r**3 * 1e9)  # consistent with bulk modulus
    K = K_tilde(r, params)
    return (1.0 / (6 * K * r**3 * 1e9)) * (   # extra 1e9 to cancel units in denominator
        -3.1068 * coul * (r0/r)**4
        + (2/3) * params["b_erg"] * (r/params["rho_cm"]) * (4*(r0/r)**2 + 3*(r/params["rho_cm"])*(r0/r) + (r/params["rho_cm"])**2) * math.exp(-r/params["rho_cm"])
        + math.sqrt(2) * params["epsilon_0_erg"] * (r/params["r_m_cm"])**3
          * (3600 * (params["r_m_cm"]/rp)**15 - 1296 * (params["r_m_cm"]/rp)**9)
    )

def C44_prime(r0, params):
    r = r0
    rp = math.sqrt(2) * r
    coul = params["Z"]**2 * E_CHARGE**2 / r
    K = K_tilde(r, params)
    return (1.0 / (6 * K * r**3 * 1e9)) * (
        5.1121 * coul * (r0/r)**4
        - 2 * params["b_erg"] * (r/params["rho_cm"]) * (2*(r0/r)**2 + (r/params["rho_cm"])*(r0/r)) * math.exp(-r/params["rho_cm"])
        + math.sqrt(2) * params["epsilon_0_erg"] * (r/params["r_m_cm"])**3
          * (1800 * (params["r_m_cm"]/rp)**15 - 432 * (params["r_m_cm"]/rp)**9)
    )

def Cs_prime(r0, params):
    r = r0
    rp = math.sqrt(2) * r
    coul = params["Z"]**2 * E_CHARGE**2 / r
    K = K_tilde(r, params)
    return (1.0 / (6 * K * r**3 * 1e9)) * (
        4.8861 * coul * (r0/r)**4
        + params["b_erg"] * (r/params["rho_cm"]) * ((r/params["rho_cm"])**2 - 2*(r0/r)**2) * math.exp(-r/params["rho_cm"])
        + math.sqrt(2) * params["epsilon_0_erg"] * (r/params["r_m_cm"])**3
          * (540 * (params["r_m_cm"]/rp)**15)
    )

# Binary search for transition pressure
def find_transition_pressure(params, alpha, start_fraction=0.7):
    # thermal offsets (constant)
    delta_K = params["K_exp"] - params["K_tilde"]
    delta_C44 = params["C44_exp"] - params["C44_tilde"]
    r0 = params["r0_cm"]

    def ratio(r):
        K = K_tilde(r, params) + delta_K
        C44 = C44_tilde(r, params) + delta_C44
        if K <= 0:
            return 0
        return C44 / K

    # search in compressed region
    lo = start_fraction * r0
    hi = r0
    # ensure sign change (ratio at hi < alpha and ratio at lo > alpha)
    r_hi = ratio(hi)
    r_lo = ratio(lo)
    # For KF and NaF, C44 decreases with pressure, so ratio decreases from hi to lo
    # We want r where ratio == alpha. If r_hi > alpha > r_lo, then bracket exists.
    if r_lo > alpha or r_hi < alpha:
        # might need wider range
        lo = 0.5 * r0; hi = 1.1 * r0
        r_lo = ratio(lo); r_hi = ratio(hi)

    for _ in range(100):
        mid = (lo + hi) / 2
        if ratio(mid) > alpha:
            lo = mid
        else:
            hi = mid
    r_mid = (lo + hi) / 2
    P = P_tilde(r_mid, params)   # static-lattice pressure; the pressure is the independent variable
    return P

# Build output
output = {"compounds": [], "phase_transitions": {}}

for name in ["NaCl", "KF", "NaF"]:
    p = compounds[name]
    r0 = p["r0_cm"]
    entry = {
        "name": name,
        "Z": p["Z"],
        "b": p["b"],
        "rho": p["rho_cm"] * 1e8,        # back to 10^{-8} cm
        "epsilon_0": p["epsilon_0"],
        "r_m": p["r_m_cm"] * 1e8,
        "P_tilde": p["P_tilde"],
        "K_tilde": p["K_tilde"],
        "C44_tilde": p["C44_tilde"],
        "Cs_tilde": p["Cs_tilde"],
        "K_prime": K_prime(r0, p),
        "C44_prime": C44_prime(r0, p),
        "Cs_prime": Cs_prime(r0, p)
    }
    output["compounds"].append(entry)

# Transition pressures (KF alpha=0.13, NaF alpha=0.14)
p_KF = compounds["KF"]
p_NaF = compounds["NaF"]
output["phase_transitions"]["KF"] = find_transition_pressure(p_KF, 0.13)
output["phase_transitions"]["NaF"] = find_transition_pressure(p_NaF, 0.14)

with open("/app/outputs/model_predictions.json", "w") as f:
    json.dump(output, f, indent=2)
