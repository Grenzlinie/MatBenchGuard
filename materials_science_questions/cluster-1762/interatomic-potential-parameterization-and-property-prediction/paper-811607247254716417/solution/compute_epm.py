#!/usr/bin/env python3
import numpy as np
from scipy.linalg import eigh
import json
import csv
import argparse
import sys
import os

# Physical constants
HBAR2_OVER_2M_EV_A2 = 3.809982   # eV*Angstrom^2
RY_TO_EV = 13.6057

# Lattice constants (Angstrom)
A_MGS = 5.62
A_ZNS = 5.409

# Symmetric (V^S) and antisymmetric (V^A) form factors in Rydberg for MgS and ZnS
# Indices refer to squared G-vector magnitude in units of (2*pi/a)^2
V_S_MGS = {3: -0.209338, 8: 0.04,      11: 0.06}
V_A_MGS = {3:  0.19,     4: 0.12,      11: -0.03}

V_S_ZNS = {3: -0.312939, 8: 0.021262,  11: 0.170554}
V_A_ZNS = {3:  0.030061, 4: 0.116,     11: 0.129269}

# Generate set of reciprocal lattice vectors for an FCC lattice (zinc-blende)
# up to squared magnitude cutoff (in reduced units).
def generate_g_vecs(cutoff_sq):
    vecs = []
    for n1 in range(-3, 4):
        for n2 in range(-3, 4):
            for n3 in range(-3, 4):
                sq = n1*n1 + n2*n2 + n3*n3
                if 0 < sq <= cutoff_sq:
                    vecs.append((n1, n2, n3))
    # sort by increasing squared magnitude
    vecs.sort(key=lambda v: v[0]*v[0] + v[1]*v[1] + v[2]*v[2])
    return vecs

G_VECS = generate_g_vecs(11)   # up to (3,1,1) = 11

# Build the secular determinant Hamiltonian for a given k-point (Cartesian coords, Angstrom^-1),
# lattice constant a, and form factor dictionaries (Rydberg).
def build_hamiltonian(k, a, v_s, v_a):
    n_g = len(G_VECS)
    H = np.zeros((n_g, n_g), dtype=complex)
    # kinetic energy
    for i, g in enumerate(G_VECS):
        k_g = k + np.array(g) * (2*np.pi / a)   # A^-1
        H[i, i] = HBAR2_OVER_2M_EV_A2 * np.dot(k_g, k_g)
    # pseudopotential matrix elements
    for i, gi in enumerate(G_VECS):
        for j, gj in enumerate(G_VECS):
            dg = np.array(gj) - np.array(gi)   # G'-G
            sq = dg[0]*dg[0] + dg[1]*dg[1] + dg[2]*dg[2]
            if sq in v_s or sq in v_a:
                # G*tau = (pi/2)*(n1+n2+n3) for tau = (1/4,1/4,1/4)*a
                phase = (np.pi/2) * (dg[0] + dg[1] + dg[2])
                c = np.cos(phase)
                s = np.sin(phase)
                vs_val = v_s.get(sq, 0.0) * RY_TO_EV
                va_val = v_a.get(sq, 0.0) * RY_TO_EV
                H[i, j] = vs_val * c - 1j * va_val * s
    return H

# Find valence band maximum (VBM) and conduction band minimum (CBM) at a given k-point.
# Returns (vbm, cbm) in eV.  We locate the largest gap between consecutive eigenvalues.
def band_edges(evals):
    diffs = np.diff(evals)
    igap = np.argmax(diffs)
    vbm = evals[igap]
    cbm = evals[igap+1]
    return vbm, cbm

# Compute binary band gaps for one compound given its a and form factors.
def binary_gaps(a, v_s, v_a):
    k_gamma = np.array([0.0, 0.0, 0.0])
    k_x = np.array([2*np.pi/a, 0.0, 0.0])
    k_l = np.array([np.pi/a, np.pi/a, np.pi/a])

    # Gamma
    evals_g = np.linalg.eigvalsh(build_hamiltonian(k_gamma, a, v_s, v_a))
    vbm_g, cbm_g = band_edges(evals_g)
    eg_gamma = cbm_g - vbm_g

    # X
    evals_x = np.linalg.eigvalsh(build_hamiltonian(k_x, a, v_s, v_a))
    # conduction minimum at X is the first eigenvalue above the VBM at Gamma
    cbm_x = evals_x[evals_x > vbm_g][0]
    eg_x = cbm_x - vbm_g

    # L
    evals_l = np.linalg.eigvalsh(build_hamiltonian(k_l, a, v_s, v_a))
    cbm_l = evals_l[evals_l > vbm_g][0]
    eg_l = cbm_l - vbm_g

    return eg_gamma, eg_x, eg_l

# Compute all binary gaps.
def compute_binary():
    eg_mg = binary_gaps(A_MGS, V_S_MGS, V_A_MGS)
    eg_zn = binary_gaps(A_ZNS, V_S_ZNS, V_A_ZNS)
    return {
        "MgS": {"Eg_Gamma": round(eg_mg[0], 4), "Eg_X": round(eg_mg[1], 4), "Eg_L": round(eg_mg[2], 4)},
        "ZnS": {"Eg_Gamma": round(eg_zn[0], 4), "Eg_X": round(eg_zn[1], 4), "Eg_L": round(eg_zn[2], 4)}
    }

