#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
export OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: step_01_magnetoelastic_params.json ===
python3 /solution/write_outputs.py step01

# === solve block: step_02_polarization_contributions.json ===
python3 /solution/write_outputs.py step02

# === solve block: step_03_field_dependence.csv ===
python3 /solution/write_outputs.py step03
