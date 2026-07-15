import json
import math
import sys
import numpy as np
from scipy import constants, integrate

# Physical constants
hbar = constants.hbar   # reduced Planck constant (J*s)
k_B = constants.k       # Boltzmann constant (J/K)
e  = constants.e        # elementary charge (C)
J_to_eV = 1.0 / e

# Paper parameters
N = 500
a = 1.5e-10
v_base = 2500.0

# ---------- helper functions ----------
def compute_V():
    """Molecular volume V for the spherical monomer."""
    factor = (3.0*N/(4.0*math.pi))**(1.0/3.0) - 0.5
    V = (4.0*math.pi/3.0) * (factor**3) * (a**3)
    return V

def get_cutoffs(V, v):
    """Return (omega_L, omega_U) for given volume and speed of sound."""
    omega_L = (math.pi/2.0) * v * (4.0*math.pi/(3.0*V))**(1.0/3.0)
    omega_U = v * (2.0*math.pi**2 * (3.0*N - 6.0 + math.pi**2/12.0) / V)**(1.0/3.0)
    return omega_L, omega_U

def U_zero(V, v, omega_L, omega_U):
    """Zero-point energy (eV) from Eq. (3) with hbar."""
    alpha = 3.0 * V * hbar / (16.0 * math.pi**2 * v**3)
    return alpha * (omega_U**4 - omega_L**4) * J_to_eV

def U_Debye(V, v, omega_L, omega_U, T):
    """Debye thermal energy (eV) at temperature T (K)."""
    if T == 0:
        return 0.0
    pref = 3.0 * V * (k_B * T)**4 / (2.0 * math.pi**2 * v**3 * hbar**3) * J_to_eV
    xL = hbar * omega_L / (k_B * T)
    xU = hbar * omega_U / (k_B * T)
    def integrand(x):
        return x**3 / (np.exp(x) - 1.0)
    I, _ = integrate.quad(integrand, xL, xU, limit=200)
    return pref * I

def F_total(V, v, omega_L, omega_U, T, U_zero_val):
    """Helmholtz free energy (eV) at temperature T."""
    if T == 0:
        return U_zero_val
    pref_F = 3.0 * V * (k_B * T)**4 / (2.0 * math.pi**2 * v**3 * hbar**3) * J_to_eV
    xL = hbar * omega_L / (k_B * T)
    xU = hbar * omega_U / (k_B * T)
    def integrand_F(x):
        return x**2 * np.log(1.0 - np.exp(-x))
    I_F, _ = integrate.quad(integrand_F, xL, xU, limit=200)
    return U_zero_val + pref_F * I_F

# ---------- compute all quantities ----------
V_mono = compute_V()

# Monomer
omega_L_m, omega_U_m = get_cutoffs(V_mono, v_base)
U_zero_m = U_zero(V_mono, v_base, omega_L_m, omega_U_m)

# Dimer (volume doubled, same v)
V_dimer = 2.0 * V_mono
omega_L_d, omega_U_d = get_cutoffs(V_dimer, v_base)
U_zero_d = U_zero(V_dimer, v_base, omega_L_d, omega_U_d)
Delta_U_zero_base = U_zero_d - 2.0 * U_zero_m

# Dimer with 5% higher speed of sound
v_dimer_high = 1.05 * v_base
omega_L_d2, omega_U_d2 = get_cutoffs(V_dimer, v_dimer_high)
U_zero_d2 = U_zero(V_dimer, v_dimer_high, omega_L_d2, omega_U_d2)
Delta_U_zero_high = U_zero_d2 - 2.0 * U_zero_m

# One-dimensional chain
omega_L_1d = math.pi * v_base / (N * a)
omega_U_1d = math.pi * (3.0*N - 6.0) * v_base / (3.0 * N * a)
pref_1d = 3.0 * V_mono * hbar / (4.0 * math.pi * v_base * a**2) * J_to_eV
U_zero_1d = pref_1d * (omega_U_1d**2 - omega_L_1d**2)

# Temperature-dependent arrays
temperatures = [0.0, 100.0, 200.0, 300.0]

def temp_loop(V_mono, v_mono, omega_L_m, omega_U_m, U_zero_m,
              V_dimer, v_dimer, omega_L_d, omega_U_d, U_zero_d,
              Delta_U_zero):
    data = []
    for T in temperatures:
        U_m_total = U_zero_m + U_Debye(V_mono, v_mono, omega_L_m, omega_U_m, T)
        U_d_total = U_zero_d + U_Debye(V_dimer, v_dimer, omega_L_d, omega_U_d, T)
        delta_U = U_d_total - 2.0*U_m_total + Delta_U_zero
        F_m = F_total(V_mono, v_mono, omega_L_m, omega_U_m, T, U_zero_m)
        F_d = F_total(V_dimer, v_dimer, omega_L_d, omega_U_d, T, U_zero_d)
        delta_F = F_d - 2.0*F_m
        data.append({
            "T": T,
            "U_mono": round(U_m_total, 6),
            "U_dimer": round(U_d_total, 6),
            "Delta_U": round(delta_U, 6),
            "Delta_F": round(delta_F, 6)
        })
    return data

base_temp = temp_loop(V_mono, v_base, omega_L_m, omega_U_m, U_zero_m,
                      V_dimer, v_base, omega_L_d, omega_U_d, U_zero_d,
                      Delta_U_zero_base)

high_temp = temp_loop(V_mono, v_base, omega_L_m, omega_U_m, U_zero_m,
                      V_dimer, v_dimer_high, omega_L_d2, omega_U_d2, U_zero_d2,
                      Delta_U_zero_high)

# ---------- assemble and write JSON ----------
result = {
    "spherical_monomer": {
        "omega_L": omega_L_m,
        "omega_U": omega_U_m,
        "V": V_mono,
        "U_zero": U_zero_m
    },
    "spherical_dimer": {
        "omega_L": omega_L_d,
        "omega_U": omega_U_d,
        "V": V_dimer,
        "U_zero": U_zero_d
    },
    "dimerization": {
        "Delta_U_zero": Delta_U_zero_base,
        "Delta_U_temperature_dependent": base_temp
    },
    "dimerization_5pct_higher_v": {
        "Delta_U_zero": Delta_U_zero_high,
        "Delta_U_temperature_dependent": high_temp
    },
    "oneD_chain": {
        "omega_L": omega_L_1d,
        "omega_U": omega_U_1d,
        "U_zero": U_zero_1d
    }
}

output_path = "/app/outputs/reproduction_results.json"
with open(output_path, "w") as f:
    json.dump(result, f, indent=2)

print("Output written to", output_path, file=sys.stderr)
