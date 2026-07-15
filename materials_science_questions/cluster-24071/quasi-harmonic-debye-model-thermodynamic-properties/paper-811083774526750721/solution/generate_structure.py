import numpy as np
import sys
import random

def main(outfile):
    # number of atoms
    N = 120
    # target degree sequence exactly matching Table 1 hybridizations (coordination = sp% assignment)
    # 5 atoms with degree 4 (sp3), 98 with degree 3 (sp2), 17 with degree 2 (sp)
    degrees = [4]*5 + [3]*98 + [2]*17
    if len(degrees) != N:
        raise ValueError
    random.shuffle(degrees)
    # create stubs
    stubs = []
    for i, d in enumerate(degrees):
        stubs.extend([i]*d)
    random.shuffle(stubs)
    adj = np.zeros((N, N), dtype=bool)
    # pair stubs avoiding self-loops and multiple edges, with fallback reshuffle
    for attempt in range(200):
        if len(stubs) % 2 != 0:
            stubs.append(random.randrange(N))
        np.random.shuffle(stubs)
        used = set()
        pairs = []
        ok = True
        for k in range(0, len(stubs), 2):
            i, j = stubs[k], stubs[k+1]
            if i == j or (i,j) in used or (j,i) in used or adj[i,j]:
                ok = False
                break
            used.add((i,j))
            pairs.append((i,j))
        if ok:
            for i,j in pairs:
                adj[i,j] = True
                adj[j,i] = True
            break
        else:
            # reshuffle stubs
            stubs = []
            for i, d in enumerate(degrees):
                stubs.extend([i]*d)
    else:
        raise RuntimeError("Could not create simple graph")
    # box size for density 1.50 g/cm³
    L = 11.67  # Angstrom
    # initialize coordinates randomly
    coords = np.random.rand(N, 3) * L
    # force-directed relaxation
    r0_bond = 1.45
    k_bond = 2.0
    # repulsive cutoff for all pairs
    r_cut = 2.5
    k_rep = 0.5
    # damping factor
    damp = 0.1
    n_steps = 5000
    for step in range(n_steps):
        forces = np.zeros_like(coords)
        # compute pairwise forces
        for i in range(N):
            for j in range(i+1, N):
                r = coords[j] - coords[i]
                dist = np.linalg.norm(r)
                if dist < 1e-6:
                    dist = 1e-6
                f = np.zeros(3)
                if adj[i,j]:
                    # bond force: harmonic
                    f_dir = r / dist
                    f_mag = -k_bond * (dist - r0_bond)
                    f = f_dir * f_mag
                elif dist < r_cut:
                    # repulsive
                    f_dir = r / dist
                    f_mag = k_rep / (dist*dist)
                    f = -f_dir * f_mag
                forces[i] += f
                forces[j] -= f
        coords += forces * damp
        coords %= L  # periodic boundary
    # write XYZ
    with open(outfile, 'w') as f:
        f.write(f"{N}\n")
        f.write(f"Lattice=\"11.67 0.0 0.0 0.0 11.67 0.0 0.0 0.0 11.67\"\n")
        for i in range(N):
            x, y, z = coords[i]
            f.write(f"C {x:.6f} {y:.6f} {z:.6f}\n")

if __name__ == '__main__':
    main(sys.argv[1])
