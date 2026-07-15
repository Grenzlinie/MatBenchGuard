#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: dispersion_100.csv ===
python3 /solution/cardan.py 100 /app/outputs/dispersion_100.csv

# === solve block: dispersion_nonsym.csv ===
python3 /solution/cardan.py nonsym /app/outputs/dispersion_nonsym.csv
