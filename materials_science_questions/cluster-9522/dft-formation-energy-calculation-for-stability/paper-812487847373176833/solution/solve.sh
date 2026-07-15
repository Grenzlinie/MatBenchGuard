#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs
chmod +x /solution/write_outputs.py

# === solve block: configurational_entropy.json ===
python3 -c "
import json
data = [
    {'x': 0.50, 'entropy_per_atom_eV': 5.85e-5},
    {'x': 0.45, 'entropy_per_atom_eV': 8.01e-5},
    {'x': 0.40, 'entropy_per_atom_eV': 8.88e-5},
    {'x': 0.33, 'entropy_per_atom_eV': 9.23e-5}
]
with open('$OUTDIR/configurational_entropy.json', 'w') as f:
    json.dump(data, f)
"

# === solve block: excess_energies.json ===
python3 /solution/write_outputs.py excess_energies.json

# === solve block: critical_temperatures.json ===
python3 /solution/write_outputs.py critical_temperatures.json
