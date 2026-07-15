#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: step_01_total_energies.json ===
python3 /solution/generate_outputs.py step_01 > /app/outputs/step_01_total_energies.json

# === solve block: step_02_formation_energies.json ===
python3 /solution/generate_outputs.py step_02 > /app/outputs/step_02_formation_energies.json

# === solve block: step_03_transition_levels.json ===
python3 /solution/generate_outputs.py step_03 > /app/outputs/step_03_transition_levels.json

# === solve block: step_04_defect_hull.json ===
python3 /solution/generate_outputs.py step_04 > /app/outputs/step_04_defect_hull.json
