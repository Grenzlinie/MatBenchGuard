#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: model1_structural_properties.json ===
python3 /solution/oracle.py model1_structural_properties.json

# === solve block: model2_structural_properties.json ===
python3 /solution/oracle.py model2_structural_properties.json

# === solve block: model1_defect_outcome.json ===
python3 /solution/oracle.py model1_defect_outcome.json

# === solve block: model2_excitation_49_50_defect.json ===
python3 /solution/oracle.py model2_excitation_49_50_defect.json

# === solve block: model2_excitation_32_54_defect.json ===
python3 /solution/oracle.py model2_excitation_32_54_defect.json

# === solve block: model2_defect_dos.json ===
python3 /solution/oracle.py model2_defect_dos.json
