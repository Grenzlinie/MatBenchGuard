#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: olson_cohen_bcc_fraction.csv ===
python3 /solution/gen_csv.py olson_cohen /app/outputs/olson_cohen_bcc_fraction.csv

# === solve block: perfect_perfect_bcc_fraction.csv ===
python3 /solution/gen_csv.py perfect_perfect /app/outputs/perfect_perfect_bcc_fraction.csv

# === solve block: volume_dependence_bcc_fraction.csv ===
python3 /solution/gen_csv.py volume_dependence /app/outputs/volume_dependence_bcc_fraction.csv
