#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: critical_plane_predictions.csv ===
python3 << 'PYEOF' > "$OUTDIR/critical_plane_predictions.csv"
import sys, math, csv

sigma_I_f = 980.0
sigma_II_f = 48.0
tau_II_f = 70.0

def r1(zeta, lam):
    disc = math.sqrt((1-zeta)**2 + 4*lam*lam)
    numer = (1+zeta) + disc
    denom = (1+zeta) - disc
    if abs(denom) < 1e-12:
        return float('inf')
    return numer/denom

def I_max_tensile(zeta, lam, R22, sigma22_max=1.0):
    sigma22_min = R22 * sigma22_max
    A = (zeta+1)/2.0 + math.sqrt(((zeta-1)/2.0)**2 + lam*lam)
    if R22 < 1:
        r1v = r1(zeta, lam)
        if r1v <= R22:
            val = A * sigma22_max           # Eq. 8a
            sigma22_used = sigma22_max
        else:  # R22 < r1
            if zeta > lam*lam:
                val = A * sigma22_max        # Eq. 8b
                sigma22_used = sigma22_max
            else:
                val = A * sigma22_min        # Eq. 8c
                sigma22_used = sigma22_min
    elif R22 > 1:
        if zeta > lam*lam:
            return 0.0, None                # Eq. 8e
        else:
            B = (zeta+1)/2.0 - math.sqrt(((zeta-1)/2.0)**2 + lam*lam)
            val = B * sigma22_min            # Eq. 8d
            sigma22_used = sigma22_min
    else:  # R22 == 1 (no variation)
        if zeta > lam*lam:
            return 0.0, None
        else:
            val = A * sigma22_max
            sigma22_used = sigma22_max
    # only tensile contribution counts
    if val < 0:
        return 0.0, None
    return val, sigma22_used

def II_max_eff(lam, R22, sigma22_max=1.0):
    sigma22_min = R22 * sigma22_max
    lam2 = lam*lam
    # Condition λ² < 1−2(τ_II^f/σ_II^f)² is never true because 1−2(70/48)² ≈ −3.25
    # Therefore cases 14a, 14i, 14j never apply and are omitted.
    if 0 <= R22 < 1:                                  # Eq. 14b
        gamma = math.pi/2
        max_eff = math.sqrt(tau_II_f**2 + lam2*sigma_II_f**2) / (sigma_II_f * tau_II_f) * sigma22_max
        return max_eff, gamma
    elif R22 > 1:
        if lam2 < 1:                                  # Eq. 14c
            gamma = 0.5 * math.acos(-lam2)
            max_eff = - (lam2+1) / (2 * tau_II_f) * sigma22_min
        else:                                         # Eq. 14d
            gamma = math.pi/2
            max_eff = abs(lam * sigma22_min) / tau_II_f
        return max_eff, gamma
    else:  # R22 < 0
        if lam2 >= 1:
            T1 = -math.sqrt(1 + tau_II_f**2 / (lam2 * sigma_II_f**2))
            if R22 >= T1:                             # Eq. 14e
                gamma = math.pi/2
                max_eff = math.sqrt(tau_II_f**2 + lam2*sigma_II_f**2) / (sigma_II_f * tau_II_f) * sigma22_max
            else:                                     # Eq. 14f
                gamma = math.pi/2
                max_eff = abs(lam * sigma22_min) / tau_II_f
        else:  # lam2 < 1
            T2 = - (2 * math.sqrt(tau_II_f**2 + lam2*sigma_II_f**2)) / ((1+lam2) * sigma_II_f)
            if R22 > T2:                              # Eq. 14g
                gamma = math.pi/2
                max_eff = math.sqrt(tau_II_f**2 + lam2*sigma_II_f**2) / (sigma_II_f * tau_II_f) * sigma22_max
            else:                                     # Eq. 14h
                gamma = 0.5 * math.acos(-lam2)
                max_eff = abs(sigma22_min) / (2 * tau_II_f) * (1+lam2)
        return max_eff, gamma

def I_beta(zeta, lam, sigma22_used):
    if sigma22_used is None:
        return 0.0
    s12 = lam * sigma22_used
    if s12 > 0:
        beta = 3*math.pi/4 - 0.5*math.atan2((zeta-1), (2*lam))
    elif s12 < 0:
        beta = math.pi/4 - 0.5*math.atan2((zeta-1), (2*lam))
    else:  # s12 == 0
        if zeta > 1:
            beta = math.pi/2
        else:
            beta = 0.0
    return beta

conditions = [
    (0.5, '+', -1.4, 3.0),
    (0.5, '-', 0.5, -0.5),
    (1.0, '+', -2.8, 9.2),
    (1.0, '-', 0.4, -1.3),
    (2.0, '+', 5.2, -25.0),
    (2.0, '-', 0.2, -2.2),
]

idx = 1
rows = []
for lglob, ply, lam, zeta in conditions:
    for Rval in [0, -1]:
        # condition IDs without zero‑padding ("cond_1", "cond_2", …)
        cid = f"cond_{idx}"
        idx += 1
        ieq_tens, sigma22_used = I_max_tensile(zeta, lam, Rval)
        ieq = ieq_tens / sigma_I_f
        iieq, gamma_ii = II_max_eff(lam, Rval)
        if ieq > iieq:
            ctype = 'I'
            beta_c = I_beta(zeta, lam, sigma22_used)
            gamma_c = math.pi/2
        else:
            ctype = 'II'
            beta_c = 0.0
            gamma_c = gamma_ii
        rows.append([cid, ctype, beta_c, gamma_c, ieq, iieq])

writer = csv.writer(sys.stdout)
writer.writerow(['condition_id', 'critical_plane_type', 'beta_c', 'gamma_c', 'max_sigma_I_eq', 'max_sigma_II_eq'])
writer.writerows(rows)
PYEOF
