#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
set -euo pipefail
python3 -m pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple numpy
OUTDIR=/app/outputs
mkdir -p $OUTDIR

# === solve block: bulk_band_edges.csv ===
python3 << 'PYEOF' > "$OUTDIR/bulk_band_edges.csv"
import numpy as np
import csv, sys

np.seterr(all='ignore')

C44_CdS = 1.49e10
rho_CdS = 4824.0
e15_CdS = -0.21
eps11_CdS = 7.99e-11

C44_ZnO = 4.25e10
rho_ZnO = 5676.0
e15_ZnO = -0.59
eps11_ZnO = 7.38e-11

Ct = np.sqrt(C44_CdS/rho_CdS)
D = 1.0
h = 0.25
hp = 0.25

def compute_T_and_cos(k, omega):
    alphaA2 = k**2 - rho_CdS * omega**2 / (C44_CdS * (1 + e15_CdS**2/(eps11_CdS*C44_CdS)))
    alphaB2 = k**2 - rho_ZnO * omega**2 / (C44_ZnO * (1 + e15_ZnO**2/(eps11_ZnO*C44_ZnO)))
    alphaA = np.sqrt(alphaA2 + 0j)
    alphaB = np.sqrt(alphaB2 + 0j)
    alphaA_s = alphaA + 1e-30j
    alphaB_s = alphaB + 1e-30j

    B_val = e15_CdS/eps11_CdS - e15_ZnO/eps11_ZnO
    C_val = k * (eps11_CdS * e15_ZnO - eps11_ZnO * e15_CdS) / (eps11_ZnO * alphaB_s * (C44_ZnO + e15_ZnO**2/eps11_ZnO))
    C_prime= k * (eps11_CdS * e15_ZnO - eps11_ZnO * e15_CdS) / (eps11_CdS * alphaA_s * (C44_CdS + e15_CdS**2/eps11_CdS))
    F = alphaA_s * (C44_CdS + e15_CdS**2/eps11_CdS) / (alphaB_s * (C44_ZnO + e15_ZnO**2/eps11_ZnO))
    FP = 1.0/F
    E = eps11_CdS / eps11_ZnO
    EP = 1.0/E

    S1 = np.sinh(k*h)
    C1 = np.cosh(k*h)
    S1p = np.sinh(k*hp)
    C1p = np.cosh(k*hp)
    Sc1 = np.sinh(2*k*h)
    Cc1 = np.cosh(2*k*h)
    Sc1p = np.sinh(2*k*hp)
    Cc1p = np.cosh(2*k*hp)

    S2 = np.sinh(alphaA*h)
    C2 = np.cosh(alphaA*h)
    S2p = np.sinh(alphaB*hp)
    C2p = np.cosh(alphaB*hp)
    Sc2 = np.sinh(2*alphaA*h)
    Cc2 = np.cosh(2*alphaA*h)
    Sc2p = np.sinh(2*alphaB*hp)
    Cc2p = np.cosh(2*alphaB*hp)

    T11 = Cc1*Cc1p + 0.5*(E+EP)*Sc1*Sc1p + 0.5*B_val*C_val*Sc1*Sc2p
    T12 = B_val*(Cc1p - Cc2p)*C1*C2 + B_val*(EP*C2*S1*Sc1p - F*C1*S2*Sc2p)
    T13 = -Sc1*Cc1p - (E*C1**2 + EP*S1**2)*Sc1p - B_val*C_val*C1**2*Sc2p
    T14 = B_val*(Cc2p - Cc1p)*C1*S2 - B_val*EP*Sc1p*S1*S2 + B_val*F*C1*C2*Sc2p

    T21 = C_prime*C1*S2*Sc1p - C_val*S1*C2*Sc2p + (E*C_prime*Cc1p - C_val*FP*Cc2p)*S1*S2
    T22 = Cc2*Cc2p + 0.5*(F+FP)*Sc2*Sc2p + 0.5*B_val*C_prime*Sc1p*Sc2
    T23 = C_val*C1*C2*Sc2p - C_prime*S1*S2*Sc1p + (C_val*FP*Cc2p - C_prime*E*Cc1p)*C1*S2
    T24 = -Cc2p*Sc2 - (FP*S2**2 + F*C2**2)*Sc2p - B_val*C_prime*Sc1p*S2**2

    T31 = -Cc1p*Sc1 - B_val*C_val*Sc2p*S1**2 - (EP*C1**2 + E*S1**2)*Sc1p
    T32 = B_val*(Cc2p - Cc1p)*S1*C2 - B_val*EP*C1*C2*Sc1p + B_val*F*S1*S2*Sc2p
    T33 = T11
    T34 = B_val*(Cc1p - Cc2p)*S1*S2 + B_val*(EP*C1*S2*Sc1p - F*S1*C2*Sc2p)

    T41 = C_val*S1*S2*Sc2p - C_prime*C1*C2*Sc1p + (C_val*FP*Cc2p - C_prime*E*Cc1p)*C2*S1
    T42 = -Cc2p*Sc2 - B_val*C_prime*Sc1p*C2**2 - (FP*C2**2 + F*S2**2)*Sc2p
    T43 = C_prime*S1*C2*Sc1p - C_val*C1*S2*Sc2p + (E*C_prime*Cc1p - C_val*FP*Cc2p)*C1*C2
    T44 = T22

    T = np.array([[T11, T12, T13, T14],
                  [T21, T22, T23, T24],
                  [T31, T32, T33, T34],
                  [T41, T42, T43, T44]], dtype=complex)
    Tinv = np.linalg.inv(T)
    M = 0.5*(T + Tinv)
    M11 = M[0,0].real
    M12 = M[0,1].real
    M21 = M[1,0].real
    M22 = M[1,1].real
    b = M11 + M22
    c = M11*M22 - M12*M21
    disc = b*b - 4*c
    if disc < -1e-12:
        return None
    disc = max(disc, 0.0)
    sqrt_disc = np.sqrt(disc)
    cos1 = 0.5*(b + sqrt_disc)
    cos2 = 0.5*(b - sqrt_disc)
    return cos1, cos2

