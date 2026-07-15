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

python3 /solution/generate.py

# === solve block: step_01_effective_exponents.tsv ===
# This block is handled by the Python script; ensure the script writes this file

# === solve block: step_02_scaled_eos.tsv ===
# This block is handled by the Python script; ensure the script writes this file
