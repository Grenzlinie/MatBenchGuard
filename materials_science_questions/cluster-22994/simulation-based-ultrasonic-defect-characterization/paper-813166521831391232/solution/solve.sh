#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
python3 -m pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple numpy scipy
mkdir -p /app/outputs

# === solve block: dispersion_curves.csv ===
python3 << 'PYEOF' > $OUTDIR/dispersion_curves.csv
import numpy as np
from scipy.linalg import svd

# --- Chebyshev differentiation matrices ---
def cheb(N):
    """Return differentiation matrices D (1st) and D2 (2nd) on [-1,1], and nodes x."""
    if N==0:
        return np.zeros((1,1)), np.zeros((1,1)), np.array([0.0])
    n = np.arange(0, N+1)
    x = np.cos(np.pi*n/N)
    c = np.ones(N+1); c[0] = 2; c[N] = 2
    c *= (-1)**n
    X = x[:, np.newaxis]
    dX = X - X.T + np.eye(N+1)                     # avoid div‑by‑zero
    D = np.zeros((N+1, N+1))
    for i in range(N+1):
        for j in range(N+1):
            if i != j:
                D[i,j] = (c[i]/c[j]) / (x[i]-x[j])
    for i in range(N+1):
        D[i,i] = -np.sum(np.delete(D[i,:], i))
    D2 = D @ D
    return D, D2, x

# --- Material and geometry ---
rho = 2800.0                    # kg/m3
E   = 70e9                      # Pa (aluminium)
nu  = 0.33
lam = E*nu/((1+nu)*(1-2*nu))
mu  = E/(2*(1+nu))
C11 = lam + 2*mu
C12 = lam
# other C_ij = 0 for isotropic

b   = 0.4                       # m, outer radius
h   = 0.001                     # m, thickness
a   = b - h                     # inner radius

# --- Chebyshev grid (number of points) ---
N = 30                          # sufficient accuracy
Dx, Dxx, xc = cheb(N)          # x in [-1,1]
r = a + (b-a)*(xc + 1)/2        # radial coordinate in [a,b]
drdx = (b-a)/2                  # constant
D1_r = (1/drdx) * Dx            # d/dr
D2_r = (1/drdx**2) * Dxx        # d^2/dr^2

int_idx = np.arange(1, N)       # interior points
bnd_idx = np.array([0, N])      # boundaries

# --- Build system matrix A(k; omega) ---
def build_matrix(k, omega):
    """
    Assembles the (3*(N+1))x(3*(N+1)) complex matrix for given
    wavenumber k [rad/m] and angular frequency omega [rad/s].
    """
    M = 3*(N+1)
    A = np.zeros((M, M), dtype=complex)
    
    # helper: block offsets for U, V, W
    Uoff = 0
    Voff = N+1
    Woff = 2*(N+1)
    
    # Interior equations (4)-(6) placed at rows of interior points
    for i in int_idx:
        ri = r[i]
        ri2 = ri*ri
        
        # ---- U equation (4) ----
        # U terms
        ud2 = ri2 * C11
        ud1 = 2*ri * C11
        ud0 = -( (2 + k**2*b**2/2)*C11 - k**2*b**2*C12/2 ) + rho*ri2*omega**2
        
        for j in range(N+1):
            A[i, Uoff+j] = ud2 * D2_r[i,j] + ud1 * D1_r[i,j] + (ud0 if j==i else 0)
        
        # W terms
        wd1 = 1j * ri * k * b * (C12 + C11) / 2
        wd0 = 1j * k * b * (-1.5*C11 + 0.5*C12)
        for j in range(N+1):
            A[i, Woff+j] = wd1 * D1_r[i,j] + (wd0 if j==i else 0)
        
        # ---- V equation (5) ----
        rowV = i + (N+1)
        vd2 = ri2 * (C11 - C12) / 2
        vd1 = ri * (C11 - C12)          # C14=C56=0
        vd0 = -( C11 + k**2*b**2*(C11-C12)/2 ) + rho*ri2*omega**2
        for j in range(N+1):
            A[rowV, Voff+j] = vd2 * D2_r[i,j] + vd1 * D1_r[i,j] + (vd0 if j==i else 0)
        
        # ---- W equation (6) ----
        rowW = i + 2*(N+1)
        ww_d2 = ri2 * (C11 - C12) / 2
        ww_d1 = ri * (C11 - C12)
        ww_d0 = ( (C12-C11)/2 - k**2*b**2*C11 ) + rho*ri2*omega**2
        for j in range(N+1):
            A[rowW, Woff+j] = ww_d2 * D2_r[i,j] + ww_d1 * D1_r[i,j] + (ww_d0 if j==i else 0)
        
        u2d1 = 1j * ri * k * b * (C11 - C12) / 2
        u2d0 = 2j * k * b * C11
        for j in range(N+1):
            A[rowW, Uoff+j] = u2d1 * D1_r[i,j] + (u2d0 if j==i else 0)
    
    # Boundary conditions at r=a (i=0) and r=b (i=N)
    for idx_b in bnd_idx:
        rb = r[idx_b]
        # BC1: u equation
        rowB1 = idx_b
        for j in range(N+1):
            A[rowB1, Uoff+j] = rb*C11 * D1_r[idx_b,j] + (-2*C12 if j==idx_b else 0)
            A[rowB1, Woff+j] = (1j*k*b*C12 if j==idx_b else 0)
        # BC2: v equation
        rowB2 = idx_b + (N+1)
        for j in range(N+1):
            A[rowB2, Voff+j] = rb*(C11-C12)/2 * D1_r[idx_b,j] + (-(C11-C12)/2 if j==idx_b else 0)
        # BC3: w equation
        rowB3 = idx_b + 2*(N+1)
        for j in range(N+1):
            A[rowB3, Woff+j] = rb*(C11-C12)/2 * D1_r[idx_b,j] + (-(C11-C12)/2 if j==idx_b else 0)
            A[rowB3, Uoff+j] = (1j*k*b*(C11-C12)/2 if j==idx_b else 0)
    
    return A

