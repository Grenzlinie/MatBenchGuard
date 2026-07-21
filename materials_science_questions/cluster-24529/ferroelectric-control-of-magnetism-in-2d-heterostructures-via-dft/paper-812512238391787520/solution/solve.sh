#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: charge_density.txt ===
echo '3.0' > "$OUTDIR/charge_density.txt"

# === solve block: surface_potential.txt ===
echo '0.2' > "$OUTDIR/surface_potential.txt"
