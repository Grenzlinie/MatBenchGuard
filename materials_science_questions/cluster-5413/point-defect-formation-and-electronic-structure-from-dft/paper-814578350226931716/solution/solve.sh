#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: density_of_states.csv ===
python3 <<'PYEOF'
import csv, math

# Energy grid: -5 to 5 eV, step 0.01 eV
emin, emax, step = -5.0, 5.0, 0.01
npoints = int((emax - emin) / step) + 1

# Band edges: VBM at -2.0 eV, CBM at 0.0 eV (Fermi level)
vbm = -2.0
cbm = 0.0
defect_center = -1.0   # Hf-derived defect state inside gap
defect_width = 0.1     # small Gaussian width

with open('/app/outputs/density_of_states.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['energy', 'total_DOS', 'Mo_DOS', 'S_DOS', 'Hf_DOS', 'O_DOS'])
    for i in range(npoints):
        e = emin + i * step
        # Mo and S DOS: valence band states below VBM, conduction band above CBM
        if e < vbm:
            mo_dos = 2.0 * math.exp((e - vbm) / 0.5)   # decaying into valence
            s_dos = 1.5 * math.exp((e - vbm) / 0.5)
        elif e > cbm:
            mo_dos = 3.0 * math.exp(-(e - cbm) / 0.3)  # conduction band onset
            s_dos = 1.0 * math.exp(-(e - cbm) / 0.3)
        else:
            # Inside gap, very small Mo/S contribution
            mo_dos = 0.01
            s_dos = 0.01
        # Hf defect peak inside gap
        hf_dos = 5.0 * math.exp(-((e - defect_center) ** 2) / (2 * defect_width ** 2))
        # O DOS: small contribution from oxide
        o_dos = 0.5 if e > cbm else 0.05
        # Sum
        total = mo_dos + s_dos + hf_dos + o_dos
        # Clip to avoid huge numbers
        total = min(total, 10.0)
        writer.writerow([
            f'{e:.2f}',
            f'{total:.4f}',
            f'{mo_dos:.4f}',
            f'{s_dos:.4f}',
            f'{hf_dos:.4f}',
            f'{o_dos:.4f}'
        ])
PYEOF
