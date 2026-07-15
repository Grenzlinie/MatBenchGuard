#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
python3 -m pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple numpy

# === solve block: step_01_err_data.csv ===
python3 << 'PYEOF'
import numpy as np
import csv
import os

# Background VTI stiffness matrix (paper eq 34)
C_b = np.array([[10,4,2.5,0,0,0],
                [4,10,2.5,0,0,0],
                [2.5,2.5,6,0,0,0],
                [0,0,0,2,0,0],
                [0,0,0,0,2,0],
                [0,0,0,0,0,3]])

def bond_rotation(C, R):
    """Apply Bond transformation: C' = A C A^T, where A is built from 3x3 rotation R."""
    # Build 6x6 Bond matrix from 3x3 rotation matrix
    A = np.zeros((6,6))
    # mapping from Voigt indices to pairs
    voigt_map = [(0,0),(1,1),(2,2),(1,2),(0,2),(0,1)]
    for i in range(6):
        a,b = voigt_map[i]
        for j in range(6):
            c,d = voigt_map[j]
            if i < 3 and j < 3:
                A[i,j] = R[a,c] * R[b,d]
            elif i < 3 and j >= 3:
                A[i,j] = R[a,c] * R[b,d] + R[a,d] * R[b,c]
            elif i >= 3 and j < 3:
                A[i,j] = R[a,c] * R[b,d] + R[a,d] * R[b,c]
            else:
                A[i,j] = R[a,c] * R[b,d] + R[a,d] * R[b,c]
    return A @ C @ A.T

def linear_slip_eff_horizontal(C, k, h_f):
    """
    Compute linear-slip effective stiffness for horizontal fractures
    (normal along x3) from given background C, hardness k and thickness h_f.
    Uses eqs (9)-(11) with Z from eq (36).
    """
    # extract 3x3 blocks N_b, P_b, M_b from C (Helbig & Schoenberg partition)
    N_b = C[2:5,2:5]  # rows/cols 2,3,4 (indices 2,3,4) in Python 0-index
    # Actually, N is the block of (c33,c34,c35; c34,c44,c45; c35,c45,c55)
    # So rows/cols indices 2,3,4
    N_b = C[2:5,2:5]
    # P_b: (c13,c14,c15; c23,c24,c25; c36,c46,c56) -> rows 0,1,5? Wait, the mapping:
    # c13 index (0,2), c14 (0,3), c15 (0,4)
    # c23 (1,2), c24 (1,3), c25 (1,4)
    # c36 (2,5), c46 (3,5), c56 (4,5)
    # So P_b is 3x3: first row: C[0,2], C[0,3], C[0,4]
    # second row: C[1,2], C[1,3], C[1,4]
    # third row: C[5,2], C[5,3], C[5,4] (since c36,c46,c56 correspond to (5,2),(5,3),(5,4) in 0-index? Actually c36 is at (2,5) but symmetric; P_b's third row is (c36, c46, c56) which are (2,5), (3,5), (4,5) in the 6x6 matrix. So we can take indices [2,3,4], [5] as rows, and [2,3,4] as cols for the last row.
    P_b = np.zeros((3,3))
    P_b[0,:] = [C[0,2], C[0,3], C[0,4]]
    P_b[1,:] = [C[1,2], C[1,3], C[1,4]]
    P_b[2,:] = [C[5,2], C[5,3], C[5,4]]
    # M_b: in-plane block, indices: c11(0,0),c12(0,1),c16(0,5); c12(1,0),c22(1,1),c26(1,5); c16(5,0),c26(5,1),c66(5,5)
    M_b = np.zeros((3,3))
    M_b[0,:] = [C[0,0], C[0,1], C[0,5]]
    M_b[1,:] = [C[1,0], C[1,1], C[1,5]]
    M_b[2,:] = [C[5,0], C[5,1], C[5,5]]

    # Z = h_f/k * inv(N_b) for the rotated background
    Z = h_f/k * np.linalg.inv(N_b)
    # N_e = inv(inv(N_b) + Z)
    N_e = np.linalg.inv(np.linalg.inv(N_b) + Z)
    # P_e = P_b @ inv(N_b) @ N_e
    P_e = P_b @ np.linalg.inv(N_b) @ N_e
    # M_e = M_b - P_b @ inv(N_b) @ P_b.T + P_b @ inv(N_b) @ N_e @ inv(N_b).T @ P_b.T
    M_e = M_b - P_b @ np.linalg.inv(N_b) @ P_b.T + P_b @ np.linalg.inv(N_b) @ N_e @ np.linalg.inv(N_b).T @ P_b.T

    # Assemble full 6x6 effective stiffness
    C_eff = np.zeros((6,6))
    # place M_e into top-left and bottom-right of in-plane axes
    C_eff[0,0], C_eff[0,1], C_eff[0,5] = M_e[0,0], M_e[0,1], M_e[0,2]
    C_eff[1,0], C_eff[1,1], C_eff[1,5] = M_e[1,0], M_e[1,1], M_e[1,2]
    C_eff[5,0], C_eff[5,1], C_eff[5,5] = M_e[2,0], M_e[2,1], M_e[2,2]
    # place P_e
    C_eff[0,2], C_eff[0,3], C_eff[0,4] = P_e[0,0], P_e[0,1], P_e[0,2]
    C_eff[1,2], C_eff[1,3], C_eff[1,4] = P_e[1,0], P_e[1,1], P_e[1,2]
    C_eff[5,2], C_eff[5,3], C_eff[5,4] = P_e[2,0], P_e[2,1], P_e[2,2]
    # symmetric entries
    C_eff[2,0], C_eff[3,0], C_eff[4,0] = P_e[0,0], P_e[0,1], P_e[0,2]
    C_eff[2,1], C_eff[3,1], C_eff[4,1] = P_e[1,0], P_e[1,1], P_e[1,2]
    C_eff[2,5], C_eff[3,5], C_eff[4,5] = P_e[2,0], P_e[2,1], P_e[2,2]
    # place N_e
    C_eff[2:5,2:5] = N_e
    return C_eff

