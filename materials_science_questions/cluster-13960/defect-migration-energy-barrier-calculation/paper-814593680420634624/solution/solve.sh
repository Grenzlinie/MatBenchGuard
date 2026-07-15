#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs
export OUTDIR=/app/outputs
python3 -m pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple numpy

# === solve block: step_01_formation_energies.csv ===
python3 /solution/generate_outputs.py step_01

# === solve block: step_02_migration_barriers_uniform.csv ===
python3 /solution/generate_outputs.py step_02

# === solve block: step_03_diffusion_coeffs.csv ===
python3 /solution/generate_outputs.py step_03

# === solve block: step_04_barrier_fits.json ===
python3 /solution/generate_outputs.py step_04

# === solve block: step_05_dislocation_barriers.csv ===
python3 /solution/generate_outputs.py step_05

# === solve block: step_06_lambda_radial.csv ===
python3 /solution/generate_outputs.py step_06
