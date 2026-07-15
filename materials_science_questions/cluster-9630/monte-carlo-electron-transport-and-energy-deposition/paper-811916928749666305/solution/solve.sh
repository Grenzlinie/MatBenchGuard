#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: electron_radial_profiles.csv ===
python3 << 'PYEOF'
import math, csv
pi = math.pi
init_dn = 1/pi

params_400 = {
    10: {'R10': 4, 'on_axis_dn': init_dn * math.exp(-10/50)},
    20: {'R10': 9, 'on_axis_dn': init_dn * math.exp(-20/50)},
    40: {'R10': 30, 'on_axis_dn': init_dn * math.exp(-40/50)},
    60: {'R10': 55, 'on_axis_dn': init_dn * math.exp(-60/50)},
    100: {'half_w': 20, 'on_axis_dn': init_dn / 10000}
}
params_600 = {
    10: {'R10': 3, 'on_axis_dn': init_dn * math.exp(-10/50)},
    20: {'R10': 7, 'on_axis_dn': init_dn * math.exp(-20/50)},
    40: {'R10': 22.5, 'on_axis_dn': init_dn * math.exp(-40/50)},
    60: {'R10': 35, 'on_axis_dn': init_dn * math.exp(-60/50)},
    100: {'half_w': 27.5, 'on_axis_dn': init_dn / 3000}
}

def gaussian(a, sigma, r):
    return a * math.exp(-r*r/(2*sigma*sigma))

rows = []
for energy, params in [(400, params_400), (600, params_600)]:
    for dist, p in params.items():
        if 'R10' in p:
            sigma = p['R10'] / math.sqrt(2*math.log(10))
            rmax = p['R10'] + 30
        else:
            sigma = p['half_w'] / math.sqrt(2*math.log(2))
            rmax = p['half_w'] + 30
        a_dn = p['on_axis_dn']
        e_factor = (1 - dist/200.0)
        r = 0.0
        dr = 0.2
        while r <= rmax:
            dn = gaussian(a_dn, sigma, r)
            de = dn * energy * e_factor
            rows.append([energy, dist, round(r, 2), dn, de])
            r += dr

with open('/app/outputs/electron_radial_profiles.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['energy_keV', 'distance_cm', 'radius_cm', 'dN_dS', 'dE_dS'])
    for row in rows:
        writer.writerow([row[0], row[1], f"{row[2]:.2f}", f"{row[3]:.6e}", f"{row[4]:.6e}"])
PYEOF
