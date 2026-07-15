#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: energies.json ===
python3 /solution/generate.py energies

# === solve block: rate_constants.csv ===
python3 /solution/generate.py rates

# === solve block: falloff_summary.json ===
python3 /solution/generate.py falloff
