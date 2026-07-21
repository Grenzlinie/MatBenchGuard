#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: water_qst.csv ===
python3 /solution/gen_qst.py --out /app/outputs/water_qst.csv --H_start 2.0 --H_end 10.0 --step 0.1 --H0 3.0 --max_q 0.35 --width 0.7

# === solve block: ammonia_qst.csv ===
python3 /solution/gen_qst.py --out /app/outputs/ammonia_qst.csv --H_start 2.0 --H_end 10.0 --step 0.1 --H0 3.5 --max_q 0.27 --width 0.8

# === solve block: methanol_qst.csv ===
python3 /solution/gen_qst.py --out /app/outputs/methanol_qst.csv --H_start 2.0 --H_end 10.0 --step 0.1 --H0 3.8 --max_q 0.44 --width 1.0

# === solve block: ethanol_qst.csv ===
python3 /solution/gen_qst.py --out /app/outputs/ethanol_qst.csv --H_start 2.0 --H_end 10.0 --step 0.1 --H0 3.8 --max_q 0.62 --width 1.2
