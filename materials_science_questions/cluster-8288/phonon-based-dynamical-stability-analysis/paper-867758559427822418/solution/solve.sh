#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: HTT_phonon_X.json ===
python3 /solution/generate_json.py HTT_phonon_X

# === solve block: LTLO_phonon_X.json ===
python3 /solution/generate_json.py LTLO_phonon_X

# === solve block: total_energy_comparison.json ===
python3 /solution/generate_json.py total_energy_comparison

# === solve block: LTLO_DOS_splitting.json ===
python3 /solution/generate_json.py LTLO_DOS_splitting
