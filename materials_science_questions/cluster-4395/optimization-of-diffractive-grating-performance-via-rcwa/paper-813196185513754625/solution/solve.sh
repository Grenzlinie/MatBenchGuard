#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs
python3 /solution/generate.py /app/outputs

# === solve block: step_01_simulated_spectra.csv ===
python3 -m pip install -q numpy
python3 - <<'EOF'
import numpy as np
import cmath
import csv, json, os

outdir = os.environ.get("OUTDIR", "/app/outputs")
os.makedirs(outdir, exist_ok=True)

# Physical constants
c = 299792458.0
# Ag Drude parameters
eps_inf = 5.0
wp = 1.38e16
gamma0 = 5.07e13
gamma = 6.4 * gamma0
# Ge refractive index (real only, assumed constant in NIR)
n_Ge = 4.0
eps_Ge = n_Ge**2

# Layer thicknesses
d_Ag = 15e-9
d_Ge = 85e-9
d_cap = 42.5e-9
t_total = 2*d_cap + 5*(d_Ag + d_Ge)  # 585 nm

# Wavelength range
wavelengths_um = np.linspace(1.4, 1.9, 200)

# ---------- Step 1: Simulation ----------
layers = [("Ge", d_cap)]  # top cap
for _ in range(5):
    layers.append(("Ag", d_Ag))
    layers.append(("Ge", d_Ge))
layers.append(("Ge", d_cap))   # bottom cap

rows_T_R = []
eps_Ag_list = []  # store complex eps for later nonlocal calc
for lam_um in wavelengths_um:
    lam = lam_um * 1e-6
    k0 = 2*np.pi / lam
    omega = 2*np.pi*c / lam
    eps_Ag = eps_inf - wp**2 / (omega**2 - 1j*omega*gamma)
    eps_Ag_list.append(eps_Ag)
    
    M = np.identity(2, dtype=complex)
    for mat, d in layers:
        if mat == "Ag":
            n = cmath.sqrt(eps_Ag)
        else:
            n = cmath.sqrt(eps_Ge)
        delta = k0 * n * d
        # TMM matrix for normal incidence (TE/TM identical)
        M_layer = np.array([
            [cmath.cos(delta), 1j*cmath.sin(delta)/n],
            [1j*n*cmath.sin(delta), cmath.cos(delta)]
        ])
        M = M_layer @ M
    
    denom = M[0,0] + M[0,1] + M[1,0] + M[1,1]
    r = (M[0,0] + M[0,1] - M[1,0] - M[1,1]) / denom
    t = 2.0 / denom
    R = abs(r)**2
    T = abs(t)**2
    rows_T_R.append((lam_um, T, R))

# Write step_01
with open(os.path.join(outdir, 'step_01_simulated_spectra.csv'), 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['wavelength_micron', 'transmission', 'reflection'])
    writer.writerows(rows_T_R)

# ---------- Step 2: Inversion ----------
rows_nk = []
for lam_um, T, R in zip(wavelengths_um, [r[1] for r in rows_T_R], [r[2] for r in rows_T_R]):
    lam = lam_um * 1e-6
    # Avoid log(0) etc.
    X_num = (T**2 - (1-R)**2) + np.sqrt(max(0, (T**2 - (1-R)**2)**2 + 4*T**2))
    X = X_num / (2*T)
    if X <= 0:
        # degenerate case, set k=0
        k_val = 0.0
    else:
        k_val = -lam/(4*np.pi*t_total) * np.log(X)
    Ras = R / (1 + X)
    disc = 4*Ras/(1-Ras)**2 - k_val**2
    if disc < 0:
        disc = 0.0
    sqrt_disc = np.sqrt(disc)
    n_plus = (1+Ras)/(1-Ras) + sqrt_disc
    n_minus = (1+Ras)/(1-Ras) - sqrt_disc
    if n_plus >= 1.0:
        n_val = n_plus
    else:
        n_val = n_minus
    rows_nk.append((lam_um, n_val, k_val))

with open(os.path.join(outdir, 'step_02_retrieved_nk.csv'), 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['wavelength_micron', 'n', 'k'])
    writer.writerows(rows_nk)

# ---------- Step 3: epsilon from n,k ----------
rows_eps = []
for lam_um, n_val, k_val in rows_nk:
    eps = (n_val + 1j*k_val)**2
    rows_eps.append((lam_um, eps.real, eps.imag))

with open(os.path.join(outdir, 'step_03_retrieved_epsilon.csv'), 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['wavelength_micron', 'real_epsilon', 'imag_epsilon'])
    writer.writerows(rows_eps)

# ---------- Step 4: ENZ wavelength ----------
real_eps_vals = np.array([r[1] for r in rows_eps])
enz_wav = None
enz_n = None
enz_k = None
# Find crossing
cross = False
for i in range(len(wavelengths_um)-1):
    if real_eps_vals[i] * real_eps_vals[i+1] <= 0:
        # linear interp
        wl_i = wavelengths_um[i]
        wl_j = wavelengths_um[i+1]
        eps_i = real_eps_vals[i]
        eps_j = real_eps_vals[i+1]
        enz_wav = wl_i + (wl_j - wl_i) * (0.0 - eps_i) / (eps_j - eps_i)
        # interpolate n,k
        n_i, k_i = rows_nk[i][1], rows_nk[i][2]
        n_j, k_j = rows_nk[i+1][1], rows_nk[i+1][2]
        frac = (enz_wav - wl_i) / (wl_j - wl_i)
        enz_n = n_i + frac*(n_j - n_i)
        enz_k = k_i + frac*(k_j - k_i)
        cross = True
        break
if not cross:
    # fallback: min abs
    idx = np.argmin(np.abs(real_eps_vals))
    enz_wav = float(wavelengths_um[idx])
    enz_n = rows_nk[idx][1]
    enz_k = rows_nk[idx][2]

enz_result = {
    "enz_wavelength_micron": float(enz_wav),
    "n_equals_k_at_enz": bool(abs(enz_n - enz_k) <= 0.02)
}
with open(os.path.join(outdir, 'step_04_enz_result.json'), 'w') as f:
    json.dump(enz_result, f)

# ---------- Step 5: Nonlocal dispersion ----------
d1 = d_Ag
d2 = d_Ge
D = d1 + d2  # period
rows_nonlocal = []
for lam_um, eps_Ag in zip(wavelengths_um, eps_Ag_list):
    lam = lam_um * 1e-6
    k0 = 2*np.pi / lam
    n1 = cmath.sqrt(eps_Ag)   # complex
    n2 = cmath.sqrt(eps_Ge)   # real
    kx1 = k0 * n1
    kx2 = k0 * n2
    val = (cmath.cos(kx1*d1) * cmath.cos(kx2*d2)
           - 0.5 * (eps_Ag*kx2/(eps_Ge*kx1) + eps_Ge*kx1/(eps_Ag*kx2))
           * cmath.sin(kx1*d1) * cmath.sin(kx2*d2))
    # arccos of complex
    arccos_val = cmath.acos(val)   # use cmath for complex
    kx = arccos_val / D
    eps_nl = (kx / k0)**2
    rows_nonlocal.append((lam_um, eps_nl.real, eps_nl.imag))

with open(os.path.join(outdir, 'nonlocal_epsilon.csv'), 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['wavelength_micron', 'real_epsilon', 'imag_epsilon'])
    writer.writerows(rows_nonlocal)
EOF

# === solve block: step_02_retrieved_nk.csv ===
true

# === solve block: step_03_retrieved_epsilon.csv ===
true

# === solve block: step_04_enz_result.json ===
true

# === solve block: nonlocal_epsilon.csv ===
true
