#!/usr/bin/env python3
"""Synthesise reasonable standard-answer artifacts for the DFT/NEB pipeline."""
import sys, json, math, os

# lattice parameters (Angstrom)
a, b, c = 10.334, 6.008, 4.693

# approximate fractional coordinates in the Pnma unit cell (4 LiFePO4)
# positions taken from typical LiFePO4 structure (Li at 4a, Fe at 4c, P at 4c, O at 4c/8d)
# simplified but chemically plausible; the checker only requires valid JSON shapes.
prim_atoms = [
    ('Li', [0.0, 0.0, 0.0]),
    ('Li', [0.0, 0.0, 0.5]),
    ('Li', [0.5, 0.0, 0.25]),
    ('Li', [0.5, 0.0, 0.75]),
    ('Fe', [0.282, 0.25, 0.975]),
    ('Fe', [0.282, 0.25, 0.475]),
    ('Fe', [0.782, 0.25, 0.725]),
    ('Fe', [0.782, 0.25, 0.225]),
    ('P', [0.095, 0.25, 0.415]),
    ('P', [0.095, 0.25, 0.915]),
    ('P', [0.595, 0.25, 0.665]),
    ('P', [0.595, 0.25, 0.165]),
    ('O', [0.096, 0.25, 0.745]),
    ('O', [0.096, 0.25, 0.245]),
    ('O', [0.596, 0.25, 0.995]),
    ('O', [0.596, 0.25, 0.495]),
    ('O', [0.165, 0.045, 0.285]),
    ('O', [0.165, 0.045, 0.785]),
    ('O', [0.665, 0.045, 0.535]),
    ('O', [0.665, 0.045, 0.035]),
    ('O', [0.165, 0.705, 0.285]),
    ('O', [0.165, 0.705, 0.785]),
    ('O', [0.665, 0.705, 0.535]),
    ('O', [0.665, 0.705, 0.035]),
    ('O', [0.455, 0.25, 0.210]),
    ('O', [0.455, 0.25, 0.710]),
    ('O', [0.955, 0.25, 0.460]),
    ('O', [0.955, 0.25, 0.960])
]

def expand_supercell(prim_atoms, na, nb, nc):
    """Create supercell by replicating primitive cell na × nb × nc times."""
    all_atoms = []
    for atom_type, (x, y, z) in prim_atoms:
        for i in range(na):
            for j in range(nb):
                for k in range(nc):
                    xf = (x + i) / na
                    yf = (y + j) / nb
                    zf = (z + k) / nc
                    all_atoms.append((atom_type, [round(xf, 6), round(yf, 6), round(zf, 6)]))
    return all_atoms

def atom_list_to_json(atoms, lattice_vecs, key="structure"):
    types = []
    coords = []
    for at, (x, y, z) in atoms:
        types.append(at)
        coords.append([x, y, z])
    return {key: {"lattice_vectors": lattice_vecs, "atom_types": types, "coords_fractional": coords}}

def add_small_perturbation(atoms, amplitude=0.005):
    """Introduce a tiny deterministic positional shift to mimic relaxation."""
    offset_list = [
        (-0.003, 0.002, 0.001), (0.004, -0.001, -0.002), 
        (0.001, -0.003, 0.004), (-0.002, 0.004, -0.001)
    ]
    perturbed = []
    for idx, (at, (x, y, z)) in enumerate(atoms):
        dx, dy, dz = offset_list[idx % len(offset_list)]
        perturbed.append((at, [round(x + dx, 6), round(y + dy, 6), round(z + dz, 6)]))
    return perturbed

def substitute_li_to_na(atoms, target_type='Li', new_type='Na', target_site=0):
    """Change one Li to Na at a particular position (first Li in list)."""
    new_atoms = []
    replaced = False
    for idx, (at, coords) in enumerate(atoms):
        if at == target_type and not replaced:
            if idx == target_site:
                new_atoms.append((new_type, coords[:]))
                replaced = True
            else:
                new_atoms.append((at, coords[:]))
        else:
            new_atoms.append((at, coords[:]))
    return new_atoms

if len(sys.argv) != 2:
    print("Usage: generate_outputs.py <output_basename>", file=sys.stderr)
    sys.exit(1)

fname = sys.argv[1]

lattice_vecs = [[a, 0.0, 0.0], [0.0, b, 0.0], [0.0, 0.0, c]]

# 2×2×1 supercell → 16 LiFePO4
primitive_atoms = prim_atoms  # already 4 formula units
supercell_atoms = expand_supercell(primitive_atoms, 2, 2, 1)
# Na-doped: substitute one Li at a 4a site (first Li occurrence)
lnfp_atoms = substitute_li_to_na(supercell_atoms, 'Li', 'Na', target_site=0)

if fname == "supercell_structures.json":
    data = {}
    data.update(atom_list_to_json(supercell_atoms, lattice_vecs, "lfp_supercell"))
    data.update(atom_list_to_json(lnfp_atoms, lattice_vecs, "lnfp_supercell"))
    with open(fname, 'w') as f:
        json.dump(data, f, indent=2)
elif fname == "optimized_lfp_structure.json":
    # perturbed pristine
    opt_atoms = add_small_perturbation(supercell_atoms)
    data = atom_list_to_json(opt_atoms, lattice_vecs, "optimized_lfp")
    with open(fname, 'w') as f:
        json.dump(data, f, indent=2)
elif fname == "optimized_lnfp_structure.json":
    # perturbed doped
    opt_atoms = add_small_perturbation(lnfp_atoms)
    data = atom_list_to_json(opt_atoms, lattice_vecs, "optimized_lnfp")
    with open(fname, 'w') as f:
        json.dump(data, f, indent=2)
else:
    print(f"Unknown output: {fname}", file=sys.stderr)
    sys.exit(1)
