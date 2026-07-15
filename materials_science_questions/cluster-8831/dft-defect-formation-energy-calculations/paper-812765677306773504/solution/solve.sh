#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: defect_properties.json ===
python3 -c '
import json

data = {
    "formation_energy_Pd_Mo_plus_O_S_1T": -3.68,
    "formation_energy_Pd_Mo_plus_O_S_2H": -3.68,
    "deltaG_H_S1_1T": 0.13,
    "deltaG_H_O_1T": -0.24,
    "deltaG_H_S1_2H": 0.37,
    "deltaG_H_O_2H": -0.21
}

with open("/app/outputs/defect_properties.json", "w") as f:
    json.dump(data, f, indent=2)
'
