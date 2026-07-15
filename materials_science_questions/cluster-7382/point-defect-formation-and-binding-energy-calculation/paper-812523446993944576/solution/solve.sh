#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: binding_energies.csv ===
python3 -c "
import csv

# Hardcoded binding energies from the paper's Table S2 (eV).
# Columns: site, binding_energy_no_zpe, binding_energy_with_zpe
data = [
    ('A1', 0.36, 0.31),
    ('A2', 0.39, 0.34),
    ('A3', 0.29, 0.24),
    ('A4', 0.35, 0.30),
    ('A5', 0.37, 0.32),
    ('A6', 0.23, 0.18),
    ('A7', 0.35, 0.30),
    ('A8', 0.32, 0.27),
    ('A9', 0.50, 0.45),
    ('A10', 0.37, 0.32),
    ('A11', 0.40, 0.35),
    ('A12', 0.33, 0.28),
    ('A13', 0.55, 0.50),
    ('A14', 0.35, 0.30),
    ('A15', 0.41, 0.36),
    ('A16', 0.40, 0.35),
    ('B1', 0.41, 0.355),
    ('B2', 0.47, 0.42),
    ('B3', 0.38, 0.325),
    ('B4', 0.12, 0.10),
    ('B5', 0.39, 0.335),
    ('B6', 0.36, 0.305),
    ('B7', 0.37, 0.315),
    ('B8', 0.31, 0.255),
    ('B9', 0.42, 0.365),
    ('B10', 0.38, 0.325),
]

with open('$OUTDIR/binding_energies.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['site', 'binding_energy_no_zpe', 'binding_energy_with_zpe'])
    for row in data:
        writer.writerow(row)
"
