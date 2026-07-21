#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
pip install numpy scipy -q -i https://pypi.tuna.tsinghua.edu.cn/simple

# === solve block: orientation_energies.csv ===
python3 /solution/compute_energies.py
