#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs
# No packages to install; the helper uses only stdlib.

# === solve block: phase_boundary_data.csv ===
python3 /solution/generate.py phase_boundary
