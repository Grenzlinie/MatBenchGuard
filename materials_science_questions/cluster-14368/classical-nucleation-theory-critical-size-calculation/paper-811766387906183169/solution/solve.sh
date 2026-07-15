#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs
python3 -m pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple numpy
# run the oracle solver that produces all outputs
python3 /solution/oracle_solve.py

# === solve block: critical_properties.csv ===
# This file is already created by oracle_solve.py; no further action.
[ -f /app/outputs/critical_properties.csv ]

# === solve block: error_analysis.json ===
# This file is already created by oracle_solve.py; no further action.
[ -f /app/outputs/error_analysis.json ]
