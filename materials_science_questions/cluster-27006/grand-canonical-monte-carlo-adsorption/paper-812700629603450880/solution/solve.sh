#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: ethanol_isotherms.csv ===
python3 /solution/gen_data.py ethanol_isotherms.csv

# === solve block: water_isotherms.csv ===
python3 /solution/gen_data.py water_isotherms.csv

# === solve block: mixture_selectivity.csv ===
python3 /solution/gen_data.py mixture_selectivity.csv
