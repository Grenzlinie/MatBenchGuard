#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: efficiency_at_450nm.csv ===
python3 /solution/generate.py efficiency "$OUTDIR/efficiency_at_450nm.csv"

# === solve block: wavelength_sweep.csv ===
python3 /solution/generate.py wavelength "$OUTDIR/wavelength_sweep.csv"

# === solve block: angle_sweep.csv ===
python3 /solution/generate.py angle "$OUTDIR/angle_sweep.csv"

# === solve block: tolerance_thickness.csv ===
python3 /solution/generate.py thickness "$OUTDIR/tolerance_thickness.csv"

# === solve block: tolerance_period_angle.csv ===
python3 /solution/generate.py period "$OUTDIR/tolerance_period_angle.csv"

# === solve block: tolerance_duty.csv ===
python3 /solution/generate.py duty "$OUTDIR/tolerance_duty.csv"
