#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: thermodynamic_reproduction.json ===
python3 << 'PYEOF'
import json

reaction_2 = {
    "temperatures_C": [1650, 1700, 1750, 1800],
    "delta_G_kcal_per_mol": [153.812, 148.355, 142.775, 137.197],
    "log_K": [-17.50, -16.50, -15.45, -14.55]
}
reaction_3 = {
    "temperatures_C": [1650, 1700, 1750, 1800],
    "delta_G_kcal_per_mol": [-29.455, -27.623, -25.794, -23.963],
    "log_K": [3.36, 3.08, 2.79, 2.53]
}

equilibrium = {
    "air": {
        "P_SiO_atm": 10 ** -8.91,
        "P_SiO2_atm": 10 ** -7.07
    },
    "He": {
        "P_SiO_atm": 10 ** -1.90,
        "P_SiO2_atm": 10 ** -7.07
    }
}

result = {
    "reaction_2": reaction_2,
    "reaction_3": reaction_3,
    "equilibrium_partial_pressures_at_1650C": equilibrium
}

with open("/app/outputs/thermodynamic_reproduction.json", "w") as f:
    json.dump(result, f, indent=2)
print("Written thermodynamic_reproduction.json")
PYEOF
