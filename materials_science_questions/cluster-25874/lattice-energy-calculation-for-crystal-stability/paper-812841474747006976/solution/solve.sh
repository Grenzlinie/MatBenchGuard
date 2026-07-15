#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: force_field_parameters.json ===
python3 /solution/write_artifacts.py force_field_parameters.json

# === solve block: gas_properties.csv ===
python3 /solution/write_artifacts.py gas_properties.csv

# === solve block: solid_density_298K.csv ===
python3 /solution/write_artifacts.py solid_density_298K.csv

# === solve block: liquid_density_Tm.csv ===
python3 /solution/write_artifacts.py liquid_density_Tm.csv
