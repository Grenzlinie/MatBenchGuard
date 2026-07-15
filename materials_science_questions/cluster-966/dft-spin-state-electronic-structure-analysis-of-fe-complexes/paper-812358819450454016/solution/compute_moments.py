import numpy as np
import csv

# ----------------------------------------------------------------------
# 1.  Build orbital angular momentum operators for L=2 in the real t2g basis
#     ( |1>, |‑1>, |xy> ) used for tetragonal symmetry.
# ----------------------------------------------------------------------
# L=2 basis: m = -2, -1, 0, 1, 2
norm = np.sqrt(2 * (2 + 1))  # not needed explicitly
# L_z in |m> basis
Lz_m = np.diag([-2, -1, 0, 1, 2])
# L+ and L- in |m> basis
Lp_m = np.zeros((5, 5))
Lm_m = np.zeros((5, 5))
for i in range(5):
    m_i = i - 2
    # L+ |m> = sqrt( l(l+1) - m(m+1) ) |m+1>
    m_j = m_i + 1
    if -2 <= m_j <= 2:
        j = m_j + 2
        Lp_m[i, j] = np.sqrt(6 - m_i * (m_i + 1))   # l(l+1)=6, -m(m+1)
    # L- |m> = sqrt( l(l+1) - m(m-1) ) |m-1>
    m_j = m_i - 1
    if -2 <= m_j <= 2:
        j = m_j + 2
        Lm_m[i, j] = np.sqrt(6 - m_i * (m_i - 1))

# Basis vectors for the real t2g orbitals in the |m> basis
# |1>   -> [0,0,1,0,0] (m=1 at index 3)
# |-1>  -> [0,1,0,0,0] (m=-1 at index 1)
# |xy>  -> (|2>-|-2>)/sqrt(2) -> [ -1/rt2, 0,0,0, 1/rt2 ]
phi = np.zeros((3, 5), dtype=complex)
phi[0, 3] = 1.0                # |1>
phi[1, 1] = 1.0                # |-1>
phi[2, 0] = -1.0 / np.sqrt(2)  # -|2>/√2
phi[2, 4] =  1.0 / np.sqrt(2)  # +|‑2>/√2

# Transform L operators to the t2g basis: L'_op = phi * L_op * phi^H
Lz = phi @ Lz_m @ phi.conj().T
Lp = phi @ Lp_m @ phi.conj().T
Lm = phi @ Lm_m @ phi.conj().T

# Check Hermiticity (should be real): Lz = Lz^H, Lp^H = Lm.
Lz = Lz.real
Lp = Lp.real
Lm = Lp.T   # enforce exact adjoint

# ----------------------------------------------------------------------
# 2.  Spin operators for S=2.
# ----------------------------------------------------------------------
S = 2
m_s = np.arange(-S, S + 1)   # -2, -1, 0, 1, 2
Sz_s = np.diag(m_s)
Sp_s = np.zeros((2*S+1, 2*S+1))
Sm_s = np.zeros((2*S+1, 2*S+1))
for i in range(2*S+1):
    m_i = m_s[i]
    # S+ |s,ms> = sqrt( s(s+1)-ms(ms+1) ) |s,ms+1>
    ms_p = m_i + 1
    if ms_p <= S:
        j = ms_p + S
        Sp_s[i, j] = np.sqrt(S*(S+1) - m_i*(m_i+1))
    # S- |s,ms> = sqrt( s(s+1)-ms(ms-1) ) |s,ms-1>
    ms_m = m_i - 1
    if ms_m >= -S:
        j = ms_m + S
        Sm_s[i, j] = np.sqrt(S*(S+1) - m_i*(m_i-1))
Sm_s = Sm_s  # real

# ----------------------------------------------------------------------
# 3.  Full 15x15 Hamiltonian:  H = H_axial + λ L·S
# ----------------------------------------------------------------------
I_orb = np.eye(3)
I_spin = np.eye(5)

def build_H(v, lam=-1.0):
    """ Δ = v * lam; axial diagonal: [+Δ/3, +Δ/3, -2Δ/3] """
    Delta = v * lam
    H_axial = np.diag([Delta/3, Delta/3, -2*Delta/3])
    # H_axial acts on orbital space, identity on spin
    H_ax_full = np.kron(H_axial, I_spin)
    # spin-orbit: λ * ( Lz⊗Sz + 1/2*(Lp⊗Sm + Lm⊗Sp) )
    H_so = lam * (np.kron(Lz, Sz_s) + 0.5 * (np.kron(Lp, Sm_s) + np.kron(Lm, Sp_s)))
    return H_ax_full + H_so

# ----------------------------------------------------------------------
# 4.  Magnetic moment operator μz = k Lz ⊗ I_spin  +  2 I_orb ⊗ Sz_s
# ----------------------------------------------------------------------
def mu_z_op(k):
    return np.kron(k * Lz, I_spin) + 2.0 * np.kron(I_orb, Sz_s)

# ----------------------------------------------------------------------
# 5.  Parameters grid
# ----------------------------------------------------------------------
ks = [1.0, 0.9, 0.8, 0.7]
vs = [10, 5, 3, 2, 1, 0, -1, -2, -3, -5, -10]
kT_over_lambdas = [0.1, 0.2, 0.3, 0.5, 0.75, 1.0, 1.5, 2.0, 3.0,
                   -0.1, -0.2, -0.3, -0.5, -0.75, -1.0, -1.5, -2.0, -3.0]

results = []

for kval in ks:
    muz_op = mu_z_op(kval)
    muz_sq = muz_op @ muz_op   # 15x15
    for vval in vs:
        H = build_H(vval, lam=-1.0)
        eigvals, eigvecs = np.linalg.eigh(H)   # eigenvalues in ascending order
        for kTov in kT_over_lambdas:
            # physical temperature: kT = kT_over_lambda * λ = -kT_over_lambda (since λ=-1)
            # Boltzmann weight ∝ exp(-E/kT)
            kT = -kTov            # because λ = -1
            # avoid overflow: use weights = exp(-(E - E0)/kT) --> not needed
            # Direct: weight = exp(-E/kT)
            weights = np.exp(-eigvals / kT)
            Z = np.sum(weights)
            # <μ_z^2> = Σ_i w_i * <i|μ_z^2|i>
            mu2_expect = 0.0
            for i in range(15):
                vi = eigvecs[:, i]
                # <i|μ_z^2|i> = v^H (μ_z^2) v
                mu2_i = np.dot(vi.conj(), np.dot(muz_sq, vi)).real
                mu2_expect += weights[i] * mu2_i
            mu2_avg = mu2_expect / Z
            mu_eff = np.sqrt(max(mu2_avg, 0.0))   # clamp to be safe
            results.append((kval, vval, kTov, round(mu_eff, 2)))

# ----------------------------------------------------------------------
# 6.  Write CSV
# ----------------------------------------------------------------------
with open('/app/outputs/calculated_moments.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['k', 'v', 'kT_over_lambda', 'mu_eff'])
    writer.writerows(results)
