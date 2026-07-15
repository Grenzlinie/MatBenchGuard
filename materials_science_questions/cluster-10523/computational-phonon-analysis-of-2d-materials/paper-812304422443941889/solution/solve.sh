#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: dispersion_pattern_a.csv ===
python3 /solution/generate_dispersion.py -p a -o /app/outputs/dispersion_pattern_a.csv

# === solve block: dispersion_pattern_b.csv ===
python3 /solution/generate_dispersion.py -p b -o /app/outputs/dispersion_pattern_b.csv
