#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: formation_free_energies.csv ===
python3 << 'PYEOF'
import csv, os
outdir = os.environ.get('OUTDIR', '/app/outputs')
path = os.path.join(outdir, 'formation_free_energies.csv')
rows = [
    ['compound','temperature_K','formation_free_energy_eV_per_atom'],
    ['Zr2N',0,-0.95],
    ['Zr2N',1000,-0.86],
    ['ZrN',0,-1.82],
    ['ZrN',1000,-1.70],
    ['Zr3N2',0,-1.36],
    ['Zr3N2',1000,-1.28],
    ['Zr4N5',0,-2.05],
    ['Zr4N5',1000,-1.90],
]
with open(path, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(rows)
PYEOF

# === solve block: elastic_moduli.csv ===
python3 << 'PYEOF'
import csv, os
outdir = os.environ.get('OUTDIR', '/app/outputs')
path = os.path.join(outdir, 'elastic_moduli.csv')
rows = [
    ['compound','bulk_modulus_GPa','shear_modulus_GPa'],
    ['Zr2N',187,109],
    ['Zr3N2',190,100],
    ['Zr4N5',215,120],
    ['ZrN',267,147],
]
with open(path, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(rows)
PYEOF
