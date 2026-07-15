#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"
python3 /solution/write_outputs.py

# === solve block: step_01_lattice_constants.json ===
echo '{"VTiRhAl": 6.16, "VTiRhGa": 6.15, "VTiRhIn": 6.38}' > "$OUTDIR/step_01_lattice_constants.json"

# === solve block: step_02_phonon_stability.json ===
# This file is written by the shared preamble script /solution/write_outputs.py

# === solve block: step_03_elastic_constants.json ===
# This file is written by the shared preamble script /solution/write_outputs.py

# === solve block: step_04_electronic_properties.json ===
# This file is written by the shared preamble script /solution/write_outputs.py

# === solve block: step_05_magnetic_moments.json ===
# This file is written by the shared preamble script /solution/write_outputs.py

# === solve block: step_06_thermoelectric.json ===
# This file is written by the shared preamble script /solution/write_outputs.py
