#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: lattice_constants.csv ===
python3 /solution/make_lattice.py

# === solve block: frozen_phonon_results.csv ===
python3 /solution/make_frozen.py
