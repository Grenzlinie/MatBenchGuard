#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"
# Install numpy only (stdlib fallback not practical for eigenvalue computation)
python3 -m pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple numpy

# === solve block: band_energies.csv ===
python3 << 'EOF'
import numpy as np
import csv, os, math

# Parameters from paper
d = 2.9  # interatomic distance in Angstrom
E_s = -17.239
E_p = -6.857

# First neighbour overlap parameters (eV)
V_ssS_1 = -0.648
V_spS_1 = 1.327
V_ppS_1 = 2.282
V_ppPi_1 = -0.549

# Second neighbour overlap parameters (eV)
V_ssS_2 = -0.089
V_spS_2 = 0.133
V_ppS_2 = 0.343
V_ppPi_2 = 0.052

def slater_koster_hoppings(l, m, n, V_ssS, V_spS, V_ppS, V_ppPi):
    """Compute E_{i,j} for given direction cosines and overlap parameters."""
    E_ss = V_ssS
    E_sp_x = l * V_spS
    E_sp_y = m * V_spS
    E_sp_z = n * V_spS
    # p-p
    E_xx = l*l * V_ppS + (1 - l*l) * V_ppPi
    E_yy = m*m * V_ppS + (1 - m*m) * V_ppPi
    E_zz = n*n * V_ppS + (1 - n*n) * V_ppPi
    E_xy = l*m * (V_ppS - V_ppPi)
    E_xz = l*n * (V_ppS - V_ppPi)
    E_yz = m*n * (V_ppS - V_ppPi)
    # s-p directions already computed as E_sp_x etc.
    return {
        'ss': E_ss,
        'sx': E_sp_x, 'sy': E_sp_y, 'sz': E_sp_z,
        'xx': E_xx, 'yy': E_yy, 'zz': E_zz,
        'xy': E_xy, 'xz': E_xz, 'yz': E_yz
    }

def build_hamiltonian(k, R, theta):
    # compute h
    h_val = math.sqrt(d**2 - 4*R**2 * math.sin(theta/2)**2) if R > 0 else d
    # positions: atom 0 at (R,0,0) (consistent with paper's eq (1))
    # atom n at (R*cos(n*theta), R*sin(n*theta), n*h_val)
    
    # First neighbour (n=1) vector
    r1 = np.array([R*(math.cos(theta)-1), R*math.sin(theta), h_val])
    dist1 = np.linalg.norm(r1)  # should be ~d
    l1, m1, n1 = r1 / dist1
    hop1 = slater_koster_hoppings(l1, m1, n1, V_ssS_1, V_spS_1, V_ppS_1, V_ppPi_1)
    
    # Second neighbour (n=2) vector
    r2 = np.array([R*(math.cos(2*theta)-1), R*math.sin(2*theta), 2*h_val])
    dist2 = np.linalg.norm(r2)
    # scaling factor: reference distance = 2*d (linear chain), inverse square scaling
    ref_dist = 2*d
    scale = (ref_dist / dist2)**2 if dist2 > 0 else 1.0
    l2, m2, n2 = r2 / dist2
    hop2_raw = slater_koster_hoppings(l2, m2, n2, V_ssS_2, V_spS_2, V_ppS_2, V_ppPi_2)
    # scale second neighbor parameters
    hop2 = {k: scale*v for k, v in hop2_raw.items()}
    
    # Precompute sums over n=1,2 as in the paper's matrix elements
    cos_k = math.cos(2*math.pi*k)
    sin_k = math.sin(2*math.pi*k)
    
    H11 = E_p + 2*cos_k * ( hop1['xx'] + hop2['xx'] )
    H22 = E_p - 2*cos_k * ( (hop1['yy'] + hop2['yy']) ) # Note sign: -(...) ; but paper: H22 = E_p - 2 sum cos(2πk)( sin(nθ)E_{x,y_n} - cos(nθ)E_{y,y_n} ). For n=1, sinθ? We need to incorporate the sin/cos factors from equations. Actually the matrix elements directly use E_{x,x_n}, E_{x,y_n}, etc. which are the Slater-Koster integrals. The sums are over n=1,2 with cos/sin(2πk) times the combination. The expressions are given without direction cosines factors because E_{i,j} already contain the angular dependence. So we must compute for each n the E_{x,x_n}, etc. using the direction cosines for that n. Then plug into formulas. The formulas involve cos(nθ) and sin(nθ) multiplicative factors. So we need to compute for n=1 and n=2 the hopping integrals and then combine with cos(nθ), sin(nθ). 

    # We'll compute directly the matrix elements as per paper eqs H11..H34.
    # For n=1: E_{x,x1}, E_{x,y1}, etc. are from hop1. For n=2: from hop2.
    # Define arrays for n=1 and n=2 with scaling already applied.
    
    # For each n, compute the relevant E_{i,j}_n (already).
    # Then compute terms
    H11 = E_p + 2*cos_k * ( ( math.cos(theta)*hop1['xx'] + math.sin(theta)*hop1['xy'] )
                          + ( math.cos(2*theta)*hop2['xx'] + math.sin(2*theta)*hop2['xy'] ) )
    H22 = E_p - 2*cos_k * ( ( math.sin(theta)*hop1['xy'] - math.cos(theta)*hop1['yy'] )
                          + ( math.sin(2*theta)*hop2['xy'] - math.cos(2*theta)*hop2['yy'] ) )
    H33 = E_p + 2*cos_k * ( hop1['zz'] + hop2['zz'] )
    H44 = E_s + 2*cos_k * ( hop1['ss'] + hop2['ss'] )
    
    H12 = -2j*sin_k * ( ( math.sin(theta)*hop1['xx'] - math.cos(theta)*hop1['xy'] )
                       + ( math.sin(2*theta)*hop2['xx'] - math.cos(2*theta)*hop2['xy'] ) )
    H13 = -2j*sin_k * ( hop1['xz'] + hop2['xz'] )
    H14 = -2*cos_k * ( hop1['sx'] + hop2['sx'] )
    H23 = 2*cos_k * ( hop1['yz'] + hop2['yz'] )
    H24 = -2j*sin_k * ( hop1['sy'] + hop2['sy'] )
    H34 = -2j*sin_k * ( hop1['sz'] + hop2['sz'] )
    
    H = np.array([
        [H11, H12, H13, H14],
        [np.conj(H12), H22, H23, H24],
        [np.conj(H13), np.conj(H23), H33, H34],
        [np.conj(H14), np.conj(H24), np.conj(H34), H44]
    ], dtype=complex)
    return H

geometries = [
    ("linear", 0.0, 0.0),
    ("helix125", 3.25, 0.1439),
    ("helix50", 3.25, 0.3375)
]

output_path = "/app/outputs/band_energies.csv"
kpts = np.linspace(-0.5, 0.5, 201)

with open(output_path, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(["k", "band", "E", "geometry"])
    for geom_name, R, theta in geometries:
        for kval in kpts:
            H = build_hamiltonian(kval, R, theta)
            eigvals = np.linalg.eigvalsh(H)  # Hermitian
            eigvals.sort()
            for band_idx, E in enumerate(eigvals):
                writer.writerow([f"{kval:.10f}", band_idx, f"{E:.10f}", geom_name])
EOF
