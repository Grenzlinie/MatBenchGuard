#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: dos_w3.csv ===
python3 /solution/generate.py --output dos_w3.csv

# === solve block: wavefunction_data.csv ===
python3 /solution/generate.py --output wavefunction_data.csv

# === solve block: hyperfine_summary.txt ===
python3 /solution/generate.py --output hyperfine_summary.txt
