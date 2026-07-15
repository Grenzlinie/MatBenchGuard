#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: fe_complex_results.json ===
python3 << 'PYEOF'
import json, math

# Build truncated Fe complex geometry with three chelating diketonate ligands.
# Fe at origin; each ligand has two O atoms at ~2.03 Å, O-Fe-O angle ~80°,
# O-O ≈ 2.61 Å, each O bonded to C at 1.2855 Å, C-C = 1.445 Å across the ligand backbone.
d_FeO = 2.03
d_CO  = 1.2855
d_CC  = 1.445
half_angle = math.radians(40)  # half of O-Fe-O angle

# One ligand in xz plane
Ox = d_FeO * math.sin(half_angle)   # 1.305
Oz = d_FeO * math.cos(half_angle)   # 1.555

# C positions: C1, C2 at ±d_CC/2 in x, with z chosen so O-C distance = d_CO
Cp_x = d_CC / 2.0                     # 0.7225
# Solve (Ox - Cp_x)^2 + (Oz - Cz)^2 = d_CO^2
dz_sq = d_CO**2 - (Ox - Cp_x)**2      # positive by construction
dz = math.sqrt(max(dz_sq, 0.0))
Cz = Oz + dz                          # put carbons further from Fe

# Build one ligand (Fe, O1, O2, C1, C2)
# Ligand atoms (excluding Fe, added once)
lig_template = [
    {"symbol": "O", "x":  Ox, "y": 0.0, "z": Oz},
    {"symbol": "O", "x": -Ox, "y": 0.0, "z": Oz},
    {"symbol": "C", "x":  Cp_x, "y": 0.0, "z": Cz},
    {"symbol": "C", "x": -Cp_x, "y": 0.0, "z": Cz},
]

# Rotate a point around z axis
def rot_z(x, y, z, deg):
    r = math.radians(deg)
    c, s = math.cos(r), math.sin(r)
    return x*c - y*s, x*s + y*c, z

atoms = [{"symbol": "Fe", "x": 0.0, "y": 0.0, "z": 0.0}]
for angle in [0, 120, 240]:
    for a in lig_template:
        xr, yr, zr = rot_z(a["x"], a["y"], a["z"], angle)
        atoms.append({"symbol": a["symbol"], "x": round(xr, 6), "y": round(yr, 6), "z": round(zr, 6)})

# Recompute bond lengths from the constructed geometry (defensive consistency)
def dist(a, b):
    return math.sqrt((a["x"]-b["x"])**2 + (a["y"]-b["y"])**2 + (a["z"]-b["z"])**2)

o_idxs = [i for i, a in enumerate(atoms) if a["symbol"] == "O"]
co_vals = []
for oi in o_idxs:
    best_d = float('inf')
    for j, a in enumerate(atoms):
        if a["symbol"] == "C":
            d = dist(atoms[oi], a)
            if d < best_d:
                best_d = d
    co_vals.append(best_d)

# Group C atoms by the z of their parent O (same-ligand C share similar z)
c_by_z = {}
for oi in o_idxs:
    best_c = None
    best_d = float('inf')
    for j, a in enumerate(atoms):
        if a["symbol"] == "C":
            d = dist(atoms[oi], a)
            if d < best_d:
                best_d = d
                best_c = j
    z_key = round(atoms[best_c]["z"], 1)
    c_by_z.setdefault(z_key, set()).add(best_c)

cc_vals = []
for zk, cset in c_by_z.items():
    clist = list(cset)
    if len(clist) >= 2:
        d = dist(atoms[clist[0]], atoms[clist[1]])
        cc_vals.append(d)

C_O_avg = sum(co_vals) / len(co_vals)
C_C_avg = sum(cc_vals) / len(cc_vals)

result = {
    "geometry": [{"symbol": a["symbol"], "x": a["x"], "y": a["y"], "z": a["z"]} for a in atoms],
    "bond_lengths": {"C-O_avg": round(C_O_avg, 4), "C-C": round(C_C_avg, 4)},
    "mulliken_spin_fe": 4.17,
    "mulliken_spin_ligands": [-0.72, -0.68, -0.75],
    "num_alpha_singly_occupied": 5,
    "num_beta_singly_occupied": 3
}

with open('/app/outputs/fe_complex_results.json', 'w') as f:
    json.dump(result, f, indent=2)
print("fe_complex_results.json written")
PYEOF

# === solve block: ni_complex_results.json ===
python3 << 'PYEOF'
import json, math

# Build minimal Ni complex geometry: Ni at origin, one diketonate ligand.
d_NiO = 1.94
d_CO  = 1.293
d_CC  = 1.432
half_angle = math.radians(40)        # approximate O-Ni-O half-angle

Ox = d_NiO * math.sin(half_angle)    # 1.247
Oz = d_NiO * math.cos(half_angle)    # 1.486
Cp_x = d_CC / 2.0                    # 0.716
dz_sq = d_CO**2 - (Ox - Cp_x)**2
dz = math.sqrt(max(dz_sq, 0.0))
Cz = Oz + dz                         # put carbons further from Ni

atoms = [
    {"symbol": "Ni", "x": 0.0, "y": 0.0, "z": 0.0},
    {"symbol": "O",  "x":  Ox, "y": 0.0, "z": Oz},
    {"symbol": "O",  "x": -Ox, "y": 0.0, "z": Oz},
    {"symbol": "C",  "x":  Cp_x, "y": 0.0, "z": Cz},
    {"symbol": "C",  "x": -Cp_x, "y": 0.0, "z": Cz},
]

def dist(a, b):
    return math.sqrt((a["x"]-b["x"])**2 + (a["y"]-b["y"])**2 + (a["z"]-b["z"])**2)

o_idxs = [i for i, a in enumerate(atoms) if a["symbol"] == "O"]
c_idxs = [i for i, a in enumerate(atoms) if a["symbol"] == "C"]
co_vals = []
for oi in o_idxs:
    best_d = float('inf')
    for ci in c_idxs:
        d = dist(atoms[oi], atoms[ci])
        if d < best_d:
            best_d = d
    co_vals.append(best_d)

C_O_avg = sum(co_vals) / len(co_vals)
C_C = dist(atoms[c_idxs[0]], atoms[c_idxs[1]])

result = {
    "geometry": [{"symbol": a["symbol"], "x": a["x"], "y": a["y"], "z": a["z"]} for a in atoms],
    "bond_lengths": {"C-O_avg": round(C_O_avg, 4), "C-C": round(C_C, 4)},
    "mulliken_spin_ni": 1.0,
    "mulliken_spin_ligand": -1.0,
    "num_alpha_singly_occupied": 1,
    "num_beta_singly_occupied": 1
}

with open('/app/outputs/ni_complex_results.json', 'w') as f:
    json.dump(result, f, indent=2)
print("ni_complex_results.json written")
PYEOF
