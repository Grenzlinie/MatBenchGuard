#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs
python3 -m pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple numpy

# === solve block: phonon_dispersion.csv ===
sed -i 's/np\.trapz/np\.trapezoid/g' /solution/compute_phonons.py && python3 /solution/compute_phonons.py && mv phonon_dispersion.csv "$OUTDIR/phonon_dispersion.csv"
