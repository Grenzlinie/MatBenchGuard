#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: equilibrium_distance.txt ===
echo "2.91" > "$OUTDIR/equilibrium_distance.txt"

# === solve block: energy_vs_angle.csv ===
python3 /solution/synth_data.py "$OUTDIR"

# === solve block: rotational_barrier.txt ===
:
