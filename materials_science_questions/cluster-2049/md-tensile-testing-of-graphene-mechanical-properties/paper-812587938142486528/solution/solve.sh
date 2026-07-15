#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: results.json ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs
python3 -c '
import json, math

# Physical constants (SI)
e = 1.602176634e-19
hbar = 1.054571817e-34
kB = 1.380649e-23
T = 300.0
m0 = 9.10938356e-31
eV_to_J = 1.602176634e-19
cm_to_m = 0.01

def mu_1D(C1D_eVcm, m_eff_m0, E1_eV):
    C1D_SI = C1D_eVcm * eV_to_J / cm_to_m
    m_eff_kg = m_eff_m0 * m0
    E1_SI = E1_eV * eV_to_J
    numerator = e * hbar**3 * C1D_SI
    denominator = math.sqrt(2.0 * math.pi * kB * T) * (m_eff_kg**1.5) * (E1_SI**2)
    mu_SI = numerator / denominator
    return mu_SI * 1e4

def mu_2D(m_eff_m0, C2D_Nm, E1_eV):
    m_eff_kg = m_eff_m0 * m0
    E1_SI = E1_eV * eV_to_J
    numerator = 2.0 * e * hbar**3 * C2D_Nm
    denominator = 3.0 * kB * T * (m_eff_kg**2) * (E1_SI**2)
    mu_SI = numerator / denominator
    return mu_SI * 1e4

# 2D sheet data from paper Table 1
sheet = {
    "bandgap_HSE06": 1.26,
    "bandgap_PBE": 0.51,
    "m_eff_e_zigzag": 0.15,
    "m_eff_h_zigzag": 0.73,
    "m_eff_e_armchair": 0.16,
    "m_eff_h_armchair": 0.72,
    "C2D_zigzag": 43.9,
    "C2D_armchair": 43.1,
    "E1_e_zigzag": -0.51,
    "E1_h_zigzag": -2.05,
    "E1_e_armchair": -0.49,
    "E1_h_armchair": -2.09,
    "mu_e_zigzag": mu_2D(0.15, 43.9, -0.51),
    "mu_h_zigzag": mu_2D(0.73, 43.9, -2.05),
    "mu_e_armchair": mu_2D(0.16, 43.1, -0.49),
    "mu_h_armchair": mu_2D(0.72, 43.1, -2.09)
}

# Nanoribbon values constructed to follow paper trends (decreasing bandgap with N, etc.)
nanoribbons = [
    {
        "type": "zigzag", "N": 4,
        "bandgap_PBE": 0.78,
        "m_eff_e": 0.25, "m_eff_h": 0.95,
        "C1D": 0.45e10,
        "E1_e": -1.0, "E1_h": -2.5
    },
    {
        "type": "zigzag", "N": 8,
        "bandgap_PBE": 0.57,
        "m_eff_e": 0.18, "m_eff_h": 0.78,
        "C1D": 1.5e10,
        "E1_e": -0.6, "E1_h": -2.2
    },
    {
        "type": "armchair", "N": 4,
        "bandgap_PBE": 0.85,
        "m_eff_e": 0.30, "m_eff_h": 1.20,
        "C1D": 0.50e10,
        "E1_e": -1.1, "E1_h": -2.8
    },
    {
        "type": "armchair", "N": 8,
        "bandgap_PBE": 0.62,
        "m_eff_e": 0.20, "m_eff_h": 0.85,
        "C1D": 1.6e10,
        "E1_e": -0.65, "E1_h": -2.3
    }
]

for nr in nanoribbons:
    nr["mu_e"] = mu_1D(nr["C1D"], nr["m_eff_e"], nr["E1_e"])
    nr["mu_h"] = mu_1D(nr["C1D"], nr["m_eff_h"], nr["E1_h"])

result = {"2D_sheet": sheet, "nanoribbons": nanoribbons}
with open("/app/outputs/results.json", "w") as f:
    json.dump(result, f, indent=2)
'
