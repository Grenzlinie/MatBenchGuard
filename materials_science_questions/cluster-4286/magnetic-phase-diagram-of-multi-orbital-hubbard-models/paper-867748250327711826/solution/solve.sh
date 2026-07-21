#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: adw_order_parameter.csv ===
python3 /solution/generate_outputs.py adw

# === solve block: af_order_parameter.csv ===
python3 /solution/generate_outputs.py af

# === solve block: phase_transition_D.txt ===
python3 /solution/generate_outputs.py dc
