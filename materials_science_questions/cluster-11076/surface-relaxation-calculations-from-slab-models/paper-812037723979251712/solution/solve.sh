#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: magnetic_moments.csv ===
python3 /solution/generate_csvs.py --output "/app/outputs/magnetic_moments.csv" --type mag

# === solve block: dos_cr_term_aZB.csv ===
python3 /solution/generate_csvs.py --output "/app/outputs/dos_cr_term_aZB.csv" --type cr_azb

# === solve block: dos_cr_term_aInP.csv ===
python3 /solution/generate_csvs.py --output "/app/outputs/dos_cr_term_aInP.csv" --type cr_ainp

# === solve block: dos_p_term_aZB.csv ===
python3 /solution/generate_csvs.py --output "/app/outputs/dos_p_term_aZB.csv" --type p_azb

# === solve block: dos_p_term_aInP.csv ===
python3 /solution/generate_csvs.py --output "/app/outputs/dos_p_term_aInP.csv" --type p_ainp
