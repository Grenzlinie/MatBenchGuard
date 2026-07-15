#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: simulated_radii.csv ===
python3 << 'PYEOF'
import csv
import math

# physical constants
R  = 8.314         # J/(mol·K)
NA = 6.022e23      # mol⁻¹
v  = 2.27e-5       # m³/mol (CdSe molar volume)

# All 33 non‑missing rows from Table S1, in exact paper order (omitting OA5 at 508 K).
# Fields: SystemID, C_np_uM, C0_mM, C_sol_nM, surface_tension_Jpm2, temperature_K
rows = [
    ("OA19",      9.1,  6.3, 0.02, 0.2, 483),
    ("OA15",      9.3,  6.3, 0.02, 0.2, 483),
    ("OA10",     13,    6.3, 0.02, 0.2, 483),
    ("OA6.5",    11,    6.3, 0.02, 0.2, 483),
    ("OA5",       8.9,  6.3, 0.02, 0.2, 483),
    ("OA19",      8,    6.3, 0.02, 0.2, 508),
    ("OA15",     10.4,  6.3, 0.02, 0.2, 508),
    ("OA10",      8.2,  6.3, 0.02, 0.2, 508),
    ("OA6.5",     6.3,  6.3, 0.02, 0.2, 508),
    # skip OA5 at 508 K (missing C_np)
    ("OA19",      9.9,  6.3, 0.02, 0.2, 528),
    ("OA15",      8.1,  6.3, 0.02, 0.2, 528),
    ("OA10",      8,    6.3, 0.02, 0.2, 528),
    ("OA6.5",     5,    6.3, 0.02, 0.2, 528),
    ("OA5",       5.7,  6.3, 0.02, 0.2, 528),
    ("OA19",      7.7,  6.3, 0.02, 0.2, 543),
    ("OA15",      9.9,  6.3, 0.02, 0.2, 543),
    ("OA10",      7,    6.3, 0.02, 0.2, 543),
    ("OA6.5",     6.8,  6.3, 0.02, 0.2, 543),
    ("OA5",       5.5,  6.3, 0.02, 0.2, 543),
    ("OA64",     12.5, 17,   0.02, 0.2, 503),
    ("OA32",     26,   17,   0.02, 0.2, 503),
    ("OA16",     39,   17,   0.02, 0.2, 503),
    ("OA8",      47.5, 17,   0.02, 0.2, 503),
    ("OA4",      57.5, 17,   0.02, 0.2, 503),
    ("OA20",     32,   16,   0.02, 0.2, 503),
    ("OA14",     47,   16,   0.02, 0.2, 503),
    ("OA11",     53,   16,   0.02, 0.2, 503),
    ("OA8.5",    56,   16,   0.02, 0.2, 503),
    ("OA5.5",    58,   16,   0.02, 0.2, 503),
    ("TMPPA3.5", 49,   26,   0.02, 0.2, 503),
    ("TMPPA2",   36,   27,   0.02, 0.2, 503),
    ("TMPPA1.5", 25,   29,   0.02, 0.2, 503),
    ("TMPPA0",   15,   31,   0.02, 0.2, 503),
]

def compute_r_eq(C_np_uM, C0_mM, C_sol_nM, gamma, T):
    # convert to SI (mol/m³, m)
    C_np = C_np_uM * 1e-3      # µM → mol/m³  (1 µM = 1e-3 mol/m³)
    C0   = C0_mM * 1.0         # mM → mol/m³  (1 mM = 1 mol/m³)
    C_s  = C_sol_nM * 1e-6     # nM → mol/m³  (1 nM = 1e-6 mol/m³)

    S0 = C0 / C_s
    # coefficients
    A = 4.0 * math.pi * gamma
    B = (4.0 * math.pi / 3.0) * (R * T / v)
    Ccoef = (4.0 * math.pi / 3.0) * (NA * C_np) / (v * C_s)   # units m⁻³

    # maximum physically allowed radius (log argument → 0⁺)
    if Ccoef <= 0 or S0 <= 0:
        raise ValueError("Invalid parameters")
    r_max = (S0 / Ccoef) ** (1.0 / 3.0) * 0.999999   # tiny safety margin

    # free energy G(r) in Joules
    def G(r):
        if r <= 0.0:
            return 0.0
        D = Ccoef * r**3
        if S0 - D <= 0.0:
            return 1e300   # effectively forbidden region
        return A * r**2 - B * r**3 * math.log(S0 - D)

    # scan for the global minimum on a fine grid up to r_max
    n_points = 20000
    best_r = 1e-20
    best_G = float('inf')
    # evaluate at r=0 as reference
    g0 = G(1e-20)
    if g0 < best_G:
        best_G = g0
        best_r = 1e-20

    for i in range(1, n_points):
        r = r_max * i / n_points
        g = G(r)
        if g < best_G:
            best_G = g
            best_r = r
    return best_r * 1e9   # convert m → nm

with open('/app/outputs/simulated_radii.csv', 'w', newline='') as fout:
    writer = csv.writer(fout)
    writer.writerow(['SystemID', 'R_sim_computed'])
    for sid, *params in rows:
        r_nm = compute_r_eq(*params)
        writer.writerow([sid, f'{r_nm:.2f}'])
PYEOF
