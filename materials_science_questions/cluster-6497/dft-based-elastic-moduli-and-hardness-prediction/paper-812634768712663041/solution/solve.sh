#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: stability_results.json ===
python3 /solution/compute.py > "/app/outputs/stability_results.json"
