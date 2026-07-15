#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs
export OUTDIR=/app/outputs

# === solve block: nucleation_rates.json ===
python3 /solution/generate.py "$OUTDIR/nucleation_rates.json" nucleation_rates
