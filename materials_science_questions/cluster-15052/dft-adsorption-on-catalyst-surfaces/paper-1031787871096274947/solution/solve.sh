#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs
OUTDIR=/app/outputs

# === solve block: ch4_barriers.json ===
python3 -c '
import json
data = [
    {"system": "Pd-CeO2", "step": "CH4_activation", "activation_energy_eV": 0.33},
    {"system": "Pd-iC-CeO2", "step": "CH4_activation", "activation_energy_eV": 1.03}
]
with open("/app/outputs/ch4_barriers.json","w") as f:
    json.dump(data, f, indent=2)
'

# === solve block: er_barriers.json ===
python3 -c '
import json
data = [
    {"system": "Pd-CeO2", "step": "CH2OH_formation", "activation_energy_eV": 1.33},
    {"system": "Pd-CeO2", "step": "CH3OH_formation", "activation_energy_eV": 1.55},
    {"system": "Pd-iC-CeO2", "step": "CH2OH_formation", "activation_energy_eV": 0.70},
    {"system": "Pd-iC-CeO2", "step": "CH3OH_formation", "activation_energy_eV": 0.44}
]
with open("/app/outputs/er_barriers.json","w") as f:
    json.dump(data, f, indent=2)
'
