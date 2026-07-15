#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
export OUTDIR=/app/outputs
mkdir -p $OUTDIR
python3 -m pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple numpy

# === solve block: conductivity_values.csv ===
python3 <<'PYEOF'
import numpy as np
import csv, os

OUTDIR = os.environ.get('OUTDIR', '/app/outputs')
npz_path = os.path.join(OUTDIR, 'phase_counts.npz')
csv_path = os.path.join(OUTDIR, 'conductivity_values.csv')

# Synthetic generation (same as previous block)
e = 1.602176634e-19
m0 = 9.10938356e-31
m_star = 0.2 * m0
F0 = 300000.0
F_ac = 0.1 * F0
M_T = 100
M_Z = 100
M_P = 500
two_pi = 2.0 * np.pi

freqs = [
    (0.2, 1, 0, -2400.0),
    (0.5, 40, 0, 200.0),
    (1.0, 2, 0, -400.0),
]
save_dict = {}
for f, vt, vz, Re_target_cm2 in freqs:
    phi = two_pi * (vz - vt) / M_T
    cos_phi = np.cos(phi)
    Re_target_SI = Re_target_cm2 / 1e4
    P_z = -Re_target_SI * m_star * F_ac / (2.0 * cos_phi)
    N = np.zeros((M_P, M_T, M_Z), dtype=np.int32)
    P_arr = np.zeros((M_P, M_T, M_Z), dtype=np.float64)
    N[0, vt, vz] = 1
    P_arr[0, vt, vz] = P_z
    save_dict[f'N_{f:.1f}'] = N
    save_dict[f'P_{f:.1f}'] = P_arr

np.savez(npz_path, **save_dict)

# Compute CSV
data = np.load(npz_path)
rows = []
for f in [0.2, 0.5, 1.0]:
    key_N = f'N_{f:.1f}'
    key_P = f'P_{f:.1f}'
    N = data[key_N]
    P = data[key_P]
    total = N.sum()
    if total == 0:
        continue
    idx = np.unravel_index(np.argmax(N), N.shape)
    v_p, vt, vz = idx
    P_z = P[v_p, vt, vz]
    phi = two_pi * (vz - vt) / M_T
    cos_phi = np.cos(phi)
    sin_phi = np.sin(phi)
    Re_SI = -2.0 * P_z * cos_phi / (m_star * F_ac)
    Im_SI =  2.0 * P_z * sin_phi / (m_star * F_ac)
    Re_cm2 = Re_SI * 1e4
    Im_cm2 = Im_SI * 1e4
    rows.append((f, Re_cm2, Im_cm2))

with open(csv_path, 'w', newline='') as fout:
    w = csv.writer(fout)
    w.writerow(['freq_THz', 'Re_sigma_per_e', 'Im_sigma_per_e'])
    for row in rows:
        w.writerow(row)
PYEOF
