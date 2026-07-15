#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: B_coefficient.csv ===
python3 <<PYEOF
import csv, json, math

k_B = 1.380649e-16
B0 = 1.5e12
n_val = 2.4e22
gamma = 2e-13
eps = -5e-10
Tc0 = 121.0
muB = 9.274e-21
GPa_to_erg = 1e10

def Tc(P_erg):
    return Tc0 - (gamma / (2 * k_B * B0)) * P_erg + (eps / (12 * k_B * B0 * B0)) * P_erg * P_erg

def B_coeff(T, P_erg):
    Tc_p = Tc(P_erg)
    gs = gamma - eps * P_erg / (3 * B0)
    return (Tc_p / T) ** 3 / 3.0 - n_val / (8 * k_B * T * B0) * gs * gs

def C_coeff(T, P_erg):
    Tc_p = Tc(P_erg)
    gs = gamma - eps * P_erg / (3 * B0)
    gs2 = gs * gs
    t1 = (1.0 / 8.0) * (n_val / (k_B * T * B0)) * ((Tc_p / T) ** 2) * gs2
    t2 = (1.0 / 64.0) * (n_val * n_val * eps) / (k_B * T * B0 * B0) * gs2
    t3 = (2.0 / 15.0) * ((Tc_p / T) ** 5)
    return t1 - t2 - t3

# --- B_coefficient.csv ---
with open("/app/outputs/B_coefficient.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["pressure_GPa", "B_value"])
    for P_GPa in [0.0, 0.5, 1.0, 1.5]:
        P_erg = P_GPa * GPa_to_erg
        T = Tc(P_erg)
        writer.writerow([P_GPa, B_coeff(T, P_erg)])

# --- tricritical_point.json ---
def f_tric(P_GPa):
    P_erg = P_GPa * GPa_to_erg
    return B_coeff(Tc(P_erg), P_erg)

lo, hi = 0.0, 10.0
f_lo = f_tric(lo)
for _ in range(60):
    mid = (lo + hi) / 2.0
    f_mid = f_tric(mid)
    if abs(f_mid) < 1e-14:
        lo = hi = mid
        break
    if f_lo * f_mid <= 0:
        hi = mid
    else:
        lo = mid
        f_lo = f_mid
P_t = (lo + hi) / 2.0
T_t = Tc(P_t * GPa_to_erg)
with open("/app/outputs/tricritical_point.json", "w") as f:
    json.dump({"P_t_GPa": round(P_t, 6), "T_t_K": round(T_t, 4)}, f)

# --- wing_critical_point.json ---
P_target = 1.4
P_erg = P_target * GPa_to_erg
Tc_P = Tc(P_erg)
def wing_f(T):
    A = (T - Tc_P) / T
    B = B_coeff(T, P_erg)
    C = C_coeff(T, P_erg)
    return A - (9.0 / 20.0) * B * B / C

T_lo = Tc_P
T_hi = Tc_P + 20.0
f_lo = wing_f(T_lo)
f_hi = wing_f(T_hi)
while f_lo * f_hi > 0:
    T_hi += 10.0
    f_hi = wing_f(T_hi)
for _ in range(80):
    mid = (T_lo + T_hi) / 2.0
    f_mid = wing_f(mid)
    if abs(f_mid) < 1e-14:
        T_lo = T_hi = mid
        break
    if f_lo * f_mid <= 0:
        T_hi = mid
    else:
        T_lo = mid
        f_lo = f_mid
T_cr = (T_lo + T_hi) / 2.0
B_cr = B_coeff(T_cr, P_erg)
C_cr = C_coeff(T_cr, P_erg)
m_cr = math.sqrt(-3.0 / 10.0 * B_cr / C_cr)
h_cr = (6.0 / 25.0) * (B_cr * B_cr / C_cr) * m_cr
H_cr_G = h_cr * k_B * T_cr / muB   # Gauss
H_cr_T = H_cr_G / 1e4
with open("/app/outputs/wing_critical_point.json", "w") as f:
    json.dump({"pressure_GPa": P_target, "T_cr_K": round(T_cr, 4), "H_cr_T": round(H_cr_T, 4), "m_cr": round(m_cr, 4)}, f)

PYEOF
exit 0

# === solve block: tricritical_point.json ===
python3 -c '
import json

k_B = 1.380649e-16
B0 = 1.5e12
n_val = 2.4e22
gamma = 2e-13
eps = -5e-10
Tc0 = 121.0
GPa_to_erg = 1e10

def Tc(P_erg):
    t1 = -(gamma / (2 * k_B * B0)) * P_erg
    t2 = (eps / (12 * k_B * B0 * B0)) * P_erg * P_erg
    return Tc0 + t1 + t2

def B_at_Tc(P_GPa):
    P_erg = P_GPa * GPa_to_erg
    Tc_ = Tc(P_erg)
    gs = gamma - eps * P_erg / (3 * B0)
    return 1.0 / 3.0 - (n_val / (8 * k_B * Tc_ * B0)) * gs * gs

lo, hi = 0.0, 10.0
flo = B_at_Tc(lo)
for _ in range(60):
    mid = (lo + hi) / 2.0
    fmid = B_at_Tc(mid)
    if abs(fmid) < 1e-14:
        lo = hi = mid
        break
    if flo * fmid <= 0:
        hi = mid
    else:
        lo = mid
        flo = fmid

P_t = round((lo + hi) / 2.0, 6)
T_t = round(Tc(P_t * GPa_to_erg), 4)
with open("/app/outputs/tricritical_point.json", "w") as f:
    json.dump({"P_t_GPa": P_t, "T_t_K": T_t}, f)
'

# === solve block: wing_critical_point.json ===
python3 /solution/calc.py wing /app/outputs/wing_critical_point.json
