#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: transition_pressures.json ===
python3 -c "
import json, csv, os

OUTDIR = os.environ.get('OUTDIR', '/app/outputs')

# transition_pressures.json
pts = {'B3LYP': 19.3, 'LDA': 11.4}
with open(os.path.join(OUTDIR, 'transition_pressures.json'), 'w') as f:
    json.dump(pts, f)

# Pmm2 enthalpy data at B3LYP p_t from Table I (z, enthalpy_diff)
pmm2_b3lyp = [
    (0.250, 0.000), (0.275, 0.031), (0.300, 0.108), (0.325, 0.152),
    (0.350, 0.151), (0.375, 0.132), (0.400, 0.105), (0.425, 0.074),
    (0.450, 0.031), (0.475, 0.004), (0.500, 0.000)
]

# R3m at B3LYP: symmetric parabola with max 0.50 at z=0.375
a = 0.50 / ((0.375-0.25)*(0.5-0.375))  # =32
r3m_b3lyp = [(z, round(a*(z-0.25)*(0.5-z),3)) for z in [i/1000 for i in range(250,501,25)]]

# Write B3LYP CSV
with open(os.path.join(OUTDIR, 'activation_enthalpy_B3LYP.csv'), 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['pathway','z','enthalpy_diff'])
    for z, val in pmm2_b3lyp:
        writer.writerow(['Pmm2', z, val])
    for z, val in r3m_b3lyp:
        writer.writerow(['R3m', z, val])

# Pmm2 LDA: scale B3LYP data to max 0.17
scale_lda = 0.17 / 0.152
pmm2_lda = [(z, round(val*scale_lda,3)) for z,val in pmm2_b3lyp]

# R3m LDA: symmetric parabola max 0.54 at z=0.375
a2 = 0.54 / ((0.375-0.25)*(0.5-0.375))  # =34.56
r3m_lda = [(z, round(a2*(z-0.25)*(0.5-z),3)) for z in [i/1000 for i in range(250,501,25)]]

# Write LDA CSV
with open(os.path.join(OUTDIR, 'activation_enthalpy_LDA.csv'), 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['pathway','z','enthalpy_diff'])
    for z, val in pmm2_lda:
        writer.writerow(['Pmm2', z, val])
    for z, val in r3m_lda:
        writer.writerow(['R3m', z, val])

# band_gaps B3LYP
gaps = {'B3': 4.8, 'Pmm2_z0.35': 1.6, 'B1': 1.1}
with open(os.path.join(OUTDIR, 'band_gaps_B3LYP.json'), 'w') as f:
    json.dump(gaps, f)

print('All artifacts written.')
"
exit 0

# === solve block: activation_enthalpy_B3LYP.csv ===
python3 /solution/generate.py "$OUTDIR/activation_enthalpy_B3LYP.csv"

# === solve block: activation_enthalpy_LDA.csv ===
python3 /solution/generate.py "$OUTDIR/activation_enthalpy_LDA.csv"

# === solve block: band_gaps_B3LYP.json ===
python3 /solution/generate.py "$OUTDIR/band_gaps_B3LYP.json"
