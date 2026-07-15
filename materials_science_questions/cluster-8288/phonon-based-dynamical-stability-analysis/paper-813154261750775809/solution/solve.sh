#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: enthalpy_curves.json ===
python3 /solution/generate_outputs.py enthalpy > /app/outputs/enthalpy_curves.json

# === solve block: phonon_frequencies.json ===
python3 /solution/generate_outputs.py phonon > /app/outputs/phonon_frequencies.json
