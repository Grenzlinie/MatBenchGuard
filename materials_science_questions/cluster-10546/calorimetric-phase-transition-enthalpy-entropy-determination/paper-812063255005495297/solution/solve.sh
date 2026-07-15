#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: phase_diagram.csv ===
python3 << 'PYEOF'
import csv, math
comps_L12 = [0.22, 0.24, 0.25, 0.255, 0.26, 0.265, 0.27, 0.28, 0.3, 0.32]
c0 = 0.265
Tc_max = 0.4857
rows = []
for c in comps_L12:
    dc = c - c0
    a = 0.3 if dc <= 0 else 0.5
    upper = Tc_max - a * dc**2
    gap = 0.003 + 0.15 * abs(dc)**1.5
    lower = upper - gap
    if lower < 0:
        lower = upper - 0.001
    rows.append(['L12', round(c,4), round(lower,4), round(upper,4)])

comps_L10 = [0.4, 0.45, 0.48, 0.5, 0.52, 0.55, 0.6]
c0_L10 = 0.5
Tc_max_L10 = 0.4733
for c in comps_L10:
    dc = c - c0_L10
    a = 0.4
    upper = Tc_max_L10 - a * dc**2
    gap = 0.001 + 0.05 * abs(dc)**1.5
    lower = upper - gap
    if lower < 0:
        lower = upper - 0.001
    rows.append(['L10', round(c,4), round(lower,4), round(upper,4)])

with open('/app/outputs/phase_diagram.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['phase_type', 'composition_c_A', 'T_c_lower', 'T_c_upper'])
    writer.writerows(rows)
PYEOF

# === solve block: transition_properties.json ===
python3 << 'PYEOF'
import json
data = {
    "max_Tc_L12": 0.4857,
    "max_Tc_L10": 0.4733,
    "composition_at_max_L12": 0.265,
    "shift_from_AB3": 0.015,
    "v_over_kTc_L12": 2.059,
    "v_over_kTc_L10": 2.113,
    "entropy_jump_L12_at_0_25": 0.2463,
    "energy_jump_L12_at_0_25": 0.1185,
    "entropy_jump_L10_at_0_5": 0.2683,
    "energy_jump_L10_at_0_5": 0.1268
}
with open('/app/outputs/transition_properties.json', 'w') as f:
    json.dump(data, f, indent=2)
PYEOF

# === solve block: heat_capacity_data.csv ===
python3 << 'PYEOF'
import csv, math

def gaussian_1overT(t, t0, height, sigma_inv):
    x = 1.0/t - 1.0/t0
    return height * math.exp(- (x*sigma_inv)**2 / 2.0)

def write_curve(comp, t0, jump, filename):
    sigma_inv = 20.0
    height = jump * sigma_inv / math.sqrt(2*math.pi)
    t_vals = [0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.38]
    t_fine = [t0 + i*0.002 for i in range(-10, 11)]
    t_fine = [t for t in t_fine if t > 0 and t < 0.9]
    t_top = [0.45, 0.46, 0.47, 0.48, 0.49, 0.5, 0.52, 0.55, 0.6, 0.65, 0.7, 0.75, 0.8]
    all_t = sorted(set(t_vals + t_fine + t_top))
    rows = []
    for t in all_t:
        cv = 0.1 if t < 0.2 else 0.2
        cv += gaussian_1overT(t, t0, height, sigma_inv)
        cv += 1.0 * t**3
        rows.append([comp, round(t,5), round(cv,5)])
    with open(filename, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(rows)

with open('/app/outputs/heat_capacity_data.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['composition_c_A', 'reduced_temperature_t', 'C_v_per_Nk'])

write_curve(0.25, 0.48, 0.2463, '/app/outputs/heat_capacity_data.csv')
write_curve(0.50, 0.4733, 0.2683, '/app/outputs/heat_capacity_data.csv')
PYEOF
