#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: density_profiles.csv ===
python3 /solution/generate.py profile > /app/outputs/density_profiles.csv

# === solve block: shell_analysis.txt ===
python3 /solution/generate.py shell > /app/outputs/shell_analysis.txt
