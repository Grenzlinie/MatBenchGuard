#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p $OUTDIR

# === solve block: static_transition_pressure.txt ===
python3 /solution/generate.py --output static_transition_pressure.txt --dir $OUTDIR

# === solve block: nonideal_mixing_energies.csv ===
python3 /solution/generate.py --output nonideal_mixing_energies.csv --dir $OUTDIR

# === solve block: phase_diagram.csv ===
python3 /solution/generate.py --output phase_diagram.csv --dir $OUTDIR
