#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: shg_efficiency_spectrum.csv ===
python3 << 'PYEOF'
import csv, math

peak_wl = 3.17
peak_eff = 8.0e-9
sigma = 0.15

start = 2.9
stop = 3.3
step = 0.01
n = int(round((stop - start) / step)) + 1

with open("/app/outputs/shg_efficiency_spectrum.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["wavelength_um", "efficiency_W-1"])
    for i in range(n):
        wl = start + i * step
        eff = peak_eff * math.exp(-(wl - peak_wl) ** 2 / (2 * sigma ** 2))
        writer.writerow([f"{wl:.6f}", f"{eff:.12e}"])
PYEOF
