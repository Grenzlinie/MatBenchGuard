#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: geometry_summary.json ===
python3 /solution/write_outputs.py --artifact geometry_summary

# === solve block: ldos_CH3S.csv ===
python3 /solution/write_outputs.py --artifact ldos
