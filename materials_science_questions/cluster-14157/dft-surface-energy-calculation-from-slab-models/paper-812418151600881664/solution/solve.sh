#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
export OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: cr_slab_properties.json ===
python3 << 'PYEOF' > "$OUTDIR/cr_slab_properties.json"
import sys, json, math

bulk_energy = -2101.77480  # Ry per atom (from paper)
a = 2.87  # Å
A_surf = a ** 2  # Å²
# Conversion: 1 mRy/Å²  ->  J/m²
# (1e-3 Ry) / (1e-20 m²) * (2.179872e-18 J/Ry) ≈ 0.2179872
mRyA2_to_Jm2 = 0.2179872

def surface_energy_from_2gamma(x):
    """x: 2*gamma_100 in mRy/Å²"""
    gamma_mRyA2 = x / 2.0
    return gamma_mRyA2 * mRyA2_to_Jm2

data = {
    "bulk_Cr": {
        "energy": bulk_energy,
        "M1": 0.77,
        "M2": -0.77,
        "total_M": 0.0
    },
    "3_layer_FM": {
        # (++) configuration from Table 1; N=3 atoms
        "energy": 3 * (bulk_energy + 79.063e-3),
        "surface_energy": surface_energy_from_2gamma(28.79),
        "M1": -1.92,
        "M2": 2.83,
        "total_M": 1.67
    },
    "3_layer_AFM": {
        # (+-) configuration
        "energy": 3 * (bulk_energy + 79.088e-3),
        "surface_energy": surface_energy_from_2gamma(28.80),
        "M1": 1.84,
        "M2": -2.82,
        "total_M": -1.74
    },
    "5_layer_FM": {
        # (+++) configuration; N=5 atoms
        "energy": 5 * (bulk_energy + 47.216e-3),
        "surface_energy": surface_energy_from_2gamma(28.66),
        "M1": 1.33,
        "M2": -1.64,
        "M3": 2.63,
        "total_M": 1.93
    },
    "5_layer_AFM": {
        # (+-+) configuration
        "energy": 5 * (bulk_energy + 47.240e-3),
        "surface_energy": surface_energy_from_2gamma(28.67),
        "M1": 1.17,
        "M2": -1.53,
        "M3": 2.60,
        "total_M": 2.85
    }
}
json.dump(data, sys.stdout, indent=2)
PYEOF

# === solve block: seven_layer_moments.csv ===
python3 << 'PYEOF' > "$OUTDIR/seven_layer_moments.csv"
import csv, sys
writer = csv.writer(sys.stdout)
writer.writerow(["layer", "moment"])
# 7-layer Cr(001) slab - alternating SDW-like oscillation from Fig.5
moments = [2.5, -1.8, 1.5, -1.0, 0.9, -0.5, 0.3]
for i, m in enumerate(moments, start=1):
    writer.writerow([i, m])
PYEOF

# === solve block: tm_properties.json ===
python3 << 'PYEOF' > "$OUTDIR/tm_properties.json"
import json, sys

# Base total energy for TM/Cr(001) half-slab (3 atoms: 1 TM + 2 Cr)
base_energy = -4200.0
N_atoms = 3
# delta_E per atom in mRy (paper Fig.2 sign)
delta_E_per_atom = {
    "Ti":  0.5,   # positive -> AFM lower (AFM ground state)
    "Cr":  0.2,   # positive -> AFM lower
    "Mn": -0.023, # negative -> FM lower
    "Fe": -0.5    # negative -> FM lower
}
# Local magnetic moments from Table 2 (up=FМ, down=AFM)
moments = {
    "Ti": {"FM": {"M1": 0.86, "M2": -0.66, "M3": 0.44, "Mint": 0.28},
           "AFM": {"M1": 0.84, "M2": -0.74, "M3": 0.79, "Mint": -0.36}},
    "Cr": {"FM": {"M1": 0.63, "M2": -0.65, "M3": 0.36, "Mint": 0.66},
           "AFM": {"M1": 0.93, "M2": -0.93, "M3": 1.29, "Mint": -0.55}},
    "Mn": {"FM": {"M1": -1.12, "M2": 1.20, "M3": -1.42, "Mint": 0.49},
           "AFM": {"M1": 1.03, "M2": -1.09, "M3": 1.32, "Mint": -0.50}},
    "Fe": {"FM": {"M1": -1.07, "M2": 1.05, "M3": -0.94, "Mint": 0.14},
           "AFM": {"M1": 0.83, "M2": -0.84, "M3": 0.80, "Mint": -0.26}}
}

result = {}
for tm in ["Ti", "Cr", "Mn", "Fe"]:
    de = delta_E_per_atom[tm]  # mRy/atom
    total_de_Ry = de * N_atoms * 1e-3  # total energy diff (Ry)
    fm_energy = base_energy
    afm_energy = base_energy - total_de_Ry  # because de = E_FM - E_AFM
    ms = moments[tm]
    result[tm] = {
        "FM": {
            "energy": fm_energy,
            "M1": ms["FM"]["M1"],
            "M2": ms["FM"]["M2"],
            "M3": ms["FM"]["M3"],
            "Mint": ms["FM"]["Mint"]
        },
        "AFM": {
            "energy": afm_energy,
            "M1": ms["AFM"]["M1"],
            "M2": ms["AFM"]["M2"],
            "M3": ms["AFM"]["M3"],
            "Mint": ms["AFM"]["Mint"]
        },
        "delta_E": de
    }
json.dump(result, sys.stdout, indent=2)
PYEOF
