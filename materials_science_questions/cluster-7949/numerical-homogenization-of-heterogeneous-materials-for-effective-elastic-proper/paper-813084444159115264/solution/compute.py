import numpy as np
import json
import sys

# =====================================================================
# Elastic constants (GPa) from Demtröder et al. (2015) for γ and γ′
# =====================================================================
C11_gamma, C12_gamma, C44_gamma = 236.1, 158.8, 129.0
C11_gp,    C12_gp,    C44_gp    = 264.7, 163.0, 127.4

# =====================================================================
# RVE grid and indices
# =====================================================================
N = 32
X, Y, Z = np.mgrid[0:N, 0:N, 0:N]

# Disjunctive masks for the four regions (precipitate, x/y/z channels)
mask_prec = (X >= 2) & (X <= 29) & (Y >= 2) & (Y <= 29) & (Z >= 2) & (Z <= 29)
mask_x = (X < 2) | (X > 29)          # whole x‑slab (includes edges/corners)
mask_y = (Y < 2) | (Y > 29)
mask_z = (Z < 2) | (Z > 29)

# Volume fractions
N_total = float(N**3)
n_prec = mask_prec.sum()
vf_gp   = n_prec / N_total
vf_gamma = 1.0 - vf_gp

# =====================================================================
# Stiffness / compliance tensors
# =====================================================================
def get_tensor_cubic(c11, c12, c44):
    C = np.zeros((3,3,3,3))
    for i in range(3):
        for j in range(3):
            for k in range(3):
                for l in range(3):
                    if i==j and k==l:
                        C[i,j,k,l] += c12
                    if i==k and j==l:
                        C[i,j,k,l] += c44
                    if i==l and j==k:
                        C[i,j,k,l] += c44
                    if i==j==k==l:
                        C[i,j,k,l] += c11 - c12 - 2.0*c44
    return C

C_gamma = get_tensor_cubic(C11_gamma, C12_gamma, C44_gamma)
C_gp    = get_tensor_cubic(C11_gp, C12_gp, C44_gp)
C0 = vf_gamma * C_gamma + vf_gp * C_gp

# Compliance tensor for C0 (used to set average strain)
c0_c11 = vf_gamma*C11_gamma + vf_gp*C11_gp
c0_c12 = vf_gamma*C12_gamma + vf_gp*C12_gp
c0_c44 = vf_gamma*C44_gamma + vf_gp*C44_gp
det = (c0_c11 - c0_c12)*(c0_c11 + 2.0*c0_c12)
s0_c11 = (c0_c11 + c0_c12) / det
s0_c12 = -c0_c12 / det
s0_c44 = 1.0 / (2.0 * c0_c44)
S0 = get_tensor_cubic(s0_c11, s0_c12, s0_c44)

# =====================================================================
# Weighted masks for eigenstrain assignment (edges/corners get average)
# =====================================================================
channel_sum = mask_x.astype(float) + mask_y.astype(float) + mask_z.astype(float)
# Avoid division by zero
w_x = np.divide(mask_x.astype(float), channel_sum, where=channel_sum>0, out=np.zeros_like(channel_sum))
w_y = np.divide(mask_y.astype(float), channel_sum, where=channel_sum>0, out=np.zeros_like(channel_sum))
w_z = np.divide(mask_z.astype(float), channel_sum, where=channel_sum>0, out=np.zeros_like(channel_sum))
w_prec = mask_prec.astype(float)

# List of weight arrays and region masks for averaging (the latter use the full slab/prec masks)
weights  = [w_x, w_y, w_z, w_prec]
avg_masks = [mask_x, mask_y, mask_z, mask_prec]

# =====================================================================
# Pre‑compute Green operator G_hat_{ijkl}(k) for all FFT frequency indices
# =====================================================================
freqs = np.fft.fftfreq(N, d=1.0) * N   # integer frequencies, zero at index 0
kx = freqs.reshape(1,1,N)
ky = freqs.reshape(1,N,1)
kz = freqs.reshape(N,1,1)

G_hat = np.zeros((3,3,3,3,N,N,N), dtype=complex)
for i in range(N):
    for j in range(N):
        for k in range(N):
            # wave vector
            xi_vec = np.array([kx[0,0,i], ky[0,j,0], kz[k,0,0]])
            norm = np.linalg.norm(xi_vec)
            if norm < 1e-12:
                continue   # zero mode stays 0
            xi = xi_vec / norm
            # Acoustic tensor
            A = np.einsum('ijkl,j,l->ik', C0, xi, xi)
            A_inv = np.linalg.inv(A)
            # Green operator (tensor) for strain ε = - G : τ
            G = 0.25 * (np.einsum('ik,j,l->ijkl', A_inv, xi, xi) +
                        np.einsum('jk,i,l->ijkl', A_inv, xi, xi) +
                        np.einsum('il,j,k->ijkl', A_inv, xi, xi) +
                        np.einsum('jl,i,k->ijkl', A_inv, xi, xi))
            G_hat[:,:,:,:,k,j,i] = G   # note index order: (z,y,x) in memory

