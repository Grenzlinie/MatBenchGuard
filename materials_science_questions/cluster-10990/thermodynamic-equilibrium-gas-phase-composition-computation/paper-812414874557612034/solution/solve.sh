#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: thermochemistry_results.json ===
python3 <<'PYEOF'
import json

output = {
    "reaction_enthalpies": {
        "Li2O(s)->Li+LiO": {
            "average_DeltaH0": 188.4,
            "standard_deviation": 1.5,
            "values": [183.9, 187.0, 188.9, 191.3, 188.5, 188.2, 188.8, 189.4, 189.4, 188.5, 188.5, 188.1, 189.0, 187.7, 189.1, 187.8]
        },
        "Li2O(g)->Li+LiO": {
            "average_DeltaH0": 89.1,
            "standard_deviation": 1.4,
            "values": [84.64, 87.78, 89.56, 92.01, 89.17, 88.55, 89.51, 89.94, 89.96, 89.13, 89.15, 89.04, 89.72, 88.86, 89.32, 88.76]
        }
    },
    "heat_of_formation": {
        "LiO_g": {"DeltaH0_0": 8.3, "uncertainty": 3.3},
        "Li2O_g": {"DeltaH0_0": -42.3, "uncertainty": 1.1}
    },
    "atomization_energy": {
        "LiO": {"D0_0": 89.2, "uncertainty": 3.3},
        "Li2O": {"D0_0": 178.3, "uncertainty": 1.1}
    }
}

with open("/app/outputs/thermochemistry_results.json", "w") as f:
    json.dump(output, f, indent=2)
PYEOF
