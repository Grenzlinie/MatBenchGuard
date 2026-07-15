#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
set -euo pipefail
export OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"
python3 -m pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple numpy
python3 /solution/compute.py

# === solve block: free_energies.csv ===
python3 << 'EOF'
import csv, math, os, collections

pi      = math.pi
# k_B in Ryd/K: 1 Ry = 13.605693 eV, 1 eV = 11604.525 K
kb      = 1.0 / (13.605693 * 11604.525)
T       = 300.0
C_dipole = math.sqrt(1.0 / 137.0)

params = {
    'V' : {'Oa':93.54, 'Zd':3.50, 'Rd':1.85, 'nd':20.95},
    'Cr': {'Oa':81.54, 'Zd':4.50, 'Rd':1.70, 'nd':9.52},
    'Mn': {'Oa':82.59, 'Zd':5.50, 'Rd':1.63, 'nd':21.23},
    'Fe': {'Oa':79.48, 'Zd':6.50, 'Rd':1.51, 'nd':41.63},
}

for el in params:
    nd = params[el]['nd']
    params[el]['TS'] = (pi**2 / 3.0) * (kb**2) * nd * (T**2)

# ——— lattice constants ———
def lattice_constant(structure, Oa):
    if   structure == 'bcc': a = (2*Oa)**(1/3)
    elif structure == 'fcc': a = (4*Oa)**(1/3)
    elif structure == 'hcp': a = (Oa * math.sqrt(2))**(1/3)
    else: raise ValueError(structure)
    return a

# ——— shell generators ———
def _round(d):
    return round(d, 8)

def shells_bcc(max_shells=12, rmax=5.0):
    pts = []
    for i in range(-5, 6):
        for j in range(-5, 6):
            for k in range(-5, 6):
                if i==0 and j==0 and k==0: continue
                d = math.hypot(math.hypot(i, j), k)
                if d <= rmax: pts.append(d)
                d2 = math.hypot(math.hypot(i+0.5, j+0.5), k+0.5)
                if d2 <= rmax: pts.append(d2)
    cnt = {}
    for d in pts:
        r = _round(d); cnt[r] = cnt.get(r, 0) + 1
    return [(d, cnt[d]) for d in sorted(cnt)[:max_shells]]

def shells_fcc(max_shells=12, rmax=5.0):
    pts = []
    for i in range(-5, 6):
        for j in range(-5, 6):
            for k in range(-5, 6):
                if i==0 and j==0 and k==0: continue
                pts.append(math.hypot(math.hypot(i, j), k))
                pts.append(math.hypot(math.hypot(i+0.5, j+0.5), k))
                pts.append(math.hypot(math.hypot(i+0.5, j), k+0.5))
                pts.append(math.hypot(math.hypot(i, j+0.5), k+0.5))
    pts = [d for d in pts if d <= rmax]
    cnt = {}
    for d in pts:
        r = _round(d); cnt[r] = cnt.get(r, 0) + 1
    return [(d, cnt[d]) for d in sorted(cnt)[:max_shells]]

def shells_hcp(max_shells=12, rmax=5.0):
    c_over_a = math.sqrt(8.0/3.0)
    a1 = (1.0, 0.0, 0.0)
    a2 = (0.5, math.sqrt(3)/2, 0.0)
    cvec = (0.0, 0.0, c_over_a)
    basis = [(0,0,0), (2/3, 1/3, 0.5)]
    bcart = []
    for f in basis:
        x = f[0]*a1[0] + f[1]*a2[0] + f[2]*cvec[0]
        y = f[0]*a1[1] + f[1]*a2[1] + f[2]*cvec[1]
        z = f[0]*a1[2] + f[1]*a2[2] + f[2]*cvec[2]
        bcart.append((x,y,z))
    pts = []
    for n1 in range(-5,6):
        for n2 in range(-5,6):
            for n3 in range(-5,6):
                tx = n1*a1[0]+n2*a2[0]+n3*cvec[0]
                ty = n1*a1[1]+n2*a2[1]+n3*cvec[1]
                tz = n1*a1[2]+n2*a2[2]+n3*cvec[2]
                for b in bcart:
                    vx,vy,vz = tx+b[0], ty+b[1], tz+b[2]
                    d = math.hypot(math.hypot(vx, vy), vz)
                    if d>0 and d<=rmax: pts.append(d)
    cnt = {}
    for d in pts:
        r = _round(d); cnt[r] = cnt.get(r, 0) + 1
    return [(d, cnt[d]) for d in sorted(cnt)[:max_shells]]

