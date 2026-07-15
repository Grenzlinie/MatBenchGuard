#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: results.json ===
python3 <<'EOF'
import json, sys, os

e = 1.602176634e-19
chi = 2.9
z = 1
d_Ang = 1.2e-10
eps_r = 3.9
eps0_eV_Vcm = 5.52e5
Nv = 2.3e22
DeltaH0 = 1.15
kB = 8.617333262145e-5

p = 3 * z * e * d_Ang  # C m
Eloc_factor = (3 + chi) / 3.0

alpha = (3 * (eps_r - 1) * eps0_eV_Vcm) / ((eps_r + 2) * Nv)

Eox_10 = 10.0
Eox_SI_10 = Eox_10 * 1e8
Eloc_SI_10 = Eloc_factor * Eox_SI_10
Eloc_Vcm_10 = Eloc_SI_10 * 0.01
p_ecm = (p / e) * 100.0
ratio = 0.5 * alpha * Eloc_Vcm_10 / p_ecm

Eox_list = [0,2,4,6,8,10]
activation_enthalpy_data = []
for Eox in Eox_list:
    Eox_SI = Eox * 1e8
    Eloc_SI = Eloc_factor * Eox_SI
    energy_eV = p * Eloc_SI / e
    delta_H = DeltaH0 - energy_eV
    activation_enthalpy_data.append({
        "E_ox": Eox,
        "E_loc": Eloc_factor * Eox,
        "delta_H": delta_H
    })

coeff = (p * Eloc_factor * 1e8) / e
slope = -coeff

field_accel = []
for T in [300,400,500]:
    kBT = kB * T
    gamma = coeff / kBT
    field_accel.append({"T": T, "gamma": gamma})

result = {
    "alpha": alpha,
    "quadratic_to_linear_ratio": ratio,
    "activation_enthalpy_slope": slope,
    "activation_enthalpy_data": activation_enthalpy_data,
    "field_acceleration_data": field_accel
}

with open("/app/outputs/results.json", "w") as f:
    json.dump(result, f, indent=2)
EOF
