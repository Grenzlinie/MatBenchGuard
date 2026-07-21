#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
python3 -m pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple numpy

# === solve block: tip_displacement.csv ===
python3 /solution/run.py tip_displacement

# === solve block: pull_in_voltage.csv ===
python3 /solution/run.py pull_in_voltage
