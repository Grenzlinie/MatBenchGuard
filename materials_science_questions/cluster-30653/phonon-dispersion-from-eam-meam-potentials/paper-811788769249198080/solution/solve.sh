#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: step_01_energy_differences.json ===
python3 /solution/generate_outputs.py step_01_energy_differences.json

# === solve block: step_02_structure_factor_data.json ===
python3 /solution/generate_outputs.py step_02_structure_factor_data.json

# === solve block: step_03_rippling_amplitudes.json ===
python3 /solution/generate_outputs.py step_03_rippling_amplitudes.json
