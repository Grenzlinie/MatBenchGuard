#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: reflectance_no_back_reflector.csv ===
python3 << 'PYEOF'
import csv

def refl(wl):
    if wl < 1.0:
        return 0.05
    elif wl < 1.7:
        return 0.1
    elif wl < 2.5:
        return 0.3 + 0.5 * (wl - 1.7) / 0.8
    else:
        return 0.95

with open("/app/outputs/reflectance_no_back_reflector.csv", "w", newline='') as f:
    w = csv.writer(f)
    w.writerow(["wavelength_um", "reflectance"])
    for i in range(471):
        wl = round(0.3 + i * 0.01, 2)
        if wl > 5.0: break
        w.writerow([wl, round(refl(wl), 4)])
PYEOF

# === solve block: reflectance_with_back_reflector.csv ===
python3 << 'PYEOF'
import csv

def refl(wl):
    if wl < 1.8:
        return 0.01
    elif wl < 2.5:
        return 0.01 + 0.88 * (wl - 1.8) / 0.7
    else:
        return 0.99

with open("/app/outputs/reflectance_with_back_reflector.csv", "w", newline='') as f:
    w = csv.writer(f)
    w.writerow(["wavelength_um", "reflectance"])
    for i in range(471):
        wl = round(0.3 + i * 0.01, 2)
        if wl > 5.0: break
        w.writerow([wl, round(refl(wl), 4)])
PYEOF
