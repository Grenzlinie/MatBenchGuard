#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
python3 -m pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple numpy

# === solve block: phase_diagram_data.csv ===
python3 << 'EOF' > "$OUTDIR/phase_diagram_data.csv"
import numpy as np, csv, itertools, sys

# ----- kagomé lattice -----
a1_k = np.array([1.0, 0.0])
a2_k = np.array([0.5, np.sqrt(3)/2])
tau_k = [np.array([0.0,0.0]), np.array([0.5,0.0]), np.array([0.25, np.sqrt(3)/4])]
lan = 0.51
hops_k = []
for i in range(3):
    for j in range(3):
        for n1 in range(-1,2):
            for n2 in range(-1,2):
                d = tau_k[j] - tau_k[i] + n1*a1_k + n2*a2_k
                if abs(np.linalg.norm(d) - 0.5) < 1e-8:
                    hops_k.append((i, j, (n1, n2), 1.0))

# ----- pyrochlore lattice -----
a1_p = np.array([0.0, 0.5, 0.5])
a2_p = np.array([0.5, 0.0, 0.5])
a3_p = np.array([0.5, 0.5, 0.0])
tau_p = [np.array([0.0,0.0,0.0]), np.array([0.25,0.25,0.0]),
         np.array([0.25,0.0,0.25]), np.array([0.0,0.25,0.25])]
lan = 0.36
hops_p = []
for i in range(4):
    for j in range(4):
        for n1 in range(-1,2):
            for n2 in range(-1,2):
                for n3 in range(-1,2):
                    d = tau_p[j] - tau_p[i] + n1*a1_p + n2*a2_p + n3*a3_p
                    if abs(np.linalg.norm(d) - 0.35355339) < 1e-8:
                        hops_p.append((i, j, (n1, n2, n3), 1.0))

# ----- spin configurations -----
sigma_x = np.array([[0,1],[1,0]], dtype=complex)
sigma_y = np.array([[0,-1j],[1j,0]], dtype=complex)
sigma_z = np.array([[1,0],[0,-1]], dtype=complex)

def zeeman_block(n_vec, K):
    nx, ny, nz = n_vec
    return -0.5*K * (nx*sigma_x + ny*sigma_y + nz*sigma_z)

# kagome configs
kagome_configs = {
    'F':  [np.array([0,0,1]), np.array([0,0,1]), np.array([0,0,1])],
    'FI': [np.array([0,0,1]), np.array([0,0,1]), np.array([0,0,-1])],
    'CI': [np.array([1,0,0]), np.array([-0.5, np.sqrt(3)/2, 0]), np.array([-0.5, -np.sqrt(3)/2, 0])]
}

# pyrochlore configs
r_p = [np.array([1,1,1])/np.sqrt(3), np.array([1,-1,-1])/np.sqrt(3),
       np.array([-1,1,-1])/np.sqrt(3), np.array([-1,-1,1])/np.sqrt(3)]
fi_p = [np.array([0,0,1]), np.array([0,0,-1]), np.array([0,0,-1]), np.array([0,0,-1])]
U_p = []; V_p = []
for r in r_p:
    if abs(np.dot(r, [1,1,1])) > 0.9:
        u = np.array([1,-1,0]) / np.sqrt(2)
    else:
        u = np.cross(r, [1,1,1])
        u = u / np.linalg.norm(u)
    v = np.cross(r, u)
    v = v / np.linalg.norm(v)
    U_p.append(u); V_p.append(v)
ci_angles = [0, np.pi/2, np.pi, 3*np.pi/2]
ci_p = [ np.cos(a)*U_p[i] + np.sin(a)*V_p[i] for i,a in enumerate(ci_angles) ]
si_p = [ r_p[0], -r_p[1], -r_p[2], r_p[3] ]

pyrochlore_configs = {
    'F':  [np.array([0,0,1]), np.array([0,0,1]), np.array([0,0,1]), np.array([0,0,1])],
    'AF': r_p,
    'FI': fi_p,
    'CI': ci_p,
    'SI': si_p
}

