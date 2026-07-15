#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p "$OUTDIR"

# === solve block: formation_energies.csv ===
python3 -c "import csv; f=open('${OUTDIR}/formation_energies.csv','w',newline=''); w=csv.writer(f); w.writerow(['phase','doping','delta_HF']); w.writerows([['B-gamma','pristine',-4.7134],['Y','pristine',-4.7229],['B-gamma','Sb',-4.6867],['Y','Sb',-4.6682],['B-gamma','Bi',-4.6960],['Y','Bi',-4.6840]]); f.close()"
