#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: step_01_mori_chain_params.json ===
python3 /solution/write_artifact.py /app/outputs mori

# === solve block: step_02_correlation_laplace.json ===
python3 /solution/write_artifact.py /app/outputs laplace
