#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
export OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"
python3 -m pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple numpy scipy
cat > /tmp/hubbard.py << 'PYEOF'
import sys, csv
import numpy as np
from itertools import combinations
from scipy.linalg import eigh

t0 = 1.0
L_list = [3, 5, 7]
BC_list = ['OBC', 'TBC']
U_vals = [0.0, 2.0, 4.0, 8.0, 16.0, 32.0, 64.0, 128.0]

def basis_states(L, N, sz_spin2):
    # sz_spin2 = 2*Sz (e.g., 1 for Sz=1/2)
    N_up = (N + sz_spin2) // 2
    N_down = (N - sz_spin2) // 2
    up_combs = list(combinations(range(L), N_up))
    down_combs = list(combinations(range(L), N_down))
    up_masks = [sum(1<<i for i in c) for c in up_combs]
    down_masks = [sum(1<<i for i in c) for c in down_combs]
    masks = []
    for um in up_masks:
        for dm in down_masks:
            masks.append((um, dm))
    state_to_idx = {m: idx for idx, m in enumerate(masks)}
    return masks, state_to_idx

def build_H(L, BC, U, N, sz_spin2):
    masks, state_to_idx = basis_states(L, N, sz_spin2)
    dim = len(masks)
    # determine dtype: TBC with odd L yields complex Hamiltonian
    is_complex = (BC == 'TBC' and L % 2 == 1)
    dtype = complex if is_complex else float
    H = np.zeros((dim, dim), dtype=dtype)
    # on-site U
    for idx, (um, dm) in enumerate(masks):
        double = bin(um & dm).count('1')
        H[idx, idx] += U * double
    # hopping edges
    edges = []
    if BC == 'OBC':
        for i in range(L-1):
            edges.append((i, i+1, t0))
    else:  # TBC
        tau = t0 * np.exp(1j * np.pi * L / 2)
        for i in range(L-1):
            edges.append((i, i+1, t0))
        edges.append((0, L-1, tau))
    # build Hamiltonian from edges
    for (i, j, kappa) in edges:
        # two directed contributions: -kappa c_j† c_i  and  -kappa* c_i† c_j
        for (a, b, coeff) in [(j, i, kappa), (i, j, np.conj(kappa))]:
            for spin in [0, 1]:  # 0=up, 1=down
                for idx, (um, dm) in enumerate(masks):
                    mask = um if spin == 0 else dm
                    if not (mask & (1 << b)):
                        continue
                    if mask & (1 << a):
                        continue
                    # sign from anticommutation
                    if a < b:
                        between = (mask >> (a+1)) & ((1 << (b-a-1)) - 1)
                    else:
                        between = (mask >> (b+1)) & ((1 << (a-b-1)) - 1)
                    sign = 1 if bin(between).count('1') % 2 == 0 else -1
                    new_mask = (mask ^ (1 << b)) | (1 << a)
                    if spin == 0:
                        target = state_to_idx.get((new_mask, dm))
                    else:
                        target = state_to_idx.get((um, new_mask))
                    if target is not None:
                        H[target, idx] += -coeff * sign
    return H

def ground_state_energy(L, BC, U):
    N = L
    sz_spin2 = 1  # Sz = 1/2
    H = build_H(L, BC, U, N, sz_spin2)
    eigvals, _ = eigh(H)
    return eigvals[0]

def min_energy_for_N(L, BC, U, N):
    # try all possible spin configurations (N_up, N_down)
    min_val = None
    for N_up in range(0, min(N, L) + 1):
        N_down = N - N_up
        if N_down < 0 or N_down > L:
            continue
        sz_spin2 = N_up - N_down
        H = build_H(L, BC, U, N, sz_spin2)
        ev = eigh(H, eigvals_only=True)[0]
        if min_val is None or ev < min_val:
            min_val = ev
    return min_val

def write_ground_state_energy():
    out_path = '/app/outputs/ground_state_energy.csv'
    with open(out_path, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['L', 'BC', 'U', 'E_per_site'])
        for L in L_list:
            for BC in BC_list:
                for U in U_vals:
                    E0 = ground_state_energy(L, BC, U)
                    writer.writerow([L, BC, U, E0 / L])

def write_energy_gap():
    out_path = '/app/outputs/energy_gap.csv'
    with open(out_path, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['L', 'BC', 'U', 'gap'])
        for L in L_list:
            for BC in BC_list:
                for U in U_vals:
                    E0_N = ground_state_energy(L, BC, U)
                    E_Nminus1 = min_energy_for_N(L, BC, U, L-1)
                    gap = E_Nminus1 - E0_N
                    writer.writerow([L, BC, U, gap])

def write_magnetization():
    out_path = '/app/outputs/magnetization_L3_OBC.csv'
    L = 3
    BC = 'OBC'
    with open(out_path, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['U', 'site', 'magnetization'])
        for U in U_vals:
            H = build_H(L, BC, U, L, sz_spin2=1)
            _, evecs = eigh(H)
            v0 = evecs[:, 0]
            masks, _ = basis_states(L, L, sz_spin2=1)
            mag = np.zeros(L)
            for idx, (um, dm) in enumerate(masks):
                prob = abs(v0[idx])**2
                for site in range(L):
                    up_occ = (um >> site) & 1
                    down_occ = (dm >> site) & 1
                    mag[site] += prob * (up_occ - down_occ)
            for site in range(L):
                writer.writerow([U, site+1, mag[site]])

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: hubbard.py {ground_state_energy|energy_gap|magnetization}')
        sys.exit(1)
    cmd = sys.argv[1]
    if cmd == 'ground_state_energy':
        write_ground_state_energy()
    elif cmd == 'energy_gap':
        write_energy_gap()
    elif cmd == 'magnetization':
        write_magnetization()
    else:
        print('Unknown command')
        sys.exit(1)
PYEOF

# === solve block: ground_state_energy.csv ===
python3 /tmp/hubbard.py ground_state_energy

# === solve block: energy_gap.csv ===
python3 /tmp/hubbard.py energy_gap

# === solve block: magnetization_L3_OBC.csv ===
python3 /tmp/hubbard.py magnetization
