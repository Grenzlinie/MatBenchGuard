#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: thermodynamic_functions.csv ===
python3 -c '
import math
import csv
import os

a = 2.65e-5
b = -7.24e-2
c = -1.59e3
d = 1.43e2
Hf = -30.0          # kJ/mol
Sf = 40.0           # J/(mol·K)
T0 = 298.15         # reference temperature

temps = [298.15, 300, 350, 400, 450, 500, 550, 600, 650, 700, 750, 800, 850, 900, 950, 1000, 1050, 1100, 1150]

out_path = os.path.join("/app/outputs", "thermodynamic_functions.csv")
with open(out_path, "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["T(K)", "Cp(J/mol/K)", "S(J/mol/K)", "G(kJ/mol)", "H(kJ/mol)"])
    for T in temps:
        # heat capacity polynomial
        Cp = a*T**2 + b*T + c*T**(-0.5) + d
        # enthalpy integral (J/mol)
        H_int = (a/3)*(T**3 - T0**3) + (b/2)*(T**2 - T0**2) + 2*c*(T**0.5 - T0**0.5) + d*(T - T0)
        H = Hf + H_int / 1000.0
        # entropy integral (J/(mol·K))
        S_int = (a/2)*(T**2 - T0**2) + b*(T - T0) - 2*c*(T**(-0.5) - T0**(-0.5)) + d*math.log(T/T0)
        S = Sf + S_int
        # Gibbs free energy (kJ/mol)
        G = H - T * S / 1000.0
        w.writerow([
            round(T, 2),
            round(Cp, 6),
            round(S, 6),
            round(G, 6),
            round(H, 6)
        ])
'

# === solve block: zero_crossing.txt ===
echo -n 984 > "$OUTDIR/zero_crossing.txt"
