#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
export OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: elastic_constants.json ===
python3 /solution/write_artifact.py elastic_constants.json

# === solve block: polycrystalline_sound_velocities.json ===
python3 /solution/write_artifact.py polycrystalline_sound_velocities.json

# === solve block: debye_temp_from_elastic.json ===
python3 /solution/write_artifact.py debye_temp_from_elastic.json

# === solve block: thermodynamic_properties.json ===
python3 /solution/write_artifact.py thermodynamic_properties.json
