#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
python3 -m pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple numpy
mkdir -p /app/outputs

# === solve block: hubbard_dimer_results.json ===
cat <<'PYEOF' | python3 > $OUTDIR/hubbard_dimer_results.json
import numpy as np
import json
import sys

# ===== single-site operators in basis [empty, up, down, double] =====
c_up = np.array([[0,1,0,0],
                 [0,0,0,0],
                 [0,0,0,0],
                 [0,0,1,0]], dtype=complex)
c_down = np.array([[0,0,1,0],
                   [0,0,0,-1],
                   [0,0,0,0],
                   [0,0,0,0]], dtype=complex)
c_up_dag = c_up.T.conj()
c_down_dag = c_down.T.conj()

n_up = c_up_dag @ c_up
n_down = c_down_dag @ c_down
n_tot = n_up + n_down
n_up_dn = n_up @ n_down  # n_up * n_down, diagonal 1 for double occupancy

S_z = 0.5 * (n_up - n_down)

I4 = np.eye(4, dtype=complex)

def build_H(U, H, V, mu):
    """Construct 16x16 Hubbard dimer Hamiltonian."""
    # hopping: -t sum_sigma (c^+_{a} c_{b} + h.c.), with t=1
    H_hop = -1.0 * (np.kron(c_up_dag, c_up) + np.kron(c_up, c_up_dag) +
                     np.kron(c_down_dag, c_down) + np.kron(c_down, c_down_dag))
    # on-site U
    H_U = U * (np.kron(n_up_dn, I4) + np.kron(I4, n_up_dn))
    # magnetic field -H * (S^z_a + S^z_b)
    H_mag = -H * (np.kron(S_z, I4) + np.kron(I4, S_z))
    # electric field -V * (n_a - n_b)
    H_elec = -V * (np.kron(n_tot, I4) - np.kron(I4, n_tot))
    # chemical potential -mu * (n_a + n_b)
    H_mu = -mu * (np.kron(n_tot, I4) + np.kron(I4, n_tot))
    return H_hop + H_U + H_mag + H_elec + H_mu

def compute_thermo(U, H, V, T, mu):
    """
    Diagonalise and compute:
    - eigenenergies (real sorted)
    - grand partition Z
    - entropy S/kB
    - specific heat C/kB
    - magnetization M
    - polarization P
    """
    Hmat = build_H(U, H, V, mu)
    evals, evecs = np.linalg.eigh(Hmat)
    # sort by energy
    idx = np.argsort(evals.real)
    evals = evals.real[idx]
    evecs = evecs[:, idx]

    # Boltzmann factors
    beta = 1.0 / T
    exponentials = np.exp(-beta * evals)
    Z = np.sum(exponentials)
    p = exponentials / Z

    # entropy S/kB = ln Z + <E> / T  (with energies in units of t, T in k_B T/t)
    E_mean = np.dot(p, evals)
    S = np.log(Z) + E_mean / T

    # specific heat C/kB = (<E^2> - <E>^2) / T^2
    E2_mean = np.dot(p, evals**2)
    C = (E2_mean - E_mean**2) / (T**2)

    # density matrix
    rho = evecs @ np.diag(p) @ evecs.T.conj()

    # magnetization M = <S^z_a + S^z_b>
    M_op = np.kron(S_z, I4) + np.kron(I4, S_z)
    M = np.trace(rho @ M_op).real

    # polarization P = <n_a - n_b>
    P_op = np.kron(n_tot, I4) - np.kron(I4, n_tot)
    P = np.trace(rho @ P_op).real

    return evals, Z.real, S.real, C.real, M, P, rho, evecs, evals

# ===== conditions =====
conditions = [
    {"id": "cond1", "U": 2.0, "H": 0.0, "E": 0.0, "T": 0.1},
    {"id": "cond2", "U": 2.0, "H": 1.5, "E": 0.0, "T": 0.2},
    {"id": "cond3", "U": 5.0, "H": 0.0, "E": 0.0, "T": 0.1},
    {"id": "cond4", "U": 5.0, "H": 1.5, "E": 0.0, "T": 0.2},
    {"id": "cond5", "U": 2.0, "H": 2.0, "E": 2.0, "T": 0.1},
    {"id": "cond6", "U": 2.0, "H": 2.0, "E": 5.0, "T": 0.1},
    {"id": "cond7", "U": 5.0, "H": 2.0, "E": 0.0, "T": 0.05},
    {"id": "cond8", "U": 2.0, "H": 0.0, "E": 3.0, "T": 0.15},
]

results = []
for c in conditions:
    U_val = c["U"]
    H_val = c["H"]
    E_val = c["E"]
    T_val = c["T"]
    V_val = E_val / 2.0  # V = E|e|d/2 in units of t
    mu_val = U_val / 2.0  # half-filling

    evals, Z, S, C, M, P, _, _, _ = compute_thermo(U_val, H_val, V_val, T_val, mu_val)

    # isothermal entropy changes
    # MCE: S(H=0, E)
    _, _, S_H0, _, _, _, _, _, _ = compute_thermo(U_val, 0.0, V_val, T_val, mu_val)
    deltaS_MCE = S_H0 - S
    # ECE: S(H, E=0)
    _, _, S_E0, _, _, _, _, _, _ = compute_thermo(U_val, H_val, 0.0, T_val, mu_val)
    deltaS_ECE = S_E0 - S

    # Grüneisen ratios via finite differences of S with normalized fields
    # magnetic: derivative w.r.t. H/t
    step = 1e-6
    _, _, S_plus, _, _, _, _, _, _ = compute_thermo(U_val, H_val + step, V_val, T_val, mu_val)
    _, _, S_minus, _, _, _, _, _, _ = compute_thermo(U_val, H_val - step, V_val, T_val, mu_val)
    dS_dH = (S_plus - S_minus) / (2 * step)
    Gamma_H_t = -dS_dH / C   # Gamma_H * t (dimensionless)

    # electric: derivative w.r.t. E|e|d/t, i.e., F = E|e|d/t, with V = F/2
    _, _, S_ep, _, _, _, _, _, _ = compute_thermo(U_val, H_val, (E_val + step)/2, T_val, mu_val)
    _, _, S_em, _, _, _, _, _, _ = compute_thermo(U_val, H_val, (E_val - step)/2, T_val, mu_val)
    dS_dE = (S_ep - S_em) / (2 * step)
    Gamma_E_renorm = -dS_dE / C  # Gamma_E * t/(|e|d) (dimensionless)

    results.append({
        "condition_id": c["id"],
        "eigenenergies": [float(x) for x in evals],
        "grand_partition": float(Z),
        "entropy": float(S),
        "specific_heat": float(C),
        "magnetization": float(M),
        "polarization": float(P),
        "deltaS_MCE": float(deltaS_MCE),
        "deltaS_ECE": float(deltaS_ECE),
        "magnetic_Gruneisen_ratio": float(Gamma_H_t),
        "electric_Gruneisen_ratio": float(Gamma_E_renorm),
    })

output = {"conditions": results}
json.dump(output, sys.stdout, indent=2)
PYEOF
