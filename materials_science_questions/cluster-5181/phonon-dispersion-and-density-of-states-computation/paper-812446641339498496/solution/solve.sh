#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
# install required packages
python3 -m pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple numpy scipy
mkdir -p "$OUTDIR"

# === solve block: step_02_dispersion_curves_sigma_a_1.30.csv ===
cat << 'PY' > /tmp/disp130.py
import sys, numpy as np, csv
output_path = sys.argv[1]

sigma = 1.0
sigma_a = 1.30
a = sigma / sigma_a

# generate fcc lattice sites (conventional cell basis)
def fcc_sites(max_repeats=6):
    basis = np.array([[0,0,0],[0.5,0.5,0],[0.5,0,0.5],[0,0.5,0.5]])
    cells = np.arange(-max_repeats, max_repeats+1)
    x,y,z = np.meshgrid(cells, cells, cells, indexing='ij')
    pos = np.stack([x.ravel(), y.ravel(), z.ravel()], axis=1)
    all_pos = pos[:, None, :] + basis[None, :, :]
    all_pos = all_pos.reshape(-1,3)
    return all_pos * a

sites = fcc_sites(6)
origin_idx = np.argmin(np.linalg.norm(sites, axis=1))
r = sites - sites[origin_idx]
mask = np.linalg.norm(r, axis=1) > 1e-12
r = r[mask]
rho = r / a
dist = np.linalg.norm(rho, axis=1)
uniq_dist = np.unique(np.round(dist, 10))
assert len(uniq_dist) >= 20, f"Only {len(uniq_dist)} shells, need >=20"
shell_cutoff = uniq_dist[19]
sel = dist <= shell_cutoff
rho_n = rho[sel]
dist_n = dist[sel]
n_list = [8,10,14,16]
rho_pow = {n: dist_n**n for n in n_list}
S8_0 = np.sum(1.0/rho_pow[8])
S14_0 = np.sum(1.0/rho_pow[14])
D0 = 24.0 * (sigma_a**8)

def compute_sums(q_val):
    phase = np.exp(2j * np.pi * q_val * rho_n[:,0])
    S_ab = {}
    for a_idx in range(3):
        for b_idx in range(3):
            num = rho_n[:,a_idx] * rho_n[:,b_idx] * phase
            S_ab[(a_idx,b_idx)] = {n: np.sum(num / rho_pow[n]) for n in n_list}
    S_scal = {n: np.sum(phase / rho_pow[n]) for n in n_list}
    return S_ab, S_scal

q_vals = np.linspace(0.0, 1.0, 101)
omega_L, omega_T = [], []
for q in q_vals:
    S_ab, S_scal = compute_sums(q)
    D = np.zeros((3,3), dtype=complex)
    for a in range(3):
        for b in range(3):
            D[a,b] = -28.0 * (sigma_a**6) * S_ab[(a,b)][16] + 8.0 * S_ab[(a,b)][10]
            if a == b:
                D[a,b] += (22.0/3.0 * (sigma_a**6) * S14_0 - 5.0/3.0 * S8_0 +
                           2.0 * (sigma_a**6) * S_scal[14] - S_scal[8])
    D *= D0
    eigvals = np.linalg.eigvalsh(D)
    omega = np.sqrt(np.abs(eigvals))
    omega_L.append(omega[2])
    omega_T.append(omega[0])

with open(output_path, 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['q','omega_L','omega_T'])
    for q, wL, wT in zip(q_vals, omega_L, omega_T):
        w.writerow([float(q), float(wL), float(wT)])
print(f"Written to {output_path}")
PY
python3 /tmp/disp130.py "$OUTDIR/step_02_dispersion_curves_sigma_a_1.30.csv"
rm /tmp/disp130.py

# === solve block: step_03_dispersion_curves_sigma_a_1.24.csv ===
python3 /solution/compute_phonons.py --sigma 1.24 --mode dispersion --output "$OUTDIR/step_03_dispersion_curves_sigma_a_1.24.csv"

# === solve block: step_04_frequency_distribution_sigma_a_1.30.csv ===
python3 /solution/compute_phonons.py --sigma 1.30 --mode dos --output "$OUTDIR/step_04_frequency_distribution_sigma_a_1.30.csv"
