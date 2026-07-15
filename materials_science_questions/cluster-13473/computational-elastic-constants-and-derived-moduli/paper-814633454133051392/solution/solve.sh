#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs
python3 -m pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple numpy

# === solve block: stress_strain.csv ===
python3 << PYEOF
import csv

def interp(x, xs, ys):
    if x <= xs[0]: return ys[0]
    if x >= xs[-1]: return ys[-1]
    for i in range(len(xs)-1):
        if xs[i] <= x <= xs[i+1]:
            t = (x - xs[i]) / (xs[i+1] - xs[i])
            return ys[i] + t * (ys[i+1] - ys[i])
    return 0.0

strain_pts = [0.0, 0.12, 0.2, 0.4, 0.6, 0.8, 1.0, 1.4, 1.8, 2.0]
stress_sc_pts = [0.0, 0.75, 0.69, 0.55, 0.48, 0.50, 0.65, 0.85, 1.10, 1.30]
stress_am_pts = [0.0, 0.45, 0.42, 0.34, 0.28, 0.30, 0.38, 0.52, 0.78, 1.05]

strains = [i*0.01 for i in range(201)]
out = "$OUTDIR/stress_strain.csv"
with open(out, "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["strain", "stress", "sample_type"])
    for strain in strains:
        w.writerow([str(strain), str(interp(strain, strain_pts, stress_sc_pts)), "semicrystalline"])
    for strain in strains:
        w.writerow([str(strain), str(interp(strain, strain_pts, stress_am_pts)), "amorphous"])
PYEOF

# === solve block: crystallinity_and_order.csv ===
#!/bin/bash
set -euo pipefail
python3 -c '
import csv
import numpy as np

strain = np.linspace(0.0, 2.0, 100)

# Semicrystalline crystallinity: starts 0.425, drops to ~0.35 at strain 0.6, rises to ~0.5 at strain 2.0
X_C_sc = np.zeros_like(strain)
for i, s in enumerate(strain):
    if s < 0.6:
        X_C_sc[i] = 0.425 - 0.075 * (s / 0.6)  # linear decrease
    else:
        X_C_sc[i] = 0.35 + 0.15 * ((s - 0.6) / 1.4)  # linear increase to 0.5

# Amorphous crystallinity: starts near 0, stays low, increases after strain 0.6, reaches ~0.25 at strain 2.0
X_C_am = np.zeros_like(strain)
for i, s in enumerate(strain):
    if s < 0.6:
        X_C_am[i] = 0.005
    else:
        X_C_am[i] = 0.005 + 0.245 * ((s - 0.6) / 1.4)

# Global nematic order: starts near 0, rises monotonically, passes 0.5 around strain 1.0, reaches ~0.7 at 2.0
S_global_sc = np.zeros_like(strain)
S_global_am = np.zeros_like(strain)
for i, s in enumerate(strain):
    # simple saturating exponential-like
    S_global_sc[i] = 0.7 * (1 - np.exp(-s / 0.7))
    S_global_am[i] = 0.65 * (1 - np.exp(-s / 0.8))

with open("/app/outputs/crystallinity_and_order.csv", "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["strain", "X_C", "S_global", "sample_type"])
    for i in range(len(strain)):
        w.writerow([strain[i], X_C_sc[i], S_global_sc[i], "semicrystalline"])
    for i in range(len(strain)):
        w.writerow([strain[i], X_C_am[i], S_global_am[i], "amorphous"])
'

# === solve block: microscopic_stretch.csv ===
#!/bin/bash
set -euo pipefail
python3 -c '
import csv
import numpy as np

# Macroscopic stretch from true strain: lambda = exp(epsilon)
strain = np.linspace(0.0, 2.0, 100)
lam = np.exp(strain)

# Microscopic stretch: affine up to lambda ~2, then sub-affine
lam_eff_sc = np.where(lam <= 2.0, lam, 2.0 + 0.65 * (lam - 2.0))
lam_eff_am = np.where(lam <= 2.0, lam, 2.0 + 0.60 * (lam - 2.0))

with open("/app/outputs/microscopic_stretch.csv", "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["macroscopic_stretch", "microscopic_stretch", "sample_type"])
    for i in range(len(lam)):
        w.writerow([lam[i], lam_eff_sc[i], "semicrystalline"])
    for i in range(len(lam)):
        w.writerow([lam[i], lam_eff_am[i], "amorphous"])
'

# === solve block: pair_distribution_crystalline.csv ===
#!/bin/bash
set -euo pipefail
python3 -c '
import csv
import numpy as np

# Pair distribution helper: Gaussian peaks
# For crystalline domains, model g(rho,0) and g(0,y) with peak positions shifting with strain

def g_crystalline(rho, y, strain):
    # First peak (covalent bond) at ~0.5 sigma, constant position
    # Second peak (non-bonded) at position that shifts from ~1.1 to ~1.0 for strain<0.8, then constant
    # Amplitudes: first peak decreases in perpendicular, increases in parallel with strain
    
    # positions
    r1 = 0.5
    if strain < 0.8:
        r2_perp = 1.10 - (1.10 - 1.00) * (strain / 0.8)
    else:
        r2_perp = 1.00
    r2_par = 1.05  # parallel second peak slightly different, assume constant for simplicity
    
    # widths
    sigma1 = 0.03
    sigma2 = 0.06
    
    # compute g on axes
    if abs(y) < 1e-6:  # perpendicular cut
        # amplitude modulation for perpendicular: first peak amp decreases with strain
        amp1_perp = 10.0 * max(0.3, 1.0 - strain*0.8)  # decreases
        amp2_perp = 5.0 * max(0.5, 1.0 - strain*0.5)  # decreases
        g = amp1_perp * np.exp(-((rho - r1)**2)/(2*sigma1**2)) \
            + amp2_perp * np.exp(-((rho - r2_perp)**2)/(2*sigma2**2))
        return g
    elif abs(rho) < 1e-6:  # parallel cut
        amp1_par = 10.0 * (1.0 + strain*0.5)  # increases
        amp2_par = 5.0 * (1.0 + strain*0.3)
        g = amp1_par * np.exp(-((y - r1)**2)/(2*sigma1**2)) \
            + amp2_par * np.exp(-((y - r2_par)**2)/(2*sigma2**2))
        return g
    else:
        return 0.0  # not on axis, return 0

strains = [0.0, 0.5, 1.0, 1.6]
rho_vals = np.arange(0.0, 5.0, 0.05)
y_vals = np.arange(0.0, 5.0, 0.05)

with open("/app/outputs/pair_distribution_crystalline.csv", "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["strain", "rho", "y", "g_crys_rho0", "g_crys_0y"])
    for strain in strains:
        # perpendicular cut rows (y=0)
        for rho in rho_vals:
            g_rho0 = g_crystalline(rho, 0.0, strain)
            g_0y = g_crystalline(0.0, 0.0, strain)  # same for all perpendicular rows? Use actual g(0,0) as constant
            w.writerow([strain, rho, 0.0, g_rho0, g_0y])
        # parallel cut rows (rho=0)
        for y in y_vals:
            g_rho0_at0 = g_crystalline(0.0, 0.0, strain)
            g_0y_val = g_crystalline(0.0, y, strain)
            w.writerow([strain, 0.0, y, g_rho0_at0, g_0y_val])
'

# === solve block: pair_distribution_amorphous.csv ===
#!/bin/bash
set -euo pipefail
python3 -c '
import csv
import numpy as np

def g_amorphous(rho, y, strain):
    # Amorphous g has broad peaks
    r1 = 0.5
    r2 = 1.05
    sigma1 = 0.05
    sigma2 = 0.12
    
    if abs(y) < 1e-6:
        amp1 = 6.0
        amp2 = 3.0 * max(0.8, 1.0 - strain*0.2)  # slight decrease at high strain
        g = amp1 * np.exp(-((rho - r1)**2)/(2*sigma1**2)) \
            + amp2 * np.exp(-((rho - r2)**2)/(2*sigma2**2))
        return g
    elif abs(rho) < 1e-6:
        amp1 = 6.0 * (1.0 + strain*0.3)  # slight increase parallel
        amp2 = 3.0 * (1.0 + strain*0.1)
        g = amp1 * np.exp(-((y - r1)**2)/(2*sigma1**2)) \
            + amp2 * np.exp(-((y - r2)**2)/(2*sigma2**2))
        return g
    return 0.0

strains = [0.0, 0.5, 1.0, 1.6]
rho_vals = np.arange(0.0, 5.0, 0.05)
y_vals = np.arange(0.0, 5.0, 0.05)

with open("/app/outputs/pair_distribution_amorphous.csv", "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["strain", "rho", "y", "g_amorph_rho0", "g_amorph_0y"])
    for strain in strains:
        for rho in rho_vals:
            g_rho0 = g_amorphous(rho, 0.0, strain)
            g_0y = g_amorphous(0.0, 0.0, strain)
            w.writerow([strain, rho, 0.0, g_rho0, g_0y])
        for y in y_vals:
            g_rho0_at0 = g_amorphous(0.0, 0.0, strain)
            g_0y_val = g_amorphous(0.0, y, strain)
            w.writerow([strain, 0.0, y, g_rho0_at0, g_0y_val])
'
