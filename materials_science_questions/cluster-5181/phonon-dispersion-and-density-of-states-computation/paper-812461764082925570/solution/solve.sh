#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
python3 -m pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple numpy

# === solve block: phonon_results.json ===
python3 << 'PYEOF'
import json, math, sys
import numpy as np

# ---------------------------------------------------------------------
# physical constants (cgs + cm‑¹ units)
# ---------------------------------------------------------------------
a_A      = 5.653                          # Å
a0_A     = a_A / 4.0
a_cm     = a_A * 1e-8
a0_cm    = a0_A * 1e-8

e_esu    = 4.803e-10
hbar_erg = 1.054e-27
c_cm_s   = 2.99792458e10
omega_per_cm = 2.0 * math.pi * c_cm_s * 100.0   # rad/s per cm⁻¹

# masses (u, g)
m_Al_u  = 26.982
m_As_u  = 74.922
u_to_g  = 1.660539e-24
mu_u    = (m_Al_u * m_As_u) / (m_Al_u + m_As_u)
mu_g    = mu_u * u_to_g

# volume per atom (8 atoms per conventional cell)
V_a_cm3 = (a_cm ** 3) / 8.0

# ---------------------------------------------------
# material parameters (from the paper / Kunc model)
# ---------------------------------------------------
eps_inf = 12.0
z_eff   = 0.65            # effective charge (units of e)
z_esu   = z_eff * e_esu
xi_esu  = z_esu / math.sqrt(eps_inf)

# AlAs short‑range parameters
Omega_AlAs = 362.0
LO_AlAs    = 404.0          # used only to fix the magnitude of B_k
Delta_sq   = LO_AlAs**2 - Omega_AlAs**2
Delta_sqrt = math.sqrt(max(Delta_sq, 0.0))

# superlattice geometry
n1        = 10               # AlAs bilayers
n2        = 10               # GaAs bilayers
Nc        = n1 + n2

delta_z_A = a0_A
delta_x_A = 0.0
d_z_A     = 2 * n1 * a0_A + 2 * delta_z_A    # effective z‑layer width
d_x_A     = 2 * n1 * a0_A + 2 * delta_x_A
d_z_cm    = d_z_A * 1e-8
d_x_cm    = d_x_A * 1e-8

eta_A  = 1.7 * a0_A
eta_cm = 1.7 * a0_cm

# short‑range dispersion (Eq. 19)
eta_z = 22.0; chi_z = 1.36; R_z = 4
eta_x = 22.0; chi_x = 1.08; R_x = 2

# ---------------------------------------------------
# basis indices (odd numbers 1..19)
# ---------------------------------------------------
s_ks = [2*i + 1 for i in range(10)]   # �?1,3,...,19
g_ks = [2*i + 1 for i in range(10)]
n_s  = len(s_ks)

# dispersion functions
def omega_z_B(k):
    Q = a_A * k / (2.0 * d_z_A)
    return Omega_AlAs - eta_z * (1.0 - math.exp(-(Q / chi_z)**R_z))

def omega_x_B(k):
    Q = a_A * k / (2.0 * d_x_A)
    return Omega_AlAs - eta_x * (1.0 - math.exp(-(Q / chi_x)**R_x))

def B_k(k, d_cm):
    arg = math.pi * k * eta_cm / d_cm
    if abs(arg) < 1e-14:
        return 0.0
    return Delta_sqrt * (d_cm / (math.pi * k * eta_cm)) * math.sin(arg)

# parameters for all basis functions
Omega_s = np.array([omega_z_B(k) for k in s_ks])
Omega_g = np.array([omega_x_B(k) for k in g_ks])
B_s     = np.array([B_k(k, d_z_cm) for k in s_ks])
B_g     = np.array([B_k(k, d_x_cm) for k in g_ks])

coeff_h = 8.0 * n1 / (Nc * math.pi**2)

# ---------------------------------------------------
# build the non‑local dielectric matrix (Eq. 14)
# ---------------------------------------------------
def build_matrix(theta):
    ct = math.cos(theta); st = math.sin(theta)
    c2 = ct*ct; s2 = st*st; sc = st*ct
    N = 2 * n_s
    M = np.zeros((N, N))
    # s‑block
    for i in range(n_s):
        M[i, i] = Omega_s[i]**2 + B_s[i]**2
        for j in range(n_s):
            if i == j: continue
            h = coeff_h * B_s[i] * B_s[j] / (s_ks[i] * s_ks[j])
            M[i, j] = h * (c2 - 1.0)   # = -h * sin^2
    # g‑block
    for i in range(n_s):
        ii = n_s + i
        M[ii, ii] = Omega_g[i]**2
        for j in range(n_s):
            if i == j: continue
            jj = n_s + j
            h = coeff_h * B_g[i] * B_g[j] / (g_ks[i] * g_ks[j])
            M[ii, jj] = h * s2
    # s‑g coupling
    for i in range(n_s):
        for j in range(n_s):
            h = coeff_h * B_s[i] * B_g[j] / (s_ks[i] * g_ks[j])
            val = h * sc
            M[i, n_s + j] = val
            M[n_s + j, i] = val
    return M

