#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: total_dos.csv ===
python3 <<PYEOF
import csv, math

# Energy grid from 0.3 to 0.9 Ryd with step 0.005 => 121 points
e_start, e_end, step = 0.3, 0.9, 0.005
energies = []
e = e_start
while e <= e_end + 1e-9:
    energies.append(e)
    e += step

# Synthetic total DOS: two peaks centred at 0.52 and 0.68 Ryd,
# sigma 0.03 and 0.04, weights roughly 4:6
dos = []
for ei in energies:
    p1 = 4.0 * math.exp(-((ei - 0.52)**2) / (2*0.03**2))
    p2 = 6.0 * math.exp(-((ei - 0.68)**2) / (2*0.04**2))
    dos.append(p1 + p2)

# Scale to integrated 10 electrons per unit cell
integral = sum((dos[i] + dos[i-1]) * 0.5 * step for i in range(1, len(dos)))
scale = 10.0 / integral if integral else 1.0
dos = [d * scale for d in dos]

# Write CSV
with open("$OUTDIR/total_dos.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["energy", "total_DOS"])
    for ei, di in zip(energies, dos):
        writer.writerow([f"{ei:.5f}", f"{di:.8f}"])
PYEOF

# === solve block: ldos_ti.csv ===
python3 /solution/generate_dos.py ti /app/outputs/ldos_ti.csv

# === solve block: ldos_ru.csv ===
python3 /solution/generate_dos.py ru /app/outputs/ldos_ru.csv
