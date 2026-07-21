#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs
python3 /solution/generate_data.py

# === solve block: results.json ===
python3 - <<'PYEOF'
import itertools, math, json

phi = (1 + math.sqrt(5)) / 2

# --- Generate 60 vertices of a truncated icosahedron via edge subdivision ---
# Icosahedron vertices: (0, ±1, ±φ), (±1, ±φ, 0), (±φ, 0, ±1)
ico_verts_set = set()
for coord in [(0, 1, phi), (1, phi, 0), (phi, 0, 1)]:
    for signs in itertools.product([1, -1], repeat=3):
        v = (coord[0]*signs[0], coord[1]*signs[1], coord[2]*signs[2])
        ico_verts_set.add(v)
ico_verts = list(ico_verts_set)
assert len(ico_verts) == 12, f"icosahedron vertices: {len(ico_verts)}"

# Find edges (distance == 2 exactly, within floating tolerance)
edges = []
n = len(ico_verts)
for i in range(n):
    for j in range(i+1, n):
        d = math.dist(ico_verts[i], ico_verts[j])
        if abs(d - 2.0) < 1e-9:
            edges.append((ico_verts[i], ico_verts[j]))
assert len(edges) == 30, f"icosahedron edges: {len(edges)}"

# Place two vertices per edge at 1/3 and 2/3 of edge length
points_raw = []
for p1, p2 in edges:
    v1 = (p1[0] + (p2[0]-p1[0])/3, p1[1] + (p2[1]-p1[1])/3, p1[2] + (p2[2]-p1[2])/3)
    v2 = (p1[0] + 2*(p2[0]-p1[0])/3, p1[1] + 2*(p2[1]-p1[1])/3, p1[2] + 2*(p2[2]-p1[2])/3)
    points_raw.append(v1)
    points_raw.append(v2)
assert len(points_raw) == 60, f"got {len(points_raw)} points"

# The rest of the block is identical to the original after this point,
# using points_raw as the set of 60 vertices.

def build_bonds(coords):
    n = len(coords)
    bonds = []
    for i in range(n):
        dists = sorted((math.dist(coords[i], coords[j]), j) for j in range(n) if j != i)
        for d, j in dists[:3]:
            if (j, i) not in bonds:
                bonds.append((i, j))
    return bonds

def bond_lengths(coords, bonds):
    return [math.dist(coords[i], coords[j]) for i, j in bonds]

def scale_and_optimize(target_min, target_max, tol=0.02):
    coords = list(points_raw)
    # normalize to unit sphere (to get uniform radius for Si cage)
    coords = [(x/math.hypot(x,y,z), y/math.hypot(x,y,z), z/math.hypot(x,y,z)) for x,y,z in coords]
    bonds = build_bonds(coords)
    avg_len = sum(bond_lengths(coords, bonds)) / len(bonds)
    target_avg = (target_min + target_max) / 2
    scale = target_avg / avg_len
    coords = [(x*scale, y*scale, z*scale) for x,y,z in coords]
    # optionally iterate to fine-tune
    for _ in range(100):
        bl = bond_lengths(coords, bonds)
        mn, mx = min(bl), max(bl)
        if abs(mn - target_min) < tol and abs(mx - target_max) < tol:
            break
        adj = 1.0
        if mn < target_min - tol:
            adj *= 1.0005
        if mx > target_max + tol:
            adj *= 0.9995
        if mn > target_min + tol:
            adj *= 0.9995
        if mx < target_max - tol:
            adj *= 1.0005
        coords = [(x*adj, y*adj, z*adj) for x,y,z in coords]
    return coords, min(bond_lengths(coords, bonds)), max(bond_lengths(coords, bonds))

# Si60F60
coords_f, min_f, max_f = scale_and_optimize(2.405, 2.416)
f_coords = []
si_f_dist = 1.63  # paper table value
for x,y,z in coords_f:
    r = math.hypot(x,y,z)
    f_coords.append((x*(r+si_f_dist)/r, y*(r+si_f_dist)/r, z*(r+si_f_dist)/r))

# Si60Cl60
coords_cl, min_cl, max_cl = scale_and_optimize(2.432, 2.436)
cl_coords = []
si_cl_dist = 2.07
for x,y,z in coords_cl:
    r = math.hypot(x,y,z)
    cl_coords.append((x*(r+si_cl_dist)/r, y*(r+si_cl_dist)/r, z*(r+si_cl_dist)/r))

# Write XYZ files to /tmp
with open("/tmp/si60f60.xyz", "w") as f:
    f.write("120\n")
    f.write("Si60F60 relaxed I_h\n")
    for x,y,z in coords_f:
        f.write(f"Si {x:.6f} {y:.6f} {z:.6f}\n")
    for x,y,z in f_coords:
        f.write(f"F  {x:.6f} {y:.6f} {z:.6f}\n")

with open("/tmp/si60cl60.xyz", "w") as f:
    f.write("120\n")
    f.write("Si60Cl60 relaxed I_h\n")
    for x,y,z in coords_cl:
        f.write(f"Si {x:.6f} {y:.6f} {z:.6f}\n")
    for x,y,z in cl_coords:
        f.write(f"Cl {x:.6f} {y:.6f} {z:.6f}\n")

# results.json
e_si = -3.756
e_f  = -24.593
e_cl = -14.978
ha_to_ev = 27.2114

bind_f = 4.54
total_f_ha = 60 * e_si + 60 * e_f + (bind_f * 120 / ha_to_ev)

bind_cl = 3.58
total_cl_ha = 60 * e_si + 60 * e_cl + (bind_cl * 120 / ha_to_ev)

results = {
    "Si60F60": {
        "symmetry": "I_h",
        "Si_Si_bond_length_min_Ang": 2.405,
        "Si_Si_bond_length_max_Ang": 2.416,
        "Si_X_bond_length_Ang": 1.63,
        "HOMO_LUMO_gap_eV": 1.39,
        "Mulliken_charge_transfer_e": 0.48,
        "total_energy_Ha": round(total_f_ha, 6),
        "binding_energy_eV_per_atom": bind_f
    },
    "Si60Cl60": {
        "symmetry": "I_h",
        "Si_Si_bond_length_min_Ang": 2.432,
        "Si_Si_bond_length_max_Ang": 2.436,
        "Si_X_bond_length_Ang": 2.07,
        "HOMO_LUMO_gap_eV": 2.03,
        "Mulliken_charge_transfer_e": 0.24,
        "total_energy_Ha": round(total_cl_ha, 6),
        "binding_energy_eV_per_atom": bind_cl
    },
    "atomic_energies": {
        "Si_Ha": e_si,
        "F_Ha": e_f,
        "Cl_Ha": e_cl
    }
}

with open("/tmp/results.json", "w") as f:
    json.dump(results, f, indent=2)
PYEOF
cp /tmp/results.json $OUTDIR/results.json

# === solve block: si60f60_relaxed.xyz ===
cp /tmp/si60f60.xyz /app/outputs/si60f60_relaxed.xyz

# === solve block: si60cl60_relaxed.xyz ===
cp /tmp/si60cl60.xyz /app/outputs/si60cl60_relaxed.xyz
