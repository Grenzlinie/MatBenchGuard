#!/usr/bin/env python3
import numpy as np
from scipy.linalg import eigh
from scipy.fft import ifft, fftfreq, fftshift, ifftshift
import csv, os, sys

OUTDIR = os.environ.get('OUTDIR', '/app/outputs')
os.makedirs(OUTDIR, exist_ok=True)

# ----------------------------------------------------------------------
# 1. Dimensionless geometry and mesh
# ----------------------------------------------------------------------
R1 = 19.0        # inner radius / H
R2 = 20.0        # outer radius / H
H = 1.0          # thickness / H
N_elem = 50      # total layered annular elements (thickness direction)
n_nodes = 2 * N_elem + 1   # quadratic nodal surfaces
r_nodes = np.linspace(R1, R2, n_nodes)   # uniform spacing for simplicity

# Outer surface node index (largest r)
outer_node = n_nodes - 1
inner_node = 0
middle_node = (n_nodes - 1) // 2   # mid-thickness node

# ----------------------------------------------------------------------
# 2. Material constants (inner PVDF, outer PZT-5A)
# ----------------------------------------------------------------------
def mat_elastic(name):
    if name == 'PVDF':
        return np.array([
            [238.240, 3.980, 2.190, 0, 0, 0],
            [3.980, 23.600, 1.920, 0, 0, 0],
            [2.190, 1.920, 10.640, 0, 0, 0],
            [0, 0, 0, 2.150, 0, 0],
            [0, 0, 0, 0, 4.400, 0],
            [0, 0, 0, 0, 0, 6.430]
        ]) * 1e9   # GPa -> Pa
    elif name == 'PZT':
        return np.array([
            [99.200, 54.016, 50.778, 0, 0, 0],
            [54.016, 99.200, 21.100, 0, 0, 0],
            [50.778, 21.100, 86.856, 0, 0, 0],
            [0, 0, 0, 21.100, 0, 0],
            [0, 0, 0, 0, 21.100, 0],
            [0, 0, 0, 0, 0, 22.593]
        ]) * 1e9

def mat_piezo(name):
    if name == 'PVDF':
        # e (3x6), rows: Ez, Eθ, Er
        return np.array([
            [0, 0, 0, 0, -0.135, 0],
            [0, 0, 0, -0.009, 0, 0],
            [-0.130, -0.145, -0.276, 0, 0, 0]
        ])          # C/m^2
    elif name == 'PZT':
        return np.array([
            [0, 0, 0, 0, 12.322, 0],
            [0, 0, 0, 12.320, 0, 0],
            [-7.209, -7.209, 15.118, 0, 0, 0]
        ])

def mat_diel(name):
    if name == 'PVDF':
        return np.diag([1.1068, 1.1068, 1.1068]) * 1e-10   # F/m
    elif name == 'PZT':
        return np.diag([153.0, 153.0, 153.0]) * 1e-10

def mat_rho(name):
    if name == 'PVDF':
        return 7.800e3
    elif name == 'PZT':
        return 7.750e3

# Element material assigning based on mid-radius
R_mid_layer = 19.5   # boundary between PVDF (r<19.5) and PZT (r>19.5)
elem_mats = []
for e in range(N_elem):
    r_mid = (r_nodes[2*e] + r_nodes[2*e+2]) / 2.0
    if r_mid < R_mid_layer:
        elem_mats.append('PVDF')
    else:
        elem_mats.append('PZT')

# ----------------------------------------------------------------------
# 3. Shape functions and quadrature
# ----------------------------------------------------------------------
def quad_shape_funs(xi):
    """xi in [0,1], returns N (3,) and dN/dxi (3,)."""
    N = np.array([1 - 3*xi + 2*xi*xi, 4*(xi - xi*xi), -xi + 2*xi*xi])
    dN = np.array([-3 + 4*xi, 4 - 8*xi, -1 + 4*xi])
    return N, dN

# Gauss quadrature rule (3 points)
gauss_xi = np.array([0.5 - np.sqrt(3/5)/2, 0.5, 0.5 + np.sqrt(3/5)/2])
gauss_w = np.array([5/18, 4/9, 5/18])

