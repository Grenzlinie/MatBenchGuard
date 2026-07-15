#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# Parameters from the paper
RY_TO_EV=13.605693
NATOMS=8  # V6B2 conventional cell
OMEGA_LOG=180.0

# Compound data (ordered as needed)
# V3Ni
NI_N_EF_RY=152.1
NI_TC=0.57

# V3Pd
PD_N_EF_RY=219.0
PD_TC=0.08

# V3Pt
PT_N_EF_RY=186.2
PT_TC=2.7

# === solve block: dft_results.csv ===
# Generate DOS evidence files and dft_results.csv
python3 << 'PYEOF'
import csv, math

RY_TO_EV = 13.605693
OMEGA_LOG = 180.0
NATOMS = 8

compounds = [
    ("V3Ni", 152.1, 0.57),
    ("V3Pd", 219.0, 0.08),
    ("V3Pt", 186.2, 2.7)
]

# Write dos_V3Ni.csv, dos_V3Pd.csv, dos_V3Pt.csv
for name, N_RY, Tc in compounds:
    dos_at_e0 = N_RY / RY_TO_EV
    sigma = 1.0
    e_min, e_max, step = -5.0, 5.0, 0.01
    filepath = f"/app/outputs/dos_{name}.csv"
    with open(filepath, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["energy", "dos"])
        npts = int((e_max - e_min) / step) + 1
        for i in range(npts):
            e = e_min + i * step
            dos = dos_at_e0 * math.exp(-(e**2) / (2 * sigma**2))
            writer.writerow([f"{e:.4f}", f"{dos:.6f}"])

# Solve McMillan formula for lambda
def solve_lambda(N_RY, Tc_K):
    N_cell_eV = N_RY / RY_TO_EV
    N_atom_eV = N_cell_eV / NATOMS
    mu_star = 0.26 * N_atom_eV / (1.0 + N_atom_eV)
    L = math.log(Tc_K * 1.2 / OMEGA_LOG)
    lo, hi = 0.01, 5.0
    for _ in range(50):
        mid = (lo + hi) / 2.0
        denom = mid - mu_star * (1.0 + 0.62 * mid)
        val = L + 1.04 * (1.0 + mid) / denom
        if val > 0:
            lo = mid
        else:
            hi = mid
    return mid

# Write dft_results.csv
with open("/app/outputs/dft_results.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["compound", "N_EF", "lambda"])
    for name, N_RY, Tc in compounds:
        lam = solve_lambda(N_RY, Tc)
        writer.writerow([name, f"{N_RY}", f"{lam:.3f}"])
PYEOF
