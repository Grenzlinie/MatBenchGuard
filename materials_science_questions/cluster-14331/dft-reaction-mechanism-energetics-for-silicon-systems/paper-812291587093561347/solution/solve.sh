#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: dimerization_results.json ===
python3 /solution/generate_dimerization_results.py > /app/outputs/dimerization_results.json

# === solve finalize ===
echo 'Reference dimerization_results.json written.'