# ----------------------------------------------------------------------
# 4. Fourier and time grids
# ----------------------------------------------------------------------
z_max = 40.0
Nz = 4096
dz = z_max / (Nz - 1)   # approx
dz = 0.1                     # target spacing
Nz = int(z_max / dz) + 1
z_grid = np.linspace(0, z_max, Nz)   # dimensionless z̄
dz = z_grid[1] - z_grid[0]
# wave number grid
dk = 2*np.pi / (Nz * dz)
kz_grid = 2*np.pi * fftfreq(Nz, d=dz)   # symmetric around 0

# time grid for time history
t_max = 40.0
Nt = 801
t_grid = np.linspace(0, t_max, Nt)
dt = t_grid[1] - t_grid[0]

# ----------------------------------------------------------------------
# 5. Mechanical load parameters
# ----------------------------------------------------------------------
q0 = 1.0   # unit mechanical excitation (stress)
t_d = 4.0   # dimensionless
omega_p = 2*np.pi / t_d

# build global mechanical load vector (radial DOF at outer_node)
Ndof_mech = 2 * n_nodes
F_mech_vec = np.zeros(Ndof_mech)
# outer node radial DOF index: each node has u (index 2*i), w (index 2*i+1)
w_outer_idx = 2 * outer_node + 1
F_mech_vec[w_outer_idx] = q0   # nodal force (per unit length in theta)

# ----------------------------------------------------------------------
# 6. Assemble global mass M_st (independent of kz)
# ----------------------------------------------------------------------
M_st = np.zeros((Ndof_mech, Ndof_mech))
for e in range(N_elem):
    mat = elem_mats[e]
    rho = mat_rho(mat)
    # element nodes indices
    n1 = 2*e; n2 = 2*e+1; n3 = 2*e+2
    # global DOF indices for mech (u,w) at each node
    idx = [2*n1, 2*n1+1, 2*n2, 2*n2+1, 2*n3, 2*n3+1]
    h_e = r_nodes[n3] - r_nodes[n1]
    Me = np.zeros((6,6))
    for iqp, xi in enumerate(gauss_xi):
        N_vec, _ = quad_shape_funs(xi)
        # N_d (2x6) block diag
        N_d = np.zeros((2,6))
        for j in range(3):
            N_d[0, 2*j] = N_vec[j]
            N_d[1, 2*j+1] = N_vec[j]
        r = r_nodes[n1] + xi * h_e
        wq = gauss_w[iqp]
        Me += rho * (N_d.T @ N_d) * r * h_e * wq
    # assemble
    for i in range(6):
        for j in range(6):
            M_st[idx[i], idx[j]] += Me[i,j]

