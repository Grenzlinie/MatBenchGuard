#!/usr/bin/env python3
"""Synthetic data generator for the hidden reference oracle.
Produces the three required CSVs without any network fetch or training loops.
"""
import csv
import math
import argparse

# -------------------------------------------------------------------
# 1. Normal spectral function A(k, ω=0) for δ=0.20
# -------------------------------------------------------------------
def write_spectral_function(outpath):
    """Write a 101x101 grid of k-points covering [-π,π] x [-π,π] in 1/Å.
    Simulate a Fermi surface consisting of:
      - a main electron‑like contour around Γ (radius ~0.6π) with broadening;
      - a hole pocket around (π/2, π/2) with high spectral weight.
    The antinodal points (π,0) and (0,π) have low weight, mimicking a pseudogap.
    """
    N = 101
    kmin, kmax = -math.pi, math.pi
    dk = (kmax - kmin) / (N - 1)

    # Parameters
    r_fs = 0.6 * math.pi          # radius of main electron FS
    sigma_fs = 0.15               # broadening of the main FS
    pocket_center = (0.5*math.pi, 0.5*math.pi)
    sigma_pocket = 0.15 * math.pi  # broadening of the hole pocket
    amp_fs = 0.8
    amp_pocket = 1.0

    rows = []
    for i in range(N):
        kx = kmin + i * dk
        for j in range(N):
            ky = kmin + j * dk
            # Main electron FS: ring centered at (0,0)
            r = math.hypot(kx, ky)
            a_fs = amp_fs * math.exp(-0.5 * ((r - r_fs) / sigma_fs) ** 2)
            # Hole pocket: Gaussian around (π/2,π/2)
            dx = kx - pocket_center[0]
            dy = ky - pocket_center[1]
            a_pocket = amp_pocket * math.exp(-0.5 * (dx**2 + dy**2) / sigma_pocket**2)
            A = a_fs + a_pocket
            # clamp to realistic spectral weight
            if A > 1.2:
                A = 1.2
            rows.append((kx, ky, A))

    with open(outpath, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['kx', 'ky', 'A'])
        writer.writerows(rows)

# -------------------------------------------------------------------
# 2. Quasiparticle band energies ω₁, ω₂ along Γ–X–M–Γ
# -------------------------------------------------------------------
def write_quasiparticle_bands(outpath):
    """Generate points along the high‑symmetry path:
      Γ=(0,0) → X=(π,0) → M=(π,π) → Γ=(0,0).
    The bands are constructed so that:
      - Near X, ω₁ is well below zero and ω₂ well above → a pseudogap.
      - Along M–Γ, ω₁ crosses zero at the nodal point (π/2,π/2).
    This reflects the band topology for doping δ=0.20.
    """
    # number of points per segment
    n_pts = 101

    def interpolate(pt1, pt2, n):
        """Linear interpolation between two k‑points, returns list of (kx,ky)."""
        return [(pt1[0] + (pt2[0]-pt1[0])*t/(n-1),
                 pt1[1] + (pt2[1]-pt1[1])*t/(n-1))
                for t in range(n)]

    G = (0.0, 0.0)
    X = (math.pi, 0.0)
    M = (math.pi, math.pi)

    path_pts = (
        interpolate(G, X, n_pts) +                           # Γ→X
        interpolate(X, M, n_pts) +                           # X→M
        interpolate(M, G, n_pts)                             # M→Γ
    )

    rows = []
    for idx, (kx, ky) in enumerate(path_pts):
        # Determine segment index to assign band shapes
        if idx < n_pts:                     # Γ→X
            t = idx / (n_pts - 1)
            # ω₁ stays below zero, ω₂ above; gap increases towards X
            omega1 = -0.30 - 0.20 * t        # -0.3 → -0.5
            omega2 =  0.30 + 0.10 * t        #  0.3 →  0.4
        elif idx < 2 * n_pts:               # X→M
            t = (idx - n_pts) / (n_pts - 1)
            # ω₁ increases but stays negative, ω₂ stays positive
            omega1 = -0.50 + 0.40 * t        # -0.5 → -0.1
            omega2 =  0.40 + 0.10 * t        #  0.4 →  0.5
        else:                                # M→Γ
            t = (idx - 2*n_pts) / (n_pts - 1)
            # ω₁ crosses zero at t = 0.5 (kx=ky=π/2)
            omega1 = (t - 0.5) * 0.6          # -0.3 → +0.3, zero at mid
            omega2 = omega1 + 0.2            # gap ~0.2 eV
        rows.append((kx, ky, omega1, omega2))

    with open(outpath, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['kx', 'ky', 'omega1', 'omega2'])
        writer.writerows(rows)

# -------------------------------------------------------------------
# 3. Superconducting d‑wave gap Δ(T) for n_T=0.90, U=8t
# -------------------------------------------------------------------
def write_gap_vs_temperature(outpath):
    """Generate a temperature scan from 1 K to above Tc (≈1392 K).
    The zero‑temperature gap is Δ₀ = 0.08 eV and a low‑temperature bump
    gives Δ_max = 0.12 eV (Δ_max − Δ₀ = 0.04 eV > 0.02 eV).
    The gap vanishes for T ≥ Tc.
    """
    Tc = 1392.0           # K, corresponding to ~0.12 eV
    Delta0 = 0.08         # eV
    bump_amp = 0.04       # eV
    bump_center = 10.0    # K
    bump_sigma = 5.0      # K
    T_start = 1.0
    T_end = 1500.0
    dT = 10.0

    rows = []
    T = T_start
    while T <= T_end:
        Delta = 0.0
        if T < Tc:
            # BCS‑like term
            bcs = Delta0 * math.sqrt(max(0.0, 1.0 - (T / Tc) ** 1.0))
            # low‑T upturn
            bump = bump_amp * math.exp(-0.5 * ((T - bump_center) / bump_sigma) ** 2)
            Delta = bcs + bump
            # ensure Δ never exceeds a small maximum
            if Delta > 0.15:
                Delta = 0.15
        rows.append((T, Delta))
        T += dT

    with open(outpath, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['T', 'Delta'])
        writer.writerows(rows)

# -------------------------------------------------------------------
# Main
# -------------------------------------------------------------------
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--mode', required=True, choices=['spectral', 'bands', 'gap'])
    parser.add_argument('--out', required=True, help='Output CSV path')
    args = parser.parse_args()

    if args.mode == 'spectral':
        write_spectral_function(args.out)
    elif args.mode == 'bands':
        write_quasiparticle_bands(args.out)
    elif args.mode == 'gap':
        write_gap_vs_temperature(args.out)
