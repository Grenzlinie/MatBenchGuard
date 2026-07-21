#!/usr/bin/env python3
"""Compute interaction energies for the four-atom Anderson model.

Usage: python3 compute.py interaction_energies <output.csv>
       python3 compute.py weak_limits <output.csv>
"""
import sys, math, csv
import numpy as np
from scipy.linalg import eigvalsh
from scipy.optimize import minimize_scalar

T = 0.5  # chain hopping in units where 2T = 1
SQRT2 = math.sqrt(2)

# ---------- basis construction for exact diagonalisation ----------
def build_basis():
    """Return list of (up_mask, down_mask) for the 36 S_z=0 states."""
    sites = [0,1,2,3]  # 0=adatom, 1,2,3=chain
    up_combos = []
    for i in range(4):
        for j in range(i+1, 4):
            up_combos.append((i,j))
    states = []
    for u in up_combos:
        for d in up_combos:
            states.append((u, d))
    return states

def mask_to_bit(occ):
    """Convert tuple of occupied sites to integer bitmask."""
    m = 0
    for s in occ:
        m |= (1 << s)
    return m

def basis_index_map(basis):
    lut = {}
    for idx, (up, down) in enumerate(basis):
        lut[(mask_to_bit(up), mask_to_bit(down))] = idx
    return lut

def apply_hop(mask, a, b):
    """If site a is set and b is clear, return (new_mask, parity).
    Parity is (-1)^{num of particles strictly between a and b}."""
    if (mask >> a) & 1 == 0:
        return None, 0
    if (mask >> b) & 1 == 1:
        return None, 0
    new_mask = (mask & ~(1 << a)) | (1 << b)
    # count particles between a and b (exclusive)
    low = min(a, b)
    high = max(a, b)
    # mask bits for sites strictly between
    between = (mask >> (low+1)) & ((1 << (high - low - 1)) - 1)
    n_between = bin(between).count('1')
    parity = 1 if n_between % 2 == 0 else -1
    return new_mask, parity

def exact_deltaW(U, V):
    """Exact interaction energy ΔW = E_ground - E0."""
    E0 = -U/2 - 2*SQRT2*T
    basis = build_basis()
    n = len(basis)
    H = np.zeros((n,n))
    lut = basis_index_map(basis)
    # single-particle site energies: site 0 has -U/2, others 0
    site_en = [-U/2, 0.0, 0.0, 0.0]
    for i, (up, down) in enumerate(basis):
        up_mask = mask_to_bit(up)
        down_mask = mask_to_bit(down)
        # diagonal
        sp_en = 0.0
        for s in up:
            sp_en += site_en[s]
        for s in down:
            sp_en += site_en[s]
        U_term = U if ((up_mask & 1) and (down_mask & 1)) else 0.0
        H[i,i] = sp_en + U_term
        # hopping: spin-up
        for a,b,t in [(0,1,V), (1,0,V), (1,2,T), (2,1,T), (2,3,T), (3,2,T)]:
            new_mask, parity = apply_hop(up_mask, a, b)
            if new_mask is not None:
                new_state = (new_mask, down_mask)
                j = lut.get(new_state)
                if j is not None:
                    H[i,j] += parity * (-t)
        # spin-down
        for a,b,t in [(0,1,V), (1,0,V), (1,2,T), (2,1,T), (2,3,T), (3,2,T)]:
            new_mask, parity = apply_hop(down_mask, a, b)
            if new_mask is not None:
                new_state = (up_mask, new_mask)
                j = lut.get(new_state)
                if j is not None:
                    H[i,j] += parity * (-t)
    # diagonalise
    eigs = np.linalg.eigvalsh(H)
    E_ground = np.min(eigs)
    return E_ground - E0

# ---------- weak-binding ----------
def weak_deltaW(U, V):
    if U == 0:
        raise ValueError("U cannot be zero")
    return -V**2/(U + 2*SQRT2*T) - 4*V**2/U

