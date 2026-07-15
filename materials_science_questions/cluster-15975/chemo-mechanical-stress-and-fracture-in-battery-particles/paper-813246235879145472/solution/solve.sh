#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: step_01_damage_vs_time.csv ===
python3 /solution/generate_outputs.py damage_csv

# === solve block: step_02_exponents.json ===
python3 /solution/generate_outputs.py exponents_json
