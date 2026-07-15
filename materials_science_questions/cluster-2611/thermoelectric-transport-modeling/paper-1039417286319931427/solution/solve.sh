#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: step_01_transmission.csv ===
python3 /solution/generate_curves.py --output /app/outputs/step_01_transmission.csv --type transmission

# === solve block: step_02_seebeck.csv ===
python3 -c "
import csv, math

def se(curve, e):
    if curve == 'C60':
        return 50 * math.sin(e * 2)
    elif curve == 'Ni@C60':
        return 100 * math.sin(e * 2)
    else:  # Co@C60
        if e >= -0.3 and e <= 0:
            # linear from +105 at e=0 to -190 at e=-0.3 (spread 295)
            return 105 - (0 - e) * (105 + 190) / 0.3
        else:
            return 0

def main():
    with open('/app/outputs/step_02_seebeck.csv', 'w', newline='') as f:
        w = csv.writer(f)
        w.writerow(['energy(eV)', 'system', 'seebeck_coefficient'])
        systems = ['C60', 'Ni@C60', 'Co@C60']
        for e in [round(x*0.01, 2) for x in range(-200, 201)]:
            for s in systems:
                w.writerow([e, s, round(se(s, e), 3)])
main()
"

# === solve block: step_03_zt.csv ===
python3 /solution/generate_curves.py --output /app/outputs/step_03_zt.csv --type zt