# --- Search for eigenvalues at given omega ---
def find_velocities(omega, n_modes=6, v_range=(500, 12000), n_samples=400):
    """
    Scan phase velocity v [m/s] and return list of v where the smallest
    singular value has a local minimum (potential guided‑wave modes).
    """
    vs = np.linspace(v_range[0], v_range[1], n_samples)
    svals = np.zeros(len(vs))
    for idx, v in enumerate(vs):
        k = omega / v
        A = build_matrix(k, omega)
        # smallest singular value
        s = svd(A, compute_uv=False)
        svals[idx] = s[-1]
    # find local minima (excluding first/last point)
    minima_idx = []
    for i in range(1, len(vs)-1):
        if svals[i] < svals[i-1] and svals[i] < svals[i+1] and svals[i] < 1e-6:
            minima_idx.append(i)
    # refine by quadratic interpolation
    refined_v = []
    for i in minima_idx:
        v0, s0 = vs[i-1], svals[i-1]
        v1, s1 = vs[i],   svals[i]
        v2, s2 = vs[i+1], svals[i+1]
        # fit parabola s = a*(v - v1)^2 + s1
        # solve for vertex
        a = ( (s2-s1)/(v2-v1) - (s0-s1)/(v0-v1) ) / ( (v2+v1) - (v0+v1) )
        v_star = v1 - ( (s2-s1)/(v2-v1) - 2*a*v1 )/(2*a) if abs(a)>1e-20 else v1
        refined_v.append(v_star)
    # sort ascending
    refined_v.sort()
    return refined_v[:n_modes]

# --- Main computation ---
freqs = np.linspace(10e3, 1e6, 50)   # 10 kHz to 1 MHz, 50 steps
prev_modes = []
mode_counter = 0
print("frequency_Hz,mode_number,phase_velocity_m_per_s")
for f in freqs:
    omega = 2*np.pi*f
    v_list = find_velocities(omega, n_modes=6, v_range=(500, 12000), n_samples=400)
    # mode tracking: match to previous modes by minimum distance in v
    if len(prev_modes) == 0:
        # first frequency: assign mode numbers 1,2,...
        for j, v in enumerate(v_list):
            print(f"{f:.6e},{j+1},{v:.6f}")
        prev_modes = v_list
    else:
        # Hungarian matching on absolute difference
        n_prev = len(prev_modes)
        n_cur  = len(v_list)
        # simple greedy: for each current mode, find closest previous
        matched = []
        used = [False]*n_prev
        for v_cur in v_list:
            dists = [abs(v_cur - v_prev) for v_prev in prev_modes]
            # find best unused previous
            best_j = -1
            best_d = 1e9
            for j in range(n_prev):
                if not used[j] and dists[j] < best_d:
                    best_d = dists[j]
                    best_j = j
            matched.append((v_cur, best_j+1 if best_j != -1 else 0))
            if best_j != -1:
                used[best_j] = True
        # if any leftover previous modes not matched, skip (mode disappears)
        for v_cur, mid in matched:
            if mid > 0:
                print(f"{f:.6e},{mid},{v_cur:.6f}")
        # update prev_modes for next step (only the matched ones, in order)
        prev_modes = [m[0] for m in matched if m[1] > 0]
PYEOF
