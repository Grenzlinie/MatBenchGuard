#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"
python3 /solution/generate.py "$OUTDIR"

# === solve block: mulliken_and_positions.csv ===
# already created by preamble

# === solve block: band_gaps.txt ===
# already created by preamble
