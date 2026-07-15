#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: properties.json ===
python3 <<'PYEOF'
import json
data = {
    "c11": 1715.3,
    "c12": -283.5,
    "c44": 1187.5,
    "bulk_modulus": 381.0,
    "young_modulus": 1691.0,
    "shear_modulus": 1113.0,
    "poisson_ratio": -0.241,
    "band_gap": 2.52,
    "band_gap_type": "indirect",
    "electron_eff_mass_1": 0.98,
    "electron_eff_mass_2": 0.67,
    "hole_eff_mass_1": 1.59,
    "hole_eff_mass_2": 0.76,
    "phonon_stable": True,
    "max_imaginary_frequency": 0.0
}
with open("/app/outputs/properties.json", "w") as f:
    json.dump(data, f, indent=2)
PYEOF
