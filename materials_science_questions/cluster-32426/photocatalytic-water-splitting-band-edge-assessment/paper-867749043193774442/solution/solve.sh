#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
# Oracle solve script – writes reference standard answers
mkdir -p /app/outputs

# === solve block: bandgap_vs_strain.csv ===
python3 /solution/generate.py bandgap

# === solve block: band_edges_vs_strain.csv ===
python3 /solution/generate.py band_edges
