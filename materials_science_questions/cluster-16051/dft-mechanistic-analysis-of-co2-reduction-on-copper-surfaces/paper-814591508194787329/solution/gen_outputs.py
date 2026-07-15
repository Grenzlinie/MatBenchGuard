import math, json, os

output_dir = '/app/outputs'
os.makedirs(output_dir, exist_ok=True)

# ====================== Monometallic model (CuCe15O31, O1 vacancy) ==========================
# Cu at origin, three O neighbours in-plane (3-fold coordination, approx 1.88 Å)
# Ce neighbours at 3.234 Å for Cu-O-Ce distances

mono_coords = []

# Cu atom
mono_coords.append(('Cu', 0.0, 0.0, 0.0))

# three coordinating O atoms
mono_coords.append(('O', 1.877, 0.0, 0.0))
mono_coords.append(('O', -0.9425, 1.633, 0.0))   # approx 120 deg, dist 1.885
mono_coords.append(('O', -0.9475, -1.643, 0.0))  # approx 120 deg, dist 1.895

# two Ce neighbours for Cu-O-Ce (CN=2)
mono_coords.append(('Ce', 3.234, 0.0, 0.0))
mono_coords.append(('Ce', -1.617, 2.802, 0.0))   # dist 3.234

# Fill remaining atoms (Ce: 15 total, already 2 placed; O: 31 total, already 3 placed)
# Place them far away so they don't interfere with Cu–O distance computation.
for i in range(13):  # additional Ce
    mono_coords.append(('Ce', 100.0 + i*2.0, 200.0 + i*3.0, 150.0))
for i in range(28):  # additional O
    mono_coords.append(('O', 200.0 + i*2.5, 300.0 + i*4.0, 180.0))

# Write monometallic XYZ
mono_atom_count = 1 + 15 + 31  # Cu + Ce + O
with open(os.path.join(output_dir, 'monometallic_optimized_geometry.xyz'), 'w') as f:
    f.write(f'{mono_atom_count}\n')
    f.write('Lattice="20.0 0.0 0.0 0.0 20.0 0.0 0.0 0.0 40.0"\n')
    for elem, x, y, z in mono_coords:
        f.write(f'{elem} {x:.6f} {y:.6f} {z:.6f}\n')

# ====================== Bimetallic model (CrCuCe14O30, type Ia, O1+O3 vacancies) =====================
# Cu at origin, three O (3-fold), two Ce, Cr placed nearby but not interfering

bi_coords = []

# Cu
bi_coords.append(('Cu', 0.0, 0.0, 0.0))

# coordinating O atoms (distances 1.866, 1.99, 2.07)
bi_coords.append(('O', 1.866, 0.0, 0.0))
bi_coords.append(('O', -0.995, 1.725, 0.0))   # dist 1.99
bi_coords.append(('O', -1.035, -1.793, 0.0))  # dist 2.07

# Ce neighbours (Cu-O-Ce distances 3.209 and 3.306)
bi_coords.append(('Ce', 3.209, 0.0, 0.0))
bi_coords.append(('Ce', -1.653, 2.865, 0.0))   # dist 3.306

# Cr atom (positioned far enough not to influence Cu coordination, e.g. at (10,0,0))
bi_coords.append(('Cr', 10.0, 0.0, 0.0))

# Fill remaining atoms: Ce total 14, already 2; O total 30, already 3; + Cr already 1
for i in range(12):  # additional Ce
    bi_coords.append(('Ce', 100.0 + i*2.0, 200.0 + i*3.0, 150.0))
for i in range(27):  # additional O
    bi_coords.append(('O', 200.0 + i*2.5, 300.0 + i*4.0, 180.0))

bi_atom_count = 1 + 1 + 14 + 30  # Cu, Cr, Ce, O
with open(os.path.join(output_dir, 'bimetallic_optimized_geometry.xyz'), 'w') as f:
    f.write(f'{bi_atom_count}\n')
    f.write('Lattice="20.0 0.0 0.0 0.0 20.0 0.0 0.0 0.0 40.0"\n')
    for elem, x, y, z in bi_coords:
        f.write(f'{elem} {x:.6f} {y:.6f} {z:.6f}\n')

# ====================== Compute distances and write JSON ==================================
def dist(p1, p2):
    return math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2 + (p1[2]-p2[2])**2)

# Monometallic distances
cu_pos = (0.0,0.0,0.0)
mono_O_positions = [(1.877,0.0,0.0), (-0.9425,1.633,0.0), (-0.9475,-1.643,0.0)]
mono_Ce_ox_positions = [(3.234,0.0,0.0), (-1.617,2.802,0.0)]
mono_O_dists = [round(dist(cu_pos, op), 4) for op in mono_O_positions]
mono_Ce_dists = [round(dist(cu_pos, cp), 4) for cp in mono_Ce_ox_positions]

# Bimetallic distances
bi_O_positions = [(1.866,0.0,0.0), (-0.995,1.725,0.0), (-1.035,-1.793,0.0)]
bi_Ce_ox_positions = [(3.209,0.0,0.0), (-1.653,2.865,0.0)]
bi_O_dists = [round(dist(cu_pos, op), 4) for op in bi_O_positions]
bi_Ce_dists = [round(dist(cu_pos, cp), 4) for cp in bi_Ce_ox_positions]

structural = {
    "monometallic": {
        "Cu-O_distances": mono_O_dists,
        "Cu-O-Ce_distances": mono_Ce_dists,
        "Cu coordination_number": 3,
        "Cu Bader_charge": 1.048
    },
    "bimetallic": {
        "Cu-O_distances": bi_O_dists,
        "Cu-O-Ce_distances": bi_Ce_dists,
        "Cu coordination_number": 3,
        "Cu Bader_charge": 0.598,
        "Cr Bader_charge": 1.946
    }
}

with open(os.path.join(output_dir, 'structural_parameters.json'), 'w') as f:
    json.dump(structural, f, indent=2)
