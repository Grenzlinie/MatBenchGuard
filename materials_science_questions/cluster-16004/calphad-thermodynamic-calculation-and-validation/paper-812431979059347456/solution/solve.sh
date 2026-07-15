#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: activation_parameters.csv ===
python3 << 'PYEOF'
import csv, math

k = 8.617333262145e-5
m = 25
G = 7.5e4
Gb3 = 7.24

data = [
    ("Ni", 0.0, 1.0, 2.79, 2.69e-3),
    ("Ni-5.6Cr", 5.6, 0.056, 3.44, 2.40e-3),
    ("Ni-22.0Cr", 22.0, 0.220, 4.29, 2.22e-3),
    ("Ni-39.9Cr", 39.9, 0.399, 4.70, 2.31e-3),
]

with open("/app/outputs/activation_parameters.csv", "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["composition","c_at_pct","tau_o_MPa","W_o_eV","n","U_meV"])
    for comp, c_at, c_frac, A, B in data:
        tau_o = math.exp(A)
        W_o = m * k / B
        n_cube = (W_o**2 / tau_o) * (4.0 * G / (Gb3**2))
        n = n_cube ** (1.0/3.0)
        U_eV = W_o**2 / (Gb3 * n**2 * math.sqrt(c_frac))
        U_meV = U_eV * 1000.0
        w.writerow([comp, c_at, round(tau_o,1), round(W_o,3), round(n,1), round(U_meV,1)])
PYEOF
