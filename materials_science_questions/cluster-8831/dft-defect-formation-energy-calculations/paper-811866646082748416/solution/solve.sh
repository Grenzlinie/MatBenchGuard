#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
export OUTDIR=/app/outputs
mkdir -p $OUTDIR
python3 -m pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple numpy

# === solve block: table2_formation_energies.csv ===
python3 /solution/helper.py table2_formation_energies.csv

# === solve block: table3_binding_energies.csv ===
python3 /solution/helper.py table3_binding_energies.csv
