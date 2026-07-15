#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: monomer_pbe_spectrum.json ===
python3 /solution/generate.py --type monomer_pbe --output /app/outputs/monomer_pbe_spectrum.json

# === solve block: monomer_b3lyp_spectrum.json ===
python3 /solution/generate.py --type monomer_b3lyp --output /app/outputs/monomer_b3lyp_spectrum.json

# === solve block: dimer_pbe_spectrum.json ===
python3 /solution/generate.py --type dimer_pbe --output /app/outputs/dimer_pbe_spectrum.json

# === solve block: results_summary.json ===
python3 /solution/generate.py --type summary --output /app/outputs/results_summary.json
