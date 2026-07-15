#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: E_vs_V_all_T.csv ===
python3 /solution/generate_data.py csv /app/outputs/E_vs_V_all_T.csv

# === solve block: Delta_E_400K.txt ===
python3 /solution/generate_data.py delta /app/outputs/Delta_E_400K.txt
