#!/usr/bin/env python3
"""Compute phonon dispersion and DOS for f.c.c. LJ crystal.

Usage:
  compute_phonons.py --sigma SIGMA_A --mode dispersion --output FILE
  compute_phonons.py --sigma SIGMA_A --mode dos --output FILE

Units: ε=1, σ=1, M=1.
"""
import sys
import csv
import argparse
import numpy as np

def make_fcc_primitive():
    """Return primitive vectors (a1,a2,a3) in units of a."""
    a1 = np.array([1.0, 1.0, 0.0])
    a2 = np.array([1.0, 0.0, 1.0])
    a3 = np.array([0.0, 1.0, 1.0])
    return a1, a2, a3

def reciprocal_primitive(a1, a2, a3):
    """Return reciprocal primitive vectors b1,b2,b3 (a_i·b_j = δ_ij)."""
    cross_a2_a3 = np.cross(a2, a3)
    volume = np.dot(a1, cross_a2_a3)
    b1 = cross_a2_a3 / volume
    b2 = np.cross(a3, a1) / volume
    b3 = np.cross(a1, a2) / volume
    return b1, b2, b3

def generate_neighbors(max_n=8):
    """Generate neighbour list in primitive integer coordinates.
    Returns n_vals (N,3) integer arrays and rho_vals (N,3) Cartesian vectors.
    Excludes the origin.
    """
    a1, a2, a3 = make_fcc_primitive()
    # integer range [-max_n, max_n]
    rng = np.arange(-max_n, max_n+1)
    n1, n2, n3 = np.meshgrid(rng, rng, rng, indexing='ij')
    n_vals = np.column_stack([n1.ravel(), n2.ravel(), n3.ravel()])
    # remove origin
    mask = ~np.all(n_vals == 0, axis=1)
    n_vals = n_vals[mask]
    # compute rho vectors
    rho_vals = (n_vals[:,0,None]*a1 + n_vals[:,1,None]*a2 + n_vals[:,2,None]*a3)
    return n_vals, rho_vals

def compute_lattice_sums(q_red, n_nei, rho_nei):
    """Compute required lattice sums for given reduced q points.
    q_red: (Nq, 3) array in primitive reciprocal coordinates.
    Returns dict of S arrays.
    """
    Nnei = n_nei.shape[0]
    Nq = q_red.shape[0]
    rho_x = rho_nei[:,0]
    rho_y = rho_nei[:,1]
    rho_z = rho_nei[:,2]
    rho = np.linalg.norm(rho_nei, axis=1)
    # dot products n·q (Nnei x Nq)
    dot_n_q = np.dot(n_nei, q_red.T)  # shape (Nnei, Nq)
    # phases: cos(2π n·q), sum is real
    phase = np.cos(2.0 * np.pi * dot_n_q)

    # Helper to compute S_n^{αβ}
    def Sn_ab(n):
        w = 1.0 / (rho ** n)
        Sxx = np.dot(w * rho_x**2, phase)
        Sxy = np.dot(w * rho_x * rho_y, phase)
        Sxz = np.dot(w * rho_x * rho_z, phase)
        Syy = np.dot(w * rho_y**2, phase)
        Syz = np.dot(w * rho_y * rho_z, phase)
        Szz = np.dot(w * rho_z**2, phase)
        return Sxx, Sxy, Sxz, Syy, Syz, Szz

    def Sn(n):
        w = 1.0 / (rho ** n)
        return np.dot(w, phase)

    S16_xx, S16_xy, S16_xz, S16_yy, S16_yz, S16_zz = Sn_ab(16)
    S10_xx, S10_xy, S10_xz, S10_yy, S10_yz, S10_zz = Sn_ab(10)
    S14 = Sn(14)
    S8  = Sn(8)
    # also need q=0 values
    # S14(0) and S8(0) can be computed as sum 1/rho^n
    S14_zero = np.sum(1.0 / (rho ** 14))
    S8_zero  = np.sum(1.0 / (rho ** 8))

    return {
        'S16': (S16_xx, S16_xy, S16_xz, S16_yy, S16_yz, S16_zz),
        'S10': (S10_xx, S10_xy, S10_xz, S10_yy, S10_yz, S10_zz),
        'S14': S14,
        'S8':  S8,
        'S14_zero': S14_zero,
        'S8_zero':  S8_zero
    }

