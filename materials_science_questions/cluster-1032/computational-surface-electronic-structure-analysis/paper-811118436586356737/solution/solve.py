import sys, json, math, numpy as np

def make_bulk_band():
    # high-symmetry path: Gamma (0,0,0) -> Z (0,0,0.5) -> T (0.5,0.5,0.5)
    N = 60
    k_gamma_z = np.linspace(0, 0.5, N, endpoint=False).reshape(-1, 1)
    k_gamma_z = np.hstack([np.zeros((N,2)), k_gamma_z])
    k_z_t = np.linspace(0, 0.5, N).reshape(-1, 1)
    k_z_t = np.hstack([k_z_t, k_z_t, 0.5*np.ones((N,1))])
    all_k = np.vstack([k_gamma_z, k_z_t[1:]])
    def bands(k):
        kz = k[2]
        # synthetic 4-band spectrum with band inversion near kz ~ 0.25
        e1 = -1.2 - 0.3*np.cos(2*np.pi*kz)
        e2 = 0.2*np.cos(2*np.pi*kz) - 0.1
        e3 = -0.05*np.cos(2*np.pi*kz) + 0.05
        e4 = 1.3 + 0.2*np.cos(2*np.pi*kz)
        return np.sort([e1, e2, e3, e4])
    evals = np.array([bands(k) for k in all_k])
    # node line: closed loop in plane kx=ky, centered at Z(0,0,0.5)
    rad = 0.18
    Nnl = 80
    theta = np.linspace(0, 2*np.pi, Nnl, endpoint=False)
    u = rad*np.cos(theta)
    v = 0.5 + rad*np.sin(theta)
    nl = np.column_stack([u, u, v])
    kpath_objs = []
    labels = ['Γ']*N + ['Z'] + ['T']*(N-1)
    for i, lab in enumerate(labels):
        kpath_objs.append({'label': lab, 'k': all_k[i].tolist()})
    return {
        'kpath': kpath_objs,
        'eigenvalues': evals.tolist(),
        'node_line_points': nl.tolist()
    }

def make_berry():
    # generate a grid of (k2,k3) covering the projected node ring
    N = 30
    ks = np.linspace(-0.5, 0.5, N)
    berry = []
    k_parallel = []
    center = np.array([0.0, 0.5])
    radius = 0.20
    for ky in ks:
        for kz in ks:
            pt = np.array([ky, kz])
            inside = np.linalg.norm(pt - center) < radius
            b = 0.0 if inside else 1.0
            k_parallel.append([ky, kz])
            berry.append(b)
    return {'k_parallel': k_parallel, 'berry_phase': berry}

def make_surface():
    # surface BZ path along k2 at k3=0.5 (crosses node ring)
    Np = 80
    k2_vals = np.linspace(-0.5, 0.5, Np)
    k3_fixed = 0.5
    k_path = [[k2, k3_fixed] for k2 in k2_vals]
    center = np.array([0.0, 0.5])
    radius = 0.20
    n_slab_bands = 20
    eig_list = []
    for k2 in k2_vals:
        pt = np.array([k2, k3_fixed])
        inside = np.linalg.norm(pt - center) < radius
        # background bands: a series of parabolas, plus a flat drumhead band at 0.0 if inside
        base_eigs = np.linspace(-1.5, 1.5, n_slab_bands).tolist()
        if inside:
            base_eigs.insert(n_slab_bands//2, 0.0)  # flat band
        else:
            base_eigs.insert(n_slab_bands//2, -0.8 if k2<0 else 0.8)  # dispersive band outside
        eig_list.append(base_eigs[:n_slab_bands+1])
    return {'k_path': k_path, 'eigenvalues': eig_list}

def main():
    target = sys.argv[1]
    if target == 'bulk_band_structure.json':
        data = make_bulk_band()
    elif target == 'berry_phase_zigzag.json':
        data = make_berry()
    elif target == 'surface_band_beard.json':
        data = make_surface()
    else:
        raise ValueError('unknown output')
    with open(target, 'w') as f:
        json.dump(data, f, indent=2)

if __name__ == '__main__':
    main()
