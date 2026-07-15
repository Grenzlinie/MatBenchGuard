#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
export OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: beam_radii.csv ===
python3 /solution/write_outputs.py beam_radii

# === solve block: flux_profile_350km.csv ===
python3 /solution/write_outputs.py flux_profile
