#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: band_proj_casi2_alb2.json ===
python3 /solution/generate_proj.py casi2_alb2 /app/outputs/band_proj_casi2_alb2.json

# === solve block: band_proj_casi2_ths2.json ===
python3 /solution/generate_proj.py casi2_ths2 /app/outputs/band_proj_casi2_ths2.json

# === solve block: band_proj_si_alb2.json ===
python3 /solution/generate_proj.py si_alb2 /app/outputs/band_proj_si_alb2.json

# === solve block: band_proj_si_ths2.json ===
python3 /solution/generate_proj.py si_ths2 /app/outputs/band_proj_si_ths2.json
