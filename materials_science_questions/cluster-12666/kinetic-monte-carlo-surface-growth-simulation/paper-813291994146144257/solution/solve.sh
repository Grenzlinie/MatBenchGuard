#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: island_density_vs_i.json ===
python3 /solution/write_outputs.py

# === solve block: selected_critical_island_size.txt ===
python3 /solution/write_outputs.py
