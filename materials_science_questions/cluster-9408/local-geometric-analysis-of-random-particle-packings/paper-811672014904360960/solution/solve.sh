#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: shape_factor_cells.json ===
python3 /solution/generate_artifacts.py shape_factor_cells.json

# === solve block: memory_effect.csv ===
python3 /solution/generate_artifacts.py memory_effect.csv
