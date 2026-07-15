#!/usr/bin/env python3
import sys, random

def main():
    alumina_type = sys.argv[1]   # 'gamma' or 'eta'
    outfile = sys.argv[2]

    if alumina_type == 'gamma':
        n_slab = 70
    else:
        n_slab = 72

    # approximate Al2O3 stoichiometry for the slab
    n_Al = int(round(n_slab * 0.4))
    n_O = n_slab - n_Al

    random.seed(42)

    # generate slab coordinates in a layered slab region (z=10-20 Å)
    slab_atoms = []
    n_layers = 5
    z_min, z_max = 10.0, 20.0
    dz = (z_max - z_min) / (n_layers - 1)
    for ilayer in range(n_layers):
        z = z_min + ilayer * dz
        n_al_layer = n_Al // n_layers
        n_o_layer = n_O // n_layers
        for _ in range(n_al_layer):
            x = random.uniform(2.0, 10.0)
            y = random.uniform(2.0, 10.0)
            slab_atoms.append(('Al', x, y, z))
        for _ in range(n_o_layer):
            x = random.uniform(2.0, 10.0)
            y = random.uniform(2.0, 10.0)
            slab_atoms.append(('O', x, y, z))

    # remaining atoms (from division rounding) placed randomly
    n_placed = n_Al + n_O
    while len(slab_atoms) < n_slab:
        elem = 'Al' if random.random() < 0.4 else 'O'
        x = random.uniform(2.0, 10.0)
        y = random.uniform(2.0, 10.0)
        z = random.uniform(z_min, z_max)
        slab_atoms.append((elem, x, y, z))

    # five NEB images, Cr moves from surface (z=22) to subsurface (z=18)
    n_images = 5
    z_surface = z_max + 2.0
    z_sub = z_max - 2.0
    cr_x, cr_y = 6.0, 6.0

    lines = []
    for i in range(n_images):
        frac = i / (n_images - 1)
        cr_z = z_surface + frac * (z_sub - z_surface)
        atom_list = slab_atoms[:]
        atom_list.append(('Cr', cr_x, cr_y, cr_z))
        random.shuffle(atom_list)
        lines.append(f"{len(atom_list)}")
        lines.append(f"image {i}")
        for elem, x, y, z in atom_list:
            lines.append(f"{elem} {x:.6f} {y:.6f} {z:.6f}")

    with open(outfile, 'w') as f:
        f.write('\n'.join(lines))

if __name__ == '__main__':
    main()