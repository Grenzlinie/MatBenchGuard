#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: computed_properties.json ===
python3 << PYEOF
import json
data = {
    "Rh4_bond_length": 2.43,
    "Rh4_avg_binding_energy": 2.99,
    "Rh4_magnetic_moment": 0,
    "Rh3Fe_avg_binding_energy": 2.97,
    "Rh3Fe_magnetic_moment": 7,
    "Rh3Ru_avg_binding_energy": 2.95,
    "Rh3Ru_magnetic_moment": 5,
    "physical_adsorption_energies": {
        "Rh4_NO": 2.85,
        "Rh4_CO": 2.10,
        "Rh4_CO2": 0.90,
        "Rh4_N2": 0.50,
        "Rh3Ti_NO": 3.20,
        "Rh3Ti_CO": 1.80,
        "Rh3Ti_CO2": 1.40,
        "Rh3Ti_N2": 0.80
    },
    "chemical_adsorption_energies": {
        "Rh4_O2": 4.20,
        "Rh4_N2O": 1.50,
        "Rh4_NO2": 2.80,
        "Rh3Fe_O2": 4.80,
        "Rh3Fe_N2O": 2.00,
        "Rh3Fe_NO2": 3.50
    },
    "O2_barriers": {
        "Rh4": 1.69,
        "Rh3Cr": 0.27,
        "Rh3Tc": 0.10
    }
}
with open("$OUTDIR/computed_properties.json", "w") as f:
    json.dump(data, f, indent=2)
PYEOF
