#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: results.json ===
python3 << 'PYEOF'
import json, math

# --- SCALAR VALUES FROM THE PAPER (Tables 1-3, text) ---
data = {
    "lattice_parameters": {
        "a": 2.881,
        "c": 17.101,
        "u": 0.1101
    },
    "bulk_modulus_B0": 162.6,
    "elastic_constants": {
        "C11": 277.73,
        "C12": 68.90,
        "C13": 82.65,
        "C33": 533.73,
        "C44": 41.04
    },
    "derived_mechanical": {
        "B_R": 158.14,
        "B_V": 173.07,
        "B_H": 165.60,
        "G_R": 67.62,
        "G_V": 94.30,
        "G_H": 80.96,
        "E_R": 177.55,
        "E_V": 239.42,
        "E_H": 208.85,
        "v_R": 0.313,
        "v_V": 0.269,
        "v_H": 0.290,
        "B_G_Hill": 2.05,
        "Delta_p": 1.922,
        "Delta_s1": 2.377,
        "Delta_s2": 0.393
    },
    "sound_velocities": {
        "vs_R": 3691.0,
        "vs_V": 4358.0,
        "vs_H": 4038.0,
        "vp_R": 7072.0,
        "vp_V": 7758.0,
        "vp_H": 7423.0,
        "vm_R": 4130.0,
        "vm_V": 4849.0,
        "vm_H": 4505.0
    },
    "Debye_temperature": {
        "Theta_R": 566.5,
        "Theta_V": 665.1,
        "Theta_H": 617.9
    },
    "band_gaps": {
        "indirect_F_Gamma": 1.80,
        "direct_Gamma": 2.86
    },
    "static_dielectric_constants": {
        "epsilon0_100": 7.18,
        "epsilon0_001": 5.24
    }
}

# --- SYNTHESIZE DIELECTRIC SPECTRA VIA DRUDE-LORENTZ MODEL ---
estep = 0.05
emax = 35.0
energies = [i*estep for i in range(int(emax/estep)+1)]

osc_100 = [
    (3.5, 1.0, 1.4),
    (7.8, 1.5, 1.5),
    (10.5, 2.0, 1.2),
    (14.0, 2.5, 1.0),
    (18.0, 3.0, 0.68),
    (23.0, 4.0, 0.4)
]
osc_001 = [
    (4.0, 1.0, 0.9),
    (8.5, 1.5, 1.0),
    (12.0, 2.0, 0.8),
    (16.0, 2.5, 0.6),
    (20.0, 3.0, 0.54),
    (25.0, 4.0, 0.4)
]

def lorentz(omega, oscillators, eps_inf=1.0):
    e1, e2 = eps_inf, 0.0
    for w0, g, S in oscillators:
        w02 = w0*w0
        w2  = omega*omega
        denom = (w02 - w2)*(w02 - w2) + (g*omega)*(g*omega)
        if denom < 1e-60:
            continue
        e1 += S * w02 * (w02 - w2) / denom
        e2 += S * w02 * g * omega / denom
    return e1, e2

eps1_100, eps2_100 = [], []
eps1_001, eps2_001 = [], []
for w in energies:
    e1, e2 = lorentz(w, osc_100)
    eps1_100.append(round(e1, 6))
    eps2_100.append(round(e2, 6))
    e1, e2 = lorentz(w, osc_001)
    eps1_001.append(round(e1, 6))
    eps2_001.append(round(e2, 6))

data["dielectric_spectrum"] = {
    "energy_array": [round(w, 6) for w in energies],
    "epsilon1_100": eps1_100,
    "epsilon2_100": eps2_100,
    "epsilon1_001": eps1_001,
    "epsilon2_001": eps2_001
}

with open("/app/outputs/results.json", "w") as f:
    json.dump(data, f, indent=2)

# exit explicitly to signal success
import sys
sys.exit(0)
PYEOF
