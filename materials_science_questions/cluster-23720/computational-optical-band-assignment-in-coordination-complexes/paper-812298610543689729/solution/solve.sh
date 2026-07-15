#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: ionization_potential.txt ===
echo "14.21" > "$OUTDIR/ionization_potential.txt"

# === solve finalize ===
echo "Oracle solve completed."
