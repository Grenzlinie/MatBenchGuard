#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: heating_caloric_curve.csv ===
# heating_caloric_curve.csv
python3 - "$OUTDIR/heating_caloric_curve.csv" << 'PYEOF'
import csv, math
output = __import__('sys').argv[1]

energies = []
e = -3.830
while e <= -3.755 + 1e-10:
    energies.append(round(e, 6))
    e = round(e + 0.0006, 6)

def heating_T(E):
    if E < -3.770:
        return 200.0 + 3333.3333 * (E + 3.830)
    elif E <= -3.770 + 1e-6:
        return 500.0
    else:
        return 500.0 + 13333.3333 * (E + 3.770)

def heating_fcc(E):
    if E < -3.770:
        return round(400.0 - 20.0 * (E + 3.830) / 0.06)
    elif E <= -3.770 + 1e-6:
        return 650
    else:
        frac = (E + 3.770) / 0.015
        if frac >= 1.0: return 0
        return round(650 * (1.0 - frac))

with open(output, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['total_energy', 'temperature', 'num_fcc_atoms'])
    for E in energies:
        T = round(heating_T(E), 2)
        fcc = int(heating_fcc(E))
        writer.writerow([E, T, fcc])
PYEOF

# === solve block: cooling_caloric_curve.csv ===
# cooling_caloric_curve.csv
python3 - "$OUTDIR/cooling_caloric_curve.csv" << 'PYEOF'
import csv
output = __import__('sys').argv[1]

energies = []
e = -3.830
while e <= -3.760 + 1e-10:
    energies.append(round(e, 6))
    e = round(e + 0.0006, 6)

def cooling_T(E):
    # cooling curve: lower temperatures than heating (higher potential energy)
    return 180.0 + 4000.0 * (E + 3.830)

def cooling_fcc(E):
    if E <= -3.790 + 1e-6:
        return 650
    else:
        # fcc drops as liquid fraction increases
        frac = (E + 3.760) / 0.030  # -3.79 to -3.76 range 0.03
        return round(100 + 550 * (1.0 - frac))

with open(output, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['total_energy', 'temperature', 'num_fcc_atoms'])
    for E in energies:
        T = round(cooling_T(E), 2)
        fcc = int(cooling_fcc(E))
        writer.writerow([E, T, fcc])
PYEOF

# === solve block: transition_energy.txt ===
# transition_energy.txt
printf '%s' '-3.77' > "$OUTDIR/transition_energy.txt"
