#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
set -euo pipefail
mkdir -p /app/outputs

# === solve block: phase_diagram_UV.csv ===
python3 /solution/write_phase_diagrams.py uv

# === solve block: phase_diagram_VT_U8.csv ===
python3 /solution/write_phase_diagrams.py vt
