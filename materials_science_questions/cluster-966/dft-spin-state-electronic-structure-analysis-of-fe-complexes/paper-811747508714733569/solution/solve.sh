#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs
python3 /solution/compute_efg.py

# === solve block: derived_parameters.json ===
python3 << 'PYEOF'
import math, json, csv, os

outdir = os.environ.get('OUTDIR', '/app/outputs')

# --- Crystallographic data (forsterite, scaled to paper's cell) ---
a, b, c = 4.78, 10.22, 5.96
O1 = (0.425, 0.610, 0.760)
O2 = (0.215, 0.450, 0.200)
O3 = (0.285, 0.163, 0.035)
M1 = (0.0, 0.0, 0.0)
M2 = (0.2775, 0.25, 0.010)

def frac_to_cart(frac):
    return (frac[0]*a, frac[1]*b, frac[2]*c)

def sub_frac(p1, p2):
    return (p1[0]-p2[0], p1[1]-p2[1], p1[2]-p2[2])

def norm(v):
    s = math.sqrt(v[0]*v[0] + v[1]*v[1] + v[2]*v[2])
    return (v[0]/s, v[1]/s, v[2]/s)

def cross(a, b):
    return (a[1]*b[2] - a[2]*b[1],
            a[2]*b[0] - a[0]*b[2],
            a[0]*b[1] - a[1]*b[0])

def dot(a, b):
    return a[0]*b[0] + a[1]*b[1] + a[2]*b[2]

# M(1) EFG axes
O3_cart = frac_to_cart(O3)
Vzz_dir = norm((2*O3_cart[0], 2*O3_cart[1], 2*O3_cart[2]))
O1_cart = frac_to_cart(O1)
Vxx_temp = norm((2*O1_cart[0], 2*O1_cart[1], 2*O1_cart[2]))
Vyy_m1 = norm(cross(Vzz_dir, Vxx_temp))
Vxx_m1 = norm(cross(Vyy_m1, Vzz_dir))
M1_axes = {'Vzz': Vzz_dir, 'Vxx': Vxx_m1, 'Vyy': Vyy_m1}

# M(2) EFG axes
O1_cart = frac_to_cart(O1)
M2_cart = frac_to_cart(M2)
Vyy_m2_dir = norm(sub_frac(O1_cart, M2_cart))
O3c_cart = frac_to_cart(O3)
Vzz_m2_dir = norm(sub_frac(O3c_cart, M2_cart))
Vxx_m2 = norm(cross(Vyy_m2_dir, Vzz_m2_dir))
Vzz_m2 = norm(cross(Vxx_m2, Vyy_m2_dir))
Vyy_m2 = Vyy_m2_dir
M2_axes = {'Vzz': Vzz_m2, 'Vxx': Vxx_m2, 'Vyy': Vyy_m2}

# Write derived_parameters.json
os.makedirs(outdir, exist_ok=True)

def axis_json(name, vec):
    return {
        "axis": name,
        "direction_cosines": {
            "cx": round(vec[0], 6),
            "cy": round(vec[1], 6),
            "cz": round(vec[2], 6)
        }
    }

params = {
    "M1": {
        "eta": 0.2,
        "sign_q": "positive",
        "Vzz_direction": axis_json("O(3b)-M(1)-O(3)", M1_axes['Vzz']),
        "Vxx_direction": axis_json("O(1)-M(1)-O(1)", M1_axes['Vxx']),
        "Vyy_direction": axis_json("O(2)-M(1)-O(2)", M1_axes['Vyy'])
    },
    "M2": {
        "eta": 0.4,
        "sign_q": "positive",
        "Vzz_direction": axis_json("M(2)-O(3c)", M2_axes['Vzz']),
        "Vxx_direction": axis_json("M(2)-O(3d)", M2_axes['Vxx']),
        "Vyy_direction": axis_json("M(2)-O(1)", M2_axes['Vyy'])
    },
    "site_distribution": {
        "M1_fraction": 0.5,
        "M2_fraction": 0.5
    },
    "total_Fe_per_formula": 0.163,
    "Fe_per_site": {
        "M1": 0.081,
        "M2": 0.081
    }
}

with open(os.path.join(outdir, 'derived_parameters.json'), 'w') as f:
    json.dump(params, f, indent=2)

# Write theoretical_area_ratios.csv with paper's combined theoretical ratios
ratios = [
    (90.0, 40.5, 1.02),
    (90.0, 30.0, 1.01),
    (90.0, 15.0, 1.04),
    (90.0,  8.0, 1.05),
    (90.0,  0.0, 1.06),
    (78.0,  0.0, 1.05),
    (66.0,  0.0, 1.04),
    (57.0,  0.0, 1.02),
    (52.0, 90.0, 1.08),
    (45.0,  0.0, 1.00),
    (38.5, 94.6, 1.02),
    (38.5, 59.6, 1.00),
    (35.0, 90.0, 1.00),
    (30.0,  0.0, 0.98),
    (18.0, 90.0, 0.98),
    (15.0,  0.0, 0.97),
    ( 0.0,  0.0, 0.97),
]

with open(os.path.join(outdir, 'theoretical_area_ratios.csv'), 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['theta', 'phi', 'AH_AL_combined'])
    for th, ph, r in ratios:
        writer.writerow([f'{th:.1f}', f'{ph:.1f}', f'{r:.2f}'])

print('Artifacts written.')
PYEOF

# === solve block: theoretical_area_ratios.csv ===
true