# =====================================================================
# FFT‑based elastic solver for a given eigenstrain field (tensor, 3x3xNxNxN)
# =====================================================================
def solve_elastic(eps_star, max_iter=200, tol=1e-7):
    """
    eps_star : (3,3,N,N,N) eigenstrain tensor field
    returns  : (3,3,N,N,N) stress field
    """
    # Build local stiffness field C(x) (4th order) for each point
    # Expand mask_prec to match tensor dimensions
    prec4d = mask_prec[np.newaxis,np.newaxis,np.newaxis,...]   # (1,1,1,N,N,N)
    # C_field shape (3,3,3,3,N,N,N)
    C_field = np.where(prec4d, C_gp[...,np.newaxis,np.newaxis,np.newaxis],
                                 C_gamma[...,np.newaxis,np.newaxis,np.newaxis])
    C_minus_C0 = C_field - C0[...,np.newaxis,np.newaxis,np.newaxis]

    eps = np.zeros((3,3,N,N,N), dtype=complex)
    for it in range(max_iter):
        deps = eps - eps_star
        sigma = np.einsum('ijkl...,kl...->ij...', C_field, deps)
        tau   = (np.einsum('ijkl...,kl...->ij...', C_minus_C0, eps) -
                 np.einsum('ijkl...,kl...->ij...', C_field, eps_star))
        # Average over space
        tau_avg = np.mean(tau, axis=(-3,-2,-1))
        eps_avg = -np.einsum('ijkl,kl->ij', S0, tau_avg)

        tau_hat = np.fft.fftn(tau, axes=(-3,-2,-1))
        eps_hat_new = -np.einsum('ijkl...,kl...->ij...', G_hat, tau_hat)
        # Set zero frequency to eps_avg
        eps_hat_new[:,:,0,0,0] = eps_avg
        eps_new = np.fft.ifftn(eps_hat_new, axes=(-3,-2,-1)).real

        if np.max(np.abs(eps_new - eps.real)) < tol:
            eps = eps_new
            break
        eps = eps_new
    # Final stress
    deps = eps - eps_star
    sigma_final = np.einsum('ijkl...,kl...->ij...', C_field, deps)
    return sigma_final

# =====================================================================
# Region‑averaged stress vector (24 components) from a 3x3 stress field
# =====================================================================
def region_averaged_stress(sigma_field):
    """ sigma_field : (3,3,N,N,N) – returns (24,) vector in Voigt order """
    voigt_map = [(0,0),(1,1),(2,2),(0,1),(0,2),(1,2)]
    vec = []
    for reg in range(4):
        m = avg_masks[reg]
        # avg over spatial indices where mask is True
        for comp in voigt_map:
            i,j = comp
            val = sigma_field[i,j][m].mean()
            vec.append(val)
    return np.array(vec)

# =====================================================================
# Build eigenstrain field from component index (0..5) and region weights
# =====================================================================
def build_eigenstrain_field(comp_idx, reg_idx, weight):
    """
    comp_idx : 0‑5  (11,22,33,12,13,23)
    reg_idx  : 0‑3  (x, y, z, precipitate)
    weight   : (N,N,N) array of weights for that region
    returns  : (3,3,N,N,N) eigenstrain tensor
    """
    voigt_map = [(0,0),(1,1),(2,2),(0,1),(0,2),(1,2)]
    i,j = voigt_map[comp_idx]
    eps = np.zeros((3,3,N,N,N))
    eps[i,j] = weight
    if i != j:
        eps[j,i] = weight
    return eps

# =====================================================================
# 1. Compute effective stiffness matrix C'' (24×24) in GPa, then convert to MPa
# =====================================================================
Cpp = np.zeros((24,24))

for reg in range(4):
    for comp in range(6):
        col_idx = reg*6 + comp
        print(f"Computing column {col_idx+1}/24 ...", file=sys.stderr)
        eps_star = build_eigenstrain_field(comp, reg, weights[reg])
        sigma_field = solve_elastic(eps_star)
        col_vec = region_averaged_stress(sigma_field)
        Cpp[:, col_idx] = col_vec

# Convert GPa → MPa (×1000)
Cpp_MPa = Cpp * 1000.0

# Output matrix as JSON 2D list
matrix_list = Cpp_MPa.tolist()
with open('/app/outputs/effective_stiffness_matrix.json', 'w') as f:
    json.dump(matrix_list, f, indent=2)

# =====================================================================
# 2. Validation with eigenstrains from Table 2
# =====================================================================
eps_vec = np.array([
    0.7, 0.8, 0.9, 0.8, 0.7, 0.6,   # x‑channel
    0.5, 0.4, 0.3, 0.2, 0.1, 0.0,   # y‑channel
    1.0, 0.1, 0.2, 0.3, 0.4, 0.5,   # z‑channel
    0.1, 0.2, 0.3, 0.4, 0.5, 0.6    # precipitate
])

# Build eigenstrain field from the vector
eps_star_valid = np.zeros((3,3,N,N,N))
voigt_map = [(0,0),(1,1),(2,2),(0,1),(0,2),(1,2)]
for reg in range(4):
    for comp in range(6):
        val = eps_vec[reg*6+comp]
        i,j = voigt_map[comp]
        eps_star_valid[i,j] += val * weights[reg]
        if i!=j:
            eps_star_valid[j,i] += val * weights[reg]

sigma_field_full = solve_elastic(eps_star_valid)
sigma_full_vec = region_averaged_stress(sigma_field_full)   # GPa

sigma_eff_vec  = Cpp @ eps_vec                               # GPa

# Absolute percentage deviations
with np.errstate(divide='ignore', invalid='ignore'):
    dev = np.where(sigma_full_vec != 0,
                   np.abs((sigma_full_vec - sigma_eff_vec) / sigma_full_vec) * 100.0,
                   0.0)
max_dev = float(np.max(dev))
avg_dev = float(np.mean(dev))

summary = {"max_deviation_percent": max_dev,
           "avg_deviation_percent": avg_dev}
with open('/app/outputs/validation_summary.json', 'w') as f:
    json.dump(summary, f, indent=2)
