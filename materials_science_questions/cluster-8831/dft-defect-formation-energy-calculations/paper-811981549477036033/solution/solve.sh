#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: reaction_energies.json ===
python3 <<'PYEOF'
import json

total = {
    "forsterite": 0.0,
    "MgO": 0.0,
    "alpha_quartz": 0.0,
    "H2O_isolated": 0.0,
    "forsterite_H2O_absorbed": 230.1/96.485,
    "MgO_H2O_absorbed": 513.6/96.485,
    "alpha_quartz_H2O_absorbed": 107.9/96.485,
    "forsterite_Si_vacancy": -5.9/96.485,
    "alpha_quartz_Si_vacancy": -2*24.8/96.485,
    "forsterite_Mg_vacancy_M1": 25.0/96.485,
    "forsterite_Mg_vacancy_M2": 113.4/96.485,
    "MgO_vacancy": 66.9/96.485
}

reaction = {
    "water_absorption_forsterite": 230.1,
    "water_absorption_MgO": 513.6,
    "water_absorption_alpha_quartz": 107.9,
    "SiO2_replacement_forsterite": -5.9,
    "SiO2_replacement_alpha_quartz": -24.8,
    "MgO_replacement_M1_forsterite": 25.0,
    "MgO_replacement_M2_forsterite": 113.4,
    "MgO_replacement_MgO": 66.9
}

output = {
    "total_energies": total,
    "reaction_energies": reaction
}

with open("/app/outputs/reaction_energies.json", "w") as f:
    json.dump(output, f, indent=2)
PYEOF