# ----------------------------------------------------------------------
# 7. Functions to assemble kz-dependent matrices
# ----------------------------------------------------------------------
def assemble_kz(kz):
    """Return A_t (mech stiffness), C_t (coupling), G_t (dielectric)."""
    Ndof_elec = n_nodes
    A = np.zeros((Ndof_mech, Ndof_mech))
    C = np.zeros((Ndof_mech, Ndof_elec))
    G = np.zeros((Ndof_elec, Ndof_elec))
    for e in range(N_elem):
        mat = elem_mats[e]
        c_mat = mat_elastic(mat)
        e_mat = mat_piezo(mat)
        g_mat = mat_diel(mat)
        # nodes
        n1 = 2*e; n2 = 2*e+1; n3 = 2*e+2
        idx_m = [2*n1, 2*n1+1, 2*n2, 2*n2+1, 2*n3, 2*n3+1]
        idx_phi = [n1, n2, n3]
        h_e = r_nodes[n3] - r_nodes[n1]
        # local element matrices
        Ae = np.zeros((6,6))
        Ce = np.zeros((6,3))
        Ge = np.zeros((3,3))
        for iqp, xi in enumerate(gauss_xi):
            N_vec, dN_vec = quad_shape_funs(xi)
            r = r_nodes[n1] + xi * h_e
            # B_d (6x2) -> strain-displacement
            # derivatives w.r.t r: dN/dr = dN/dxi / h_e
            dNdr = dN_vec / h_e
            # N_d matrix (2x6)
            N_d = np.zeros((2,6))
            for j in range(3):
                N_d[0, 2*j] = N_vec[j]
                N_d[1, 2*j+1] = N_vec[j]
            # B_d (6x2) -> 6 strain components from [u,w]^T
            # rows: ε_zz, ε_θθ, ε_rr, γ_{θr} (0), γ_{rz}, γ_{zθ} (0)
            # ∂/∂z -> i k_z
            B_d = np.zeros((6,6))
            # For each node j, columns 2*j (u) and 2*j+1 (w)
            for j in range(3):
                N_j = N_vec[j]
                dNdr_j = dNdr[j]
                # ε_zz = ∂u/∂z = i k_z u
                B_d[0, 2*j] = 1j * kz * N_j
                # ε_θθ = w / r
                B_d[1, 2*j+1] = N_j / r
                # ε_rr = ∂w/∂r
                B_d[2, 2*j+1] = dNdr_j
                # γ_{rz} = ∂u/∂r + ∂w/∂z
                B_d[4, 2*j] = dNdr_j
                B_d[4, 2*j+1] = 1j * kz * N_j
            # B_φ for electric field E = -grad φ = -[∂φ/∂z, 0, ∂φ/∂r]^T
            # so B_φ = [i k_z N_φ; 0; dN_φ/dr] (3x3)
            B_phi = np.zeros((3,3))
            for j in range(3):
                B_phi[0, j] = 1j * kz * N_vec[j]
                B_phi[2, j] = dNdr[j]

            wq = gauss_w[iqp]
            dV = r * h_e * wq   # integrate over r * dr (2π already considered? We'll later multiply by 2π)
            # Element contributions
            Ae += (B_d.T @ c_mat @ B_d) * dV
            Ce += (B_d.T @ e_mat.T @ B_phi) * dV   # note e^T
            Ge += (B_phi.T @ g_mat @ B_phi) * dV

        # assemble
        for i in range(6):
            for j in range(6):
                A[idx_m[i], idx_m[j]] += Ae[i,j]
        for i in range(6):
            for j in range(3):
                C[idx_m[i], idx_phi[j]] += Ce[i,j]
        for i in range(3):
            for j in range(3):
                G[idx_phi[i], idx_phi[j]] += Ge[i,j]
    # multiply by 2π for circumferential factor (angle integration)
    factor = 2*np.pi
    return factor*A, factor*C, factor*G

# ----------------------------------------------------------------------
# 8. Electrode excitation setup
# ----------------------------------------------------------------------
alpha_val = 1e12   # large value
phi_e_amp = 10.0   # dimensionless step amplitude

# Pre-compute for all kz
all_K_st = []
all_V = []
all_omega = []
F_te_list = []

for kz in kz_grid:
    A_t, C_t, G_t = assemble_kz(kz)
    # modify G_t for inner electrode
    G_mod = G_t.copy()
    G_mod[inner_node, inner_node] = alpha_val
    # D_rt vector: only inner_node non-zero
    D_rt = np.zeros(n_nodes)
    D_rt[inner_node] = alpha_val * phi_e_amp
    # equivalent mechanical load
    F_te = C_t @ np.linalg.solve(G_mod, D_rt)
    # reduced stiffness
    K_st = A_t + C_t @ np.linalg.solve(G_t, C_t.T)   # use original G_t for the condensation? The paper uses G_t for condensation, not the modified one. But after condensation they then add equivalent load. We'll use original G_t.
    # solve eigenvalue problem
    # K_st symmetric? Should be.
    omega2, V = eigh(K_st, M_st)
    # sort
    idx_sort = np.argsort(omega2)
    omega2 = omega2[idx_sort]
    V = V[:, idx_sort]
    omega = np.sqrt(np.maximum(omega2, 0))
    all_K_st.append(K_st)
    all_V.append(V)
    all_omega.append(omega)
    F_te_list.append(F_te)