def generalized_eff_x1(C_b, k, h_f):
    """Generalized effective stiffness for fractures normal to x1-axis, using Appendix B formulas (B4)-(B12)."""
    c11b, c12b, c13b, c22b, c23b, c33b, c44b, c55b, c66b = C_b[0,0], C_b[0,1], C_b[0,2], C_b[1,1], C_b[1,2], C_b[2,2], C_b[3,3], C_b[4,4], C_b[5,5]
    denom = c11b * h_f + c33b * k - c33b * h_f * k
    c11 = (c11b * c33b * k) / denom
    c22 = h_f*k*(c22b - c23b**2/c33b) + (1-h_f)*(c22b - c12b**2/c11b) + (c11b*c33b*k * (c12b*(1-h_f)/c11b + c23b*h_f/c33b)**2) / denom
    c33 = h_f*k*(c11b - c13b**2/c33b) + (1-h_f)*(c33b - c13b**2/c11b) + (c11b*c33b*k * (c13b*(1-h_f)/c11b + c13b*h_f/c33b)**2) / denom
    c12 = (c12b*c33b*k + c11b*c23b*h_f*k - c12b*c33b*h_f*k) / denom
    c13 = (c13b*k*(c33b + c11b*h_f - c33b*h_f)) / denom
    term = (c11b*c33b*k * (c13b*(1-h_f)/c11b + c13b*h_f/c33b) * (c12b*(1-h_f)/c11b + c23b*h_f/c33b)) / denom
    c23 = h_f*k*(c12b - c13b*c23b/c33b) + (1-h_f)*(c23b - c12b*c13b/c11b) + term
    c44 = c44b - c44b*h_f + c66b*h_f*k
    c55 = (c55b*k) / (h_f + k - h_f*k)
    c66 = (c66b*c44b*k) / (c66b*h_f + c44b*k - c44b*h_f*k)
    C_eff = np.zeros((6,6))
    C_eff[0,0], C_eff[0,1], C_eff[0,2] = c11, c12, c13
    C_eff[1,0], C_eff[1,1], C_eff[1,2] = c12, c22, c23
    C_eff[2,0], C_eff[2,1], C_eff[2,2] = c13, c23, c33
    C_eff[3,3] = c44
    C_eff[4,4] = c55
    C_eff[5,5] = c66
    return C_eff

def linear_slip_eff_x1(C_b, k, h_f):
    """Linear-slip effective stiffness for fractures normal to x1-axis, via rotation."""
    # rotation matrix R: new axes: x' = -x3, y' = x2, z' = x1
    R = np.array([[0,0,-1],[0,1,0],[1,0,0]])
    C_b_rot = bond_rotation(C_b, R)
    C_l_rot = linear_slip_eff_horizontal(C_b_rot, k, h_f)
    # rotate back: inverse of R is transpose
    C_l = bond_rotation(C_l_rot, R.T)
    return C_l

def relative_error(C_b, C_eff, C_l_eff):
    """Relative error in percent, eq (33)."""
    delta_l = C_b - C_l_eff
    delta = C_b - C_eff
    norm_diff = np.linalg.norm(delta_l - delta)
    norm_delta_l = np.linalg.norm(delta_l)
    if norm_delta_l == 0:
        return 0.0
    return 100.0 * norm_diff / norm_delta_l

output_path = os.path.join(os.environ.get('OUTDIR','/app/outputs'), 'step_01_err_data.csv')

scenarios = []
# vary_k: h_f=1e-5, k from 1e-6 to 1
h_f_fixed = 1e-5
k_vals = np.logspace(-6, 0, 20)
for k in k_vals:
    scenarios.append(('vary_k', k, h_f_fixed, k))

# vary_hf: k=1e-5, h_f from 1e-6 to 1
k_fixed = 1e-5
h_vals = np.logspace(-6, 0, 20)
for h_f in h_vals:
    scenarios.append(('vary_hf', h_f, k_fixed, h_f))

# cumul_Z10: k/h_f=10, vary h_f
h_f_vals = np.logspace(-6, 0, 20)
for h_f in h_f_vals:
    k = 10 * h_f
    scenarios.append(('cumul_Z10', h_f, k, h_f))

# cumul_Z1: k/h_f=1
for h_f in h_f_vals:
    k = h_f
    scenarios.append(('cumul_Z1', h_f, k, h_f))

# cumul_Z05: k/h_f=0.5
for h_f in h_f_vals:
    k = 0.5 * h_f
    scenarios.append(('cumul_Z05', h_f, k, h_f))

with open(output_path, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['scenario','parameter_value','err_percent'])
    for scenario, p_val, k, h_f in scenarios:
        C_eff = generalized_eff_x1(C_b, k, h_f)
        C_l_eff = linear_slip_eff_x1(C_b, k, h_f)
        err = relative_error(C_b, C_eff, C_l_eff)
        writer.writerow([scenario, p_val, err])

print(f"Written {output_path}")
PYEOF

# === solve block: step_02_slowness_surfaces.csv ===
python3 /solution/step02.py
