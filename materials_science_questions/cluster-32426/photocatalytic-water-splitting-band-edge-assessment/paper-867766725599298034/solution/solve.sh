#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: figure_of_merit.csv ===
python3 /solution/write_outputs.py --fom

# === solve block: water_splitting_counts.csv ===
python3 /solution/write_outputs.py --ws
