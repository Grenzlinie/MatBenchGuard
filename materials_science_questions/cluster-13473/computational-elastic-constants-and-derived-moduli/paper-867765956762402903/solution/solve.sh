#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs
python3 -m pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple numpy

# === solve block: heat_capacity.csv ===
python3 /solution/generate.py --output heat_capacity.csv

# === solve block: helicity_modulus.csv ===
python3 /solution/generate.py --output helicity_modulus.csv

# === solve block: susceptibility.csv ===
python3 /solution/generate.py --output susceptibility.csv
