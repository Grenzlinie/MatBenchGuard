#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: dft_results.json ===
python3 /solution/write_results.py dft /app/outputs/dft_results.json

# === solve block: strain_results.json ===
python3 /solution/write_results.py strain /app/outputs/strain_results.json
