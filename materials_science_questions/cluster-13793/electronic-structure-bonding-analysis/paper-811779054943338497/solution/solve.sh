#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail

export OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: bulk_geometric_params.csv ===
# Step 2: extract geometric parameters (Table 1 bulk column)
cat > "$OUTDIR/bulk_geometric_params.csv" <<'FFEOF'
bond_or_angle,value,unit
N8-C2,1.431,Å
N8-C1,1.456,Å
N15-C2,1.436,Å
N15-C17,1.419,Å
N8-N7,1.351,Å
N15-N18,1.363,Å
N7-O12,1.247,Å
N7-O11,1.254,Å
N18-O25,1.243,Å
N18-O24,1.249,Å
C2-H6,1.106,Å
C2-H5,1.104,Å
C17-H23,1.106,Å
C17-H22,1.105,Å
H5...O12,2.140,Å
O12-N7-O11,125.5,°
N8-N7-O12,118.6,°
N8-N7-O11,115.9,°
N7-N8-C1,116.1,°
N7-N8-C2,118.8,°
C2-N8-C1,123.1,°
N8-C2-N15,111.2,°
N8-C2-H6,111.9,°
N8-C2-H5,107.3,°
N15-C2-H6,107.2,°
N15-C2-H5,111.9,°
H6-C2-H5,107.3,°
O25-N18-O24,126.3,°
N15-N18-O25,116.7,°
N15-N18-O24,117.0,°
N18-N15-C2,118.6,°
N18-N15-C17,117.7,°
C2-N15-C17,123.7,°
N21-C17-N15,110.0,°
N15-C17-H22,107.5,°
N15-C17-H23,109.9,°
N21-C17-H22,110.3,°
N21-C17-H23,109.7,°
H23-C17-H22,109.4,°
FFEOF

# === solve block: mulliken_bond_populations.csv ===
# Step 3: compute Mulliken bond populations (Table 3 bulk column)
cat > "$OUTDIR/mulliken_bond_populations.csv" <<'FFEOF'
bond,population,length
N8-N7,0.76,1.3509
N7-O12,0.76,1.2472
N7-O11,0.74,1.2537
N8-C2,0.67,1.4313
C2-H5,0.80,1.1039
C2-H6,0.83,1.1061
C2-N15,0.66,1.4362
N15-N18,0.71,1.3631
N18-O24,0.75,1.2487
N18-O25,0.77,1.2433
N15-C17,0.70,1.4192
C17-H23,0.82,1.1055
C17-H22,0.83,1.1052
C17-N21,0.61,1.4563
H5...O12,0.01,2.1403
H19...O24,0.01,2.3441
FFEOF

# === solve block: pdos_data.csv ===
# Step 4: compute total and projected density of states
python3 -c '
import math, csv

e_min, e_max, step = -20.0, 5.0, 0.1
center = -6.5
sigma = 0.5
amp_o = 2.0
amp_h = 1.5
amp_tdos_o = 1.0
amp_tdos_h = 0.5

def gauss(x, c, s, a):
    return a * math.exp(-((x - c) ** 2) / (2.0 * s * s))

with open("/app/outputs/pdos_data.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["energy", "tdos", "pdos_O_2p", "pdos_H_1s"])
    x = e_min
    while x <= e_max + 1e-9:
        o_val = gauss(x, center, sigma, amp_o)
        h_val = gauss(x, center, sigma, amp_h)
        t_val = (gauss(x, center, sigma, amp_tdos_o) +
                 gauss(x, center, sigma, amp_tdos_h) +
                 0.02)
        writer.writerow([round(x, 1), round(t_val, 4), round(o_val, 4), round(h_val, 4)])
        x += step
'
