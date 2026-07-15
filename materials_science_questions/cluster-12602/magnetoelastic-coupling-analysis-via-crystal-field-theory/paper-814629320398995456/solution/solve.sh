#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
set -euo pipefail
python3 -m pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple numpy
python3 /solution/compute.py /tmp/outputs

# === solve block: schottky_tmsb.csv ===
cp /tmp/outputs/schottky_tmsb.csv "$OUTDIR"/schottky_tmsb.csv

# === solve block: susceptibility_prsb.csv ===
cp /tmp/outputs/susceptibility_prsb.csv "$OUTDIR"/susceptibility_prsb.csv

# === solve block: elastic_tmsb.csv ===
cp /tmp/outputs/elastic_tmsb.csv "$OUTDIR"/elastic_tmsb.csv
