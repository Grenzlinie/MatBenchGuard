#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: froehlich_frequencies.csv ===
python3 <<'EOF' > "$OUTDIR/froehlich_frequencies.csv"
import csv, sys, math

OMEGA_TO_PAR  = 783.0
OMEGA_LO_PAR  = 964.0
OMEGA_TO_PERP = 798.0
OMEGA_LO_PERP = 966.4
EPS_INF_PAR   = 6.52
EPS_INF_PERP   = 6.72
F = 0.12

def compute_primed(L_dir, omega_TO, omega_LO, eps_inf):
    if L_dir == 1.0:
        omega_LO_prime = omega_TO
        D = -(1-F)/F
        if eps_inf != D:
            omega_TO_prime = math.sqrt(max(0, (eps_inf * omega_LO**2 - D * omega_TO**2) / (eps_inf - D)))
        else:
            omega_TO_prime = float('nan')
        return omega_TO_prime, omega_LO_prime
    else:
        C = (-F/(1-F) - L_dir) / (1 - L_dir)
        D = -(1-F)*L_dir / (F + (1-F)*(1-L_dir))
        w2_LO = (eps_inf * omega_LO**2 - C * omega_TO**2) / (eps_inf - C)
        w2_TO = (eps_inf * omega_LO**2 - D * omega_TO**2) / (eps_inf - D)
        return math.sqrt(max(0, w2_TO)), math.sqrt(max(0, w2_LO))

writer = csv.writer(sys.stdout)
writer.writerow(["L_parallel", "omega_T_parallel", "omega_L_parallel", "omega_T_perpendicular", "omega_L_perpendicular"])

for i in range(11):
    L_par = i / 10.0
    omega_T_par, omega_L_par = compute_primed(L_par, OMEGA_TO_PAR, OMEGA_LO_PAR, EPS_INF_PAR)
    L_perp = (1 - L_par) / 2.0
    omega_T_perp, omega_L_perp = compute_primed(L_perp, OMEGA_TO_PERP, OMEGA_LO_PERP, EPS_INF_PERP)
    writer.writerow([L_par, round(omega_T_par, 6), round(omega_L_par, 6), round(omega_T_perp, 6), round(omega_L_perp, 6)])
EOF
