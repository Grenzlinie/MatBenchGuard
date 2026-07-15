#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
python3 -m pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple numpy

# === solve block: phonon_frequencies.csv ===
python3 /solution/generate_outputs.py --output phonon_frequencies.csv

# === solve block: elastic_constants.csv ===
python3 /solution/generate_outputs.py --output elastic_constants.csv

# === solve block: zero_point_energy.csv ===
python3 /solution/generate_outputs.py --output zero_point_energy.csv
