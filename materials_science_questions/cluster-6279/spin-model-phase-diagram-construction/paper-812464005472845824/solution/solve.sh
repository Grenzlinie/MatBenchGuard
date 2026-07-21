#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: phase_boundaries.csv ===
python3 << 'PYEOF'
import math, csv, itertools, random

z = 4
KoverJs = [5, 3, -0.1, -0.8, -1, -2.5, -3, -3.5]

T_min, T_max, nT = 0.01, 3.0, 100
D_min, D_max, nD = -5.0, 5.0, 100
T_vals = [T_min + (T_max - T_min) * i / (nT - 1) for i in range(nT)]
D_vals = [D_min + (D_max - D_min) * i / (nD - 1) for i in range(nD)]

def phi(u, v, J, K, Delta):
    eD = math.exp(Delta)
    eK = math.exp(K)
    eJ = math.exp(J)
    emJ = math.exp(-J)
    uz = u ** (z - 1)
    vz = v ** (z - 1)
    num = eD + eK * (eJ * uz + emJ * vz)
    denom = eD + uz + vz
    return num / denom

def iterate(x0, y0, J, K, Delta, max_iter=5000, tol=1e-8):
    x, y = x0, y0
    hist_x, hist_y = [], []
    for i in range(max_iter):
        xn = phi(x, y, J, K, Delta)
        yn = phi(y, x, J, K, Delta)
        if i > 200 and abs(xn - x) < tol and abs(yn - y) < tol:
            return ('fixed', xn, yn)
        x, y = xn, yn
        if i >= max_iter - 50:
            hist_x.append(x)
            hist_y.append(y)
    if len(hist_x) < 4:
        return ('none', None, None)
    diffs = []
    for i in range(1, min(20, len(hist_x)), 2):
        if i+1 < len(hist_x):
            diffs.append(abs(hist_x[-i] - hist_x[-i-2]) + abs(hist_y[-i] - hist_y[-i-2]))
    if diffs and max(diffs) < tol * 10:
        return ('cycle2', (hist_x[-2], hist_y[-2]), (hist_x[-1], hist_y[-1]))
    return ('none', None, None)

def free_energy(x, y, Delta):
    xz = x ** z
    yz = y ** z
    xz1 = x ** (z - 1)
    yz1 = y ** (z - 1)
    if (xz + yz) < 1e-300:
        term1 = 0.0
    else:
        term1 = math.log(1.0 + math.exp(-Delta) * (xz + yz))
    if (xz1 + yz1) < 1e-300:
        term2 = 0.0
    else:
        term2 = (z / (2 - z)) * math.log(1.0 + math.exp(-Delta) * (xz1 + yz1))
    return -(term1 + term2)

def order_params(x, y, Delta):
    eD = math.exp(Delta)
    xz = x ** z
    yz = y ** z
    denom = eD + xz + yz
    m = (xz - yz) / denom if denom != 0 else 0.0
    q = (xz + yz) / denom if denom != 0 else 0.0
    return m, q

def classify_attractor(att, Delta):
    typ = att[0]
    if typ == 'fixed':
        x, y = att[1], att[2]
        m, q = order_params(x, y, Delta)
        if abs(x - y) < 1e-6:
            phase = 'd'
        else:
            phase = 'f'
        return phase, m, q, None, None
    elif typ == 'cycle2':
        (xA, yA), (xB, yB) = att[1], att[2]
        mA, qA = order_params(xA, yA, Delta)
        mB, qB = order_params(xB, yB, Delta)
        if abs(mA) < 1e-6 and abs(mB) < 1e-6:
            if abs(qA - qB) < 1e-6:
                phase = 'd'
            else:
                phase = 'a'
        else:
            if abs(mA - mB) < 5e-3:
                phase = 'f'
            else:
                phase = 'i'
        return phase, mA, qA, mB, qB
    else:
        return 'unknown', 0, 0, None, None

def attractor_key(att):
    if att[0] == 'fixed':
        return (att[1], att[2])
    elif att[0] == 'cycle2':
        return (att[1][0], att[1][1], att[2][0], att[2][1])
    else:
        return None

points = []

