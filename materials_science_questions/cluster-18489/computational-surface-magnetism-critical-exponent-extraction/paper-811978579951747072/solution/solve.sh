#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
export OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"
python3 -m pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple numpy scipy

# === solve block: fig1_csA_vs_cA.csv ===
python3 /solution/generate_ref.py fig1

# === solve block: fig2_csA_vs_mu.csv ===
python3 /solution/generate_ref.py fig2

# === solve block: fig3_mu_vs_T.csv ===
python3 /solution/generate_ref.py fig3
