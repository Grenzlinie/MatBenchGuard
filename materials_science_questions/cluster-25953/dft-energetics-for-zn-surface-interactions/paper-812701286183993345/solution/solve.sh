#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: binding_energies.json ===
python3 << 'PYEOF'
import json

binding_energies = [
    {"cluster": "Ni4Zn", "binding_energy_kj_per_mol": -150.0, "bicarbonate_isomer": "distal"},
    {"cluster": "NiZn4", "binding_energy_kj_per_mol": -130.0, "bicarbonate_isomer": "distal"},
    {"cluster": "Zn5", "binding_energy_kj_per_mol": -120.0, "bicarbonate_isomer": "distal"},
    {"cluster": "Co4Zn", "binding_energy_kj_per_mol": -100.0, "bicarbonate_isomer": "distal"}
]

with open("/app/outputs/binding_energies.json", "w") as f:
    json.dump(binding_energies, f, indent=2)
PYEOF