def propagate(k, omega):
    res = compute_T_and_cos(k, omega)
    if res is None:
        return False
    c1, c2 = res
    return abs(c1) <= 1+1e-12 or abs(c2) <= 1+1e-12

kD_vals = np.linspace(0, np.pi, 101)
Omega_scan = np.linspace(0, 1.5, 1500)
writer = csv.writer(sys.stdout)
writer.writerow(["k_parallel_D", "band1_lower", "band1_upper", "band2_lower", "band2_upper"])

for kD in kD_vals:
    if kD == 0.0:
        k = 1e-8
    else:
        k = kD
    omega_vals = Omega_scan * 2 * np.pi * Ct / D
    prop = np.array([propagate(k, w) for w in omega_vals], dtype=bool)
    intervals = []
    in_band = False
    start_ome = 0.0
    for i, p in enumerate(prop):
        if p and not in_band:
            in_band = True
            start_ome = Omega_scan[i]
        elif not p and in_band:
            in_band = False
            intervals.append((start_ome, Omega_scan[i-1]))
    if in_band:
        intervals.append((start_ome, Omega_scan[-1]))
    if len(intervals) >= 1:
        b1_l, b1_u = intervals[0]
    else:
        b1_l = b1_u = 0.0
    if len(intervals) >= 2:
        b2_l, b2_u = intervals[1]
    else:
        b2_l = b2_u = 0.0
    writer.writerow([kD, b1_l, b1_u, b2_l, b2_u])
PYEOF

# === solve block: surface_phase_velocities.csv ===
python3 /solution/compute.py surface

# === solve block: effective_constants.json ===
python3 /solution/compute.py effective
