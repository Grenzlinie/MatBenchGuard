#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: reversal_times.csv ===
python3 /solution/generate_reversal.py

# === solve block: avrami_decay.csv ===
python3 /solution/generate_avrami.py
