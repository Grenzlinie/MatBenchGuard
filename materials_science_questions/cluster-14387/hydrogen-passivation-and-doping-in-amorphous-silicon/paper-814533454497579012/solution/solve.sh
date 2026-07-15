#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"
python3 /solution/compute_outputs.py

# === solve block: step_01_probability_amplitudes.json ===
# written by compute_outputs.py

# === solve block: step_02_entanglement_entropy.json ===
# written by compute_outputs.py

# === solve block: step_03_U_over_t.json ===
# written by compute_outputs.py

# === solve block: step_04_full_curves.json ===
# written by compute_outputs.py
