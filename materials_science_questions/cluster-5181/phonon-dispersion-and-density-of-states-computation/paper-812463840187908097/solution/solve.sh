#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
python3 -m pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple scipy numpy
OUTDIR=/app/outputs

# === solve block: reproduction_results.json ===
python3 -c '
import json, math, sys
import numpy as np
from scipy import constants, integrate

# Parameters
N_mono = 500
a = 1.5e-10
v_base = 2500.0
v_dimer_high = 1.05 * v_base
hbar = constants.hbar  # J*s
kB = constants.k      # J/K
eV = constants.e      # J
J_to_eV = 1.0 / eV

# Volume function
def compute_V(N, a):
    factor = (3.0*N/(4.0*math.pi))**(1/3) - 0.5
    return (4.0/3.0)*math.pi * factor**3 * a**3

# Cutoff functions
def compute_cutoffs(V, v, N):
    omega_L = (math.pi/2.0) * v * (4.0*math.pi/(3.0*V))**(1/3)
    omega_U = v * (2.0*math.pi**2 * (3*N - 6 + math.pi**2/12.0) / V)**(1/3)
    return omega_L, omega_U

def compute_U_zero(V, v, omega_L, omega_U):
    # analytic: (3/16) * (V*h) / (pi^2*v^3) * (omega_U^4 - omega_L^4)  with h=2*pi*hbar
    coeff = 3.0 * V * (2.0*math.pi*hbar) / (16.0 * math.pi**2 * v**3)
    return coeff * (omega_U**4 - omega_L**4) * J_to_eV

def integrand_U(omega, T, V, v):
    # factor from Debye formula: 3 * (V*omega^2/(2*pi^2*v^3)) * (hbar*omega/(exp(hbar*omega/kT)-1))
    # returns value in J (integrand)
    x = hbar * omega / (kB * T)
    if x < 1e-10:
        return 0.0
    return 3.0 * V * omega**2 / (2.0*math.pi**2 * v**3) * hbar*omega / (np.exp(x) - 1.0)

def integrate_U(V, v, omega_L, omega_U, T):
    if T == 0.0:
        return 0.0
    res, err = integrate.quad(integrand_U, omega_L, omega_U, args=(T, V, v), limit=200)
    return res * J_to_eV

def integrand_lnZ(omega, T, V, v):
    g = 3.0 * V * omega**2 / (2.0*math.pi**2 * v**3)
    x = hbar * omega / (kB * T)
    term = hbar*omega/(2.0*kB*T) + np.log(1.0 - np.exp(-x))
    return g * term

def compute_F(V, v, omega_L, omega_U, T):
    if T == 0.0:
        return compute_U_zero(V, v, omega_L, omega_U)  # at T=0, F = U_zero
    res, err = integrate.quad(integrand_lnZ, omega_L, omega_U, args=(T, V, v), limit=200)
    lnZ = -res
    return -kB * T * lnZ * J_to_eV

# Compute monomer
V_mono = compute_V(N_mono, a)
omega_L_mono, omega_U_mono = compute_cutoffs(V_mono, v_base, N_mono)
U_zero_mono = compute_U_zero(V_mono, v_base, omega_L_mono, omega_U_mono)

# Dimer: N=1000
N_dimer = 2 * N_mono
V_dimer = compute_V(N_dimer, a)
omega_L_dimer, omega_U_dimer = compute_cutoffs(V_dimer, v_base, N_dimer)
U_zero_dimer = compute_U_zero(V_dimer, v_base, omega_L_dimer, omega_U_dimer)
Delta_U_zero = U_zero_dimer - 2*U_zero_mono

# Temperature sweeps
Ts = [0.0, 100.0, 200.0, 300.0]

def compute_dimerization_entries(V_mono, v_mono, omega_L_mono, omega_U_mono,
                                 V_dimer, v_dimer, omega_L_dimer, omega_U_dimer,
                                 Delta_U_zero):
    entries = []
    for T in Ts:
        U_mono = integrate_U(V_mono, v_mono, omega_L_mono, omega_U_mono, T)
        U_dimer = integrate_U(V_dimer, v_dimer, omega_L_dimer, omega_U_dimer, T)
        Delta_U = U_dimer - 2*U_mono + Delta_U_zero
        F_mono = compute_F(V_mono, v_mono, omega_L_mono, omega_U_mono, T)
        F_dimer = compute_F(V_dimer, v_dimer, omega_L_dimer, omega_U_dimer, T)
        Delta_F = F_dimer - 2*F_mono
        entries.append({
            "T": T,
            "U_mono": U_mono,
            "U_dimer": U_dimer,
            "Delta_U": Delta_U,
            "Delta_F": Delta_F
        })
    return entries

# Baseline dimerization
entries_baseline = compute_dimerization_entries(
    V_mono, v_base, omega_L_mono, omega_U_mono,
    V_dimer, v_base, omega_L_dimer, omega_U_dimer,
    Delta_U_zero
)

# 5% higher dimer speed
v_dimer_high = 1.05 * v_base
# Recompute dimer cutoffs with new v
omega_L_dimer_high, omega_U_dimer_high = compute_cutoffs(V_dimer, v_dimer_high, N_dimer)
U_zero_dimer_high = compute_U_zero(V_dimer, v_dimer_high, omega_L_dimer_high, omega_U_dimer_high)
Delta_U_zero_high = U_zero_dimer_high - 2*U_zero_mono
entries_high = compute_dimerization_entries(
    V_mono, v_base, omega_L_mono, omega_U_mono,
    V_dimer, v_dimer_high, omega_L_dimer_high, omega_U_dimer_high,
    Delta_U_zero_high
)

# One-dimensional chain (N=500, same V)
omega_L_1d = math.pi * v_base / (N_mono * a)
omega_U_1d = math.pi * (3*N_mono - 6) * v_base / (3 * N_mono * a)
V_chain = V_mono  # same volume
U_zero_1d = (3.0 * V_chain * hbar / (4.0 * math.pi * v_base * a**2)) * (omega_U_1d**2 - omega_L_1d**2) * J_to_eV

# Build output
output = {
    "spherical_monomer": {
        "omega_L": omega_L_mono,
        "omega_U": omega_U_mono,
        "V": V_mono,
        "U_zero": U_zero_mono
    },
    "spherical_dimer": {
        "omega_L": omega_L_dimer,
        "omega_U": omega_U_dimer,
        "V": V_dimer,
        "U_zero": U_zero_dimer
    },
    "dimerization": {
        "Delta_U_zero": Delta_U_zero,
        "Delta_U_temperature_dependent": entries_baseline
    },
    "dimerization_5pct_higher_v": {
        "Delta_U_zero": Delta_U_zero_high,
        "Delta_U_temperature_dependent": entries_high
    },
    "oneD_chain": {
        "omega_L": omega_L_1d,
        "omega_U": omega_U_1d,
        "U_zero": U_zero_1d
    }
}

json.dump(output, sys.stdout, indent=2)
' > "$OUTDIR/reproduction_results.json"
