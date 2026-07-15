#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
export OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: results.csv ===
python3 /solution/compute.py "$OUTDIR" results

# === solve block: critical_stress.txt ===
python3 /solution/compute.py "$OUTDIR" critical
