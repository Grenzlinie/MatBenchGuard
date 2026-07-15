#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
set -euo pipefail
mkdir -p /app/outputs

# === solve block: all_electron_H_O_energies.tsv ===
python3 /solution/generate_curves.py

# === solve block: all_electron_O_O_energies.tsv ===
true

# === solve block: ecp_H_O_energies.tsv ===
true

# === solve block: ecp_O_O_energies.tsv ===
true
