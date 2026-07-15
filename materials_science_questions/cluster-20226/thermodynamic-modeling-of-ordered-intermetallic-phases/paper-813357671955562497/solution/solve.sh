#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: U0_curves.csv ===
python3 /solution/generate_artifacts.py U0_curves.csv

# === solve block: V_curves.csv ===
python3 /solution/generate_artifacts.py V_curves.csv

# === solve block: phase_boundaries.json ===
python3 /solution/generate_artifacts.py phase_boundaries.json
