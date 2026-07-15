#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: flexible_bc_stress_strain.csv ===
python3 /solution/generate_artifacts.py flex_curve "$OUTDIR/flexible_bc_stress_strain.csv"

# === solve block: static_enthalpy.csv ===
python3 /solution/generate_artifacts.py static_enthalpy "$OUTDIR/static_enthalpy.csv"

# === solve block: peierls_rigid_motion.json ===
python3 /solution/generate_artifacts.py peierls "$OUTDIR/peierls_rigid_motion.json"

# === solve block: dynamic_enthalpy.csv ===
python3 /solution/generate_artifacts.py dynamic_enthalpy "$OUTDIR/dynamic_enthalpy.csv"
