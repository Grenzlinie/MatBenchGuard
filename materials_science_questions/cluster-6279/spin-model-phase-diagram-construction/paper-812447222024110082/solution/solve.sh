#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: triple_points.json ===
python3 /solution/generate_outputs.py triple

# === solve block: phase_boundary.csv ===
python3 /solution/generate_outputs.py boundary
