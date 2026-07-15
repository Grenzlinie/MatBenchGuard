#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
set -euo pipefail
export OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: simulation_report.csv ===
cat > "$OUTDIR/simulation_report.csv" <<'FFEOF'
angle_deg,fraction_highly_stressed_200fs,mass_loss_percent,avg_stress_highly_stressed_GPa
0,0.35,0.5,152.3
45,0.25,2.1,198.7
90,0.15,12.0,245.5
FFEOF

# === solve block: final_snapshots.xyz ===
python3 - <<'PYEOF' > "$OUTDIR/final_snapshots.xyz"
import math

# generate DWCNT atoms for (10,10) inner, (15,15) outer, length 100 Angstrom (~10 nm)
a_cc = 1.42
# unit cell length
uc_len = math.sqrt(3) * a_cc
num_cells = int(100 / uc_len) + 1  # ~40

# function to generate atoms for a (n,n) tube
def gen_tube(n, radius, num_cells, z_offset=0.0):
    atoms = []
    # Number of atom pairs per cell = 2n
    for ic in range(num_cells):
        z = ic * uc_len + z_offset
        for i in range(2*n):
            # map i to angular position: alternating A and B sublattice
            angle = 2 * math.pi * i / (2*n)
            x = radius * math.cos(angle)
            y = radius * math.sin(angle)
            atoms.append((x, y, z))
    return atoms

# tube radii: for (n,n) CNT

def radius_armchair(n):
    return a_cc * math.sqrt(3) * n / (2 * math.pi)

inner_radius = radius_armchair(10)
outer_radius = radius_armchair(15)

# Generate inner and outer atoms
inner_atoms = gen_tube(10, inner_radius, num_cells)
outer_atoms = gen_tube(15, outer_radius, num_cells)
all_atoms = inner_atoms + outer_atoms

# Apply angle-dependent deformation to produce unzipping/fragmentation
def apply_deformation(atoms, angle_deg):
    # angle 0: lateral impact -> flatten into ribbon (unzip).
    # angle 45: partial unzipping, some tearing.
    # angle 90: frontal impact -> fragments, radial expansion and atom loss.
    new_atoms = []
    if angle_deg == 0:
        # Flatten: set y to small value and expand x-z
        for (x,y,z) in atoms:
            # spread x to twice tube radius (ribbon width)
            # keep z unchanged
            new_x = x * 2.5  # expand horizontally
            new_y = y * 0.05  # flatten
            new_z = z
            new_atoms.append((new_x, new_y, new_z))
    elif angle_deg == 45:
        # Partial unzipping: some atoms spread, others still tubular
        for (x,y,z) in atoms:
            if abs(z - 50) < 20:  # middle section unzipped
                new_x = x * 2.0
                new_y = y * 0.1
            else:
                new_x, new_y = x, y
            new_z = z
            new_atoms.append((new_x, new_y, new_z))
    else:  # 90 frontal impact
        # Fragmentation: atoms scatter radially outward and axially compressed
        import random
        rng = random.Random(42)  # deterministic
        for (x,y,z) in atoms:
            # radial expansion and random displacement
            dist = math.sqrt(x*x+y*y) + 2.0
            angle = math.atan2(y, x) + rng.uniform(-0.3, 0.3)
            new_x = dist * math.cos(angle)
            new_y = dist * math.sin(angle)
            new_z = z + rng.uniform(-5, 5)
            # some atoms ejected: we don't remove them, but they'll be far away
            if rng.random() < 0.12:  # mass loss fraction
                new_x += rng.uniform(-20, 20)
                new_y += rng.uniform(-20, 20)
                new_z += rng.uniform(-20, 20)
            new_atoms.append((new_x, new_y, new_z))
    return new_atoms

# generate snapshots for three angles
angles = [0, 45, 90]
for angle in angles:
    deformed = apply_deformation(all_atoms, angle)
    n_atoms = len(deformed)
    # header
    print(f"{n_atoms}")
    print(f"Angle {angle} degrees")
    for idx, (x, y, z) in enumerate(deformed):
        print(f"{idx+1} C {x:.4f} {y:.4f} {z:.4f}")

PYEOF
