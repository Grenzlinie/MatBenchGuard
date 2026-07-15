#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
export OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: u_distribution.csv ===
python3 /solution/generate_data.py --output u_distribution.csv --outdir "$OUTDIR"

# === solve block: am_distribution.csv ===
python3 /solution/generate_data.py --output am_distribution.csv --outdir "$OUTDIR"

# === solve block: pu_distribution.csv ===
python3 /solution/generate_data.py --output pu_distribution.csv --outdir "$OUTDIR"

# === solve block: equilibrium_constants.csv ===
python3 /solution/generate_data.py --output equilibrium_constants.csv --outdir "$OUTDIR"