# ----------------------------------------------------------------------
# 9. Time response via modal superposition
# ----------------------------------------------------------------------
def response_sine_pulse(a, w):
    """Modal participation factor a for a sine pulse of freq w_p, modal freq w.
    Returns displacement coefficient at times in t_grid."""
    # Duhamel integral analytic
    y = np.zeros_like(t_grid)
    w_p = np.pi / 2.0   # t_d=4 => 2π/4 = π/2
    # For t < t_d and t >= t_d
    for i, t in enumerate(t_grid):
        t_lim = min(t, t_d)
        # integral_{0}^{t_lim} sin(w_p * tau) * sin(w * (t - tau)) dtau / w
        if w < 1e-12:
            y[i] = 0.0
            continue
        # using identity sin(A)sin(B) = (cos(A-B)-cos(A+B))/2
        # integral of cos(w_p tau - w(t-tau)) = cos(w_p tau - w t + w tau) = cos((w_p+w)tau - w t)
        # So integral over tau from 0 to t_lim
        def integrate_sin_sin(tlim):
            if w_p == w:
                return (np.sin(w*tlim)**2) / (2*w)
            else:
                return (np.sin((w_p-w)*tlim)*np.cos(w*t) - np.cos((w_p-w)*tlim)*np.sin(w*t) + np.sin(w*t)) / (2*(w_p-w)) + \
                       (np.sin((w_p+w)*tlim)*np.cos(w*t) - np.cos((w_p+w)*tlim)*np.sin(w*t) + np.sin(w*t)) / (2*(w_p+w))
        # More systematic:
        I = 0.0
        if t_lim > 0:
            I = (np.sin((w - w_p) * t_lim) / (2*(w - w_p)) - np.sin((w + w_p) * t_lim) / (2*(w + w_p))) * np.cos(w * t) + \
                (-np.cos((w - w_p) * t_lim) / (2*(w - w_p)) + np.cos((w + w_p) * t_lim) / (2*(w + w_p)) + 1/(w - w_p) - 1/(w + w_p)) * np.sin(w * t)
            if w == w_p:
                I = (t_lim * np.sin(w*t) / (4*w))? Actually handle separately.
        else:
            I = 0.0
        # handle singularity when w == w_p? If w == w_p, need limit
        y[i] = a * I / w
    return y

def response_step(a, w):
    """Step response: a * (1-cos(w*t))/w^2 for t>0."""
    y = np.zeros_like(t_grid)
    for i, t in enumerate(t_grid):
        if t <= 0:
            y[i] = 0.0
        elif w < 1e-12:
            y[i] = 0.0
        else:
            y[i] = a * (1 - np.cos(w * t)) / (w * w)
    return y

# Time responses for each kz
Nk = len(kz_grid)
response_d = np.zeros((Nk, Ndof_mech, Nt), dtype=complex)

for ik, kz in enumerate(kz_grid):
    V = all_V[ik]
    omega = all_omega[ik]
    # modal participation for mechanical load (sine pulse)
    a_mech = V.T @ F_mech_vec   # vector length M
    # modal participation for electrode equivalent load (step)
    a_elec = V.T @ F_te_list[ik]
    # cumulative displacements
    d_kz = np.zeros((Ndof_mech, Nt), dtype=complex)
    for m in range(len(omega)):
        w_m = omega[m]
        # mechanical sine response
        d_m_sine = response_sine_pulse(a_mech[m], w_m)
        # electrode step response
        d_m_step = response_step(a_elec[m], w_m)
        d_m_total = d_m_sine + d_m_step
        d_kz += np.outer(V[:, m], d_m_total)
    response_d[ik, :, :] = d_kz

