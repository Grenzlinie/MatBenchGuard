#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: scan_LaMn2Ge2.csv ===
python3 /solution/generate_scans.py LaMn2Ge2

# === solve block: scan_LaMn2Si2.csv ===
python3 /solution/generate_scans.py LaMn2Si2
