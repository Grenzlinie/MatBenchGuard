#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p "$OUTDIR"

# === solve block: mechanical_properties.json ===
python3 << 'PYEOF'
import json, os

outdir = os.environ.get('OUTDIR', '/app/outputs')

systems = [
    {"system": "SiO2 30k", "strength_GPa": 10.9, "strain_at_failure_percent": 14.5, "youngs_modulus_GPa": 78.1},
    {"system": "SiO2 30k with Notch 1.0 nm long.", "strength_GPa": 9.0, "strain_at_failure_percent": None, "youngs_modulus_GPa": 76.5},
    {"system": "SiO2 30k with Notch 2.0 nm long.", "strength_GPa": 8.2, "strain_at_failure_percent": None, "youngs_modulus_GPa": 75.5},
    {"system": "SiO2 Nanowire", "strength_GPa": 8.7, "strain_at_failure_percent": 13.0, "youngs_modulus_GPa": 73.2},
    {"system": "NS20 30k", "strength_GPa": 5.1, "strain_at_failure_percent": 17.0, "youngs_modulus_GPa": 50.5},
    {"system": "NS20 60k", "strength_GPa": 5.1, "strain_at_failure_percent": 17.0, "youngs_modulus_GPa": 50.5},
    {"system": "NS20 Nanowire", "strength_GPa": 4.6, "strain_at_failure_percent": 17.3, "youngs_modulus_GPa": 37.2}
]

with open(os.path.join(outdir, "mechanical_properties.json"), "w") as f:
    json.dump(systems, f, indent=2)
PYEOF
