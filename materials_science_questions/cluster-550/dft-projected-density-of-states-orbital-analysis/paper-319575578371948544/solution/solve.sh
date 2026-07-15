#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs
python3 /solution/generate_all.py

# === solve block: total_dos.dat ===
export OUTDIR=/app/outputs
python3 -c "
from collections import defaultdict
import os

pfile = os.path.join(os.environ['OUTDIR'], 'projected_dos.dat')
tfile = os.path.join(os.environ['OUTDIR'], 'total_dos.dat')

target_atoms = {1, 12, 14, 15, 16, 17, 18, 19}

pdos_sum = defaultdict(float)
energies = set()

with open(pfile) as f:
    for line in f:
        line = line.strip()
        if not line or line.startswith('#'):
            continue
        parts = line.split()
        if len(parts) != 3:
            continue
        e = float(parts[0])
        atom_idx = int(parts[1])
        pdos = float(parts[2])
        energies.add(e)
        if atom_idx in target_atoms:
            pdos_sum[e] += pdos

energies = sorted(energies)
with open(tfile, 'w') as f:
    for e in energies:
        total = pdos_sum.get(e, 0.0) / 0.70
        f.write(f'{e:.6f} {total:.12f}\n')
"

# === solve block: projected_dos.dat ===
# written by preamble

# === solve block: band_structure.dat ===
# written by preamble

# === solve block: fermi_surface_sheets.txt ===
# written by preamble
