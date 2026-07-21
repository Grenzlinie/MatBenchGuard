#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: step_01_transmission.csv ===
python3 /solution/compute.py --csv "$OUTDIR/step_01_transmission.csv" > /dev/null

# === solve block: step_02_thermal_conductance.txt ===
python3 /solution/compute.py --txt "$OUTDIR/step_02_thermal_conductance.txt" > /dev/null
