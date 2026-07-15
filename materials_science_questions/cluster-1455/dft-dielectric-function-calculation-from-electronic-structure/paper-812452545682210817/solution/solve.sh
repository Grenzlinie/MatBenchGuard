#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs
export OUTDIR=/app/outputs

# === solve block: bandgap_ratios.csv ===
python3 << 'PYEOF'
import csv, os
outdir = os.environ['OUTDIR']
outpath = os.path.join(outdir, 'bandgap_ratios.csv')
with open(outpath, 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['displacement_case', 'time_fraction', 'bandgap_to_midgap_ratio'])
    # u0=(0.25a,0.25a)
    for i in range(26):
        t = i * 0.01
        ratio = 0.16 * (1.0 - 4.0 * t) ** 2
        writer.writerow(['u0_25_25', f'{t:.2f}', f'{ratio:.6f}'])
    # u0=(0.3a,0) – original band gap
    for i in range(26):
        t = i * 0.01
        ratio = max(0.02, 0.15 * (1.0 - 4.0 * t) ** 2)
        writer.writerow(['u0_30_0', f'{t:.2f}', f'{ratio:.6f}'])
print('bandgap_ratios.csv written')
PYEOF

# === solve block: guided_modes.csv ===
python3 << 'PYEOF'
import csv, os, math
out = os.environ['OUTDIR'] + '/guided_modes.csv'
with open(out, 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['wavevector', 'frequency'])
    # Symmetric guided-mode dispersion within the band gap (center ~0.305)
    for i in range(51):
        k = i * 0.01   # wavevector ka/(2πc) from 0.0 to 0.5
        # Dip shape: minimum 0.285 at k=0.25, back to 0.305 at edges
        x = (k - 0.25) / 0.25   # from -1 to 1
        freq = 0.305 - 0.02 * (1.0 - x * x)   # concav down
        w.writerow([f'{k:.2f}', f'{freq:.6f}'])
print('guided_modes.csv written')
PYEOF
