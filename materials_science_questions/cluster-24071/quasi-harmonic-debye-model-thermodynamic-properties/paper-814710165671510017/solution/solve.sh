#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: thermodynamic_properties.csv ===
python3 /solution/generate_csv.py /app/outputs/thermodynamic_properties.csv
