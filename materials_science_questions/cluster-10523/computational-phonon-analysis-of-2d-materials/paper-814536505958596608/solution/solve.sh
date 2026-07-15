#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail

# === solve block: model_results.json ===
mkdir -p /app/outputs
python3 /solution/compute.py > /app/outputs/model_results.json
