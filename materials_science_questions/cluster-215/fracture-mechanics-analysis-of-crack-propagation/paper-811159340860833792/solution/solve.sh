#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: crack_area_analytical.csv ===
python3 << 'PYEOF'
import math
import csv

# material constants from Table 1 (SI units)
f = 0.34
E_f = 410e9   # Pa
E_m = 110e9   # Pa
D = 140e-6    # m
tau = 23e6    # Pa
I0 = 1.0
I1 = 1.2

# geometry / formula constants
c1 = 4 * I1**2 / math.pi
c2 = (math.pi / (2 * I1)) ** 2 * I0

Sigma_a_list = [0.01, 0.1, 1, 2, 5, 10, 20, 50, 100]

rows = []
for Sigma in Sigma_a_list:
    # A_short: valid only for Sigma_a > 1
    if Sigma > 1:
        A_short = c1 * ((math.sqrt(1 + c2 * Sigma) - 1) ** 2)
    else:
        A_short = float('nan')
    
    # A_long (Eq. 25)
    A_long = Sigma**2 - 0.225 * Sigma**3
    
    # A_unbridged
    A_unbridged = math.pi * Sigma
    
    # DeltaA_short = 2 * A_short(Sigma_a/2) if Sigma_a/2 > 1
    if Sigma / 2 > 1:
        Sig_half = Sigma / 2
        DeltaA_short = 2 * c1 * ((math.sqrt(1 + c2 * Sig_half) - 1) ** 2)
    else:
        DeltaA_short = float('nan')
    
    # DeltaA_long = 2 * A_long(Sigma_a/2)
    Sig_half = Sigma / 2
    DeltaA_long = 2 * (Sig_half**2 - 0.225 * Sig_half**3)
    
    rows.append([Sigma, A_short, A_long, A_unbridged, DeltaA_short, DeltaA_long])

header = ['Sigma_a', 'A_short', 'A_long', 'A_unbridged', 'DeltaA_short', 'DeltaA_long']

with open('/app/outputs/crack_area_analytical.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerows(rows)
PYEOF
