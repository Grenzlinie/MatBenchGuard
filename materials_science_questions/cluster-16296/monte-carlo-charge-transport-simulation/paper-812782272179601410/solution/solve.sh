#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
python3 -m pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple numpy

# === solve block: transient_current_AlGaAs.csv ===
python3 /solution/generate.py transient_current_AlGaAs.csv

# === solve block: transient_current_InP.csv ===
python3 /solution/generate.py transient_current_InP.csv

# === solve block: peak_velocity_vs_field.csv ===
python3 /solution/generate.py peak_velocity_vs_field.csv

# === solve block: responsivity_vs_frequency.csv ===
python3 /solution/generate.py responsivity_vs_frequency.csv
