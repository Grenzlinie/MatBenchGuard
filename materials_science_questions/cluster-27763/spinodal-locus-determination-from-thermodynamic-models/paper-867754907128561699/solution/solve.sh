#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: equilibrium_densities.csv ===
python3 /solution/helper.py equilibrium_densities.csv

# === solve block: laplace_verification.csv ===
python3 /solution/helper.py laplace_verification.csv

# === solve block: domain_growth.csv ===
python3 /solution/helper.py domain_growth.csv

# === solve block: growth_exponent.txt ===
python3 /solution/helper.py growth_exponent.txt
