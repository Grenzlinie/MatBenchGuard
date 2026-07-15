#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: temperature_values.csv ===
sed -i '1a import csv' /solution/compute_temperature.py
python3 /solution/compute_temperature.py
