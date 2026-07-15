#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: gamma_C_data.csv ===
python3 /solution/generate_gamma_c.py

# === solve finalize ===
echo 'All artifacts written.'
