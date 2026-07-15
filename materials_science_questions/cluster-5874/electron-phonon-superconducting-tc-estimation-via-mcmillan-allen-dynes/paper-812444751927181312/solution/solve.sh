#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: element_electronegativity.csv ===
python3 << 'EOF'
import csv, os

# Exact IP and EA from Table 1 of the paper, and the paper's reported χ.
# Tc is empty for non-superconducting elements.
rows = [
    ['Cs',   '',       3.90, 0.472, 2.19],
    ['Rb',   '',       4.18, 0.486, 2.33],
    ['K',    '',       4.34, 0.502, 2.42],
    ['Na',   '',       5.14, 0.548, 2.84],
    ['Li',   '',       5.40, 0.618, 3.01],
    ['In',   3.408,    5.79, 0.3,   3.05],
    ['Ga',   1.038,    6.00, 0.3,   3.15],
    ['Tl',   2.38,     6.11, 0.2,   3.16],
    ['Al',   1.75,     5.99, 0.441, 3.22],
    ['Sc',   '',       6.54, 0.188, 3.36],
    ['Hf',   0.128,    6.78, 0,     3.39],
    ['Zr',   0.65,     6.84, 0.426, 3.63],
    ['V',    5.40,     6.74, 0.525, 3.63],
    ['Cr',   '',       6.77, 0.666, 3.72],
    ['W',    0.0154,   6.90, 0.815, 3.86],
    ['Pb',   7.196,    7.42, 0.364, 3.89],
    ['Nb',   9.25,     6.89, 0.893, 3.89],
    ['Tc',   7.8,      7.28, 0.55,  3.91],
    ['Mo',   0.915,    7.10, 0.746, 3.92],
    ['Re',   1.697,    7.89, 0.15,  4.02],
    ['Fe',   '',       7.87, 0.163, 4.02],
    ['Ta',   4.47,     7.89, 0.322, 4.11],
    ['Ti',   0.40,     6.82, 0.079, 4.11],   # paper's χ, computed from IP/EA would be ≈3.45
    ['Bi',   '',       7.29, 0.946, 4.12],
    ['Ru',   0.49,     7.37, 1.05,  4.21],
    ['Co',   '',       7.86, 0.661, 4.26],
    ['Sn',   3.722,    7.35, 1.2,   4.28],
    ['B',    '',       8.30, 0.277, 4.29],
    ['Rh',   '',       7.46, 1.14,  4.30],
    ['Ni',   '',       7.64, 1.16,  4.40],
    ['Ag',   '',       7.58, 1.30,  4.44],
    ['Ge',   '',       7.90, 1.2,   4.46],
    ['Cu',   '',       7.73, 1.23,  4.48],
    ['Si',   '',       8.16, 1.39,  4.77],
    ['Sb',   '',       8.62, 1.07,  4.85],
    ['As',   '',       9.79, 0.81,  5.30],
    ['Ir',   0.1125,   9.12, 1.57,  5.34],
    ['Te',   '',       9.01, 1.97,  5.49],
    ['Pt',   '',       9.02, 2.13,  5.57],
    ['P',    '',       10.5, 0.747, 5.62],
    ['Au',   '',       9.23, 2.31,  5.77],
    ['Se',   '',       9.76, 2.02,  5.89],
    ['C',    '',       11.3, 1.263, 6.36],
    ['H',    '',       13.6, 0.754, 7.18],
    ['N',    '',       14.5, -0.07, 7.23],
    ['O',    '',       13.6, 1.46,  7.54],
]

outdir = os.environ.get('OUTDIR', '/app/outputs')
fname = os.path.join(outdir, 'element_electronegativity.csv')
with open(fname, 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['element', 'Tc', 'IP', 'EA', 'chi'])
    w.writerows(rows)
EOF

# === solve block: alloy_equilibrium_electronegativity.csv ===
python3 /solution/compute.py alloys

# === solve block: weighted_averages.json ===
python3 /solution/compute.py averages
