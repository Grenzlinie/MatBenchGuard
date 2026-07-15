#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: high_temp_P2.csv ===
python3 -c "
import math, csv
gamma=1.0; m1=1.0; m2=4.0; hbar=1.0; kB=1.0; T=1.0
w1sq = 2*gamma/m1
w2sq = 2*gamma/m2
rows=[]
for r in range(1,21):
    if r%2==1:
        if r==1:
            p2 = w1sq/(24*m1)
        else:
            p2 = w1sq/(12*m1)
    else:
        if r==20:
            p2 = w2sq/(24*m2)
        else:
            p2 = w2sq/(12*m2)
    rows.append([r, p2])
with open('/app/outputs/high_temp_P2.csv','w',newline='') as f:
    w=csv.writer(f)
    w.writerow(['atom_index','P2_value'])
    w.writerows(rows)
"

# === solve block: low_temp_msv.csv ===
python3 -c "
import math, csv
N=20; m=1.0; gamma=1.0; hbar=1.0
omega_L = math.sqrt(4*gamma/m)
factor = hbar * omega_L / (16 * N * m)
pi = math.pi
d = pi/(8*N)
rows=[]
for r in range(1, N+1):
    arg1 = (4*r-1)*d
    arg2 = (4*r-3)*d
    cot1 = math.cos(arg1)/math.sin(arg1)
    cot2 = math.cos(arg2)/math.sin(arg2)
    cotd = math.cos(d)/math.sin(d)
    term = cot1 - cot2 + 2*cotd
    msv = factor * term
    rows.append([r, msv])
with open('/app/outputs/low_temp_msv.csv','w',newline='') as f:
    w=csv.writer(f)
    w.writerow(['atom_index','mean_square_velocity'])
    w.writerows(rows)
"