def compute_frequencies(q_red, n_nei, rho_nei, sigma_a):
    """Return frequencies (Nq,3) and eigenvectors (Nq,3,3) for given q points."""
    sums = compute_lattice_sums(q_red, n_nei, rho_nei)
    Nq = q_red.shape[0]
    sigma_a6 = sigma_a ** 6
    prefactor = 24.0 * (sigma_a ** 8)

    S16_xx, S16_xy, S16_xz, S16_yy, S16_yz, S16_zz = sums['S16']
    S10_xx, S10_xy, S10_xz, S10_yy, S10_yz, S10_zz = sums['S10']
    S14 = sums['S14']
    S8  = sums['S8']
    S14z = sums['S14_zero']
    S8z  = sums['S8_zero']

    freqs = np.zeros((Nq, 3))
    evecs = np.zeros((Nq, 3, 3), dtype=complex)

    for i in range(Nq):
        D = np.zeros((3,3), dtype=complex)
        # off-diagonal part
        off_xx = -28.0 * sigma_a6 * S16_xx[i] + 8.0 * S10_xx[i]
        off_xy = -28.0 * sigma_a6 * S16_xy[i] + 8.0 * S10_xy[i]
        off_xz = -28.0 * sigma_a6 * S16_xz[i] + 8.0 * S10_xz[i]
        off_yy = -28.0 * sigma_a6 * S16_yy[i] + 8.0 * S10_yy[i]
        off_yz = -28.0 * sigma_a6 * S16_yz[i] + 8.0 * S10_yz[i]
        off_zz = -28.0 * sigma_a6 * S16_zz[i] + 8.0 * S10_zz[i]
        D[0,0] = off_xx
        D[1,1] = off_yy
        D[2,2] = off_zz
        D[0,1] = D[1,0] = off_xy
        D[0,2] = D[2,0] = off_xz
        D[1,2] = D[2,1] = off_yz
        # diagonal extra term
        extra = (22.0/3.0 * sigma_a6 * S14z - 5.0/3.0 * S8z
                 + 2.0 * sigma_a6 * S14[i] - S8[i])
        for a in range(3):
            D[a,a] += extra
        D *= prefactor
        # diagonalize (D is real symmetric, use eigh)
        evals, evects = np.linalg.eigh(D.real)
        # evals are ω^2, take sqrt, sort ascending (already)
        omega = np.sqrt(np.maximum(evals, 0.0))
        freqs[i,:] = omega
        evecs[i,:,:] = evects
    return freqs, evecs

def dispersion_mode(sigma_a, outfile):
    max_n = 8   # neighbour shells
    n_nei, rho_nei = generate_neighbors(max_n)
    # reciprocal vectors for direction
    a1, a2, a3 = make_fcc_primitive()
    b1, b2, b3 = reciprocal_primitive(a1, a2, a3)
    B = np.column_stack([b1, b2, b3])  # 3x3

    # q points along Γ-X: q_red = (t/2, t/2, 0), t in [0,1]
    t_vals = np.linspace(0.0, 1.0, 101)
    q_red = np.zeros((len(t_vals), 3))
    q_red[:,0] = t_vals / 2.0
    q_red[:,1] = t_vals / 2.0

    freqs, evecs = compute_frequencies(q_red, n_nei, rho_nei, sigma_a)

    with open(outfile, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['q', 'omega_L', 'omega_T'])
        for i, t in enumerate(t_vals):
            q_val = t
            if t == 0.0:
                omega_L = 0.0
                omega_T = 0.0
            else:
                q_cart = q_red[i] @ B   # unnormalised direction
                q_hat = q_cart / np.linalg.norm(q_cart)
                # compute projection of each eigenvector
                proj = np.abs(np.dot(evecs[i,:,:].T, q_hat))
                idx_L = np.argmax(proj)
                omega_L = freqs[i, idx_L]
                # pick one transverse (the others are degenerate)
                idx_T = 0 if idx_L != 0 else 1
                omega_T = freqs[i, idx_T]
            writer.writerow([f"{q_val:.6f}", f"{omega_L:.8f}", f"{omega_T:.8f}"])

def dos_mode(sigma_a, outfile):
    max_n = 8
    n_nei, rho_nei = generate_neighbors(max_n)
    Nmesh = 16   # 16x16x16 grid in primitive BZ
    q1 = np.linspace(0.0, 1.0, Nmesh, endpoint=False)
    q2 = np.linspace(0.0, 1.0, Nmesh, endpoint=False)
    q3 = np.linspace(0.0, 1.0, Nmesh, endpoint=False)
    qg1, qg2, qg3 = np.meshgrid(q1, q2, q3, indexing='ij')
    q_red = np.column_stack([qg1.ravel(), qg2.ravel(), qg3.ravel()])
    freqs, _ = compute_frequencies(q_red, n_nei, rho_nei, sigma_a)
    all_freqs = freqs.ravel()
    max_freq = np.max(all_freqs) * 1.01
    bins = np.linspace(0.0, max_freq, 101)  # 100 bins
    counts, bin_edges = np.histogram(all_freqs, bins=bins)
    with open(outfile, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['bin_start', 'bin_end', 'count'])
        for j in range(len(counts)):
            writer.writerow([f"{bin_edges[j]:.8f}", f"{bin_edges[j+1]:.8f}", counts[j]])

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--sigma', type=float, required=True)
    parser.add_argument('--mode', choices=['dispersion', 'dos'], required=True)
    parser.add_argument('--output', type=str, required=True)
    args = parser.parse_args()
    if args.mode == 'dispersion':
        dispersion_mode(args.sigma, args.output)
    elif args.mode == 'dos':
        dos_mode(args.sigma, args.output)

if __name__ == '__main__':
    main()