# VCA interpolation
def ternary_gaps(x, eg_mg, eg_zn):
    # form factors linear interpolation
    vs = {}
    va = {}
    for sq in [3,4,8,11]:
        vs[sq] = x * V_S_MGS.get(sq, 0.0) + (1-x) * V_S_ZNS.get(sq, 0.0)
        va[sq] = x * V_A_MGS.get(sq, 0.0) + (1-x) * V_A_ZNS.get(sq, 0.0)
    a = x * A_MGS + (1-x) * A_ZNS

    k_gamma = np.array([0.0, 0.0, 0.0])
    k_x = np.array([2*np.pi/a, 0.0, 0.0])
    k_l = np.array([np.pi/a, np.pi/a, np.pi/a])

    # Gamma
    evals_g = np.linalg.eigvalsh(build_hamiltonian(k_gamma, a, vs, va))
    vbm_g, cbm_g = band_edges(evals_g)
    eg_gamma = cbm_g - vbm_g

    # X
    evals_x = np.linalg.eigvalsh(build_hamiltonian(k_x, a, vs, va))
    cbm_x = evals_x[evals_x > vbm_g][0]
    eg_x = cbm_x - vbm_g

    # L
    evals_l = np.linalg.eigvalsh(build_hamiltonian(k_l, a, vs, va))
    cbm_l = evals_l[evals_l > vbm_g][0]
    eg_l = cbm_l - vbm_g

    # antisymmetric gap at X: difference between the two highest valence eigenvalues at X
    # Valence bands are those below the large gap; the top valence band is the highest eigenvalue below gap.
    # We find the gap at X using diffs.
    diffs_x = np.diff(evals_x)
    igap_x = np.argmax(diffs_x)
    vbm_x_idx = igap_x          # index of highest valence
    vbm_x = evals_x[vbm_x_idx]
    if vbm_x_idx >= 1:
        second_valence_x = evals_x[vbm_x_idx-1]
        antisymmetric = vbm_x - second_valence_x
    else:
        antisymmetric = 0.0    # fallback

    return eg_gamma, eg_x, eg_l, antisymmetric

# Refractive index models
def refractive_moss(eg):
    A = 25*eg + 212
    B = 0.21*eg + 4.25
    n4 = 1 + A / (eg + B)**2
    return n4**0.25

def refractive_ghosh(eg):
    n4 = 1 + (25*eg + 212) / (eg + 4.25)**2
    return n4**0.25

def reflection(n):
    return ((n - 1)**2) / ((n + 1)**2)

# Main routines per output file
def write_binary(output_dir):
    data = compute_binary()
    path = os.path.join(output_dir, "binary_band_gaps.json")
    with open(path, "w") as f:
        json.dump(data, f, indent=2)

def write_ternary(output_dir):
    # Compute binary gaps via EPM to have the exact reference values (not hardcoded)
    eg_mg = binary_gaps(A_MGS, V_S_MGS, V_A_MGS)
    eg_zn = binary_gaps(A_ZNS, V_S_ZNS, V_A_ZNS)
    xs = np.linspace(0.0, 1.0, 11)   # 0.0,0.1,...,1.0
    rows = []
    for x in xs:
        eg_gamma, eg_x, eg_l, antisym = ternary_gaps(x, eg_mg, eg_zn)
        rows.append([round(x, 1), round(eg_gamma, 4), round(eg_x, 4), round(eg_l, 4), round(antisym, 4)])
    path = os.path.join(output_dir, "ternary_band_gaps.csv")
    with open(path, "w", newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["x", "Eg_Gamma", "Eg_X", "Eg_L", "antisymmetric_gap"])
        writer.writerows(rows)

def write_optical(output_dir):
    # Use the direct gap from the ternary computation
    eg_mg = binary_gaps(A_MGS, V_S_MGS, V_A_MGS)
    eg_zn = binary_gaps(A_ZNS, V_S_ZNS, V_A_ZNS)
    xs = np.linspace(0.0, 1.0, 11)
    rows = []
    for x in xs:
        eg_gamma, _, _, _ = ternary_gaps(x, eg_mg, eg_zn)
        n_m = refractive_moss(eg_gamma)
        n_g = refractive_ghosh(eg_gamma)
        r_m = reflection(n_m)
        r_g = reflection(n_g)
        rows.append([round(x, 1), round(n_m, 4), round(n_g, 4), round(r_m, 4), round(r_g, 4)])
    path = os.path.join(output_dir, "optical_properties.csv")
    with open(path, "w", newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["x", "n_Moss", "n_Ghosh", "R_Moss", "R_Ghosh"])
        writer.writerows(rows)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-dir", required=True)
    parser.add_argument("--binary", action="store_true")
    parser.add_argument("--ternary", action="store_true")
    parser.add_argument("--optical", action="store_true")
    args = parser.parse_args()
    if args.binary:
        write_binary(args.output_dir)
    elif args.ternary:
        write_ternary(args.output_dir)
    elif args.optical:
        write_optical(args.output_dir)
    else:
        # If no flag, write all three (useful for verifier)
        write_binary(args.output_dir)
        write_ternary(args.output_dir)
        write_optical(args.output_dir)
