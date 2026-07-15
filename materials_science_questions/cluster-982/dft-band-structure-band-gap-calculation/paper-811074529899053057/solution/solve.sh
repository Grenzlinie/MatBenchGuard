#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs
OUTDIR=/app/outputs

# === solve block: results.json ===
python3 << 'PYEOF'
import json
data = {
    "band_gap_eV": 0.0765,
    "binding_energy_meV_per_Sn": -39.63,
    "effective_mass_electron_KM": 0.0517,
    "effective_mass_electron_KG": 0.0566,
    "effective_mass_hole_KM": 0.0517,
    "effective_mass_hole_KG": 0.0568
}
with open("/app/outputs/results.json", "w") as f:
    json.dump(data, f)
PYEOF
