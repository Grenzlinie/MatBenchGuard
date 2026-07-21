#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: surface_magnetization_data.csv ===
python3 /solution/compute_ms.py csv

# === solve block: critical_exponents.json ===
python3 /solution/compute_ms.py json
