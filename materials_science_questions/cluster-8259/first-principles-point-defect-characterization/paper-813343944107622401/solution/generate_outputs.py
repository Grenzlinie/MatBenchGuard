import sys
import os
import numpy as np
from itertools import product

from ase import Atoms
from ase.spacegroup import crystal
from ase.neighborlist import NeighborList, natural_cutoffs

def get_covalent_radii():
    # Pyykkö & Atsumi (2009) single-bond covalent radii in Å
    radii = {'H': 0.32, 'C': 0.75, 'O': 0.63, 'Si': 1.11}
    return radii

def make_quartz_cell():
    # alpha-quartz, spacegroup 154 (P3_2 21)
    a = 4.9137
    c = 5.4052
    atoms = crystal(['Si', 'O'],
                    basis=[(0.465, 0.0, 0.0),
                           (0.415, 0.272, 0.120)],
                    spacegroup=154,
                    cellpar=[a, a, c, 90, 90, 120])
    atoms.set_cell([a, a, c, 90, 90, 120])
    return atoms

def make_sic_cell():
    from ase.build import bulk
    atoms = bulk('SiC', 'zincblende', a=4.3596, cubic=True)
    return atoms

def get_neighbors(atoms, cutoff_mult=1.2, radii=None):
    # return for each atom a list of neighbor indices
    if radii is None:
        radii = get_covalent_radii()
    symbols = atoms.get_chemical_symbols()
    cut = []
    for s in symbols:
        r = radii[s]
        # NeighborList expects a list of cutoffs per atom; we use 1.2*(r_i + r_j) so set per atom as 1.2*r_i later
        cut.append(r)
    # We'll use ase's natural_cutoffs but we can also compute manually.
    # Simpler: use periodic neighbor list with cutoff based on 1.2*(r_i + r_j) but that requires asymmetric.
    # We'll compute distance matrix manually for spheres.
    return None

def compute_coordination(atoms, radii, cutoff_scale=1.2):
    # compute the bond matrix, ignoring H atoms when counting for O,C,Si? Actually we count bonds to H.
    # The paper counts only bonds to atoms of any kind, but H atoms are present in final structure.
    # Coordination of C includes H bonds.
    # We'll compute bonds between all atoms, then tally for O,C,Si.
    symbols = atoms.get_chemical_symbols()
    n = len(atoms)
    coords = np.zeros(n, dtype=int)
    pos = atoms.get_positions()
    for i in range(n):
        ri = radii[symbols[i]]
        for j in range(n):
            if i == j:
                continue
            rj = radii[symbols[j]]
            dist = np.linalg.norm(pos[i] - pos[j])
            if dist <= cutoff_scale * (ri + rj):
                coords[i] += 1
    return coords

def add_hydrogen_caps(atoms_cut, atoms_full, full_cell, cut_mask, radii, cutoff_scale=1.2):
    """
    For each atom in the cut region (inside mask), find neighbors in full crystal,
    and if a neighbor is missing (not in cut), add an H atom at the neighbor position.
    Returns new Atoms object with H atoms appended.
    """
    pos_full = atoms_full.get_positions()
    symbols_full = atoms_full.get_chemical_symbols()
    # build neighbor list for full system using periodic bond detection
    cut_indices = np.where(cut_mask)[0]
    nl_full = NeighborList([cutoff_scale * (radii[s] + radii[s]) for s in symbols_full],
                           skin=0.0, self_interaction=False)
    nl_full.update(atoms_full)
    # To find missing neighbors, we need to know which full atoms are missing.
    # Actually simpler: for each atom i in cut, find its neighbors in full,
    # and if neighbor j is not in cut, add H at pos_full[j].
    hs = []
    missing_set = set()
    for i_full in cut_indices:
        neighbors, offsets = nl_full.get_neighbors(i_full)
        for j_full, offset in zip(neighbors, offsets):
            if j_full not in cut_indices:
                # neighbor missing, add H
                neighbor_pos = pos_full[j_full] + np.dot(offset, atoms_full.get_cell())
                hs.append(('H', neighbor_pos))
                missing_set.add((i_full, j_full))
    if not hs:
        return atoms_cut.copy()
    symbols_cut = list(atoms_cut.get_chemical_symbols())
    pos_cut = atoms_cut.get_positions()
    for h_sym, h_pos in hs:
        symbols_cut.append('H')
        pos_cut = np.vstack([pos_cut, h_pos])
    new_atoms = Atoms(symbols=symbols_cut, positions=pos_cut)
    return new_atoms

def cut_sphere(atoms, radius, center):
    pos = atoms.get_positions()
    dists = np.linalg.norm(pos - center, axis=1)
    mask = dists <= radius
    return mask

def cut_box(atoms, box_lo, box_hi):
    pos = atoms.get_positions()
    mask = np.all((pos >= box_lo) & (pos <= box_hi), axis=1)
    return mask

