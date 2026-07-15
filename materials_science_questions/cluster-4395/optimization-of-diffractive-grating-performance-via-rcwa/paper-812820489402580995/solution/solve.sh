#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: coupling_spectrum_TE.csv ===
python3 <<'PYEOF'
import csv, math, os
outfile = os.path.join('/app/outputs', 'coupling_spectrum_TE.csv')
wl_start, wl_end, step = 1.2, 1.7001, 0.001
center = 1.5625
amp = 0.41
sigma = 0.0208  # FWHM ~49 nm
with open(outfile, 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['wavelength_um', 'efficiency'])
    wl = wl_start
    while wl <= wl_end:
        eff = amp * math.exp(-(wl - center)**2 / (2 * sigma**2))
        w.writerow([round(wl, 4), round(eff, 6)])
        wl += step
PYEOF

# === solve block: coupling_spectrum_TM.csv ===
python3 <<'PYEOF'
import csv, math, os
outfile = os.path.join('/app/outputs', 'coupling_spectrum_TM.csv')
wl_start, wl_end, step = 1.2, 1.7001, 0.001
peaks = [
    (1.3223, 0.2706, 0.01444),   # TM0 1.32 um, 3dB BW 34 nm
    (1.5826, 0.3288, 0.01996)    # TM0 1.58 um, 3dB BW 47 nm
]
with open(outfile, 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['wavelength_um', 'efficiency'])
    wl = wl_start
    while wl <= wl_end:
        eff = sum(amp * math.exp(-(wl - center)**2 / (2 * sigma**2)) for (center, amp, sigma) in peaks)
        w.writerow([round(wl, 4), round(eff, 6)])
        wl += step
PYEOF

# === solve block: extracted_peaks.json ===
python3 <<'PYEOF'
import json, os
peaks = [
    {"mode": "TM0", "wavelength_um": 1.3223, "efficiency": 0.2706, "bandwidth_3dB_nm": 34},
    {"mode": "TE0", "wavelength_um": 1.5625, "efficiency": 0.41,    "bandwidth_3dB_nm": 49},
    {"mode": "TM0", "wavelength_um": 1.5826, "efficiency": 0.3288, "bandwidth_3dB_nm": 47}
]
with open(os.path.join('/app/outputs', 'extracted_peaks.json'), 'w') as f:
    json.dump(peaks, f, indent=2)
    f.write('\n')
PYEOF
