#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs
python3 -m pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple numpy

# === solve block: results_half_filling_JAF0.json ===
python /solution/generate.py half0

# === solve block: results_half_filling_JAF01.json ===
python /solution/generate.py half01

# === solve block: results_quarter_filling_JAF0.json ===
python /solution/generate.py quarter0

# === solve block: results_quarter_filling_JAF01.json ===
python /solution/generate.py quarter01
