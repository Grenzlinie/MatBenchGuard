#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"
python3 /solution/generate_outputs.py

# === solve block: surface_energies.csv ===
true

# === solve block: work_of_adhesion.csv ===
true

# === solve block: interfacial_energies.csv ===
true