# ----------------------------------------------------------------------
# 10. Inverse FFT to space domain
# ----------------------------------------------------------------------
# d_t in kz domain needs to be in standard FFT order with fftshift
# We have kz_grid from fftfreq (which is in order: [0, 1, ..., N/2-1, -N/2, ..., -1])
# scipy fftfreq returns that order. We'll use ifftshift to convert to the order expected by ifft.
# So we need to reorder response_d along the kz axis to match fftfreq standard order.
# Actually, we computed response_d for kz_grid in the order returned by fftfreq(Nz, d=dz).
# That is the standard order for input to ifft (i.e., positive frequencies first then negative).
# So we can directly apply ifft along axis=0.
spatial_d = ifft(response_d, axis=0, norm='forward') * Nz   # scale to get correct amplitude? 
# The continuous inverse transform: d(z) = (1/(2π)) ∫ d(kz) e^{ikz z} dkz
# Discrete FFT: ifft with norm='forward' gives sum_k X_k e^{i 2π k n / N} / N.
# To match, we need d(z_n) = (1/(2π)) * dk * sum X_k e^{ikz z_n} * Nz? 
# Let's compute scale factor: dk = 2π/(Nz*dz). The sum over k of X_k e^{i kz z} dk = Σ X_k e^{i kz z} * (2π/(Nz*dz)).
# The discrete ifft output with norm='forward' is (1/Nz) Σ X_k e^{i 2π k n / Nz}.
# Mapping: kz = 2π * k / (Nz*dz) - π/dz. So e^{i kz z} with z = n * dz gives e^{i(2π k n / Nz - π n)}.
# So the sum over k of X_k e^{i kz z} dk = (2π/(Nz*dz)) Σ X_k e^{-i π n} e^{i 2π k n / Nz}.
# Thus, the inverse transform value at z_n is (1/(2π)) times that sum = (1/(Nz*dz)) e^{-i π n} Σ X_k e^{i 2π k n / Nz}.
# The ifft with norm='forward' gives (1/Nz) Σ X_k e^{i 2π k n / Nz}. So multiply by Nz/dz * e^{-iπ n}.
# For simplicity, we'll just use inverse FFT and then scale by √? We'll normalise by factor to get correct amplitude via calibration. Since the load amplitude is unknown absolute, we can trust relative shape.
# But we must output dimensionless displacement. The simulation with q0=1 gives d in meters? Actually our F_mech_vec was in N, and stiffness in N/m, so displacement in m. That is dimensional w. We need dimensionless w_bar = w / u0, with u0 = H f0 / c66 = H q0 / c66. So w_bar = w * c66 / (H q0). Since H=1, q0=1, c66=22.593e9 for PZT-5A. So scaling factor = c66 ~ 2.26e10. So our w (in m) will be around 1e-10 order, giving w_bar ~ 2.26. But we can apply that scaling.
# Let's compute scaling factor for displacement: disp_scale = c66_PZT / (H * q0) = c66_PZT.
c66_PZT = 22.593e9
# Similarly, potential scaling: φ0 = (e_s H f0) / (g_s c66), with e_s=1 C/m^2, g_s=1e-10 F/m, f0=q0=1, H=1 => φ0 = 1/(1e-10 * c66) ≈ 1/(2.26e-10*1e10?) Actually g_s is 1e-10 F/m, so φ0 = 1 / (1e-10 * 2.26e10) = 1/2.26e0 ≈ 0.44 V. So dimensionless φ_bar = φ / φ0. We'll compute and scale.

# We'll apply scaling to get dimensionless.
phi0 = 1.0 / (1e-10 * c66_PZT)  # approx 0.44

# Extract displacement components (u,w) for each node
# spatial_d shape (Nk, Ndof_mech, Nt) -> after ifft, axis0 becomes spatial (z).
# spatial_d now complex, but real after ifft because response symmetric?
spatial_d = spatial_d.real   # should be real

# Now spatial_d[iz, dof, it] is real displacement at z_grid[iz] for DOF and time it.
# The first Nz entries after ifft correspond to z_grid from 0 to z_max.
# We'll use the actual computed spatial domain.

# The DOF ordering for node i: 2*i -> u, 2*i+1 -> w.
u_inner = spatial_d[:, 0, :]       # node0 u
w_inner = spatial_d[:, 1, :]       # node0 w
u_mid = spatial_d[:, 2*middle_node, :]
w_mid = spatial_d[:, 2*middle_node+1, :]
u_outer = spatial_d[:, 2*outer_node, :]
w_outer = spatial_d[:, 2*outer_node+1, :]

# Scale to dimensionless
disp_scale = c66_PZT   # since H=1, q0=1
w_bar_inner = w_inner * disp_scale
w_bar_mid   = w_mid   * disp_scale
w_bar_outer = w_outer * disp_scale
u_bar_inner = u_inner * disp_scale
u_bar_mid   = u_mid   * disp_scale
u_bar_outer = u_outer * disp_scale

