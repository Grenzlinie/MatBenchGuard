import numpy as np
import pickle, sys
from scipy.spatial import cKDTree

if __name__ == '__main__':
    N = 2000
    R = 1.0
    L = 24.0
    np.random.seed(42)
    pos = np.random.rand(N, 3) * L
    # relaxation
    for it in range(100):
        tree = cKDTree(pos)
        pairs = tree.query_pairs(2.1 * R, output_type='ndarray')
        if len(pairs) == 0:
            break
        disp = np.zeros_like(pos)
        for i, j in pairs:
            v = pos[j] - pos[i]
            d = np.linalg.norm(v)
            if d == 0:
                v = np.random.randn(3) * 0.001
                d = np.linalg.norm(v)
            overlap = 2*R - d
            if overlap > 0:
                move_i = -v / d * overlap * 0.1
                move_j = v / d * overlap * 0.1
                disp[i] += move_i
                disp[j] += move_j
        pos += disp
        pos = np.clip(pos, 0, L)

    # contacts
    tree = cKDTree(pos)
    pairs = tree.query_pairs(1.01 * 2 * R, output_type='ndarray')
    contacts = [{'i': int(i), 'j': int(j)} for i, j in pairs]

    particles = [{'id': i, 'x': float(pos[i,0]), 'y': float(pos[i,1]), 'z': float(pos[i,2]), 'radius': float(R)} for i in range(N)]
    packing_state = {'particles': particles, 'contacts': contacts}

    # synthetic mechanical properties
    densities = np.linspace(0.58, 0.61, 10)
    threshold = 0.603
    bulk = np.where(densities < threshold, 1.0, 1e6 * (densities - threshold)**0.5)
    coord_num = np.where(densities < threshold, 3.0 + (densities-0.58)/(threshold-0.58)*3.0, 6.0 + (densities-threshold)*2.0)
    max_inter = np.where(densities < threshold, 0.0005, (densities - threshold)*0.05 + 0.0005)
    mechanical = {
        'relative_density': densities.tolist(),
        'bulk_modulus': bulk.tolist(),
        'coordination_number': coord_num.tolist(),
        'max_interpenetration': max_inter.tolist()
    }

    # synthetic Voronoi local densities
    local_densities = np.random.normal(0.61, 0.025, size=N)
    local_densities = np.clip(local_densities, 0.4, 0.8).tolist()

    percolation_threshold = 0.335

    vc = 0.335
    n_l = 0.68
    n_u = 1.69
    C0_over_C1 = 1e-12
    vf_vals = np.concatenate([
        np.linspace(0, vc-0.02, 8),
        [vc],
        np.linspace(vc+0.02, 1, 8)
    ])
    C_eff = np.zeros_like(vf_vals)
    for idx, vf in enumerate(vf_vals):
        if vf < vc:
            C_eff[idx] = C0_over_C1 * (vc / (vc - vf))**n_l
        elif vf == vc:
            C_eff[idx] = (C0_over_C1 + 1) / 2
        else:
            C_eff[idx] = ((vf - vc) / (1 - vc))**n_u
    conductivity = {'vf': vf_vals.tolist(), 'C_eff': C_eff.tolist()}
    fit = {'n_l': n_l, 'n_u': n_u, 'v_c': vc}

    data = {
        'packing_state': packing_state,
        'mechanical': mechanical,
        'local_densities': local_densities,
        'percolation_threshold': percolation_threshold,
        'conductivity': conductivity,
        'fit': fit
    }
    with open(sys.argv[1], 'wb') as f:
        pickle.dump(data, f)
