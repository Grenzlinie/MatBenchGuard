#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs
python3 /solution/generate_outputs.py

# === solve block: single_crystal_elastic_constants.json ===
# written by preamble script /solution/generate_outputs.py

# === solve block: derived_properties.json ===
# written by preamble script /solution/generate_outputs.py
