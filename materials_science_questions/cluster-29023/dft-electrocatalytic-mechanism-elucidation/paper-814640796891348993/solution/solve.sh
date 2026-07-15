#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: step_05_adsorption_energies.json ===
python3 /solution/write_artifacts.py

# === solve block: step_07_overpotential.json ===
python3 /solution/write_artifacts.py
