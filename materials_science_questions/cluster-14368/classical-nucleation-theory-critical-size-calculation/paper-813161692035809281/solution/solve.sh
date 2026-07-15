#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
python3 -m pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple numpy
mkdir -p /tmp/oracle_outputs
python3 /solution/generate_all.py

# === solve block: precipitate_fraction.csv ===
cp /tmp/oracle_outputs/precipitate_fraction.csv /app/outputs/precipitate_fraction.csv

# === solve block: sauter_spread.csv ===
cp /tmp/oracle_outputs/sauter_spread.csv /app/outputs/sauter_spread.csv

# === solve block: csd_snapshots.csv ===
cp /tmp/oracle_outputs/csd_snapshots.csv /app/outputs/csd_snapshots.csv
