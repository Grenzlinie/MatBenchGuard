#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: step_01_results.json ===
python3 << EOF
import math, json, sys

R = 8.314  # J/mol/K

coeffs = {
    "O": [
        (298.15, 1400, 252.36, -6.2747e-2, -1.3294e-6, -527.69, 0.0, 0.0),
        (1400, 6000, 259.03, -6.7710e-2, -1.6525e-8, -3747.4, 0.0, 0.0)
    ],
    "U": [
        (298.15, 1400, 539.11, -1.6007e-1, 1.7321e-5, -1046.4, 0.0, 0.0),
        (1400, 4435, 749.73, -8.3008e-2, -2.0904e-6, 0.0, -40.548, 0.0),
        (4435, 6000, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0)
    ],
    "UO": [
        (298.15, 1400, 26.863, -1.0515e-1, 1.6100e-5, -1002.4, 0.0, 0.0),
        (1400, 4435, 178.98, -4.2342e-2, 2.0064e-6, 0.0, -29.432, 0.0),
        (4435, 6000, -521.65, 5.8124e-2, 2.4020e-6, 0.0, 0.0, 0.0)
    ],
    "UO2": [
        (298.15, 1400, -501.42, -4.2567e-2, 1.4530e-5, 0.0, 7.5475, 0.0),
        (1400, 4435, -367.02, 1.4476e-2, 1.7735e-6, 0.0, -18.571, 0.0),
        (4435, 6000, -989.24, 1.1823e-1, 2.0798e-6, 0.0, 0.0, 0.0)
    ],
    "UO3": [
        (298.15, 1400, -822.97, 2.5295e-2, 1.4770e-5, 0.0, 4.9754, 0.0),
        (1400, 4435, -707.37, 8.0256e-2, 1.9058e-6, 0.0, -18.131, 0.0),
        (4435, 6000, -1321.1, 1.8201e-1, 2.4230e-6, 0.0, 0.0, 0.0)
    ],
    "UO2c": [
        (298.15, 1400, -1131.0, 1.4405e-1, 8.1068e-6, 0.0, 9.7445, 0.0),
        (1400, 2670, -1079.8, 1.5714e-1, 1.2365e-4, 0.0, 0.0, -2.6564e-1),
        (2670, 3120, -1167.1, 2.4280e-1, -1.4569e-5, 0.0, 0.0, 0.0),
        (3120, 4435, -1002.7, 1.6163e-1, -5.4369e-6, 0.0, 0.0, 0.0),
        (4435, 6000, -1453.7, 2.5458e-1, -3.4634e-6, 0.0, 0.0, 0.0)
    ]
}

def eval_free_energy(species, T):
    ranges = coeffs[species]
    for low, high, A, B, C, D, E, F in ranges:
        if low <= T <= high:
            val = A + B*T + C*T*T + D/T + E*math.log(T) + F*T*T*T
            return val * 1000.0  # J/mol
    raise ValueError(f"No range for T={T} in species {species}")

def blackburn_pO2(T, x):
    A1, B1 = 7.680, -57576
    # FIXED: A2 is -25.986 (not -25986) to avoid overflow and match the paper's results
    A2, B2 = -25.986, 147352
    K1 = math.exp(A1 + B1/T)
    denom = 4*K1 - 1
    arg = 1 - (x*x - 1) * denom
    sqrt_arg = math.sqrt(arg)
    U4 = (-1 + sqrt_arg) / denom
    U2 = (1 + x - U4) / 2.0
    ln_pO2 = 2 * math.log(U4 * (2-x) / U2) - A2 - B2/T
    pO2_atm = math.exp(ln_pO2)
    pO2_MPa = pO2_atm * 0.101325
    return pO2_MPa, pO2_atm

