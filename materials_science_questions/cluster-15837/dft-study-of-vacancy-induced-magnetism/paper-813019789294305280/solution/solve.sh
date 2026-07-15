#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
python3 -m pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple numpy

# === solve block: atomic_moments.csv ===
python3 /solution/write_outputs.py atomic_moments.csv

# === solve block: moment_per_fu.txt ===
python3 /solution/write_outputs.py moment_per_fu.txt

# === solve block: dos_data.csv ===
python3 /solution/write_outputs.py dos_data.csv

# === solve block: bandgap.txt ===
python3 -c "
import csv
with open('$OUTDIR/dos_data.csv') as f:
    reader = csv.reader(f)
    next(reader)  # header
    energies, up, down = [], [], []
    for row in reader:
        energies.append(float(row[0]))
        up.append(float(row[1]))
        down.append(float(row[2]))

# highest occupied (E<0, DOS>0) and lowest unoccupied (E>0, DOS>0)
occ_up   = max(e for e,d in zip(energies,up)   if e < 0 and d > 1e-10)
unocc_up = min(e for e,d in zip(energies,up)   if e > 0 and d > 1e-10)
occ_down   = max(e for e,d in zip(energies,down) if e < 0 and d > 1e-10)
unocc_down = min(e for e,d in zip(energies,down) if e > 0 and d > 1e-10)
bandgap = min(unocc_up - occ_up, unocc_down - occ_down)
with open('$OUTDIR/bandgap.txt', 'w') as f:
    f.write(str(bandgap) + '\n')
"