# ----- compute total energy (single k-point) -----
def total_energy(lattice, config_vecs, n, K, J, mesh):
    if lattice == 'kagome':
        hops = hops_k
        nsites = 3
    else:
        hops = hops_p
        nsites = 4
    all_eigs = []
    dim = 2*nsites
    for kcoords in mesh:
        H = np.zeros((dim, dim), dtype=complex)
        for (i,j, Rvec, t) in hops:
            phase = np.exp(2j*np.pi * np.dot(kcoords, Rvec))
            H[2*i:2*i+2, 2*j:2*j+2] += t * phase * np.eye(2)
        for i in range(nsites):
            H[2*i:2*i+2, 2*i:2*i+2] += zeeman_block(config_vecs[i], K)
        eigvals = np.sort(np.linalg.eigvalsh(H))
        all_eigs.append(eigvals)
    all_eigs = np.concatenate(all_eigs)
    Nk = len(mesh)
    n_electrons = n * Nk
    n_int = int(np.floor(n_electrons))
    fraction = n_electrons - n_int
    if n_int > 0:
        Eband = np.sum(all_eigs[:n_int]) / Nk
    else:
        Eband = 0.0
    if n_int < len(all_eigs):
        Eband += fraction * all_eigs[n_int] / Nk
    E_ex = 0.0
    for (i, j, Rvec, t) in hops:
        E_ex += np.dot(config_vecs[i], config_vecs[j])
    E_ex *= J * 0.5
    return Eband + E_ex

# ----- use single k-point meshes -----
kagome_mesh_pts = np.array([[0.0, 0.0]])
pyro_mesh_pts = np.array([[0.0, 0.0, 0.0]])

# Parameter ranges
J_vals = [0.0, 0.02, 0.04]
K_vals = np.linspace(0, 8, 17)
n_vals_k = np.linspace(0, 6, 31)
n_vals_p = np.linspace(0, 8, 41)

rows = []
# Kagome sweeps
for J in J_vals:
    for n in n_vals_k:
        for K in K_vals:
            energies = {}
            for name, config in kagome_configs.items():
                energies[name] = total_energy('kagome', config, n, K, J, kagome_mesh_pts)
            min_conf = min(energies, key=energies.get)
            row = {'lattice':'kagome', 'n':round(n,6), 'K_over_t':round(K,6), 'J_over_t':round(J,6),
                   'E_F':round(energies['F'],10), 'E_FI':round(energies['FI'],10), 'E_CI':round(energies['CI'],10),
                   'E_AF':'', 'E_SI':'', 'ground_state':min_conf}
            rows.append(row)
# Pyrochlore sweeps
for J in J_vals:
    for n in n_vals_p:
        for K in K_vals:
            energies = {}
            for name, config in pyrochlore_configs.items():
                energies[name] = total_energy('pyrochlore', config, n, K, J, pyro_mesh_pts)
            min_conf = min(energies, key=energies.get)
            row = {'lattice':'pyrochlore', 'n':round(n,6), 'K_over_t':round(K,6), 'J_over_t':round(J,6),
                   'E_F':round(energies['F'],10), 'E_FI':round(energies['FI'],10), 'E_CI':round(energies['CI'],10),
                   'E_AF':round(energies['AF'],10), 'E_SI':round(energies['SI'],10),
                   'ground_state':min_conf}
            rows.append(row)

# K-J cross sections at n=1.0
KJ_K_vals = np.linspace(0,8,17)
KJ_J_vals = np.linspace(0,0.1,11)
n_fixed = 1.0
for lattice, configs, n_val, mesh in [('kagome', kagome_configs, n_fixed, kagome_mesh_pts),
                                        ('pyrochlore', pyrochlore_configs, n_fixed, pyro_mesh_pts)]:
    for K in KJ_K_vals:
        for J in KJ_J_vals:
            energies = {}
            for name, config in configs.items():
                energies[name] = total_energy(lattice, config, n_val, K, J, mesh)
            min_conf = min(energies, key=energies.get)
            if lattice=='kagome':
                row = {'lattice':'kagome', 'n':n_val, 'K_over_t':K, 'J_over_t':J,
                       'E_F':round(energies['F'],10), 'E_FI':round(energies['FI'],10), 'E_CI':round(energies['CI'],10),
                       'E_AF':'', 'E_SI':'', 'ground_state':min_conf}
            else:
                row = {'lattice':'pyrochlore', 'n':n_val, 'K_over_t':K, 'J_over_t':J,
                       'E_F':round(energies['F'],10), 'E_FI':round(energies['FI'],10), 'E_CI':round(energies['CI'],10),
                       'E_AF':round(energies['AF'],10), 'E_SI':round(energies['SI'],10),
                       'ground_state':min_conf}
            rows.append(row)

# Write CSV
fieldnames = ['lattice','n','K_over_t','J_over_t','E_F','E_FI','E_CI','E_AF','E_SI','ground_state']
writer = csv.DictWriter(sys.stdout, fieldnames=fieldnames)
writer.writeheader()
for row in rows:
    writer.writerow(row)
EOF
