#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: energy_spectrum.csv ===
python3 /solution/generate_outputs.py energy > "$OUTDIR/energy_spectrum.csv"

# === solve block: spatial_distribution.csv ===
python3 /solution/generate_outputs.py spatial > "$OUTDIR/spatial_distribution.csv"

# === solve block: time_profile.csv ===
python3 /solution/generate_outputs.py time > "$OUTDIR/time_profile.csv"

# === solve finalize ===
# All outputs written.
