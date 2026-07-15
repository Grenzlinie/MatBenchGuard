#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: table1_results.json ===
python3 /solution/table1.py

# === solve block: spectral_width_report.json ===
python3 /solution/spectral.py
