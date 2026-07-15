#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs
python3 /solution/generate.py

# === solve block: step_01_pure_co2_isotherms.csv ===
true

# === solve block: step_02_pure_co2_qst.csv ===
true

# === solve block: step_03_mixture_isotherms.csv ===
true

# === solve block: step_04_md_diffusion.csv ===
true
