#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: reorganization_energies.json ===
python3 << 'PYEOF'
import json

ha_per_ev = 1.0 / 27.2114

molecules_data = [
    {"name": "pentacene",           "l1": 0.048, "l2": 0.046, "l3": 0.056, "l4": 0.094},
    {"name": "2-fluoropentacene",    "l1": 0.046, "l2": 0.095, "l3": 0.068, "l4": 0.128},
    {"name": "2-chloropentacene",    "l1": 0.049, "l2": 0.054, "l3": 0.081, "l4": 0.052},
    {"name": "2-bromopentacene",     "l1": 0.060, "l2": 0.046, "l3": 0.079, "l4": 0.057},
    {"name": "2,9-difluoropentacene","l1": 0.071, "l2": 0.053, "l3": 0.081, "l4": 0.046},
    {"name": "2,9-dichloropentacene","l1": 0.062, "l2": 0.054, "l3": 0.080, "l4": 0.060},
    {"name": "2,9-dibromopentacene", "l1": 0.060, "l2": 0.048, "l3": 0.060, "l4": 0.079},
]

output = []
for mol in molecules_data:
    l1_ha = mol["l1"] * ha_per_ev
    l2_ha = mol["l2"] * ha_per_ev
    l3_ha = mol["l3"] * ha_per_ev
    l4_ha = mol["l4"] * ha_per_ev
    entry = {
        "molecule": mol["name"],
        "E0_Q0": 0.0,
        "E0_Qplus": l1_ha,
        "E0_Qminus": l3_ha,
        "Eplus_Q0": l2_ha,
        "Eplus_Qplus": 0.0,
        "Eminus_Q0": l4_ha,
        "Eminus_Qminus": 0.0,
    }
    output.append(entry)

with open("/app/outputs/reorganization_energies.json", "w") as f:
    json.dump({"molecules": output}, f, indent=2)
PYEOF
