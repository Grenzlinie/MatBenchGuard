#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
set -euo pipefail
mkdir -p /app/outputs
OUTDIR=/app/outputs

# === solve block: f_value.txt ===
python3 -c "import math; f = 4 * 1e15 * (0.1 * 5e-6)**2 / (3 * math.pi * 5); print(f)" > "$OUTDIR/f_value.txt"