shells_pre = {
    'bcc': shells_bcc(),
    'fcc': shells_fcc(),
    'hcp': shells_hcp(),
}

# ——— compute and write files ———
outdir = os.environ.get('OUTDIR', '/app/outputs')
fname_free = os.path.join(outdir, 'free_energies.csv')
fname_diff = os.path.join(outdir, 'energy_differences.csv')

rows_free = []

with open(fname_free, 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['element','structure','shell','method','N_atoms',
                'interatomic_distance','pair_potential_Ud',
                'cumulative_free_energy_Fd'])
    for el_name, p in params.items():
        Zd, Rd = p['Zd'], p['Rd']
        TS = p['TS']
        A_scale = Zd * (1.0 - Zd/10.0) * (56.12/pi) * (Rd**3)
        B_rep   = (450.0/(pi**2)) * Zd * (Rd**6)
        for struct in ['bcc','fcc','hcp']:
            a = lattice_constant(struct, p['Oa'])
            Nc = 8 if struct=='bcc' else 12
            shells = [(d_u * a, N) for d_u, N in shells_pre[struct]]
            for method in ['Nc','extended']:
                cum = 0.0
                for idx, (R, N) in enumerate(shells, start=1):
                    if method == 'Nc':
                        # attractive: total contribution per shell = N * U_pair_attractive
                        att_contrib = -A_scale * math.sqrt(12.0 / Nc) * N / (R**5)
                    else:  # extended
                        # attractive: replace Nc -> N, total = N * U_pair_attractive = -A_scale * sqrt(12/N) * N / R^5
                        att_contrib = -A_scale * math.sqrt(12.0 / N) * N / (R**5)
                    rep_contrib = B_rep * N / (R**8)
                    dip_contrib = C_dipole * N / (R**3)
                    cum += (att_contrib + rep_contrib + dip_contrib)
                    Fd_cum = 0.5 * cum - TS
                    # per-pair U_d for this shell (for documentation)
                    if method == 'Nc':
                        pref_pair = math.sqrt(12.0 / Nc)
                    else:
                        pref_pair = math.sqrt(12.0 / N)
                    U_pair = (-A_scale * pref_pair / (R**5)
                              + B_rep / (R**8) + C_dipole / (R**3))
                    w.writerow([el_name, struct, idx, method, N,
                                R, U_pair, Fd_cum])
                    rows_free.append((el_name, struct, idx, method, Fd_cum))

# ——— energy differences ———
diff_map = {}
for el, struct, shell, method, Fd in rows_free:
    diff_map[(el, method, shell, struct)] = Fd

diff_rows = []
for (el, method, shell), _ in {k[:3]:k for k in diff_map}.items():
    try:
        fb = diff_map[(el, method, shell, 'bcc')]
        ff = diff_map[(el, method, shell, 'fcc')]
        fh = diff_map[(el, method, shell, 'hcp')]
    except KeyError:
        continue
    diff_rows.append((el, method, shell, ff - fb, ff - fh))

with open(fname_diff, 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['element','method','shell','delta_F_fcc_bcc','delta_F_fcc_hcp'])
    for row in sorted(diff_rows):
        w.writerow(row)
EOF

# === solve block: energy_differences.csv ===
true
