#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
export OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"
python3 -m pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple scipy
python3 /solution/compute_site_fractions.py "$OUTDIR"

# === solve block: site_fractions_setA.csv ===
echo 'Site fractions Set A computed.'

# === solve block: site_fractions_setB.csv ===
echo 'Site fractions Set B computed.'
