#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: pdos_co3d.csv ===
python3 /solution/generate_pdos.py co3d

# === solve block: pdos_pd4d.csv ===
python3 /solution/generate_pdos.py pd4d
