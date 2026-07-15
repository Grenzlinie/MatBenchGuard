#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail

# Install required packages from the Tsinghua PyPI mirror (fast, no network issues)
python3 -m pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple scipy numpy

mkdir -p /app/outputs

# === solve block: cop_ZnS.csv ===
python3 /solution/compute.py cop ZnS /app/outputs/cop_ZnS.csv

# === solve block: cop_ZnSe.csv ===
python3 /solution/compute.py cop ZnSe /app/outputs/cop_ZnSe.csv

# === solve block: cop_ZnTe.csv ===
python3 /solution/compute.py cop ZnTe /app/outputs/cop_ZnTe.csv

# === solve block: strain_reduction_factors.csv ===
python3 /solution/compute.py strain_reduction /app/outputs/strain_reduction_factors.csv
