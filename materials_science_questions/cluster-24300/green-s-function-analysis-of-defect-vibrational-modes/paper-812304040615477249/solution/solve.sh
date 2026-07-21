#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: b_values.csv ===
python3 << 'PYEOF'
import csv
import math

C = (8 * math.pi**2) / 3

# Table 1: HA 50-500 K, B-values (in Å²)
rows_ha = [
    (50, 0.64, 0.13, 0.11, 0.16, 0.10),
    (100, 0.67, 0.16, 0.14, 0.19, 0.13),
    (150, 0.74, 0.20, 0.18, 0.24, 0.17),
    (200, 0.84, 0.24, 0.23, 0.28, 0.21),
    (250, 0.95, 0.29, 0.28, 0.34, 0.26),
    (300, 1.08, 0.34, 0.33, 0.39, 0.30),
    (350, 1.22, 0.39, 0.38, 0.46, 0.35),
    (400, 1.36, 0.44, 0.43, 0.51, 0.40),
    (450, 1.51, 0.49, 0.48, 0.57, 0.44),
    (500, 1.65, 0.54, 0.53, 0.63, 0.49)
]

# Table 2: ⟨u²⟩ in Å²; format: (T, ⟨u²⟩_I, ⟨u²⟩_F_D, ⟨u²⟩_Ca_D, ⟨u²⟩_F_H, ⟨u²⟩_Ca_H)
rows_ha_2 = [
    (300, 0.041, 0.013, 0.013, 0.015, 0.011),
    (1000, 0.121, 0.040, 0.040, 0.047, 0.037),
    (1500, 0.179, 0.060, 0.060, 0.070, 0.055)
]
rows_qha = [
    (300, 0.041, 0.015, 0.014, 0.016, 0.012),
    (1000, 0.206, 0.077, 0.053, 0.061, 0.046),
    (1500, 0.425, 0.107, 0.081, 0.095, 0.071)
]

with open('/app/outputs/b_values.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['temperature', 'approximation', 'B_interstitial', 'B_F_D', 'B_Ca_D', 'B_F_H', 'B_Ca_H'])
    for t, bI, bFD, bCaD, bFH, bCaH in rows_ha:
        writer.writerow([t, 'HA', f'{bI:.2f}', f'{bFD:.2f}', f'{bCaD:.2f}', f'{bFH:.2f}', f'{bCaH:.2f}'])
    for t, uI, uFD, uCaD, uFH, uCaH in rows_ha_2:
        writer.writerow([t, 'HA', f'{C*uI:.2f}', f'{C*uFD:.2f}', f'{C*uCaD:.2f}', f'{C*uFH:.2f}', f'{C*uCaH:.2f}'])
    for t, uI, uFD, uCaD, uFH, uCaH in rows_qha:
        writer.writerow([t, 'QHA', f'{C*uI:.2f}', f'{C*uFD:.2f}', f'{C*uCaD:.2f}', f'{C*uFH:.2f}', f'{C*uCaH:.2f}'])
PYEOF
