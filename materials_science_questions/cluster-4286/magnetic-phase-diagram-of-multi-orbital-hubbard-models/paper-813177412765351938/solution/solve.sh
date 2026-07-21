#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
# No packages to install; the helper script uses Python stdlib (csv, math) only.

# === solve block: normal_spectral_function.csv ===
python3 /solution/generate_data.py --mode spectral --out "${OUTDIR}/normal_spectral_function.csv"

# === solve block: quasiparticle_bands.csv ===
python3 /solution/generate_data.py --mode bands --out "${OUTDIR}/quasiparticle_bands.csv"

# === solve block: gap_vs_temperature.csv ===
python3 /solution/generate_data.py --mode gap --out "${OUTDIR}/gap_vs_temperature.csv"
