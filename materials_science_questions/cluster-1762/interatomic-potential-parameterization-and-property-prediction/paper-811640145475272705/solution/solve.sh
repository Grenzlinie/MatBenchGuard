#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=${OUTDIR:-/app/outputs}
mkdir -p "$OUTDIR"

# === solve block: absorption_energies.csv ===
python3 << 'EOF'
import csv

# Physical constant
e2 = 14.3996  # e^2 in eV*Angstrom

# Crystal parameters
crystals = {
    "MgO": dict(struct="rocksalt", r0=2.1015, A=1.7476, alpha_M=0.10, alpha_X=2.25, I2=14.96, E2=-8.5, dU1=0.0, dU2=0.0, chi=0.5),
    "CaO": dict(struct="rocksalt", r0=2.4053, A=1.7476, alpha_M=0.54, alpha_X=2.25, I2=11.82, E2=-8.5, dU1=0.0, dU2=0.0, chi=0.5),
    "SrO": dict(struct="rocksalt", r0=2.58, A=1.7476, alpha_M=1.0, alpha_X=2.25, I2=10.98, E2=-8.5, dU1=0.0, dU2=0.0, chi=0.5),
    "BaO": dict(struct="rocksalt", r0=2.75, A=1.7476, alpha_M=2.08, alpha_X=2.25, I2=9.96, E2=-8.5, dU1=0.0, dU2=0.0, chi=0.5),
    "CdO": dict(struct="rocksalt", r0=2.3415, A=1.7476, alpha_M=0.54, alpha_X=2.25, I2=16.84, E2=-8.5, dU1=1.55, dU2=1.09, chi=3.5),
    "CaS": dict(struct="rocksalt", r0=2.84, A=1.7476, alpha_M=0.54, alpha_X=6.00, I2=11.82, E2=-8.0, dU1=0.0, dU2=0.0, chi=1.2),
    "SrS": dict(struct="rocksalt", r0=2.935, A=1.7476, alpha_M=1.0, alpha_X=6.00, I2=10.98, E2=-8.0, dU1=0.0, dU2=0.0, chi=1.2),
    "BaS": dict(struct="rocksalt", r0=3.175, A=1.7476, alpha_M=2.08, alpha_X=6.00, I2=9.96, E2=-8.0, dU1=0.0, dU2=0.0, chi=1.2),
    "ZnS": dict(struct="zincblende", r0=2.3513, A=1.6381, alpha_M=0.17, alpha_X=6.00, I2=17.89, E2=-8.0, dU1=1.11, dU2=0.81, chi=1.5),
    "CdS": dict(struct="wurtzite", r0=2.5352, A=1.63, alpha_M=0.54, alpha_X=6.00, I2=16.84, E2=-8.0, dU1=1.07, dU2=0.77, chi=0.5),
}

rows = []
for name, p in crystals.items():
    r0 = p["r0"]
    A = p["A"]
    alpha_sum = p["alpha_M"] + p["alpha_X"]
    VM = 2 * A * e2 / r0
    electro = 2 * (2*A - 1) * e2 / r0
    if p["struct"] == "rocksalt":
        omega1 = -2.027 * e2 * alpha_sum / (r0**4)
        omega2 = -7.00  * e2 * alpha_sum / (2 * r0**4)
    else:  # zincblende or wurtzite
        omega1 = 0.0
        omega2 = -3.50  * e2 * alpha_sum / (2 * r0**4)
    Omega1 = -0.4189 * e2 / r0
    hv1 = electro + p["E2"] - p["I2"] + omega1 + Omega1 + p["dU1"]
    hv2 = VM      + p["E2"] - p["chi"] + omega2 + p["dU2"]
    rows.append((name, round(hv1, 2), round(hv2, 2)))

with open("/app/outputs/absorption_energies.csv", "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["crystal", "hν1_eV", "hν2_eV"])
    w.writerows(rows)
EOF
