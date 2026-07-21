#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
export OUTDIR=/app/outputs
mkdir -p "$OUTDIR"
python3 -m pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple numpy scipy

# === solve block: pe_energies.csv ===
python3 /solution/compute.py --output pe_energies.csv

# === solve block: cpe_energies.csv ===
python3 /solution/compute.py --output cpe_energies.csv

# === solve block: slab_energies.csv ===
python3 /solution/compute.py --output slab_energies.csv
