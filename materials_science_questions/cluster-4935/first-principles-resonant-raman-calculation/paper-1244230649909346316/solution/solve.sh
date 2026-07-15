#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
export OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"
python3 -m pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple numpy

# === solve block: dsf_gap_vs_J3.csv ===
python3 /solution/generate.py dsf_M_curves.npz && python3 /solution/generate.py dsf_gap_vs_J3.csv

# === solve block: raman_intensity.csv ===
python3 /solution/generate.py raman_intensity.csv
