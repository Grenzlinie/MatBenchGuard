#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: qtaim_bcps.json ===
python3 /solution/gen_outputs.py --qtaim > /app/outputs/qtaim_bcps.json

# === solve block: hirshfeld_results.json ===
python3 /solution/gen_outputs.py --hirshfeld > /app/outputs/hirshfeld_results.json
