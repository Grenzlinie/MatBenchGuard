#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: delta_T_vs_temperature.csv ===
python3 /solution/compute_elastocaloric.py "$OUTDIR/delta_T_vs_temperature.csv"
