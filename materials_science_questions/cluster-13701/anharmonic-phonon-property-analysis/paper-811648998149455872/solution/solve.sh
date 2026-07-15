#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
export OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"
python3 -m pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple numpy  # fallback if numpy needed; stdlib only actually

# === solve block: step_01_cv_ch.csv ===
python3 /solution/anharmonic_analysis.py --output-csv "$OUTDIR/step_01_cv_ch.csv"

# === solve block: step_02_fitted_params.json ===
python3 /solution/anharmonic_analysis.py --output-json "$OUTDIR/step_02_fitted_params.json"
