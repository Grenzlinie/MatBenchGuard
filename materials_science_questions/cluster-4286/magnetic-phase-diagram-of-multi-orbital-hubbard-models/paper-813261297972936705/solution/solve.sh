#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: step_01_scan_results.csv ===
python3 /solution/generate_outputs.py

# === solve block: step_02_phase_analysis.json ===
python3 /solution/generate_outputs.py