def integrate_delta(T, x_target):
    if x_target <= 0:
        return 0.0
    n = 100
    dx = x_target / n
    xs = [i * dx for i in range(n+1)]
    lns = []
    for x in xs:
        if x == 0:
            _, pO2_atm = blackburn_pO2(T, 0.0)
            lnp = math.log(pO2_atm)
        else:
            _, pO2_atm = blackburn_pO2(T, x)
            lnp = math.log(pO2_atm)
        lns.append(lnp)
    integral = 0.0
    for i in range(n):
        integral += (lns[i] + lns[i+1]) * dx / 2.0
    deltaG = (R * T / 2.0) * integral  # J/mol
    return deltaG

def compute_total_pressure_and_ratio(T, x, pO2_atm, deltaGf_UO2x_c, deltaGf_UO2_g):
    RT = R * T
    ln_pO2 = math.log(pO2_atm)
    dGf_O = eval_free_energy("O", T)
    ln_pO = 0.5 * ln_pO2 - dGf_O / RT
    pO_atm = math.exp(ln_pO)
    ln_pUO2 = (x/2) * ln_pO2 + (deltaGf_UO2x_c - deltaGf_UO2_g) / RT
    pUO2_atm = math.exp(ln_pUO2)
    dGf_UO = eval_free_energy("UO", T)
    ln_pUO = ln_pUO2 - 0.5 * ln_pO2 + (deltaGf_UO2_g - dGf_UO) / RT
    pUO_atm = math.exp(ln_pUO)
    dGf_UO3 = eval_free_energy("UO3", T)
    ln_pUO3 = ln_pUO2 + 0.5 * ln_pO2 + (deltaGf_UO2_g - dGf_UO3) / RT
    pUO3_atm = math.exp(ln_pUO3)
    dGf_U = eval_free_energy("U", T)
    ln_pU = ln_pUO2 - ln_pO2 + (deltaGf_UO2_g - dGf_U) / RT
    pU_atm = math.exp(ln_pU)
    p_total_atm = pO_atm + pO2_atm + pUO2_atm + pUO_atm + pUO3_atm + pU_atm
    p_total_MPa = p_total_atm * 0.101325
    num = pO_atm + 2*pO2_atm + pUO_atm + 2*pUO2_atm + 3*pUO3_atm
    den = pU_atm + pUO_atm + pUO2_atm + pUO3_atm
    vapor_OU = num / den if den > 0 else 0.0
    return p_total_MPa, vapor_OU

output = {}
# target pO2 conditions
for T, x, lbl in [
    (3150, 0.10, "3150_1_90"),
    (3150, 0.04, "3150_1_96"),
    (3150, 0.00, "3150_2_00"),
    (6000, 0.10, "6000_1_90"),
    (6000, 0.04, "6000_1_96"),
    (6000, 0.00, "6000_2_00")
]:
    pO2_MPa, _ = blackburn_pO2(T, x)
    output[f"pO2_{lbl}"] = pO2_MPa

# 5000 K, x=0.00: total pressure
T5 = 5000.0
pO2_00_MPa, pO2_00_atm = blackburn_pO2(T5, 0.0)
dGf_UO2c = eval_free_energy("UO2c", T5)
dGf_UO2g = eval_free_energy("UO2", T5)
# Δ(0,0) = 0, so ΔGf°(UO2-x,c) = ΔGf°(UO2,c) for x=0
p_total, _ = compute_total_pressure_and_ratio(T5, 0.0, pO2_00_atm, dGf_UO2c, dGf_UO2g)
output["total_pressure_5000_UO2"] = p_total

# 5000 K, x=0.04: vapor O/U ratio
x04 = 0.04
pO2_04_MPa, pO2_04_atm = blackburn_pO2(T5, x04)
delta_integral = integrate_delta(T5, x04)
dGf_UO2x_c_04 = dGf_UO2c - delta_integral
_, vapor_OU = compute_total_pressure_and_ratio(T5, x04, pO2_04_atm, dGf_UO2x_c_04, dGf_UO2g)
output["vapor_OU_5000_UO1_96"] = vapor_OU

with open("$OUTDIR/step_01_results.json", "w") as f:
    json.dump(output, f, indent=2)
EOF