# ---------- RSC ----------
def RSC_deltaW(U, V):
    # surface complex (dimer) exact ground state
    disc = (U/4)**2 + 4*V**2
    E_SC = -U/4 - math.sqrt(disc)   # most negative
    # separation energy
    E_32 = 2*(SQRT2 - 1)*T
    Delta_W_SC = E_SC + E_32

    # rebonding correction Eq. (20)
    disc2 = U**2 + 16*V**2
    E_plus = 0.25 * (-U + math.sqrt(disc2))
    E_minus = 0.25 * (-U - math.sqrt(disc2))

    denom1 = 2*E_minus + T - E_SC
    num1 = (E_SC*E_minus + 2*V**2)**2
    factor1 = num1 / (denom1 * (E_SC**2+4*V**2) * (E_minus**2+V**2))

    denom2 = 2*E_plus + T - E_SC
    num2 = (E_SC*E_plus + 2*V**2)**2
    factor2 = num2 / (denom2 * (E_SC**2+4*V**2) * (E_plus**2+V**2))

    Delta_W_R = - (T**2) * (factor1 + factor2)  # note: factor of 2 already included? Eq (20) says 1/2 ΔW_R = -T^2(...), so ΔW_R = -2*T^2*(...). Let's double-check: paper: "1/2 ΔW_R = -T^2 ( ... )". Yes, ΔW_R = 2 * that expression.
    # Actually the paper writes: "1/2 ΔW_R = -T^2 ( ... )". So I must multiply by 2.
    Delta_W_R = 2 * Delta_W_R   # now correct
    return Delta_W_SC + Delta_W_R

# ---------- RHF ----------
def RHF_deltaW(U, V):
    term = V**2 + 2*T**2
    disc = math.sqrt(V**4 + 4*T**4)
    sqrt1 = math.sqrt(term + disc)
    sqrt2 = math.sqrt(term - disc) if term - disc > 0 else 0.0
    return -SQRT2 * (sqrt1 + sqrt2 - 2*T)

# ---------- URHF ----------
def URHF_deltaW(U, V):
    """Find x that minimizes epsilon(x) and return Delta W = epsilon(x) - E0."""
    E0 = -U/2 - 2*SQRT2*T
    # matrix for given x and spin sign sigma (±1 for up/down)
    def epsilon(x):
        # x is the magnetization: n_up - n_down = 2x, n_up = 1/2 + x, n_down = 1/2 - x
        # Up matrix with E_a↑ = -U x
        M_up = np.array([[-U*x, -V, 0, 0],
                         [-V, 0, -T, 0],
                         [0, -T, 0, -T],
                         [0, 0, -T, 0]], dtype=float)
        M_down = np.array([[ U*x, -V, 0, 0],
                           [-V, 0, -T, 0],
                           [0, -T, 0, -T],
                           [0, 0, -T, 0]], dtype=float)
        e_up = eigvalsh(M_up)
        e_down = eigvalsh(M_down)
        # sum of two lowest (most negative) for each
        E_sum = sum(sorted(e_up)[:2]) + sum(sorted(e_down)[:2])
        counter = U*(0.25 - x**2)
        return E_sum - counter

    # Check if RHF (x=0) is the minimum
    e_rhf = epsilon(0.0)
    # Find any lower value for x in (0, 0.5]
    # Use a fine scan then local refinement
    xs = np.linspace(0.001, 0.5, 200)
    vals = [epsilon(x) for x in xs]
    min_idx = np.argmin(vals)
    x_best = xs[min_idx]
    # refine with golden-section search (no derivative)
    res = minimize_scalar(lambda x: epsilon(x), method='bounded', bounds=(1e-4, 0.5), options={'maxiter': 1000, 'xatol': 1e-8})
    # compare with RHF
    if res.fun < e_rhf - 1e-12:
        return res.fun - E0
    else:
        return e_rhf - E0

# ---------- main ----------
def generate_interaction(output_path):
    U_vals = [1.0, 2.5, 4.0]
    V_vals = [0.0, 0.25, 0.5, 0.75, 1.0, 1.25, 1.5, 1.75, 2.0, 2.25, 2.5]
    with open(output_path, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['U','V','exact_deltaW','weak_deltaW','RSC_deltaW','RHF_deltaW','URHF_deltaW'])
        for U in U_vals:
            for V in V_vals:
                exact = exact_deltaW(U, V)
                weak = weak_deltaW(U, V) if V != 0 else 0.0
                rsc = RSC_deltaW(U, V)
                rhf = RHF_deltaW(U, V)
                urhf = URHF_deltaW(U, V)
                writer.writerow([U, V, exact, weak, rsc, rhf, urhf])

def generate_weak_limits(output_path):
    cases = [(4.0, 1e-4), (0.1, 1e-4)]
    with open(output_path, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['U','V','ratio'])
        for U, V in cases:
            dw = weak_deltaW(U, V)
            ratio = abs(dw) * U / V**2
            writer.writerow([U, V, ratio])

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print(f"Usage: {sys.argv[0]} interaction_energies|weak_limits <output.csv>")
        sys.exit(1)
    mode = sys.argv[1]
    out = sys.argv[2]
    if mode == 'interaction_energies':
        generate_interaction(out)
    elif mode == 'weak_limits':
        generate_weak_limits(out)
    else:
        print(f"Unknown mode {mode}")
        sys.exit(1)
