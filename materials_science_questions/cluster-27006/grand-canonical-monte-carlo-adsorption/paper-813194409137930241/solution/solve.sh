#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: zero_coverage_qst.txt ===
echo '48.0' > /app/outputs/zero_coverage_qst.txt

# === solve block: uptake_at_1atm.txt ===
echo '95' > /app/outputs/uptake_at_1atm.txt
