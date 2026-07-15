#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs
export PYTHONPATH="/solution:${PYTHONPATH:-}"

# === solve block: step_01_band_structure.json ===
python3 -c "from generate_data import write_band_structure; write_band_structure('/app/outputs/step_01_band_structure.json')"

# === solve block: step_02_phonon_dispersion.json ===
python3 -c "from generate_data import write_phonon_dispersion; write_phonon_dispersion('/app/outputs/step_02_phonon_dispersion.json')"

# === solve block: step_03_strain_results.json ===
python3 -c "from generate_data import write_strain_results; write_strain_results('/app/outputs/step_03_strain_results.json')"
