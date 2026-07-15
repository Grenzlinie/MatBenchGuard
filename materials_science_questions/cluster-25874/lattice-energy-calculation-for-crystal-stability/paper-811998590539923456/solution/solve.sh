#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: computed_results.json ===
python3 <<'PYEOF'
import json, math

anion_volume = 0.102

cation_volumes = {
    "1": 0.131,
    "2": 0.157,
    "3": 0.178,
    "4": 0.199,
    "5": 0.201,
    "6": 0.203,
    "7": 0.218,
    "8": 0.221,
    "9": 0.223
}

lattice_energies = {}
for label, v_cat in cation_volumes.items():
    V = v_cat + anion_volume
    UL = 2.0 * (117.3 * (V ** (-1.0/3.0)) + 51.9)
    dHL = UL + 5.0
    dGL = dHL - 298.0 * (1360.0 * V + 15.0) / 1000.0
    lattice_energies[label] = {
        "UL": round(UL, 1),
        "dHL": round(dHL, 1),
        "dGL": round(dGL, 1)
    }

result = {
    "anion_volume_nm3": anion_volume,
    "cation_volumes_nm3": cation_volumes,
    "lattice_energies_kJmol": lattice_energies
}

with open("/app/outputs/computed_results.json", "w") as f:
    json.dump(result, f, indent=2)
PYEOF
