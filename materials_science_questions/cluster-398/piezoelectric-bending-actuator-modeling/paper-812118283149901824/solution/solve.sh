#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs
python3 -m pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple numpy scipy
python3 /solution/compute_stresses.py

# === solve block: peak_stresses.csv ===
# This block is intentionally empty; the Python script writes the output.
# The preamble above runs /solution/compute_stresses.py which creates /app/outputs/peak_stresses.csv.
