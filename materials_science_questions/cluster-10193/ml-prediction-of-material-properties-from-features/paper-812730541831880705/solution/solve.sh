#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"
# Generate all reference artifacts via the bundled script
python3 /solution/generate_reference.py

# === solve block: step_01_stability_screening.csv ===
python3 /solution/generate_reference.py step_01

# === solve block: step_02_DeltaG_Ostar.csv ===
python3 /solution/generate_reference.py step_02

# === solve block: step_03_selective_SACs.csv ===
python3 /solution/generate_reference.py step_03

# === solve block: step_04_activity_ZnPcN4.csv ===
python3 /solution/generate_reference.py step_04

# === solve finalize ===
echo "All reference artifacts written."
