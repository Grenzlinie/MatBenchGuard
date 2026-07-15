#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: reflectance_spectrum.csv ===
python3 /solution/write_reflectance.py

# === solve block: field_intensity_550nm.csv ===
python3 /solution/write_field_intensity.py
