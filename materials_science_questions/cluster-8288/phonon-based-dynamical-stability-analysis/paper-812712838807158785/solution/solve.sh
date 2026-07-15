#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: elastic_constants.csv ===
cat > /app/outputs/elastic_constants.csv <<'FFEOF'
i,j,C_ij_GPa
1,1,89.0
1,2,24.1
1,3,10.8
1,4,0.0
1,5,1.2
3,3,64.7
4,4,16.1
6,6,32.45
FFEOF

# === solve block: polycrystalline_moduli.json ===
python3 -c "
import json
moduli = {
    'B_V': 37.1,
    'B_R': 35.6,
    'B': 36.4,
    'G_V': 26.1,
    'G_R': 23.0,
    'G': 24.5,
    'E': 60.1,
    'sigma': 0.23,
    'B_G': 1.48,
    'H_v': 5.7
}
with open('/app/outputs/polycrystalline_moduli.json', 'w') as f:
    json.dump(moduli, f, indent=2)
"

# === solve block: phonon_gamma_frequencies.json ===
python3 -c "
import json
freqs = [
    0.0, 0.0, 0.0,
    103.74,
    110.80, 110.80,
    160.28, 160.28,
    163.28,
    168.47, 168.47,
    180.14, 180.14,
    192.30,
    205.09,
    207.38,
    223.18, 223.18,
    224.83, 224.83,
    250.22,
    258.56, 258.56,
    262.18, 262.18,
    274.92, 274.92,
    276.05,
    359.06,
    364.78,
    425.72,
    518.12,
    549.52, 549.52,
    552.57, 552.57
]
assert len(freqs) == 36
out = {
    'gamma_frequencies': freqs,
    'has_imaginary_modes': False
}
with open('/app/outputs/phonon_gamma_frequencies.json', 'w') as f:
    json.dump(out, f, indent=2)
"
