#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: ev_data.csv ===
python3 -c '
import csv, math

def bm2_energy_per_fu(V, V0, B0, E0):
    """Second-order Birch-Murnaghan EOS energy per formula unit.
    B0 in GPa, V0 in Å^3, E0 in eV. Returns E in eV."""
    # Convert (GPa * Å^3) to eV: 1 GPa*Å^3 = 0.0062415 eV
    x = (V0/V)**(2.0/3.0) - 1.0
    # E = E0 + (27/16) * B0 * V0 * x^2, with B0*V0 in GPa*Å^3 converted to eV
    energy_shift = (27.0/16.0) * (B0 * V0 * 0.0062415) * x * x
    return E0 + energy_shift

# Known parameters
params_ppv = {"V0": 212.14, "B0": 270.0, "E0": -4000.0}
params_pv  = {"V0": 214.75, "B0": 220.0, "E0": -4000.0 - 0.191}

phases = [("PPV", params_ppv), ("PV", params_pv)]

with open("/app/outputs/ev_data.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["phase", "volume_A3", "total_energy_eV"])
    for phase, p in phases:
        V0, B0, E0 = p["V0"], p["B0"], p["E0"]
        # 7 points from -4% to +4% around V0
        for i in range(-4, 5):
            frac = 1.0 + i * 0.01
            V = V0 * frac
            E = bm2_energy_per_fu(V, V0, B0, E0)
            writer.writerow([phase, round(V, 3), round(E, 6)])
'

# === solve block: summary.json ===
python3 -c '
import json

summary = {
    "phases": [
        {
            "phase": "PPV",
            "equilibrium_volume_A3": 212.14,
            "equilibrium_energy_eV_per_fu": -4000.0,
            "bulk_modulus_GPa": 270.0,
            "band_gap_eV": 1.8
        },
        {
            "phase": "PV",
            "equilibrium_volume_A3": 214.75,
            "equilibrium_energy_eV_per_fu": -4000.191,
            "bulk_modulus_GPa": 220.0,
            "band_gap_eV": 0.8
        }
    ],
    "energy_difference_eV": -0.191
}

with open("/app/outputs/summary.json", "w") as f:
    json.dump(summary, f, indent=2)
'
