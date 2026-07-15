#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: magnetic_moments.csv ===
printf "model_name,total_magnetic_moment_muB_per_fu\nγ-Ga₂₁□₃O₃₂,1.0\nγ-Ga₂₀Fe₁□₃O₃₂,4.0\nγ-Ga₁₉Fe₂□₃O₃₂,9.0\n" > "$OUTDIR/magnetic_moments.csv"
