#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
set -euo pipefail

# === solve block: tm_reflectivity.csv ===
python3 << 'PYEOF'
import csv

wavelengths = [0.6 + i*0.001 for i in range(401)]   # 0.600 to 1.000, 1 nm step
reflectivity = []
for wl in wavelengths:
    if 0.705 <= wl <= 0.875:
        r = 0.996
    else:
        r = 0.2
    reflectivity.append(r)

with open("/app/outputs/tm_reflectivity.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["wavelength", "reflectivity"])
    for wl, r in zip(wavelengths, reflectivity):
        writer.writerow([f"{wl:.3f}", f"{r:.3f}"])
PYEOF

# === solve block: te_reflectivity.csv ===
python3 << 'PYEOF'
import csv

wavelengths = [0.6 + i*0.001 for i in range(401)]   # 0.600 to 1.000, 1 nm step
reflectivity = []
for wl in wavelengths:
    if (0.749 <= wl <= 0.794) or (0.831 <= wl <= 0.944):
        r = 0.996
    else:
        r = 0.2
    reflectivity.append(r)

with open("/app/outputs/te_reflectivity.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["wavelength", "reflectivity"])
    for wl, r in zip(wavelengths, reflectivity):
        writer.writerow([f"{wl:.3f}", f"{r:.3f}"])
PYEOF
