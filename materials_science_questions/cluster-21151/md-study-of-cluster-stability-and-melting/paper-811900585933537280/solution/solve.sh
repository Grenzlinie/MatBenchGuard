#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: Ni_ground_state_energy.csv ===
python3 /solution/generate_data.py

# === solve block: Ni_delta2_temperature.csv ===
python3 /solution/generate_data.py
