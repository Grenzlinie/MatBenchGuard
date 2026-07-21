#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: magnetization_curve.csv ===
python3 /solution/gen_outputs.py
test -s /app/outputs/magnetization_curve.csv

# === solve block: sqrt_coefficient.txt ===
python3 /solution/gen_outputs.py
test -s /app/outputs/sqrt_coefficient.txt
