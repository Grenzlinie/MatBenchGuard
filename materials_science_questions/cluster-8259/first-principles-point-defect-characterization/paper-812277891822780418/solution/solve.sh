#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: predictions.json ===
python3 -c "
import json
b = 0.263  # nm
d1 = 1.805 * b
d2 = 2.108 * b
e2 = 1.44   # eV·nm (e^2/(4πε0))
U1 = e2 / d1
U2 = e2 / d2
stokes = 18 * 0.026  # eV
hnu1 = U1 - stokes
hnu2 = U2 - stokes

result = {
    'geometry': 'sp2',
    'E1_U_eV': round(U1, 6),
    'E2_U_eV': round(U2, 6),
    'E1_hnu_eV': round(hnu1, 6),
    'E2_hnu_eV': round(hnu2, 6),
    'stokes_shift_eV': round(stokes, 6)
}

with open('$OUTDIR/predictions.json', 'w') as f:
    json.dump(result, f, indent=2)
print('predictions.json written')
"
