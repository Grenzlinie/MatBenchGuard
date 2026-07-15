#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: bond_lengths.csv ===
python3 /solution/generate.py bond_lengths /app/outputs/bond_lengths.csv

# === solve block: rse.csv ===
python3 /solution/generate.py rse /app/outputs/rse.csv

# === solve block: pa.csv ===
python3 /solution/generate.py pa /app/outputs/pa.csv

# === solve block: heats_of_formation.csv ===
python3 /solution/generate.py heats_of_formation /app/outputs/heats_of_formation.csv
