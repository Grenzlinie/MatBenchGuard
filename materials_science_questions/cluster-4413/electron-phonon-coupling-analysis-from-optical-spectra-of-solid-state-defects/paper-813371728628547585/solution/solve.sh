#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: spectral_weight_transfer.csv ===
#!/bin/bash
# Generate spectral_weight_transfer.csv with reference values
python3 << 'PYEOF'
import csv, math

# Temperature grid (0 to 2500 K, step 50 K)
temps = [i for i in range(0, 2550, 50)]

# Phenomenological parameters for three tubes
# tube -> (h0, h_2500, l_2500, l_thresh)  -- h0: higher sideband at 0 K; h_2500, l_2500: at 2500 K; l_thresh: T where lower sideband activates
params = {
    '19,0': (0.05, 0.25, 0.30, 500),
    '20,0': (0.03, 0.20, 0.25, 500),
    '21,0': (0.01, 0.15, 0.20, 500)
}

rows = []
for tube, (h0, h_2500, l_2500, l_thresh) in params.items():
    for T in temps:
        # Higher sideband: quadratic rise from h0 to h_2500 at 2500 K
        frac = min(1.0, T / 2500.0)
        h = h0 + (h_2500 - h0) * frac * frac
        # Lower sideband: zero below threshold, then ramps up
        if T <= l_thresh:
            l = 0.0
        else:
            frac_l = (T - l_thresh) / (2500.0 - l_thresh)
            l = l_2500 * frac_l * frac_l
        # Zero-phonon line weight keeps total = 1.0
        zpl = 1.0 - h - l
        rows.append([tube, T, round(zpl, 6), round(h, 6), round(l, 6)])

# Sort by tube and temperature
sort_key = {'19,0': 0, '20,0': 1, '21,0': 2}
rows.sort(key=lambda r: (sort_key[r[0]], r[1]))

with open('/app/outputs/spectral_weight_transfer.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['tube_index', 'temperature_K', 'zpl_weight', 'higher_sideband_weight', 'lower_sideband_weight'])
    writer.writerows(rows)
PYEOF
