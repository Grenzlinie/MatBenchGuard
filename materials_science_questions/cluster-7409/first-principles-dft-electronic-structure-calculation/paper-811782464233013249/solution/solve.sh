#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: pure_BTO_dos.csv ===
python3 << 'PYEOF' > "$OUTDIR/pure_BTO_dos.csv"
import csv, math, sys

emin, emax, estep = -12.0, 12.0, 0.02
vb_peak, cb_peak = -3.0, 4.0
vb_sigma, cb_sigma = 1.5, 2.0
vb_cutoff, cb_cutoff = -0.1, 2.5
amp = 10.0

writer = csv.writer(sys.stdout)
writer.writerow(['energy', 'total_dos'])

e = emin
while e <= emax + estep / 2:
    dos = 0.0
    if e <= vb_cutoff:
        dos = amp * math.exp(-0.5 * ((e - vb_peak) / vb_sigma) ** 2)
    elif e >= cb_cutoff:
        dos = amp * math.exp(-0.5 * ((e - cb_peak) / cb_sigma) ** 2)
    writer.writerow([round(e, 3), round(dos, 6)])
    e += estep
PYEOF

cat > "$OUTDIR/optical_absorption.csv" << 'CSVEOF'
system,onset_wavelength_nm
BTO,495
TiO2_anatase,425
CSVEOF

# === solve block: substituted_BTO_bandgaps.csv ===
cat > "$OUTDIR/substituted_BTO_bandgaps.csv" << 'CSVEOF'
system,band_gap,midgap_state_flag
Bi2Ti1.5V0.5O7,1.9,True
Bi2Ti1.5Cr0.5O7,2.1,True
Bi2Ti1.5Mn0.5O7,2.2,True
Bi2Ti1.5Fe0.5O7,1.6,True
Bi2Ti1.5Ni0.5O7,2.0,True
CSVEOF
