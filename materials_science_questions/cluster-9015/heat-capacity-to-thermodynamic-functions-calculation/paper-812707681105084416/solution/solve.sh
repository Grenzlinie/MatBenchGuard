#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: phase_stability.tsv ===
python3 /solution/generate_phase_stability.py > "$OUTDIR/phase_stability.tsv"

# === solve block: gas_composition.tsv ===
python3 /solution/generate_gas_composition.py > "$OUTDIR/gas_composition.tsv"
