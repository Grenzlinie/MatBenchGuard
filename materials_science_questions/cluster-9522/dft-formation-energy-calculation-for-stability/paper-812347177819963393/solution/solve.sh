#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs
python3 /solution/generate.py

# === solve block: eos_parameters.json ===
:

# === solve block: volume_difference_vs_pressure.csv ===
:

# === solve block: dG_vs_pressure_static.csv ===
:

# === solve block: dG_vs_pressure_entropy.csv ===
:
