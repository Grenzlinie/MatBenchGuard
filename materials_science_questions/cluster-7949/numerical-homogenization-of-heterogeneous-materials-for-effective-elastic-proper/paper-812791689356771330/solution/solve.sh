#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: validation_errors.csv ===
python3 /solution/generate.py validation /app/outputs

# === solve block: clustering_results.csv ===
python3 /solution/generate.py clustering /app/outputs
