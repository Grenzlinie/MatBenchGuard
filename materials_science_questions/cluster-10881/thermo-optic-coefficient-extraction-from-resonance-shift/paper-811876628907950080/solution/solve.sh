#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: thermo_optic_data_532nm.csv ===
python3 - "$OUTDIR/thermo_optic_data_532nm.csv" << 'PYEOF'
import csv, math, sys

# ---------- constants ----------
E1_eV = 15.759
E2_eV = 27.629
kB_eV = 8.617333262145e-5
kB_J = 1.380649e-23
h_J = 6.62607015e-34
me_kg = 9.10938356e-31
P_pa = 101325.0

# Loschmidt constant and precomputed factors for 532 nm
factor_atom = 1.05959e-23
factor_e    = -1.2623e-22

# ---------- partition functions ----------
def Z1_T(T):
    # Ar+  ^2P_3/2 (4) + ^2P_1/2 (2)  at 0.1776 eV
    return 4.0 + 2.0 * math.exp(-0.1776 / (kB_eV * T))

def Z2_T(T):
    # Ar++ ground ^3P_2(5), ^3P_1(3) 0.138 eV, ^3P_0(1) 0.195 eV, ^1D(5) 2.5 eV
    return (5.0
            + 3.0 * math.exp(-0.138  / (kB_eV * T))
            + 1.0 * math.exp(-0.195  / (kB_eV * T))
            + 5.0 * math.exp(-2.5    / (kB_eV * T)))

# ---------- C factor in cm^-3 K^-3/2 ----------
C_SI = 2.0 * (2*math.pi*me_kg*kB_J / h_J**2) ** 1.5
C_cm = C_SI * 1e-6

# ---------- cubic root via binary search ----------
def solve_Ne(T):
    Nt_cm = P_pa / (kB_J * T) * 1e-6          # cm^-3
    Z1 = Z1_T(T)
    Z2 = Z2_T(T)
    K1 = C_cm * (Z1/1.0) * (T**1.5) * math.exp(-E1_eV/(kB_eV*T))
    K2 = C_cm * (Z2/Z1)  * (T**1.5) * math.exp(-E2_eV/(kB_eV*T))
    a = 1.0
    b = 2.0 * K1
    c = 3.0*K1*K2 - K1*Nt_cm
    d = -2.0*K1*K2*Nt_cm
    lo, hi = 0.0, Nt_cm
    f_lo = d
    if f_lo == 0:
        return 0.0, K1, K2, Nt_cm
    for _ in range(60):
        mid = (lo + hi) * 0.5
        f_mid = ((mid + b)*mid + c)*mid + d
        if f_mid == 0.0 or (hi - lo) < 1e-12 * Nt_cm:
            break
        if math.copysign(1, f_mid) == math.copysign(1, f_lo):
            lo = mid
            f_lo = f_mid
        else:
            hi = mid
    return mid, K1, K2, Nt_cm

# ---------- compute n-1 and dn/dT ----------
def compute_row(T):
    Ne, K1, K2, Nt = solve_Ne(T)
    if Ne == 0.0:
        N1 = N2 = Ni = Na = 0.0
    else:
        denom = Ne + 2.0*K2
        N1 = (Ne*Ne) / denom if denom > 0 else 0.0
        N2 = K2 * N1 / Ne
        Ni = N1 + N2
        Na = N1 * Ne / K1 if K1 > 0 else 0.0
    n1 = factor_atom * (Na + 0.67*Ni) + factor_e * Ne
    return n1

# ---------- main ----------
outfile = sys.argv[1]
temps = list(range(5000, 20501, 500))
delta_T = 200.0

with open(outfile, 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['T', 'N_e', 'n-1', 'dn/dT', 'e'])
    for T in temps:
        Ne, _, _, _ = solve_Ne(T)
        n0 = compute_row(T)
        # finite-difference derivative
        Tup = T + delta_T
        Tdn = max(T - delta_T, 100.0)
        n_up = compute_row(Tup)
        n_dn = compute_row(Tdn)
        if T - delta_T < 100.0:
            dndT = (n_up - n0) / delta_T
        else:
            dndT = (n_up - n_dn) / (2*delta_T)
        denom = abs(dndT) * T
        e = 1e-5 / denom if denom > 1e-30 else 1e10
        w.writerow([T, Ne, n0, dndT, e])
PYEOF

# === solve block: error_intervals_532nm.csv ===
python3 /solution/gen_data.py --output /app/outputs/error_intervals_532nm.csv --mode 532_intervals

# === solve block: thermo_optic_data_808nm.csv ===
python3 /solution/gen_data.py --output /app/outputs/thermo_optic_data_808nm.csv --mode 808_data

# === solve block: error_intervals_808nm.csv ===
python3 /solution/gen_data.py --output /app/outputs/error_intervals_808nm.csv --mode 808_intervals
