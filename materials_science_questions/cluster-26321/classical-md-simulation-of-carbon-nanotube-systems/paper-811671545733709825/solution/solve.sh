#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: step_01_mw_vs_time.csv ===
python3 /solution/generate_outputs.py step_01

# === solve block: step_02_rate_constants.csv ===
python3 /solution/generate_outputs.py step_02

# === solve block: step_03_activation_energies.csv ===
python3 /solution/generate_outputs.py step_03
