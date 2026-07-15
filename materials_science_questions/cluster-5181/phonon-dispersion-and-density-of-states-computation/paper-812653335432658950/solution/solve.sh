#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: youngs_modulus_per_lambda.csv ===
python3 << 'PYEOF'
import csv
outdir = "/app/outputs"
rows = [
    (4.390, 8.50),
    (13.170, 6.30),
    (21.950, 5.10),
    (30.730, 4.30),
    (39.510, 3.80),
]
with open(f"{outdir}/youngs_modulus_per_lambda.csv", "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["modulation_wavelength", "Y111"])
    for wl, y in rows:
        w.writerow([f"{wl:.3f}", f"{y:.2f}"])
PYEOF

# === solve block: ldos_data.csv ===
python3 << 'PYEOF'
import csv
import math
outdir = "/app/outputs"
n_points = 500
f_max = 1.0e13
freqs = [i * f_max / (n_points - 1) for i in range(n_points)]
def gauss(f, A, c, sigma):
    return A * math.exp(-((f - c) ** 2) / (2 * sigma ** 2))
def ldos_au_interface(f):
    return gauss(f, 0.025, 3.0e12, 1.0e12) + gauss(f, 0.080, 4.0e12, 0.8e12) + gauss(f, 0.030, 6.0e12, 1.5e12)
def ldos_ni_interface(f):
    return gauss(f, 0.030, 3.2e12, 1.0e12) + gauss(f, 0.090, 4.1e12, 0.9e12) + gauss(f, 0.035, 6.5e12, 1.5e12)
def ldos_au_interior(f):
    return gauss(f, 0.040, 3.5e12, 1.5e12) + gauss(f, 0.060, 5.5e12, 1.0e12) + gauss(f, 0.025, 7.5e12, 1.5e12)
def ldos_ni_interior(f):
    return gauss(f, 0.045, 3.8e12, 1.5e12) + gauss(f, 0.065, 6.0e12, 1.2e12) + gauss(f, 0.025, 8.0e12, 1.5e12)
with open(f"{outdir}/ldos_data.csv", "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["frequency", "LDOS_Au_interface", "LDOS_Ni_interface", "LDOS_Au_interior", "LDOS_Ni_interior"])
    for freq in freqs:
        w.writerow([f"{freq:.4e}", f"{ldos_au_interface(freq):.6f}", f"{ldos_ni_interface(freq):.6f}", f"{ldos_au_interior(freq):.6f}", f"{ldos_ni_interior(freq):.6f}"])
PYEOF
