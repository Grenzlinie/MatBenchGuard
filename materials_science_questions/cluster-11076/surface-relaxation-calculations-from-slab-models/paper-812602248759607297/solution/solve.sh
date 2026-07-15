#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: phonon_dispersion.csv ===
python3 -m pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple numpy
python3 << 'PYEOF'
import numpy as np

# ======== constants ========
a = 2.887               # Angstrom
d = a / np.sqrt(2)     # interlayer spacing
sqrt2 = np.sqrt(2)

# masses (amu -> g)
amu_to_g = 1.660539e-24
m_Ni = 58.69 * amu_to_g
m_Al = 26.98 * amu_to_g

# force constants in dyn/cm = g/s^2
fc_bulk = {
    ('Ni','Al',1): (31420, 1150),
    ('Al','Ni',1): (31420, 1150),
    ('Al','Al',2): (18380,  760),
    ('Ni','Ni',2): ( 2180, -440),
    ('Al','Al',3): ( 4036,-1484),
    ('Ni','Ni',3): ( 4760, -620),
}

# MS model surface modifications (layer indices 0 .. 14)
ms_mod = {}
# phi'' modifications
ms_mod[('Al','Ni',0,1,1)] = (25136, None)
ms_mod[('Ni','Al',0,1,1)] = (47130, None)
ms_mod[('Ni','Ni',0,1,2)] = ( 3052, None)
ms_mod[('Ni','Ni',0,2,3)] = ( 6664, None)
# intralayer tangential phi' for first-layer Ni
ms_mod[('Ni','Ni',0,0,2)] = (None,  2000)
ms_mod[('Ni','Ni',0,0,3)] = (None, -2000)
# balanced forces phi' (overrides for specific bonds)
# stored as (pair,layer_i,layer_j,shell,'p')
ms_mod[('Al','Ni',0,1,1,'p')] = 264
ms_mod[('Ni','Ni',0,1,1,'p')] = 145
ms_mod[('Al','Al',0,1,1,'p')] = 724

# in-plane lattice vectors
a1 = np.array([a*sqrt2, 0.0, 0.0])
a2 = np.array([0.0, a, 0.0])

# ======== build slab atoms ========
layers = 15
atoms = []  # [('Ni'/'Al', position, layer_index)]
for l in range(layers):
    z_bulk = l * d
    if l % 2 == 0:
        ni_frac = np.array([0.0, 0.0])
        al_frac = np.array([0.5, 0.5])
    else:
        ni_frac = np.array([0.5, 0.0])
        al_frac = np.array([0.0, 0.5])
    ni_pos = ni_frac[0]*a1 + ni_frac[1]*a2
    al_pos = al_frac[0]*a1 + al_frac[1]*a2
    if l == 0:
        ni_z = z_bulk - 0.06*d
        al_z = z_bulk + 0.046*d
    else:
        ni_z = z_bulk
        al_z = z_bulk
    ni_pos[2] = ni_z
    al_pos[2] = al_z
    atoms.append(('Ni', ni_pos, l))
    atoms.append(('Al', al_pos, l))
n_atoms = len(atoms)
mass = np.array([m_Ni if atom[0]=='Ni' else m_Al for atom in atoms])

# mirror partner for parity: y -> -y
partner = np.zeros(n_atoms, dtype=int)
for i, (el, pos, l) in enumerate(atoms):
    pos_mir = np.array([pos[0], -pos[1], pos[2]])
    best_j = -1
    best_d = 1e9
    for j, (el2, pos2, l2) in enumerate(atoms):
        if el2==el and l2==l:
            dy = abs((pos_mir[1] - pos2[1] + a/2) % a - a/2)
            dist = np.sqrt((pos_mir[0]-pos2[0])**2 + dy**2 + (pos_mir[2]-pos2[2])**2)
            if dist < best_d:
                best_d = dist
                best_j = j
    partner[i] = best_j

