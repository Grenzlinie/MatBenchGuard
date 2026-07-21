#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: resolved_shear_stresses.csv ===
python3 << 'EOF'
import csv, os

outdir = os.environ.get('OUTDIR', '/app/outputs')

data = [
    (1, 1.6e-6, 1.94e4, 0.498),
    (2, 2.0e-6, 1.48e4, 0.474),
    (3, 2.0e-6, 1.83e4, 0.498),
    (4, 2.0e-6, 1.44e4, 0.476),
    (6, 5.0e-6, 1.22e4, 0.463),
]

with open(os.path.join(outdir, 'resolved_shear_stresses.csv'), 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['specimen', 'resolved_shear_stress_kg_per_mm2'])
    for specimen, strain, modulus, factor in data:
        stress = (strain * modulus) / factor
        writer.writerow([specimen, stress])
EOF
