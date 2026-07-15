#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
export OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: elastic_moduli.csv ===
python3 << 'PYEOF'
import csv, os, math

output_dir = os.environ.get('OUTDIR', '/app/outputs')
os.makedirs(output_dir, exist_ok=True)
outfile = os.path.join(output_dir, 'elastic_moduli.csv')

def compute_moduli(c11, c12, c44):
    B = (c11 + 2*c12) / 3.0
    G_v = (c11 - c12 + 3*c44) / 5.0
    denom = 4*c44 + 3*(c11 - c12)
    G_r = 5.0 * (c11 - c12) * c44 / denom if denom != 0 else 0.0
    G = 0.5 * (G_v + G_r)
    E = 9 * B * G / (3*B + G)
    nu = (3*B - 2*G) / (2*(3*B + G))
    G_over_B = G / B
    return B, G, E, nu, G_over_B

compounds = [
    ('ZrN', 520, 110, 120),
    ('TiN', 600, 130, 160),
    ('AlN', 460, 140, 240),
    ('Zr0.50Ti0.50N', 530, 140, 125),
    ('Zr0.50Al0.50N', 400, 140, 110),
]

with open(outfile, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['compound', 'C11', 'C12', 'C44', 'B', 'G', 'E', 'nu', 'G_over_B'])
    for name, c11, c12, c44 in compounds:
        B, G, E, nu, G_over_B = compute_moduli(c11, c12, c44)
        writer.writerow([name, round(c11, 1), round(c12, 1), round(c44, 1),
                         round(B, 2), round(G, 2), round(E, 2),
                         round(nu, 4), round(G_over_B, 4)])

print('elastic_moduli.csv written')
PYEOF
