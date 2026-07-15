#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs
python3 /solution/generate.py

# === solve block: sr_data.csv ===
# This block is intentionally empty – the preamble already writes sr_data.csv.

# === solve block: alpha_c_data.csv ===
# This block is intentionally empty – the preamble already writes alpha_c_data.csv.

# === solve block: lower_limit_data.csv ===
# This block is intentionally empty – the preamble already writes lower_limit_data.csv.
