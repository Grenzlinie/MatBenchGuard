#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: analytical_restoring_force.json ===
python3 /solution/generate.py analytical

# === solve block: static_friction_vs_pressure.csv ===
python3 /solution/generate.py static

# === solve block: kinetic_friction_vs_pressure.csv ===
python3 /solution/generate.py kinetic
