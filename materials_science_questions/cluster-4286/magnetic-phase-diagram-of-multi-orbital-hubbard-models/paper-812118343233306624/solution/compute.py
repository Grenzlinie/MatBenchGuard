#!/usr/bin/env python3
"""Fast self-consistent mean-field solver to generate reference outputs."""

import sys
import os
import numpy as np

# ========== parameters ==========
N = 32  # k-grid size
V = 1.0
d_screen = 4.0
U_val = 4.8
T_hopping = 0.53   # for doping_hopping
T_order = 0.1      # for order_parameter
x_vals = np.arange(0.0, 0.21, 0.02)

# bare hopping parameters (key: (lx,ly) -> t)
t_params = {
    (1,0):  1.0,
    (1,1): -0.325,
    (2,0):  0.17,
    (2,1): -0.121,
    (2,2): -0.07
}

# build k-grid
kx = 2*np.pi * np.arange(N) / N
ky = 2*np.pi * np.arange(N) / N
KX, KY = np.meshgrid(kx, ky, indexing='ij')  # shape (N,N)
k_indices = [(ix, iy) for ix in range(N) for iy in range(N)]
KX_flat = KX.flatten()
KY_flat = KY.flatten()

def epsilon(kx, ky):
    """Band dispersion from bare hoppings."""
    e = 0.0
    # nearest-neighbour (1,0) / (0,1)
    e += -2*t_params[(1,0)] * (np.cos(kx) + np.cos(ky))
    # (1,1)
    e += -2*t_params[(1,1)] * (np.cos(kx+ky) + np.cos(kx-ky))
    # (2,0)
    e += -2*t_params[(2,0)] * (np.cos(2*kx) + np.cos(2*ky))
    # (2,1)
    e += -2*t_params[(2,1)] * (np.cos(2*kx+ky) + np.cos(2*kx-ky) +
                                 np.cos(kx+2*ky) + np.cos(kx-2*ky))
    # (2,2)
    e += -2*t_params[(2,2)] * (np.cos(2*kx+2*ky) + np.cos(2*kx-2*ky))
    return e

# precompute bare ε on the full grid
eps_k = epsilon(KX, KY)  # (N,N)
eps_k_flat = eps_k.flatten()

# Q-shift index (π,π)
shift = N // 2
# map Q-shift: (kx+π, ky+π) modulo 2π
# for grid points, we can shift the index by N/2 (periodic)
def eps_shifted(ix, iy):
    si = (ix + shift) % N
    sj = (iy + shift) % N
    return eps_k[si, sj]

# Coulomb interaction v_l and its Fourier transform v(k)
# truncated to vectors with |l| <= 10
v_dict = {}  # l -> v_l
max_r = 10
for lx in range(-max_r, max_r+1):
    for ly in range(-max_r, max_r+1):
        r = np.sqrt(lx*lx + ly*ly)
        if r < 1e-12:
            continue
        v_dict[(lx,ly)] = V * np.exp(-r/d_screen) / r

# Precompute v(k) for each k point on the grid
v_k = np.zeros((N,N), dtype=float)
for (lx,ly), vl in v_dict.items():
    v_k += vl * np.cos(lx*KX + ly*KY)   # real, symmetric

v_k_flat = v_k.flatten()

# ---------- paramagnetic self-consistent Σ^x ----------
def paramagnetic_solution(x, T):
    """
    Return converged (mu, Sigma_x_k) for given doping x and temperature T.
    """
    n_target = (1 + x) / 2.0   # per spin
    beta = 1.0 / T if T > 0 else 1e12
    # initialize Sigma_x to zero
    Sigma_k_flat = np.zeros(N*N, dtype=float)
    for _ in range(50):
        # effective dispersion
        eff_eps = eps_k_flat + Sigma_k_flat
        # find mu such that sum f = n_target * N^2
        mu_low = np.min(eff_eps) - 5.0
        mu_high = np.max(eff_eps) + 5.0
        for _bis in range(100):
            mu = 0.5*(mu_low + mu_high)
            occ = 1.0 / (1.0 + np.exp(beta*(eff_eps - mu)))
            n_est = np.mean(occ)
            if abs(n_est - n_target) < 1e-8:
                break
            if n_est > n_target:
                mu_low = mu
            else:
                mu_high = mu
        # new Sigma
        # Σ^x(k) = - (1/N^2) Σ_{k'} v(k-k') occ(k')
        # Use convolution via FFT? For small N we use loops.
        Sigma_new = np.zeros(N*N, dtype=float)
        # k' index loop
        for ikp in range(N*N):
            if occ[ikp] < 1e-15:
                continue
            # v(k - k') : note periodicity
            # Get k indices
            ik = np.arange(N*N)
            # Instead of double loop, we can vectorise: compute v(k - k') as a matrix
            # But N=32 gives 1024 points, so N^2 = 1e6, which is heavy but okay for a few iterations
        # I'll do a more efficient approach: use FFT for convolution
        # But to keep code simple, I'll just precompute a v-matrix V_mat[ik,ikp]? That's too large.
        # Instead, I'll use the fact that v(k - kp) = v(dk) where dk is difference.
        # I can reshape to 2D, use numpy.roll for convolution.
        pass
    # For brevity, I'll implement a lightweight version: assume Sigma_k is small initially and converge quickly.
    # Actually, I need the self-consistent loop. Since N=32, I can precompute v(k - k') using FFT-based convolution.
    # I'll do that.
    ... # placeholder
```

The code above is a sketch. To provide a complete working script, I'll need to implement the self-consistent paramagnetic solver efficiently using FFT-based convolution for Σ^x. Since I'm the solve author, I can include a fully functional implementation. I'll write a proper compute.py with all details.

Let's craft the full solution script with clear vectorised operations.

I'll write compute.py that runs and outputs the needed files.
