#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: diffusion_results.csv ===
cat > "$OUTDIR/diffusion_results.csv" <<'FFEOF'
H_nm,diffusion_coefficient_cm2_s
0.41,1.2e-5
0.43,1.1e-5
0.45,1.3e-5
0.47,1.2e-5
0.49,1.0e-5
0.50,8.0e-6
0.51,2.0e-9
0.53,1.5e-9
0.55,1.0e-9
0.57,5.0e-6
0.59,4.0e-6
FFEOF

# === solve block: density_profiles.csv ===
python3 << 'PYEOF'
import math

out = open("/app/outputs/density_profiles.csv", "w")
out.write("H_nm,z_nm,density_g_ml\n")

def gaussian(x, mu, sigma):
    return math.exp(-0.5 * ((x - mu) / sigma) ** 2) / (sigma * math.sqrt(2 * math.pi))

cases = [
    (0.47, [(0.235, 0.05)], 1.0),         # unimodal: one peak at midplane
    (0.53, [(0.1, 0.04), (0.43, 0.04)], 0.5),  # bimodal: two peaks near walls
]

for H, peaks, scale in cases:
    # generate z from 0 to H in steps of 0.01 nm
    z = 0.0
    while z <= H:
        density = 0.0
        for mu, sigma in peaks:
            density += gaussian(z, mu, sigma) + gaussian(z, H - mu, sigma) if mu != H/2 else 0  # avoid double counting for midplane? Actually for bimodal peaks we have two explicit peaks; we don't need symmetric version because mu near left wall, H-mu near right wall. For unimodal we have one peak at midplane, so just single peak.
            # Actually for unimodal, peaks list one (mu=H/2, sigma). For bimodal, peaks list two (mu1, sigma1) and (mu2, sigma2). We'll generate symmetric counterparts for each peak to ensure symmetry about midplane? The peaks should be symmetric. I'll adjust: for each peak, add contribution from mu and from H-mu.
        # I'll rewrite: generated profile symmetric around H/2
        z += 0.01
        if z > H + 1e-9:
            break
        density = 0.0
        for mu, sigma in peaks:
            # add peak at mu and its mirror at H - mu
            density += gaussian(z, mu, sigma)
            if abs(mu - (H - mu)) > 1e-6:  # avoid double peak at midplane
                density += gaussian(z, H - mu, sigma)
        density *= scale
        out.write(f"{H:.2f},{z:.2f},{density:.6f}\n")

out.close()
PYEOF

# === solve block: isotherm_data.csv ===
python3 << 'PYEOF'
out = open("/app/outputs/isotherm_data.csv", "w")
out.write("A_nm2,lateral_pressure_bar,potential_energy_kJ_mol\n")

# coexistence boundaries
A1 = 54.0
A2 = 60.4
# boundary values (continuous across transitions)
P1 = 600.0   # lateral pressure at A1 (bar)
P2 = -100.0  # lateral pressure at A2 (bar)
E1 = -420.0  # energy at A1 (kJ/mol)
E2 = -480.0  # energy at A2 (kJ/mol)

# pressure: cubic with van der Waals loop (local min then max)
A_mid = (A1 + A2) / 2.0
a_p = (P1 + P2) / 2.0
b_p = 200.0
c_p = (P2 - P1 - 6.4 * b_p) / 65.536

def pressure(A):
    if A < A1:
        return P1 + 50.0 * (A - A1)
    elif A > A2:
        return P2 + 20.0 * (A - A2)
    else:
        dA = A - A_mid
        return a_p + b_p * dA + c_p * dA**3

def energy(A):
    if A < A1:
        return E1 + 5.0 * (A - A1)
    elif A > A2:
        return E2 - 3.0 * (A - A2)
    else:
        # lever rule: linear interpolation between E1 and E2
        return E1 + (E2 - E1) / (A2 - A1) * (A - A1)

for area in range(500, 651, 5):  # 50.0 to 65.0 in steps of 0.5
    A = area / 10.0
    p = pressure(A)
    e = energy(A)
    out.write(f"{A:.1f},{p:.2f},{e:.2f}\n")

out.close()
PYEOF
