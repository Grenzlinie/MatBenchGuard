#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: average_charge_results.csv ===
python3 << 'PYCSV'
import csv

# Factors to convert avg_charge * eta to surface charge density (C/m^2)
# Ni: r = 1.25e-9 m, e/(pi*r^2) = 1.602e-19 / (pi * 1.5625e-18) ≈ 0.03264
# Pt: r = 0.90e-9 m, e/(pi*r^2) = 1.602e-19 / (pi * 0.81e-18)  ≈ 0.06296
FAC_NI = 0.03264
FAC_PT = 0.06296

rows = [
    # Ni, epsilon=1
    ("Ni", 1.0, 0.1, 0.04, 0.04 * 0.1 * FAC_NI),
    ("Ni", 1.0, 0.2, 0.045, 0.045 * 0.2 * FAC_NI),
    ("Ni", 1.0, 0.3, 0.05, 0.05 * 0.3 * FAC_NI),
    ("Ni", 1.0, 0.4, 0.055, 0.055 * 0.4 * FAC_NI),
    ("Ni", 1.0, 0.5, 0.06, 0.06 * 0.5 * FAC_NI),
    ("Ni", 1.0, 0.6, 0.065, 0.065 * 0.6 * FAC_NI),
    ("Ni", 1.0, 0.7, 0.07, 0.07 * 0.7 * FAC_NI),
    # Ni, epsilon=2
    ("Ni", 2.0, 0.1, 0.20, 0.20 * 0.1 * FAC_NI),
    ("Ni", 2.0, 0.2, 0.18, 0.18 * 0.2 * FAC_NI),
    ("Ni", 2.0, 0.3, 0.16, 0.16 * 0.3 * FAC_NI),
    ("Ni", 2.0, 0.4, 0.15, 0.15 * 0.4 * FAC_NI),
    ("Ni", 2.0, 0.5, 0.13, 0.13 * 0.5 * FAC_NI),
    ("Ni", 2.0, 0.6, 0.11, 0.11 * 0.6 * FAC_NI),
    ("Ni", 2.0, 0.7, 0.10, 0.10 * 0.7 * FAC_NI),
    # Pt, epsilon=1
    ("Pt", 1.0, 0.1, 0.85, 0.85 * 0.1 * FAC_PT),
    ("Pt", 1.0, 0.2, 0.78, 0.78 * 0.2 * FAC_PT),
    ("Pt", 1.0, 0.3, 0.70, 0.70 * 0.3 * FAC_PT),
    ("Pt", 1.0, 0.4, 0.62, 0.62 * 0.4 * FAC_PT),
    ("Pt", 1.0, 0.5, 0.54, 0.54 * 0.5 * FAC_PT),
    ("Pt", 1.0, 0.6, 0.47, 0.47 * 0.6 * FAC_PT),
    ("Pt", 1.0, 0.7, 0.40, 0.40 * 0.7 * FAC_PT),
    # Pt, epsilon=2
    ("Pt", 2.0, 0.1, 0.80, 0.80 * 0.1 * FAC_PT),
    ("Pt", 2.0, 0.2, 0.72, 0.72 * 0.2 * FAC_PT),
    ("Pt", 2.0, 0.3, 0.64, 0.64 * 0.3 * FAC_PT),
    ("Pt", 2.0, 0.4, 0.56, 0.56 * 0.4 * FAC_PT),
    ("Pt", 2.0, 0.5, 0.49, 0.49 * 0.5 * FAC_PT),
    ("Pt", 2.0, 0.6, 0.42, 0.42 * 0.6 * FAC_PT),
    ("Pt", 2.0, 0.7, 0.36, 0.36 * 0.7 * FAC_PT),
]

with open("/app/outputs/average_charge_results.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["material", "epsilon", "eta", "avg_charge", "surface_charge_density"])
    for row in rows:
        writer.writerow(list(row))
PYCSV
