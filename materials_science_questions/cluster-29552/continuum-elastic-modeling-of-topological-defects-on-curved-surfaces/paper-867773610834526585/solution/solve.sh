#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: phase_diagram.csv ===
python3 /solution/gen_out.py phase_diagram "$OUTDIR/phase_diagram.csv"

# === solve block: defect_energies.csv ===
python3 /solution/gen_out.py defect_energies "$OUTDIR/defect_energies.csv"
