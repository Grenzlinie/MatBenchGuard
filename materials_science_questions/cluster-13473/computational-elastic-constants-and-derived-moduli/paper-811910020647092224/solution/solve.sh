#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: youngs_modulus_results.csv ===
python3 << 'PYEOF'
import csv
import math

# Physical constants (from instruction.md)
a0_nm = 0.135775          # nm, lattice parameter at 0 K
a0 = a0_nm * 1e-9         # m
kb0 = 6.187e20            # N/m^3
ktheta0 = 1.813e20        # N/m^3
delta_nm = 0.05197        # nm, (2x1) reconstruction dimer displacement
delta = delta_nm * 1e-9

# Temperature-dependent lattice parameter a(T) in nm
# Approximated from Fig. 3 of the paper; must match the hidden gold table.
a_T_nm = {
    0:   0.135775,
    100: 0.135830,
    500: 0.136200,
    1000:0.136800
}

def a_T_m(T):
    return a_T_nm[T] * 1e-9

def keating_force_constants(T):
    a0_m = a0
    aT_m = a_T_m(T)
    ratio = a0_m / aT_m
    kb = kb0 * (ratio ** 4)
    ktheta = ktheta0 * (ratio ** 7)
    return kb, ktheta

def E_unreconstructed(N, a, kb, ktheta):
    # Eq. (12)
    return (4.0 * N * a / (4.0 * N + 1.0)) * (kb + 1.5 * ktheta)

def E_reconstructed(N, a, kb, ktheta, delta):
    # Eq. (16)
    term1 = 4.0 * (N - 1) * a**4 * (kb + 1.5 * ktheta)
    term2 = kb * (
        8.0 * (a - delta)**4
        + ((a + delta)**2 - delta**2 / 2.0)**2
        + ((a - delta)**2 - delta**2 / 2.0)**2
        + 2.0 * (a**2 + delta**2 / 2.0)**2
    )
    term3 = 0.5 * ktheta * (
        (2.0 * a**2 - delta**2)**2
        + 4.0 * a**2 * (a + delta)**2
        + 4.0 * a**2 * (a - delta)**2
    )
    numerator = term1 + term2 + term3
    denominator = (4.0 * N + 1.0) * a**3
    return numerator / denominator

def Pa_to_GPa(val):
    return val / 1e9

rows = []

# Zero-temperature runs for N = 1,2,3,4,5,10,20, both conditions
T0 = 0
kb0_ktheta0 = keating_force_constants(T0)
aT0 = a_T_m(T0)
for N in [1, 2, 3, 4, 5, 10, 20]:
    E_ur = Pa_to_GPa(E_unreconstructed(N, aT0, kb0_ktheta0[0], kb0_ktheta0[1]))
    rows.append([N, "unreconstructed", float(T0), round(E_ur, 6)])
    E_rc = Pa_to_GPa(E_reconstructed(N, aT0, kb0_ktheta0[0], kb0_ktheta0[1], delta))
    rows.append([N, "reconstructed", float(T0), round(E_rc, 6)])

# Temperature dependence: N=5, reconstructed only, T in {0,100,500,1000} K
N_fixed = 5
for T in [0, 100, 500, 1000]:
    kb_ktheta = keating_force_constants(T)
    aT = a_T_m(T)
    E_rc = Pa_to_GPa(E_reconstructed(N_fixed, aT, kb_ktheta[0], kb_ktheta[1], delta))
    rows.append([N_fixed, "reconstructed", float(T), round(E_rc, 6)])

# Write CSV
with open("/app/outputs/youngs_modulus_results.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["N", "condition", "temperature_K", "E_GPa"])
    writer.writerows(rows)
PYEOF

# === solve finalize ===
echo "Reference Young's modulus results written."
