#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: dos_4x4.csv ===
python3 /solution/generate_all.py dos_4x4

# === solve block: dos_8x8.csv ===
python3 /solution/generate_all.py dos_8x8

# === solve block: epsilon2_4x4.csv ===
python3 /solution/generate_all.py epsilon2_4x4

# === solve block: epsilon2_8x8.csv ===
python3 /solution/generate_all.py epsilon2_8x8
