#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: overall_rep.csv ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs
python3 -c '
import csv, math

def gauss(x, mu, sigma):
    return math.exp(-((x - mu) / sigma) ** 2)

wl_range = [150.0 + i * 0.5 for i in range(301)]
wl_dip = 215.0
sigma_dip = 3.0

# dip depths: deeper for higher overtones
dip = {
    "fundamental": 0.92,
    "ov2": 0.97,
    "ov3": 0.99,
    "ov4": 0.995,
    "ov5": 0.998,
}

# amplitude scales (consistent arbitrary units)
amp = {
    "fundamental": 1.0,
    "ov2": 0.30,
    "ov3": 0.12,
    "ov4": 0.04,
    "ov5": 0.012,
}

with open("/app/outputs/overall_rep.csv", "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["wavelength_nm", "intensity_fundamental", "intensity_overtone_2", "intensity_overtone_3", "intensity_overtone_4", "intensity_overtone_5"])
    for wl in wl_range:
        # base profile: two broad humps plus a weak baseline
        base = 0.6 * gauss(wl, 180, 18) + 0.9 * gauss(wl, 260, 30) + 0.3
        dip_factor = math.exp(-((wl - wl_dip) / sigma_dip) ** 2)
        I_f = max(amp["fundamental"] * base * (1 - dip["fundamental"] * dip_factor), 0.0)
        I_2 = max(amp["ov2"] * base * (1 - dip["ov2"] * dip_factor), 0.0)
        I_3 = max(amp["ov3"] * base * (1 - dip["ov3"] * dip_factor), 0.0)
        I_4 = max(amp["ov4"] * base * (1 - dip["ov4"] * dip_factor), 0.0)
        I_5 = max(amp["ov5"] * base * (1 - dip["ov5"] * dip_factor), 0.0)
        w.writerow([f"{wl:.1f}", I_f, I_2, I_3, I_4, I_5])
'
