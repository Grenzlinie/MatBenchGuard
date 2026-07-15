#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: self_energy_imag.dat ===
python3 << EOF
energy_list = [i * 0.001 for i in range(121)]
im_sigma = []
for e in energy_list:
    if e < 0.016:
        im = 0.0
    elif 0.016 <= e <= 0.038:
        im = 0.005
    elif 0.038 < e < 0.046:
        im = 0.0001
    elif 0.046 <= e <= 0.068:
        im = 0.005
    else:
        im = 0.0
    im_sigma.append(im)
with open('$OUTDIR/self_energy_imag.dat', 'w') as f:
    for e, im in zip(energy_list, im_sigma):
        f.write(f'{e:.6f}\t{im:.6f}\n')
EOF

# === solve block: spectral_function.dat ===
python3 /solution/generate_outputs.py spectral_function.dat

# === solve block: quasiparticle_poles.json ===
python3 /solution/generate_outputs.py quasiparticle_poles.json
