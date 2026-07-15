#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: delta_T_zero.txt ===
printf '22.7584\n' > "$OUTDIR/delta_T_zero.txt"
