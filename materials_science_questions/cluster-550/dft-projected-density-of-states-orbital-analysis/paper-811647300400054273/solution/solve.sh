#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs
python3 << 'PYEOF'
import json, csv, os

outdir = '/app/outputs'

# --- Write simulated EXAFS peaks ---
peaks = {
    '(Au-Au)1_peak_R': 2.80,
    '(Au-Au)2_peak_R': 2.95,
    '(Au-Au)3_peak_R': 3.15
}
with open(os.path.join(outdir, 'simulated_exafs_peaks.json'), 'w') as f:
    json.dump(peaks, f, indent=2)

# --- Write site-specific l-DOS ---
site_l_dos = [
    {'site': 'central', 's_count': 1.20, 'p_count': 0.10, 'd_count': 9.70},
    {'site': 'surface', 's_count': 1.40, 'p_count': 0.15, 'd_count': 9.55},
    {'site': 'staple',  's_count': 1.65, 'p_count': 0.25, 'd_count': 9.30}
]
csv_path = os.path.join(outdir, 'site_specific_l_dos.csv')
with open(csv_path, 'w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=['site', 's_count', 'p_count', 'd_count'])
    writer.writeheader()
    writer.writerows(site_l_dos)
print('Reference oracle artifacts written.')
PYEOF

# === solve block: simulated_exafs_peaks.json ===
python3 -c "
import json
peaks = {
    '(Au-Au)1_peak_R': 2.80,
    '(Au-Au)2_peak_R': 2.95,
    '(Au-Au)3_peak_R': 3.15
}
with open('$OUTDIR/simulated_exafs_peaks.json', 'w') as f:
    json.dump(peaks, f, indent=2)
"

# === solve block: site_specific_l_dos.csv ===
# Already included in preamble
# No separate block needed
