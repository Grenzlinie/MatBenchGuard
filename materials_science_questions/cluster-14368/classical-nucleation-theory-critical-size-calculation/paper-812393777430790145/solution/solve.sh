#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: unit_rate_threshold.csv ===
python3 /solution/generate_outputs.py unit

# === solve block: critical_composition.csv ===
python3 /solution/generate_outputs.py comp
