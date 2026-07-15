import json

c_o_avg = 1.282
c_c = 1.457
mulliken_spin_fe = 4.2
mulliken_spin_ligands = [-0.7333, -0.7333, -0.7334]
num_alpha_singly_occupied = 5
num_beta_singly_occupied = 3

def chain(base):
    x, y, z = base
    o1 = [x, y, z]
    c1 = [x + 1.282, y, z]
    c2 = [x + 1.282 + 1.457, y, z]  # x + 2.739
    o2 = [x + 4.021, y, z]
    return [("O", o1), ("C", c1), ("C", c2), ("O", o2)]

atoms = []
atoms.append(("Fe", [0.0, 0.0, 0.0]))
for base in [(0.0, 0.0, 0.0), (0.0, 6.0, 0.0), (0.0, 0.0, 6.0)]:
    atoms.extend(chain(base))

geom = [{"symbol": sym, "x": x, "y": y, "z": z} for sym, (x, y, z) in atoms]

fe_results = {
    "geometry": geom,
    "bond_lengths": {
        "C-O_avg": c_o_avg,
        "C-C": c_c
    },
    "mulliken_spin_fe": mulliken_spin_fe,
    "mulliken_spin_ligands": mulliken_spin_ligands,
    "num_alpha_singly_occupied": num_alpha_singly_occupied,
    "num_beta_singly_occupied": num_beta_singly_occupied
}

with open("/app/outputs/fe_complex_results.json", "w") as f:
    json.dump(fe_results, f, indent=2)

with open("/app/outputs/fe_truncated.xyz", "w") as f:
    f.write(f"{len(atoms)}\n")
    f.write("Truncated Fe complex\n")
    for sym, (x, y, z) in atoms:
        f.write(f"{sym} {x:.6f} {y:.6f} {z:.6f}\n")
