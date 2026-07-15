#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs
cat > /tmp/gen.py << 'PYEOF'
import csv, json, math

sigma = 1.5
step = 0.05
start, end = 770.0, 805.0
n = int((end - start)/step) + 1
energies = [start + i*step for i in range(n)]

amp_gauss = 2.0
area_one_gauss = amp_gauss * sigma * math.sqrt(2*math.pi)
area_both_gauss = 2 * area_one_gauss
target_total_area = 100.0
background_level = (target_total_area - area_both_gauss) / (end - start)
bg = background_level

def gauss(x, center, amplitude):
    return amplitude * math.exp(-((x - center)**2) / (2 * sigma**2))

def gen_xas(outfile):
    with open('/app/outputs/' + outfile, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['energy', 'intensity'])
        for e in energies:
            xas = bg + gauss(e, 778.0, amp_gauss) + gauss(e, 793.0, amp_gauss)
            writer.writerow([e, xas])

gauss_area_factor = sigma * math.sqrt(2*math.pi)
amp_L3 = 17.0 / gauss_area_factor
amp_L2 = -14.5 / gauss_area_factor

def gen_xmcd(outfile):
    with open('/app/outputs/' + outfile, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['energy', 'xmcd'])
        for e in energies:
            xmcd = gauss(e, 778.0, amp_L3) + gauss(e, 793.0, amp_L2)
            writer.writerow([e, xmcd])

def trapezoidal(xs, ys):
    total = 0.0
    for i in range(len(xs)-1):
        dx = xs[i+1] - xs[i]
        total += (ys[i] + ys[i+1]) * dx / 2.0
    return total

def compute_moments():
    xas = [bg + gauss(e, 778.0, amp_gauss) + gauss(e, 793.0, amp_gauss) for e in energies]
    xmcd = [gauss(e, 778.0, amp_L3) + gauss(e, 793.0, amp_L2) for e in energies]
    I_tot = trapezoidal(energies, xas)
    midpoint = 785.5
    L3_x = []; L3_y = []; L2_x = []; L2_y = []
    for e, y in zip(energies, xmcd):
        if e <= midpoint:
            L3_x.append(e); L3_y.append(y)
        else:
            L2_x.append(e); L2_y.append(y)
    A = trapezoidal(L3_x, L3_y)
    B = trapezoidal(L2_x, L2_y)
    n_holes = 3.0
    orb = abs((4.0/3.0) * (A + B) / I_tot * n_holes)
    spin_raw = abs((A - 2*B) / I_tot * n_holes)
    correction = 0.92
    spin_moment = spin_raw / correction
    total = spin_moment + orb
    return spin_moment, orb, total

def gen_json():
    spin, orb, total = compute_moments()
    data = {
        'spin_moment': round(spin, 6),
        'orbital_moment': round(orb, 6),
        'total_magnetic_moment': round(total, 6)
    }
    with open('/app/outputs/magnetic_moment.json', 'w') as f:
        json.dump(data, f, indent=2)

if __name__ == '__main__':
    import sys
    mode = sys.argv[1]
    if mode == 'xas':
        gen_xas('xas.csv')
    elif mode == 'xmcd':
        gen_xmcd('xmcd.csv')
    elif mode == 'json':
        gen_json()
    else:
        print('unknown mode')
PYEOF

# === solve block: magnetic_moment.json ===
python3 /tmp/gen.py json
