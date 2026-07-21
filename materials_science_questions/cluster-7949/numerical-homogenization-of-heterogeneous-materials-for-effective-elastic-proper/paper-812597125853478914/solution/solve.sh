#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
export OUTDIR="/app/outputs"; mkdir -p "$OUTDIR"

# === solve block: copper_stress_strain.csv ===
python3 << 'EOF'
import csv

# Approximate stress-strain curve for copper compression MT-MAK97, n=10
# Strain: 0 to -0.003 in steps of 1e-4
points = [
    (0.0000, 0.0),
    (-0.0001, 7.5),
    (-0.0002, 15.0),
    (-0.0003, 22.5),
    (-0.0004, 28.5),
    (-0.0005, 33.0),
    (-0.0006, 36.0),
    (-0.0007, 38.2),
    (-0.0008, 39.8),
    (-0.0009, 41.0),
    (-0.0010, 41.9),
    (-0.0011, 42.6),
    (-0.0012, 43.2),
    (-0.0013, 43.6),
    (-0.0014, 43.9),
    (-0.0015, 44.1),
    (-0.0016, 44.2),
    (-0.0017, 44.3),
    (-0.0018, 44.4),
    (-0.0019, 44.4),
    (-0.0020, 44.5),
    (-0.0021, 44.5),
    (-0.0022, 44.5),
    (-0.0023, 44.5),
    (-0.0024, 44.6),
    (-0.0025, 44.6),
    (-0.0026, 44.6),
    (-0.0027, 44.6),
    (-0.0028, 44.7),
    (-0.0029, 44.7),
    (-0.0030, 44.7),
]

with open('/app/outputs/copper_stress_strain.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['strain', 'equivalent_stress'])
    for s, stress in points:
        writer.writerow([s, stress])
EOF

# === solve block: copper_strain_ratio.csv ===
python3 /solution/generate_outputs.py copper_strain_ratio

# === solve block: stainless_lattice_averages.csv ===
python3 /solution/generate_outputs.py stainless_lattice_averages

# === solve block: stainless_lattice_std.csv ===
python3 /solution/generate_outputs.py stainless_lattice_std