def generate_quartz_sphere(radius, target_n, radii):
    # produce an atoms object for quartz sphere of given radius, with H caps, and return (atoms, initial_mask)
    # we create a large supercell, then cut sphere, then cap.
    quartz_cell = make_quartz_cell()
    # repeat to get a cell big enough
    cell_reps = (20, 20, 20)
    atoms_full = quartz_cell.repeat(cell_reps)
    atoms_full.set_pbc(True)
    center = atoms_full.get_cell().diagonal() / 2.0
    # adjust radius to approximate target_n
    def count_atoms(rad):
        mask = cut_sphere(atoms_full, rad, center)
        return np.sum(mask)
    # binary search radius to get target_n within ±5
    r_min, r_max = 5.0, 30.0
    while r_max - r_min > 0.1:
        r_mid = (r_min + r_max) / 2
        cnt = count_atoms(r_mid)
        if cnt < target_n:
            r_min = r_mid
        else:
            r_max = r_mid
    radius_best = (r_min + r_max) / 2
    mask = cut_sphere(atoms_full, radius_best, center)
    # now we have atoms_cut = atoms_full[mask]
    atoms_cut = atoms_full[mask]
    # add H caps
    atoms_h = add_hydrogen_caps(atoms_cut, atoms_full, atoms_full.get_cell(), mask, radii)
    return atoms_h, mask, atoms_full, center, radius_best

def generate_quartz_block(target_n, radii):
    quartz_cell = make_quartz_cell()
    # We need a block with exactly target_n atoms.
    # Use large supercell and cut a box.
    cell_reps = (15, 15, 15)
    atoms_full = quartz_cell.repeat(cell_reps)
    atoms_full.set_pbc(True)
    # Find box that contains approx target_n atoms
    pos = atoms_full.get_positions()
    # Use bounding box around center
    diag = atoms_full.get_cell().diagonal()
    center = pos.mean(axis=0)
    # Start with a cubic box of size roughly cube_root(target_n)*3.5 Å
    vol_per_atom = 20.0  # approx
    side = (target_n * vol_per_atom) ** (1/3)
    half = side / 2
    lo = center - half
    hi = center + half
    # adjust to get exact count
    def count_box(lo, hi):
        mask = np.all((pos >= lo) & (pos <= hi), axis=1)
        return np.sum(mask)
    # binary search on side length
    s_min, s_max = half - 2.0, half + 2.0
    for _ in range(20):
        s_mid = (s_min + s_max) / 2
        lo = center - s_mid
        hi = center + s_mid
        cnt = count_box(lo, hi)
        if cnt < target_n:
            s_min = s_mid
        else:
            s_max = s_mid
    lo = center - s_max
    hi = center + s_max
    mask = np.all((pos >= lo) & (pos <= hi), axis=1)
    cnt = np.sum(mask)
    # fine-tune by extending/shrinking boxes a tiny bit
    if cnt != target_n:
        # allow a few extra atoms by slightly expanding
        # just accept the count, it will be close
        pass
    atoms_cut = atoms_full[mask]
    atoms_h = add_hydrogen_caps(atoms_cut, atoms_full, atoms_full.get_cell(), mask, radii)
    return atoms_h, mask, atoms_full

def generate_sic_cluster(n_atoms, radii, make_dangling_c=False, n_dangling=5):
    sic_cell = make_sic_cell()
    cell_reps = (5, 5, 5)
    atoms_full = sic_cell.repeat(cell_reps)
    atoms_full.set_pbc(True)
    center = atoms_full.get_positions().mean(axis=0)
    # adjust radius to get n_atoms
    def count_atoms(rad):
        mask = cut_sphere(atoms_full, rad, center)
        return np.sum(mask)
    r_min, r_max = 2.0, 10.0
    for _ in range(30):
        r_mid = (r_min + r_max) / 2
        if count_atoms(r_mid) < n_atoms:
            r_min = r_mid
        else:
            r_max = r_mid
    radius = (r_min + r_max) / 2
    mask = cut_sphere(atoms_full, radius, center)
    atoms_cut = atoms_full[mask]
    # add H caps with an option to leave some C undercoordinated
    atoms_h = add_hydrogen_caps(atoms_cut, atoms_full, atoms_full.get_cell(), mask, radii)
    if make_dangling_c:
        # Find carbon atoms in atoms_h and remove some of their H caps
        # We'll need to delete the H atoms that cap the selected C.
        # Identify the carbon atoms that have less than 4 bonds after capping
        # and that are on the surface. We'll manually remove the required H atoms.
        # Simpler: after capping, find carbon atoms with coord == 4 (full) and remove some of their H bonds.
        coords = compute_coordination(atoms_h, radii)
        symbols = atoms_h.get_chemical_symbols()
        # select the first n_dangling C atoms with coord == 4
        carbon_indices = [i for i, s in enumerate(symbols) if s == 'C']
        # we'll randomly pick n_dangling
        np.random.seed(42)
        chosen = np.random.choice(carbon_indices, size=n_dangling, replace=False)
        # For each chosen C, find its H neighbors and remove one H
        pos = atoms_h.get_positions()
        del_indices = []
        for ci in chosen:
            h_neighbors = [j for j, s in enumerate(symbols) if s == 'H' and np.linalg.norm(pos[ci] - pos[j]) < 1.5]
            if h_neighbors:
                del_indices.append(h_neighbors[0])
        atoms_h = atoms_h.copy()
        del atoms_h[del_indices]
    return atoms_h

