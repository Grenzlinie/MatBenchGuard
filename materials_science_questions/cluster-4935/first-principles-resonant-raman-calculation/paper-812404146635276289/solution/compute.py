import numpy as np
from scipy.integrate import quad
from scipy.constants import hbar, e, pi, epsilon_0, h

# Parameters
R = 1.0e-7  # m
W = 1.0e-8  # m
m0 = 9.10938356e-31
meff = 0.067 * m0
eps_s = 12.9
eps0 = epsilon_0

phi0 = h/e  # flux quantum

# Radial energy for K=1
Erad = (hbar**2 * pi**2) / (2 * meff * W**2)  # J
# Rotational constant
E0 = hbar**2 / (2 * meff * R**2)  # J
# Coulomb energy scale
C = e**2 / (4 * pi * eps0 * eps_s * R)  # J
ECoul = C / 2.0

# relative angular kinetic coefficient
alpha = hbar**2 / (R**2 * meff)  # J

def V_int(k):
    if k == 0:
        return quad(lambda g: 1.0/np.sin(g/2), 0, pi, limit=200)[0]
    else:
        return quad(lambda g: np.cos(k*g)/np.sin(g/2), 0, pi, limit=200)[0]

Nmax = 20
n_list = np.arange(-Nmax, Nmax+1)
V_coeffs = np.zeros(len(n_list))
for i, n in enumerate(n_list):
    V_coeffs[i] = C / pi * V_int(abs(n))

def build_H(p):
    N = len(n_list)
    H = np.diag(alpha * (n_list + p)**2)
    for i in range(N):
        for j in range(N):
            dn = n_list[i] - n_list[j]
            idx = np.where(n_list == dn)[0]
            if len(idx):
                H[i,j] += V_coeffs[idx[0]]
    return H

p_vals = [0.0, 0.5]
eigvals = {}
eigvecs = {}
for p in p_vals:
    H = build_H(p)
    w, v = np.linalg.eigh(H)
    eigvals[p] = w
    eigvecs[p] = v

Eosc = {p: eigvals[p] - ECoul for p in p_vals}

# conversion to meV
def J_to_meV(E_J):
    return E_J / (e * 1e-3)

Erad_meV = J_to_meV(Erad)
E0_meV = J_to_meV(E0)
ECoul_meV = J_to_meV(ECoul)
Eosc_meV = {p: J_to_meV(Eosc[p]) for p in p_vals}

def log_info():
    print(f"Radial energy (K=1): {Erad_meV:.6f} meV")
    print(f"Rotational constant E0/2: {E0_meV/2:.6f} meV")
    print(f"E_Coul: {ECoul_meV:.6f} meV")
    for p in p_vals:
        print(f"E_osc for p={p}: {Eosc_meV[p][:5]} meV")
    print(f"Ground state para p=0 j=0 Eosc: {Eosc_meV[0][0]:.6f} meV")
    print(f"Ground state ortho p=0.5 j=0 Eosc: {Eosc_meV[0.5][0]:.6f} meV")

def persistent_current(filename):
    phi_ratio = np.arange(-2.0, 2.0+1e-12, 0.01)
    J_vals = np.arange(-10, 11)
    even_mask = (J_vals % 2 == 0)
    odd_mask = ~even_mask
    E_rot_J_all = (E0_meV/2) * ((J_vals[np.newaxis,:] + 2*phi_ratio[:,np.newaxis])**2)
    E_para_min = np.min(E_rot_J_all[:, even_mask], axis=1)
    E_ortho_min = np.min(E_rot_J_all[:, odd_mask], axis=1)
    E_rot_opt = np.minimum(E_para_min, E_ortho_min)
    E_ground = Erad_meV*2 + ECoul_meV + Eosc_meV[0][0] + E_rot_opt
    dE_dphi_ratio_meV = np.gradient(E_ground, phi_ratio)
    dE_dphi_ratio_J = dE_dphi_ratio_meV * (e * 1e-3)
    I = - dE_dphi_ratio_J / phi0
    I_nA = I * 1e9
    with open(filename, 'w') as f:
        f.write("flux,current_nA\n")
        for phi, cur in zip(phi_ratio, I_nA):
            f.write(f"{phi:.6f},{cur:.8f}\n")

