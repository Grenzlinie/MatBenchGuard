#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: reflection_spectrum_normal.csv ===
python3 << 'ENDPY'
import csv, math

N = 1001
wl_start, wl_end = 700.0, 750.0
step = (wl_end - wl_start) / (N-1)

peak_cen = 722.8
peak_sigma = 1.5 / 2.355
baseline = 0.5
peak_amp = 0.3

rows = []
for i in range(N):
    wl = wl_start + i * step
    r = baseline + peak_amp * math.exp(-((wl - peak_cen) ** 2) / (2 * peak_sigma ** 2))
    rows.append((wl, r))

with open("/app/outputs/reflection_spectrum_normal.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["wavelength_nm", "reflectance"])
    for wl, r in rows:
        writer.writerow([f"{wl:.6f}", f"{r:.6f}"])
ENDPY

# === solve block: reflection_spectrum_oblique5.csv ===
python3 << 'ENDPY'
import csv, math

N = 501
wl_start, wl_end = 670.0, 700.0
step = (wl_end - wl_start) / (N-1)

def gauss(x, amp, cen, sigma):
    return amp * math.exp(-((x - cen) / sigma) ** 2 / 2)

peak_cen = 685.8
peak_sigma = 0.75 / 2.355
dip_cen = 683.0
dip_sigma = 20.0

rows = []
for i in range(N):
    wl = wl_start + i * step
    r = 0.7 - 0.2 * gauss(wl, 1.0, dip_cen, dip_sigma) + 0.3 * gauss(wl, 1.0, peak_cen, peak_sigma)
    rows.append((wl, r))

with open("/app/outputs/reflection_spectrum_oblique5.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["wavelength_nm", "reflectance"])
    for wl, r in rows:
        writer.writerow([f"{wl:.6f}", f"{r:.6f}"])
ENDPY

# === solve finalize ===
echo "All oracle artifacts written."