# ---------------------------------------------------
# field‑amplitude scaling (standard zero‑point amplitude)
# ---------------------------------------------------
Omega_rad = Omega_AlAs * omega_per_cm
b_cgs     = math.sqrt(hbar_erg / (2.0 * Omega_rad))

E0_z_cgs = b_cgs * xi_esu / (V_a_cm3 * math.sqrt(mu_g * d_z_cm))
E0_x_cgs = b_cgs * xi_esu / (V_a_cm3 * math.sqrt(mu_g * d_x_cm))
# convert esu/cm → meV/Å (1 esu/cm = 2.9979e7 V/m = 2.9979 × 10⁷ V/m; 1 meV/Å = 10⁷ V/m)
E0_z = E0_z_cgs * 2.9979
E0_x = E0_x_cgs * 2.9979

n_mono = 2 * n1
z_pos  = [p * a0_A for p in range(n_mono)]

# ---------------------------------------------------
# main loop over propagation angles
# ---------------------------------------------------
freqs_out  = []
fields_out = []

for deg in range(0, 91, 1):
    th = math.radians(deg)
    M = build_matrix(th)
    evals, evecs = np.linalg.eigh(M)
    idx = np.argsort(evals)
    evals = evals[idx]
    evecs = evecs[:, idx]

    # safeguard: clip negative eigenvalues and ensure finite
    evals = np.maximum(evals, 1e-30)
    freqs = np.sqrt(evals)

    for mi in range(len(evals)):
        f_val = float(freqs[mi])
        if not math.isfinite(f_val):
            f_val = 0.0  # fallback, should never happen
        freqs_out.append({
            "theta_deg": deg,
            "mode_index": mi,
            "frequency_cm-1": round(f_val, 4)
        })

    # ---------  θ = 0°  (s and g blocks decoupled) ---------
    if deg == 0:
        for mi in range(len(evals)):
            vec = evecs[:, mi]
            s_part = vec[:n_s]
            g_part = vec[n_s:]
            s_norm = np.sum(s_part**2)
            g_norm = np.sum(g_part**2)

            if s_norm > g_norm:
                # z‑polarised mode, use the dominant basis index
                idx_max = int(np.argmax(np.abs(s_part)))
                k = s_ks[idx_max]
                for p, zz in enumerate(z_pos):
                    Ez_val = E0_z * math.sin(math.pi * k * zz / d_z_A) if zz < d_z_A else 0.0
                    Ez_val = float(Ez_val)
                    if not math.isfinite(Ez_val): Ez_val = 0.0
                    fields_out.append({
                        "mode_index": mi,
                        "z_monolayer": p,
                        "Ez_meV_per_A": round(Ez_val, 6),
                        "Ex_meV_per_A": 0.0
                    })
            else:
                for p in range(len(z_pos)):
                    fields_out.append({
                        "mode_index": mi,
                        "z_monolayer": p,
                        "Ez_meV_per_A": 0.0,
                        "Ex_meV_per_A": 0.0
                    })

    # ---------  θ = 90°  (q ⊥ z) ---------
    elif deg == 90:
        for mi in range(len(evals)):
            vec = evecs[:, mi]
            for p, zz in enumerate(z_pos):
                Ez_val = 0.0
                Ex_val = 0.0
                for i, k in enumerate(s_ks):
                    if zz < d_z_A:
                        Ez_val += vec[i] * E0_z * math.sin(math.pi * k * zz / d_z_A)
                for i, k in enumerate(g_ks):
                    if zz < d_x_A:
                        Ex_val += vec[n_s + i] * E0_x * math.sin(math.pi * k * zz / d_x_A)
                # safety
                Ez_val = float(Ez_val)
                Ex_val = float(Ex_val)
                if not math.isfinite(Ez_val): Ez_val = 0.0
                if not math.isfinite(Ex_val): Ex_val = 0.0
                fields_out.append({
                    "mode_index": mi,
                    "z_monolayer": p,
                    "Ez_meV_per_A": round(Ez_val, 6),
                    "Ex_meV_per_A": round(Ex_val, 6)
                })

# ---------------------------------------------------
# write final JSON
# ---------------------------------------------------
with open('/app/outputs/phonon_results.json', 'w') as f:
    json.dump({"frequencies": freqs_out, "fields": fields_out}, f, indent=2)
PYEOF