def absorption_spectrum(filename):
    # odd transitions from p=0 j=0 to p=0.5
    odd_deltas = []
    odd_j_idx = []
    for j_idx, j_E in enumerate(Eosc_meV[0.5]):
        if j_idx % 2 == 1:
            odd_j_idx.append(j_idx)
            odd_deltas.append(j_E - Eosc_meV[0][0])
    if not odd_deltas:
        raise RuntimeError("No odd j_f states")
    u0_coeffs = eigvecs[0][:, 0]
    uf_coeffs = eigvecs[0.5]
    odd_intens = []
    for j_idx in odd_j_idx:
        overlap = np.vdot(uf_coeffs[:, j_idx], u0_coeffs)
        odd_intens.append(np.abs(overlap)**2)
    freq = np.arange(0.0, 10.0 + 1e-12, 0.02)
    gamma = 0.05
    spec = np.zeros_like(freq)
    for delta, I in zip(odd_deltas, odd_intens):
        E_trans = delta + E0_meV/2
        spec += I * gamma / ((freq - E_trans)**2 + gamma**2) / np.pi
    spec_max = np.max(spec)
    if spec_max > 0:
        spec = spec / spec_max
    with open(filename, 'w') as f:
        f.write("frequency_meV,absorption_power\n")
        for fr, sp in zip(freq, spec):
            f.write(f"{fr:.6f},{sp:.10f}\n")

def raman_cross_section(filename):
    # even transitions (depolarized)
    even_deltas = []
    even_j_idx = []
    for j_idx, j_E in enumerate(Eosc_meV[0.5]):
        if j_idx % 2 == 0:
            even_j_idx.append(j_idx)
            even_deltas.append(j_E - Eosc_meV[0][0])
    u0_coeffs = eigvecs[0][:, 0]
    uf_coeffs = eigvecs[0.5]
    even_intens = []
    for j_idx in even_j_idx:
        overlap = np.vdot(uf_coeffs[:, j_idx], u0_coeffs)
        even_intens.append(np.abs(overlap)**2)
    freq = np.arange(0.0, 10.0 + 1e-12, 0.02)
    gamma = 0.05
    # polarized = odd (same as absorption)
    odd_deltas = []
    odd_j_idx = []
    for j_idx, j_E in enumerate(Eosc_meV[0.5]):
        if j_idx % 2 == 1:
            odd_j_idx.append(j_idx)
            odd_deltas.append(j_E - Eosc_meV[0][0])
    odd_intens = []
    for j_idx in odd_j_idx:
        overlap = np.vdot(uf_coeffs[:, j_idx], u0_coeffs)
        odd_intens.append(np.abs(overlap)**2)
    spec_pol = np.zeros_like(freq)
    for delta, I in zip(odd_deltas, odd_intens):
        E_trans = delta + E0_meV/2
        spec_pol += I * gamma / ((freq - E_trans)**2 + gamma**2) / np.pi
    spec_pol_max = np.max(spec_pol)
    if spec_pol_max > 0:
        spec_pol = spec_pol / spec_pol_max
    spec_depol = np.zeros_like(freq)
    for delta, I in zip(even_deltas, even_intens):
        E_trans = delta + E0_meV/2
        spec_depol += I * gamma / ((freq - E_trans)**2 + gamma**2) / np.pi
    spec_depol_max = np.max(spec_depol)
    if spec_depol_max > 0:
        spec_depol = spec_depol / spec_depol_max
    with open(filename, 'w') as f:
        f.write("frequency_meV,cross_section,polarization\n")
        for fr, sp in zip(freq, spec_pol):
            f.write(f"{fr:.6f},{sp:.10f},polarized\n")
        for fr, sp in zip(freq, spec_depol):
            f.write(f"{fr:.6f},{sp:.10f},depolarized\n")

if __name__ == "__main__":
    import sys
    mode = sys.argv[1]
    outfile = sys.argv[2]
    if mode == "log":
        log_info()
    elif mode == "persistent":
        persistent_current(outfile)
    elif mode == "absorption":
        absorption_spectrum(outfile)
    elif mode == "raman":
        raman_cross_section(outfile)
    else:
        raise ValueError("Unknown mode")