for KoverJ in KoverJs:
    print(f"Processing K/J = {KoverJ}", flush=True)
    for iT, T in enumerate(T_vals):
        for iD, D in enumerate(D_vals):
            if T < 1e-4:
                continue
            J = 1.0 / (z * T)
            Delta = D / T
            K = KoverJ * J
            initial_guesses = [
                (0.1, 0.1),
                (1.0, 1.0),
                (0.5, 2.0),
                (2.0, 0.5),
                (random.uniform(0.1, 2.0), random.uniform(0.1, 2.0)),
                (random.uniform(0.1, 2.0), random.uniform(0.1, 2.0))
            ]
            attractors = []
            for x0, y0 in initial_guesses:
                att = iterate(x0, y0, J, K, Delta)
                if att[0] != 'none':
                    ak = attractor_key(att)
                    if ak not in [attractor_key(a) for a in attractors]:
                        new = True
                        for a in attractors:
                            if att[0] == a[0]:
                                if att[0] == 'fixed':
                                    if abs(att[1]-a[1])<1e-5 and abs(att[2]-a[2])<1e-5:
                                        new = False; break
                                elif att[0] == 'cycle2':
                                    (a1,a2),(b1,b2)=att[1],att[2]
                                    (c1,c2),(d1,d2)=a[1],a[2]
                                    if (abs(a1-c1)<1e-5 and abs(a2-c2)<1e-5 and abs(b1-d1)<1e-5 and abs(b2-d2)<1e-5) or \
                                       (abs(a1-d1)<1e-5 and abs(a2-d2)<1e-5 and abs(b1-c1)<1e-5 and abs(b2-c2)<1e-5):
                                        new = False; break
                        if new:
                            attractors.append(att)
            if not attractors:
                continue
            best_att = None
            best_fe = float('inf')
            for att in attractors:
                if att[0] == 'fixed':
                    fe = free_energy(att[1], att[2], Delta)
                elif att[0] == 'cycle2':
                    fe1 = free_energy(att[1][0], att[1][1], Delta)
                    fe2 = free_energy(att[2][0], att[2][1], Delta)
                    fe = (fe1 + fe2) / 2.0
                else:
                    continue
                if fe < best_fe:
                    best_fe = fe
                    best_att = att
            if best_att:
                phase, m, q, mA, qA = classify_attractor(best_att, Delta)
                points.append((KoverJ, T, D, phase, best_fe, best_att))

phase_grid = {}
fe_grid = {}
for KoverJ in KoverJs:
    phase_grid[KoverJ] = {}
    fe_grid[KoverJ] = {}
    for iT in range(nT):
        for iD in range(nD):
            phase_grid[KoverJ][(iT,iD)] = None
            fe_grid[KoverJ][(iT,iD)] = None
for rec in points:
    k, T, D, ph, fe, att = rec
    iT = int(round((T - T_min) / (T_max - T_min) * (nT - 1)))
    iD = int(round((D - D_min) / (D_max - D_min) * (nD - 1)))
    if 0 <= iT < nT and 0 <= iD < nD:
        phase_grid[k][(iT,iD)] = ph
        fe_grid[k][(iT,iD)] = fe

transitions = []
for KoverJ in KoverJs:
    for iT in range(nT - 1):
        for iD in range(nD - 1):
            for (diT, diD) in [(1,0), (0,1)]:
                iT2 = iT + diT
                iD2 = iD + diD
                p1 = phase_grid[KoverJ].get((iT,iD))
                p2 = phase_grid[KoverJ].get((iT2,iD2))
                if p1 is None or p2 is None or p1 == p2:
                    continue
                T_mid = (T_vals[iT] + T_vals[iT2]) / 2.0
                D_mid = (D_vals[iD] + D_vals[iD2]) / 2.0
                if p1 == 'd' and p2 == 'f':
                    att_f = next((r[5] for r in points if r[0]==KoverJ and abs(r[1]-T_vals[iT2])<1e-6 and abs(r[2]-D_vals[iD2])<1e-6), None)
                    if att_f is not None:
                        _, m_f, _, _, _ = classify_attractor(att_f, D_vals[iD2]/T_vals[iT2] if T_vals[iT2]>0 else 0)
                        trans_type = 'second_order' if abs(m_f) < 0.1 else 'first_order'
                    else:
                        trans_type = 'second_order'
                else:
                    trans_type = 'first_order'
                transitions.append((KoverJ, D_mid, T_mid, trans_type, p1, p2))

with open('/app/outputs/phase_boundaries.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['K_over_J', 'delta_over_zJ', 'temperature_over_zJ', 'transition_type', 'phase_from', 'phase_to'])
    for row in transitions:
        writer.writerow(row)

print(f"Wrote {len(transitions)} transition points.")
PYEOF
