#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: rdf_data.csv ===
python3 /solution/generate_rdf.py

# === solve block: yielding_strain.csv ===
python3 /solution/generate_yielding.py
