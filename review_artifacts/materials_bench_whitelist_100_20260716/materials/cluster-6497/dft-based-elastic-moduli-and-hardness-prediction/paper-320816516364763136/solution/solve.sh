#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: e_v_data.csv ===
python3 /solution/write_ev_csv.py > "/app/outputs/e_v_data.csv"
