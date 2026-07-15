#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs
chmod +x /solution/compute_diffusion.py

# === solve block: diffusion_constants.csv ===
python3 /solution/compute_diffusion.py csv

# === solve block: arrhenius_params.json ===
python3 /solution/compute_diffusion.py json
