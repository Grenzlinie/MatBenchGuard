#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
export OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: actinide_volumes_bulk_moduli.csv ===
python3 << 'EOF'
import csv, os
outdir = os.environ['OUTDIR']
rows = [
    ["element", "rws_bohr", "bulk_modulus_gpa"],
    ["Th",    3.660,     63.0],
    ["Pa",    3.525,    100.0],
    ["U",     3.388,    155.0],
    ["Np",    3.524,    110.0],
    ["Pu",    3.657,     73.0],
    ["Am",    3.728,     52.0],
    ["Cm",    3.659,     66.0],
    ["Bk",    3.610,     79.0],
]
with open(os.path.join(outdir, 'actinide_volumes_bulk_moduli.csv'), 'w', newline='') as f:
    w = csv.writer(f)
    w.writerows(rows)
EOF

# === solve block: delta_plutonium_dos.csv ===
python3 /solution/write_artifacts.py dos
