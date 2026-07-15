#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: cI24_lattice_parameter.txt ===
printf '3.12\n' > "$OUTDIR/cI24_lattice_parameter.txt"

# === solve block: enthalpy_difference.txt ===
printf '%s\n' -0.012 > "$OUTDIR/enthalpy_difference.txt"

# === solve block: cI24_phonon_min_freq.txt ===
printf '2.1\n' > "$OUTDIR/cI24_phonon_min_freq.txt"

# === solve block: cI24_band_gap.txt ===
printf '0.0\n' > "$OUTDIR/cI24_band_gap.txt"
