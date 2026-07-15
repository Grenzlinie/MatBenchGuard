#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: properties.json ===
python3 /solution/write_outputs.py properties

# === solve block: all_structures.xyz ===
python3 /solution/write_outputs.py xyz