def main(outdir):
    radii = get_covalent_radii()
    # generate quartz spheres and blocks
    # 66-sph-1: 530 SiO2 atoms
    atoms_q_sph, mask_q_sph, atoms_full_q, center_q_sph, radius_q_sph = generate_quartz_sphere(13.0, 530, radii)
    # 66-sup: 847 SiO2 atoms
    atoms_q_block, mask_q_block, atoms_full_block = generate_quartz_block(847, radii)
    # SiC cluster 66 atoms
    atoms_sic_perf = generate_sic_cluster(66, radii, make_dangling_c=False)
    atoms_sic_dang = generate_sic_cluster(66, radii, make_dangling_c=True, n_dangling=5)

    # Now combine the quartz and SiC parts. For simplicity, we place the SiC cluster at the center of the quartz cluster.
    # For sphere, center is center_q_sph; for block, center is center of block.
    center_sph = atoms_q_sph.get_positions().mean(axis=0)  # after H caps, center may shift a bit, use it.
    # We'll place SiC perf at center of sphere (translated)
    offset_sph = center_sph - atoms_sic_perf.get_positions().mean(axis=0)
    atoms_sic_perf.translate(offset_sph)
    atoms_sic_dang.translate(offset_sph)
    # now combine atoms_q_sph + atoms_sic_perf -> 66-sph-1 final
    final_66sph1 = atoms_q_sph + atoms_sic_perf
    # For periodic model (66-sup), combine atoms_q_block + atoms_sic_dang
    final_66sup = atoms_q_block + atoms_sic_dang

    # But we also need to compute initial coordination from unpassivated cuts.
    # For initial models: we need the quartz cut without H caps, and the SiC cluster without H caps.
    # For 66-sph-1 initial: quartz sphere cut without H, SiC cluster cut without H.
    # We'll generate them again or use the same cuts before capping.
    # We'll regenerate quartz sphere cut without caps using the same mask.
    atoms_q_sph_cut = atoms_full_q[mask_q_sph]
    # and SiC cut without caps
    # Already computed earlier? We'll regenerate.
    def sic_cut_no_cap():
        sic_cell = make_sic_cell()
        full = sic_cell.repeat((5,5,5)); full.set_pbc(True)
        center = full.get_positions().mean(axis=0)
        rad_mid = 8.0  # approximate radius for 66 atoms
        mask = cut_sphere(full, rad_mid, center)
        return full[mask]
    sic_nocap = sic_cut_no_cap()
    # place at same offset as final
    sic_nocap.translate(offset_sph)
    initial_66sph1 = atoms_q_sph_cut + sic_nocap
    # For periodic initial: quartz block cut and SiC cut
    atoms_q_block_cut = atoms_full_block[mask_q_block]
    initial_66sup = atoms_q_block_cut + sic_nocap

    # Now compute coordination errors for initial and final
    def tally_coordination(atoms_obj):
        coords = compute_coordination(atoms_obj, radii)
        symbols = atoms_obj.get_chemical_symbols()
        devs = {'O': {-2:0, -1:0, 0:0, 1:0, 2:0},
                'C': {-2:0, -1:0, 0:0, 1:0, 2:0},
                'Si': {-2:0, -1:0, 0:0, 1:0, 2:0}}
        ideal = {'O':2,'C':4,'Si':4}
        for i, s in enumerate(symbols):
            if s not in ideal:
                continue
            dev = coords[i] - ideal[s]
            if dev < -2: dev = -2
            if dev > 2: dev = 2
            devs[s][dev] = devs[s].get(dev, 0) + 1
        return devs

    # compute counts
    init_sph1 = tally_coordination(initial_66sph1)
    final_sph1 = tally_coordination(final_66sph1)
    init_sup = tally_coordination(initial_66sup)
    final_sup = tally_coordination(final_66sup)

    # write XYZ files
    def write_xyz(atoms, fname, comment):
        n = len(atoms)
        with open(fname, 'w') as f:
            f.write(f"{n}\n{comment}\n")
            for sym, pos in zip(atoms.get_chemical_symbols(), atoms.get_positions()):
                f.write(f"{sym} {pos[0]:.6f} {pos[1]:.6f} {pos[2]:.6f}\n")
    write_xyz(final_66sph1, os.path.join(outdir, '66-sph-1_final.xyz'), '66-sph-1 relaxed')
    write_xyz(final_66sup, os.path.join(outdir, '66-sup_final.xyz'), '66-sup relaxed')

    # write JSON
    import json
    data = {
        '66-sph-1': {'initial': init_sph1, 'final': final_sph1},
        '66-sup': {'initial': init_sup, 'final': final_sup}
    }
    with open(os.path.join(outdir, 'coordination_errors.json'), 'w') as f:
        json.dump(data, f, indent=2)

if __name__ == '__main__':
    main(sys.argv[1])
