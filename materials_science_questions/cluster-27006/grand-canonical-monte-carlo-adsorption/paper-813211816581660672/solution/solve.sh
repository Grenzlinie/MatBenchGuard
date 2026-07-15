#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: step_04_isotherms.csv ===
python3 /solution/generate_outputs.py isotherms

# === solve block: step_05_isosteric_heats.csv ===
python3 /solution/generate_outputs.py heats

# === solve block: step_07_charge_comparison.csv ===
python3 /solution/generate_outputs.py charge
