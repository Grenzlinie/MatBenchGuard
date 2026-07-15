#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: results.json ===
python3 /solution/generate_outputs.py "$OUTDIR/results.json" results

# === solve block: stationary_points.json ===
python3 /solution/generate_outputs.py "$OUTDIR/stationary_points.json" stationary
