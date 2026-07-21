#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs
python3 /solution/generate_outputs.py

# === solve block: step_properties.csv ===
# step_properties.csv already created by /solution/generate_outputs.py
