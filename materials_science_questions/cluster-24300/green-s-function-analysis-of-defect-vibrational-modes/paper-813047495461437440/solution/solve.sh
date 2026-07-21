#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: curved_line_energies.csv ===
python3 /solution/generate.py curved_line_energies.csv

# === solve block: pair_interaction_energies.csv ===
python3 /solution/generate.py pair_interaction_energies.csv

# === solve finalize ===
echo "All artifacts written."
