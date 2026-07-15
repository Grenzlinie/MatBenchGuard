#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
export OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: volumetric_loading_unloading.csv ===
python3 /solution/gen_data.py vol "$OUTDIR/volumetric_loading_unloading.csv"

# === solve block: critical_state_data.csv ===
python3 /solution/gen_data.py crit "$OUTDIR/critical_state_data.csv"
