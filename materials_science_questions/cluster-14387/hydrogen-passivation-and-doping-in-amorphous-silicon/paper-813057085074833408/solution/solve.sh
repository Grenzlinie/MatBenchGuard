#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: dass_domain_energies.json ===
python3 -c "
import json

eps0 = -3.91
c1 = 1.49
c2 = 1.84
c = 2.71
s0 = 0.249
kBT = 0.05627

data = [
    (1, 3, 0, 0, 60.5),
    (2, 0, 2, 1, 66.5),
    (3, 1, 1, 2, 127.0),
    (4, 2, 2, 2, 111.5),
    (5, 2, 3, 2, 188.0),
    (6, 2, 4, 2, 250.0),
    (7, 2, 5, 2, 305.0),
    (8, 2, 6, 2, 345.5),
    (9, 2, 7, 2, 372.0),
    (10, 2, 8, 2, 391.0),
]

results = []
for mf, n_ch1, n_ch2, n_ch3, nf in data:
    eds = mf * eps0 + n_ch1*c1 + n_ch2*c2 + n_ch3*c
    f_das = eds + s0 * kBT * nf
    results.append({
        'm_F': mf,
        'E_DS_eV': round(eds, 6),
        'n_f': nf,
        'F_DAS_eV': round(f_das, 6)
    })

with open('$OUTDIR/dass_domain_energies.json', 'w') as f:
    json.dump(results, f, indent=2)
"
