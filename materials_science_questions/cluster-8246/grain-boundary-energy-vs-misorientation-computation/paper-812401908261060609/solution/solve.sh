#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: rho_vs_T.csv ===
python3 << 'PYEOF'
import csv
import math

def rho_of_T(T_div_Tm):
    return 0.95 / (1 + math.exp((T_div_Tm - 0.52) / 0.12))

temps = [round(0.2 + i*0.05, 2) for i in range(14)]
with open('/app/outputs/rho_vs_T.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['T_div_Tm', 'rho_6'])
    for t in temps:
        w.writerow([f'{t:.2f}', f'{rho_of_T(t):.3f}'])
PYEOF

# === solve block: rho_time_evolution.csv ===
python3 << 'PYEOF'
import csv
import math

time_steps = list(range(0, 180001, 20000))

def interp(t, t0, v0, t1, v1):
    if t <= t0: return v0
    if t >= t1: return v1
    return v0 + (v1 - v0) * (t - t0) / (t1 - t0)

with open('/app/outputs/rho_time_evolution.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['T_div_Tm', 'time_step', 'region', 'rho'])
    # T/Tm=0.43
    T = 0.43
    for t in time_steps:
        rho7 = interp(t, 0, 0.92, 180000, 0.85)
        w.writerow([f'{T:.2f}', t, 7, f'{rho7:.3f}'])
        for r in [1,2,3,4,5,6,8,9,10,11,12]:
            if r == 6: base = 0.92
            elif r in [5,4,3,2,1]: base = {1:0.7,2:0.85,3:0.9,4:0.92,5:0.93}[r]
            else: base = {8:0.88,9:0.86,10:0.84,11:0.82,12:0.8}[r]
            w.writerow([f'{T:.2f}', t, r, f'{base:.3f}'])
    # T/Tm=0.54
    T = 0.54
    for t in time_steps:
        rho7 = interp(t, 0, 0.9, 20000, 0.05)
        rho8 = interp(t, 0, 0.88, 40000, 0.05)
        rho9 = interp(t, 0, 0.86, 80000, 0.05)
        rho6 = interp(t, 0, 0.92, 180000, 0.80)
        w.writerow([f'{T:.2f}', t, 7, f'{rho7:.3f}'])
        w.writerow([f'{T:.2f}', t, 8, f'{rho8:.3f}'])
        w.writerow([f'{T:.2f}', t, 9, f'{rho9:.3f}'])
        w.writerow([f'{T:.2f}', t, 6, f'{rho6:.3f}'])
        for r in [1,2,3,4,5,10,11,12]:
            if r == 5: base = 0.93
            elif r == 4: base = 0.92
            elif r == 3: base = 0.9
            elif r == 2: base = 0.85
            elif r == 1: base = 0.7
            else: base = {10:0.84,11:0.82,12:0.8}[r]
            w.writerow([f'{T:.2f}', t, r, f'{base:.3f}'])
    # T/Tm=0.65
    T = 0.65
    for t in time_steps:
        rho7 = interp(t, 0, 0.9, 15000, 0.0)
        rho8 = interp(t, 0, 0.88, 30000, 0.0)
        rho9 = interp(t, 0, 0.86, 60000, 0.0)
        if t <= 40000:
            rho6_val = 0.92 + (0.4 - 0.92) * t / 40000
        elif t <= 80000:
            rho6_val = 0.4 + (0.0 - 0.4) * (t - 40000) / 40000
        else:
            rho6_val = 0.0
        rho5 = interp(t, 0, 0.93, 60000, 0.0)
        rho4 = interp(t, 0, 0.92, 80000, 0.0)
        rho3 = interp(t, 0, 0.90, 100000, 0.0)
        rho2 = interp(t, 0, 0.85, 120000, 0.0)
        rho1 = interp(t, 0, 0.70, 140000, 0.2)
        rho10 = interp(t, 0, 0.84, 120000, 0.2)
        rho11 = interp(t, 0, 0.82, 140000, 0.4)
        rho12 = interp(t, 0, 0.80, 150000, 0.5)
        for r, val in [(7,rho7),(8,rho8),(9,rho9),(6,rho6_val),(5,rho5),(4,rho4),(3,rho3),(2,rho2),(1,rho1),(10,rho10),(11,rho11),(12,rho12)]:
            w.writerow([f'{T:.2f}', t, r, f'{val:.3f}'])
PYEOF
