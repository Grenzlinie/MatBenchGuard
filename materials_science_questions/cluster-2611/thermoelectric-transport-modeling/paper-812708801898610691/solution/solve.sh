#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: m_star_over_m.csv ===
python3 -c "
import csv
data = [
    ('PGa-4', 1.5, 0.23),
    ('PGa-4', 2.0, 0.29),
    ('PGa-4', 2.5, 0.35),
    ('PGa-4', 3.0, 0.40),
    ('PGa-4', 4.0, 0.47),
    ('PGa-5', 1.5, 0.225),
    ('PGa-5', 2.0, 0.31),
    ('PGa-5', 2.5, 0.36),
    ('PGa-5', 3.0, 0.38),
    ('PGa-5', 4.0, 0.40),
    ('AsGa-4', 1.5, 0.21),
    ('AsGa-4', 2.0, 0.265),
    ('AsGa-4', 2.5, 0.315),
    ('AsGa-4', 3.0, 0.365),
    ('AsGa-4', 4.0, 0.47),
    ('AsGa-5', 1.5, 0.22),
    ('AsGa-5', 2.0, 0.30),
    ('AsGa-5', 2.5, 0.365),
    ('AsGa-5', 3.0, 0.43),
    ('AsGa-5', 4.0, 0.52),
    ('SbIn-4\'', 1.5, 0.28),
    ('SbIn-4\'', 2.0, 0.345),
    ('SbIn-4\'', 2.5, 0.40),
    ('SbIn-4\'', 3.0, 0.42),
    ('SbGa-4\'', 1.5, 0.285),
    ('SbGa-4\'', 2.0, 0.35),
    ('SbGa-4\'', 2.5, 0.43),
    ('SbGa-4\'', 3.0, 0.48),
    ('SbGa-4\'', 4.0, 0.51),
]
with open('/app/outputs/m_star_over_m.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['sample', 'temperature_K', 'm_star_over_m'])
    for row in data:
        writer.writerow(row)
"
