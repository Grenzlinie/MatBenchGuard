#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: computed_properties.csv ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs
python3 /solution/compute.py
