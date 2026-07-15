#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs
export OUTDIR=/app/outputs

# === solve block: defect_energies.json ===
python3 -c "
import json
data = {
    'Si_dangling_bond_Si3N4': 2.6,
    'Si_dangling_bond_Si3N4_O': 2.8,
    'Si_Si_bond_Si3N4': -0.7,
    'Si_Si_bond_Si3N4_O': -0.55,
    'Si_dangling_bond_SiO2': 3.9,
    'Si_dangling_bond_SiO2_N': 3.7,
    'Si_Si_bond_SiO2': 0.7,
    'Si_Si_bond_SiO2_N': 0.5
}
with open('/app/outputs/defect_energies.json', 'w') as f:
    json.dump(data, f)
"
