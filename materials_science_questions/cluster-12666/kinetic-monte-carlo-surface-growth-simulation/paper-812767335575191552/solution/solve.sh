#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: step_01_island_stats.json ===
python3 -c 'import sys; sys.path.insert(0,"/solution"); from helper import write_island_stats; write_island_stats("/app/outputs/step_01_island_stats.json")'

# === solve block: step_02_bragg_roughness.json ===
python3 -c 'import sys; sys.path.insert(0,"/solution"); from helper import write_bragg_roughness; write_bragg_roughness("/app/outputs/step_02_bragg_roughness.json")'
