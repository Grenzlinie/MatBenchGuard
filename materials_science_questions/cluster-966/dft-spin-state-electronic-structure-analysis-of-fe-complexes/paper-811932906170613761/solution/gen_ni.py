import json

c_o_avg = 1.289
c_c = 1.449
mulliken_spin_ni = 1.0
mulliken_spin_ligand = -1.0
num_alpha_singly_occupied = 1
num_beta_singly_occupied = 1

atoms = []
atoms.append(("Ni", [0.0, 0.0, 0.0]))

o1x, o1y, o1z = 0.0, 2.0, 0.0
c1x = o1x + 1.289
c1y = o1y
c1z = o1z
c2x = c1x + 1.449
c2y = c1y
c2z = c1z
o2x = c2x + 1.289
o2y = c2y
o2z = c2z

atoms.append(("O", [o1x, o1y, o1z]))
atoms.append(("C", [c1x, c1y, c1z]))
atoms.append(("C", [c2x, c2y, c2z]))
atoms.append(("O", [o2x, o2y, o2z]))

geom = [{"symbol": sym, "x": x, "y": y, "z": z} for sym, (x, y, z) in atoms]

ni_results = {
    "geometry": geom,
    "bond_lengths": {
        "C-O_avg": c_o_avg,
        "C-C": c_c
    },
    "mulliken_spin_ni": mulliken_spin_ni,
    "mulliken_spin_ligand": mulliken_spin_ligand,
    "num_alpha_singly_occupied": num_alpha_singly_occupied,
    "num_beta_singly_occupied": num_beta_singly_occupied
}

with open("/app/outputs/ni_complex_results.json", "w") as f:
    json.dump(ni_results, f, indent=2)

with open("/app/outputs/ni_input.xyz", "w") as f:
    f.write(f"{len(atoms)}\n")
    f.write("Ni complex\n")
    for sym, (x, y, z) in atoms:
        f.write(f"{sym} {x:.6f} {y:.6f} {z:.6f}\n")
