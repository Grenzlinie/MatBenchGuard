#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: ni_tau_c_vs_L.csv ===
python3 -c '
import csv, math
a=0.35e-9; b=0.14e-9; gamma_m=0.17; gamma_0=0.12; gamma_s=0.12; lam=0.6; G=76e9
W_A = G/65.0
p = a / math.sqrt(3)
C = (p*W_A - lam*gamma_0) / b
tau_base = lam*math.pi*gamma_m/b + C
sqrt2 = math.sqrt(2)
Lprime = [5,10,15,20,25]
with open("/app/outputs/ni_tau_c_vs_L.csv","w",newline="") as f:
    w = csv.writer(f)
    w.writerow(["L_nm","tau_c_GPa"])
    for Lp in Lprime:
        L_m = Lp * sqrt2 * 1e-9
        tau = tau_base + gamma_s / L_m
        w.writerow([Lp, f"{tau*1e-9:.6f}"])
'

# === solve block: si_tau_c_vs_L.csv ===
python3 -c '
import csv, math
a=0.54e-9; b=0.22e-9; gamma_m=1.67; gamma_0=0.075; gamma_s=1.5; lam=0.1; W_A=8.13e8; W_cr_glass=0.23; n=5
p = a / math.sqrt(3)
C = ( ((n-2)/n)*(p*W_A - lam*gamma_0) + (2.0/n)*W_cr_glass ) / b
tau_base = lam*math.pi*gamma_m/b + C
sqrt2 = math.sqrt(2)
Lprime = [5,10,15,20,25]
with open("/app/outputs/si_tau_c_vs_L.csv","w",newline="") as f:
    w = csv.writer(f)
    w.writerow(["L_nm","tau_c_GPa"])
    for Lp in Lprime:
        L_m = Lp * sqrt2 * 1e-9
        tau = tau_base + gamma_s / L_m
        w.writerow([Lp, f"{tau*1e-9:.6f}"])
'
