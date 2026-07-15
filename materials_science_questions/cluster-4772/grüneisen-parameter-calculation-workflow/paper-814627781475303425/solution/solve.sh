#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
set -euo pipefail
mkdir -p /app/outputs

# === solve block: si_thermo.csv ===
python3 /solution/gen_thermo.py si

# === solve block: hsi_thermo.csv ===
python3 /solution/gen_thermo.py hsi

# === solve block: ge_thermo.csv ===
python3 /solution/gen_thermo.py ge

# === solve block: hge_thermo.csv ===
python3 /solution/gen_thermo.py hge

# === solve block: anharmonicity.json ===
python3 /solution/gen_anharm.py
