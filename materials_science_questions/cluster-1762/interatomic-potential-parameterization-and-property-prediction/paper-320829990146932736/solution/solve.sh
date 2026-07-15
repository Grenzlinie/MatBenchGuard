#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: coulomb_results.json ===
python3 /solution/compute.py coulomb /app/outputs/coulomb_results.json

# === solve block: vdw_results.json ===
python3 /solution/compute.py vdw /app/outputs/vdw_results.json

# === solve block: full_results.json ===
python3 /solution/compute.py full /app/outputs/full_results.json
