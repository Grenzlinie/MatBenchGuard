#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR="${OUTDIR:-/app/outputs}"
mkdir -p "$OUTDIR"

# === solve block: formation_energies.csv ===
printf 'system,shape,formation_energy\n' > "$OUTDIR/formation_energies.csv"
printf 'Pt4/Cu,4S,1.09\n' >> "$OUTDIR/formation_energies.csv"
printf 'Pt4/Cu,4N,0.90\n' >> "$OUTDIR/formation_energies.csv"
printf 'Pt4/Cu,4T,0.95\n' >> "$OUTDIR/formation_energies.csv"
printf 'Pt4/Cu,4L,0.94\n' >> "$OUTDIR/formation_energies.csv"
printf 'Pt4/Cu,4l,1.28\n' >> "$OUTDIR/formation_energies.csv"
printf 'Au4/Ag,4S,0.63\n' >> "$OUTDIR/formation_energies.csv"
printf 'Au4/Ag,4N,0.62\n' >> "$OUTDIR/formation_energies.csv"
printf 'Au4/Ag,4T,0.64\n' >> "$OUTDIR/formation_energies.csv"
printf 'Au4/Ag,4L,0.59\n' >> "$OUTDIR/formation_energies.csv"
printf 'Au4/Ag,4l,0.86\n' >> "$OUTDIR/formation_energies.csv"