# ======== neighbour list ========
cutoff = 4.5
images_xy = [(nx, ny) for nx in range(-1,2) for ny in range(-1,2)]
bonds = []
known_dist = {
    (0,1,1):2.5, (1,0,1):2.5,
    (0,0,2):2.89, (1,1,2):2.89,
    (0,0,3):4.08, (1,1,3):4.08
}
dist_tol = 0.3
for i in range(n_atoms):
    pos_i = atoms[i][1]
    el_i = atoms[i][0]
    li   = atoms[i][2]
    for j in range(n_atoms):
        pos_j = atoms[j][1]
        el_j = atoms[j][0]
        lj   = atoms[j][2]
        for (nx,ny) in images_xy:
            R = np.array([nx, ny, 0.0])
            rvec = pos_j + nx*a1 + ny*a2 - pos_i
            dist = np.linalg.norm(rvec)
            if dist < 1e-6:
                continue
            if dist > cutoff:
                continue
            # determine shell
            pair = (el_i, el_j)
            e0 = 0 if el_i=='Ni' else 1
            e1 = 0 if el_j=='Ni' else 1
            shell = None
            for s in [1,2,3]:
                nom = known_dist.get((e0,e1,s), None)
                if nom is not None and abs(dist-nom) < dist_tol:
                    shell = s
                    break
            if shell is None:
                continue
            # canonical ordering to avoid double counting
            if not (i<j or (i==j and (nx>0 or (nx==0 and ny>0)))):
                continue
            bonds.append((i, j, li, lj, (nx,ny), dist, rvec, shell, pair))

# ======== build D(q) ========
def get_phi(i, j, li, lj, rim, shell, pair):
    el_i, el_j = pair
    phi2, phi1 = fc_bulk.get((el_i, el_j, shell))
    # apply MS overrides
    key_base = (el_i, el_j, li, lj, shell)
    if key_base in ms_mod:
        p2, p1 = ms_mod[key_base]
        if p2 is not None: phi2 = p2
        if p1 is not None: phi1 = p1
    # balanced phi' overrides
    pkey = (el_i, el_j, li, lj, shell, 'p')
    if pkey in ms_mod:
        phi1 = ms_mod[pkey]
    return phi2, phi1

def build_D(q):
    D = np.zeros((n_atoms,3,n_atoms,3), dtype=complex)
    for bond in bonds:
        i, j, li, lj, rim, dist, rvec, shell, pair = bond
        phi2, phi1 = get_phi(i, j, li, lj, rim, shell, pair)
        if phi2 is None:
            continue
        e = rvec / dist
        K = phi2 * np.outer(e, e) + phi1 * (np.eye(3) - np.outer(e, e))
        R = np.array([rim[0], rim[1], 0.0])
        phase = np.exp(1j * np.dot(q, R))
        D[i,:,j,:] -= K * phase
        D[j,:,i,:] -= K * np.conj(phase)  # Hermitian
        D[i,:,i,:] += K
        D[j,:,j,:] += K
    # mass weighting
    Dtilde = np.zeros((n_atoms*3, n_atoms*3), dtype=complex)
    for i in range(n_atoms):
        for j in range(n_atoms):
            Dtilde[3*i:3*i+3, 3*j:3*j+3] = D[i,:,j,:] / np.sqrt(mass[i]*mass[j])
    return Dtilde

def parity_even(vec):
    s = 0.0
    for i in range(n_atoms):
        pi = partner[i]
        up = vec[3*pi:3*pi+3]
        um = np.array([up[0], -up[1], up[2]])
        s += np.dot(vec[3*i:3*i+3], um)
    return s > 0.1  # approximate threshold

# ======== dispersion ========
c_ms = 2.99792458e10  # cm/s
a1_len = a * sqrt2
a2_len = a
zetas = np.linspace(0.0, 1.0, 41)   # fine grid

def compute_dir(dir_lbl, q_func):
    rows = []
    for zt in zetas:
        q = q_func(zt)
        Dtilde = build_D(q)
        vals, vecs = np.linalg.eigh(Dtilde)
        freqs = np.sqrt(np.abs(vals)) / (2*np.pi * c_ms)
        for k in range(len(freqs)):
            if parity_even(vecs[:,k]):
                rows.append((dir_lbl, round(zt,6), float(freqs[k])))
    return rows

# ΓY – wave‑vector along y (short axis)
q_gy = lambda z: np.array([0.0, z*np.pi/a2_len, 0.0])
# ΓX – wave‑vector along x (long axis)
q_gx = lambda z: np.array([z*np.pi/a1_len, 0.0, 0.0])

rows = compute_dir('GY', q_gy) + compute_dir('GX', q_gx)

import csv
with open('/app/outputs/phonon_dispersion.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['direction','reduced_wavevector','frequency_cm1'])
    w.writerows(rows)
PYEOF
