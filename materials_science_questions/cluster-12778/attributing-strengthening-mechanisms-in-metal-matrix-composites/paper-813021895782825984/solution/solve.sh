#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: step_01_formation_enthalpies.json ===
python3 << 'PYEOF' > "$OUTDIR/step_01_formation_enthalpies.json"
import json
data = {"Re_Al": 0.910, "Re_Ni": 0.996, "Al_Ni": -0.968, "Ni_Al": 2.04, "perfect": 0.0}
print(json.dumps(data, indent=2))
PYEOF

# === solve block: step_02_energy_factor.json ===
python3 << 'PYEOF' > "$OUTDIR/step_02_energy_factor.json"
import json
data = {"E_Re_Ni_to_Al": -1.05}
print(json.dumps(data, indent=2))
PYEOF

# === solve block: step_03_correlative_energies.json ===
python3 << 'PYEOF' > "$OUTDIR/step_03_correlative_energies.json"
import json
data = {
    "configurations": [
        {"label": "Al-Al 2nd", "d": 3.635, "Delta_E": 0.120},
        {"label": "Al-Al 6th", "d": 6.182, "Delta_E": 0.014},
        {"label": "Al-Ni 1st", "d": 2.541, "Delta_E": -0.079},
        {"label": "Ni-Ni 1st", "d": 2.431, "Delta_E": -0.212}
    ]
}
print(json.dumps(data, indent=2))
PYEOF

# === solve block: step_04_shear_strengths.json ===
python3 << 'PYEOF' > "$OUTDIR/step_04_shear_strengths.json"
import json
data = {
    "configurations": [
        {"label": "pure", "sigma_max": 4.23},
        {"label": "Re_Al", "sigma_max": 5.59},
        {"label": "Re_Ni1", "sigma_max": 3.78},
        {"label": "V_Re_Al_Re_Al(2nd)", "sigma_max": 6.90}
    ]
}
print(json.dumps(data, indent=2))
PYEOF
