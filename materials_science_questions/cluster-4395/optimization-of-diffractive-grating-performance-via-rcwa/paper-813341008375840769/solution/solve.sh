#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs && python3 /solution/generate_outputs.py

# === solve block: step_01_efficiency_table.csv ===
:

# === solve block: step_02_polarization_dependence.csv ===
:

# === solve block: step_03_angular_error_phi.csv ===
:

# === solve block: step_04_angular_error_dpsi.csv ===
:

# === solve block: step_05_wavelength_dependence.csv ===
:

# === solve block: step_06_tilt_dependence_sample.csv ===
:
