#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
export OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"
python3 -m pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple numpy

# === solve block: dgs_curves_standard_equivalent.csv ===
python3 /solution/generate_dgs.py square "$OUTDIR/dgs_curves_standard_equivalent.csv"

# === solve block: dgs_curves_32element.csv ===
python3 /solution/generate_dgs.py 32element "$OUTDIR/dgs_curves_32element.csv"

# === solve block: dgs_curves_16element.csv ===
python3 /solution/generate_dgs.py 16element "$OUTDIR/dgs_curves_16element.csv"