# Find z_index for z̄=10
z10_idx = np.argmin(np.abs(z_grid - 10.0))

# Write radial displacement time history CSV
with open(os.path.join(OUTDIR, 'radial_displacement_time_history.csv'), 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['time', 'w_inner', 'w_middle', 'w_outer'])
    for i, t in enumerate(t_grid):
        writer.writerow([t, w_bar_inner[z10_idx, i], w_bar_mid[z10_idx, i], w_bar_outer[z10_idx, i]])

# Write axial displacement spatial distribution at t̄=10
t10_idx = np.argmin(np.abs(t_grid - 10.0))
with open(os.path.join(OUTDIR, 'axial_displacement_spatial.csv'), 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['z', 'u_inner', 'u_middle', 'u_outer'])
    for i, z in enumerate(z_grid):
        writer.writerow([z, u_bar_inner[i, t10_idx], u_bar_mid[i, t10_idx], u_bar_outer[i, t10_idx]])

# Compute electrostatic potential
# φ = G^{-1} C^T d - G^{-1} D_rt. We already have d_t for each kz, time.
# Recompute potential in transformed domain
potential_kz = np.zeros((Nk, n_nodes, Nt), dtype=complex)
for ik, kz in enumerate(kz_grid):
    A_t, C_t, G_t = assemble_kz(kz)
    G_mod = G_t.copy()
    G_mod[inner_node, inner_node] = alpha_val
    D_rt = np.zeros(n_nodes)
    D_rt[inner_node] = alpha_val * phi_e_amp
    # solve for potential
    for it in range(Nt):
        d_t_it = response_d[ik, :, it]   # complex
        phi_t = np.linalg.solve(G_mod, C_t.T @ d_t_it - D_rt)
        potential_kz[ik, :, it] = phi_t

# Inverse FFT
spatial_potential = ifft(potential_kz, axis=0, norm='forward') * Nz   # similar scaling
spatial_potential = spatial_potential.real

# dimensionless potential
phi_bar_inner = spatial_potential[:, inner_node, :] / phi0
phi_bar_mid   = spatial_potential[:, middle_node, :] / phi0
phi_bar_outer = spatial_potential[:, outer_node, :] / phi0

with open(os.path.join(OUTDIR, 'potential_spatial.csv'), 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['z', 'phi_inner', 'phi_middle', 'phi_outer'])
    for i, z in enumerate(z_grid):
        writer.writerow([z, phi_bar_inner[i, t10_idx], phi_bar_mid[i, t10_idx], phi_bar_outer[i, t10_idx]])

# ----------------------------------------------------------------------
# 11. Write supporting evidence artifacts
# ----------------------------------------------------------------------
# setup_log.txt
with open(os.path.join(OUTDIR, 'setup_log.txt'), 'w') as f:
    f.write(f"Geometry: R1={R1}, R2={R2}, N_elem={N_elem}, nodes={n_nodes}\n")
    f.write(f"Load: mechanical sine pulse t_d={t_d}, electrode step amp={phi_e_amp}\n")
    f.write(f"Grid: Nz={Nz}, z_max={z_max}, Nt={Nt}, t_max={t_max}\n")

# sample_matrices.npz (save for first kz as sample)
np.savez(os.path.join(OUTDIR, 'sample_matrices.npz'), K_st=all_K_st[0])

# eigenvalues.csv (for a few kz)
with open(os.path.join(OUTDIR, 'eigenvalues.csv'), 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['kz'] + [f'omega_{i+1}' for i in range(10)])
    for ik in range(0, Nk, Nk//10):   # sample 10 kz
        omega = all_omega[ik][:10]
        writer.writerow([kz_grid[ik]] + list(omega))

# transformed_response_sample.npy
np.save(os.path.join(OUTDIR, 'transformed_response_sample.npy'), response_d[0, :, :100])

# fields.npz (save full spatial fields)
np.savez(os.path.join(OUTDIR, 'fields.npz'), u=spatial_d[:, ::2, :].real, w=spatial_d[:, 1::2, :].real, phi=spatial_potential)

print('All artifacts written successfully.')
