#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: phase_diagrams.csv ===
python3 /solution/generate.py csv /app/outputs/phase_diagrams.csv

# === solve block: invariant_reactions.json ===
python3 /solution/generate.py json /app/outputs/invariant_reactions.json
