#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: predictions.csv ===
python3 /solution/generate.py

# === solve block: metrics.json ===
python3 /solution/generate.py
