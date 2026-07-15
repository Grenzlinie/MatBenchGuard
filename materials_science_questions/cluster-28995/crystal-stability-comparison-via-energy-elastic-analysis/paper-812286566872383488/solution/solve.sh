#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs && python3 /solution/generate_outputs.py

# === solve block: separation_limit_s_levels.json ===
# written by preamble

# === solve block: separation_limit_p_levels.json ===
# written by preamble

# === solve block: hybridization_limit_levels.json ===
# written by preamble

# === solve block: total_energies.json ===
# written by preamble
