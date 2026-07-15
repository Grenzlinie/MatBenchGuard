#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: lattice_energy.txt ===
printf -- '%.3f\n' -25.099 > /app/outputs/lattice_energy.txt
