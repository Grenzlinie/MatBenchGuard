#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: potential_I_results.json ===
python3 /solution/write_results.py potential_I > /app/outputs/potential_I_results.json

# === solve block: potential_II_results.json ===
python3 /solution/write_results.py potential_II > /app/outputs/potential_II_results.json
