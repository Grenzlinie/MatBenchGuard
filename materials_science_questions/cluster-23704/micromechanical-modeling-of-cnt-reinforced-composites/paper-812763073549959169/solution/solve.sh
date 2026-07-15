#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
export OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: frequencies.csv ===
python3 /solution/write_frequencies.py > "$OUTDIR/frequencies.csv"

# === solve finalize ===
echo "All outputs written."
