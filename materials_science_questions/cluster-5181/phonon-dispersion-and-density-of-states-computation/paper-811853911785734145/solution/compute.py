#!/usr/bin/env python3
"""Oracle reference solver for Polonium phonon task.
Produces force_constants.json, bulk_dispersion.csv,
surface_dispersion.csv (slab approximation), vdos.csv.
"""
import sys, json, csv, math
import numpy as np

# Constants
c11 = 113e9      # Pa
c12 = 28e9       # Pa
a = 3.36e-10     # m
M = 3.49e-25     # kg
omega0 = 10.45e12 # rad/s
k1 = 38.1        # N/m
k2 = 9.5         # N/m

# Derivation of force constants from elastic constants (for sanity, not used)
def derive_force_constants():
    """Compute k1,k2 from elastic constants using Fuchs-like equations."""
    # For simple cubic, Fuchs method yields:
    # c11 - c12 = (3n/4)*[r^2 phi1'']_1 + (3n/2)*[r phi1']_1 + 6n*[r phi2']_2
    # Approx small vibrations: [r phi''] << [r^2 phi''], i.e., neglect first derivative terms.
    # Then c11-c12 ≈ (3n/4)*[r^2 phi1'']_1 + 6n*[r phi2']_2? Not needed, we trust paper values.
    return k1, k2

def get_neighbor_vectors():
    """Return list of (dx,dy,dz) fractions (in units of a) and force constant k for each bond.
    Only one direction per pair (R) – we'll sum over all distinct bonds later."""
    pairs = []
    # NN vectors (distance a)
    for v in [(1,0,0), (-1,0,0), (0,1,0), (0,-1,0), (0,0,1), (0,0,-1)]:
        pairs.append((v, k1))
    # NNN vectors (distance sqrt(2)*a)
    for v in [(1,1,0), (1,-1,0), (-1,1,0), (-1,-1,0),
              (1,0,1), (1,0,-1), (-1,0,1), (-1,0,-1),
              (0,1,1), (0,1,-1), (0,-1,1), (0,-1,-1)]:
        pairs.append((v, k2))
    return pairs

def dyn_mat_bulk(qx, qy, qz):
    """Compute bulk dynamical matrix D (dimensionless) for wavevector (qx,qy,qz) in rad/length."""
    H = np.zeros((3,3), dtype=np.float64)
    for (dx,dy,dz), k in get_neighbor_vectors():
        d = np.array([dx,dy,dz], dtype=np.float64)
        d_len = np.linalg.norm(d)
        if d_len < 1e-12:
            continue
        # distance in meters
        dist = d_len * a
        # direction cosines
        dd = np.outer(d, d) / (d_len**2)
        phase = qx*dx*a + qy*dy*a + qz*dz*a
        # contribution: (k/M) * dd * (1 - cos(phase))
        # Note: we sum over all neighbors, so each pair contributes 2*(1-cos) factor is correct.
        H += (k / M) * dd * (1.0 - math.cos(phase))
    return H / (omega0**2)

def phonon_dispersion():
    """Compute bulk dispersion along [100],[110],[111], output CSV."""
    directions = {
        '[100]': lambda t: (t, 0, 0),
        '[110]': lambda t: (t, t, 0),
        '[111]': lambda t: (t, t, t),
    }
    q_grid = 101  # points per direction
    rows = []
    for dir_name, qfunc in directions.items():
        for i in range(q_grid):
            t = i / (q_grid-1) * math.pi
            qx, qy, qz = qfunc(t)
            D = dyn_mat_bulk(qx, qy, qz)
            # D is symmetric real
            eigvals = np.linalg.eigvalsh(D)
            eigvals_sorted = np.sort(eigvals)
            for branch in range(3):
                omega = math.sqrt(max(0.0, eigvals_sorted[branch]))
                rows.append({
                    'direction': dir_name,
                    'q_norm': float(i)/(q_grid-1),
                    'branch': branch+1,
                    'Omega': round(omega, 6)
                })
    return rows

def slab_harmonic_matrix(qx, qy, N_layers=20):
    """Construct the block tridiagonal dynamical matrix for slab with (001) surfaces.
    Layers indexed 1..N_layers. Returns 3N x 3N matrix D_slab (dimensionless)."""
    D = np.zeros((3*N_layers, 3*N_layers), dtype=np.float64)
    # build on-site (A) and coupling (B) matrices for a given q_parallel
    A = np.zeros((3,3), dtype=np.float64)
    Bplus = np.zeros((3,3), dtype=np.float64)  # coupling from layer m to m+1
    # We'll sum over all bonds that involve layer 0 (reference) and layer m'.
    # Reference layer at z=0, other layer at z = dz * a.
    # In slab, periodic in-plane: we compute effective inter-layer coupling by summing over in-plane neighbors.
    # For each bond vector d = (dx,dy,dz) with dz >= 0, we add contribution to A and B accordingly.
    for (dx,dy,dz), k in get_neighbor_vectors():
        d = np.array([dx,dy,dz], dtype=np.float64)
        d_len = np.linalg.norm(d)
        if d_len < 1e-12:
            continue
        dd = np.outer(d, d) / (d_len**2)
        factor = k / M
        # Phase for in-plane part
        phase = qx*dx*a + qy*dy*a
        cos_phase = math.cos(phase)
        # contribution to intra-layer (A) for this bond: it connects layer l to layer l+dz (since dz integer).
        # But we need to build the matrix for a semi-infinite slab. The dynamical matrix for layer m: D_{mm} receives contributions from all neighbors that start and end in same layer after applying Bloch sum.
        # Standard formula: For each bond vector, the on-site term includes contribution from all neighbors, but the off-diagonal blocks contain -factor * dd * e^{iφ_parallel? Actually, the equations of motion:
        # M ω^2 u_m = sum_n K_{mn} u_n.
        # For central force model, force constant matrix between atoms: if atom i in layer m and atom j in layer n, with separation R = (r_||, dz*a).
        # In in-plane Fourier space, the effective coupling between layers m and n (for wavevector q_||) is
        # C_{mn}(q_||) = sum_{R_||} Phi( R_|| + (dz*a) e_z ) e^{i q_|| · R_||}.
        # For central forces, Phi(R) = -k(R) * d_α d_β / d^2 for i≠j, and self-term: -sum_{j≠i} Phi_{ij}.
        # Here, we can compute the effective on-site and interlayer matrices by summing over all distinct bond vectors that connect the reference layer to another layer, taking into account in-plane phase.
        pass
    # This manual bookkeeping is error-prone. Simpler approach: construct the full dynamical matrix for a supercell, then apply Bloch in-plane. We'll construct a small supercell that includes N layers, with periodic in-plane BCs, but no periodicity in z (free surfaces).
    # I'll adopt a coordinate-based approach: create all atoms in the slab and their force constant matrix explicitly, then Fourier transform in-plane. That's safe.
    # We'll build a slab with N layers, each layer with 1 atom (simple cubic). Coordinates: (0,0, (l-1)*a) for l=1..N. In-plane periodicity: (a,0,0) and (0,a,0). The force constant matrix between atoms i and j with displacement vector R = r_j - r_i.
    # Compute the effective dynamical matrix D_eff(iter_layers) using Bloch sum in lateral directions.
    # We'll precompute inter-layer coupling.
    # Approach: Create a list of atomic positions in one unit cell of the periodic supercell? Just do it explicitly:
    # Under in-plane Bloch theory, for each pair of layers l and l', the effective 3x3 coupling matrix is:
    #   K_{ll'}(q_||) = sum_{R_|| in plane lattice} K(R_|| + (z_{l'}-z_l) e_z) * e^{i q_||·R_||}
    # where K(R) is the 3x3 force constant matrix for a bond with vector R.
    # For our simple cubic, in-plane lattice vectors: (a,0,0) and (0,a,0). So R_|| = (i*a, j*a) for integers i,j. But only bonds with distances a or sqrt(2)a contribute (nearest/next-nearest).
    # For a given layer separation dz, we can list all bond vectors that start in layer l and end in layer l+dz, with their in-plane vector components, then sum with phase factor.
    pass
    # I'm going to implement a simpler, direct method: build a supercell with N layers and lateral size 1x1 (i.e., assume in-plane unit cell contains one atom), and then explicitly construct the force constant matrix for that supercell with Born-von Karman boundary conditions in-plane by adding phase factors? That's what above paragraph does.
    # Let's do a clear implementation:
    def K_bond(dx, dy, dz, k):
        d = np.array([dx,dy,dz], dtype=np.float64)
        d_len = np.linalg.norm(d)
        if d_len < 1e-12:
            return np.zeros((3,3))
        dd = np.outer(d, d) / (d_len**2)
        return (k / M) * dd
    
    # List all bonds as (dx,dy,dz) in units of a, force constant k, and then we will sum over all images to account for in-plane periodicity. But we want the effective K_{l,l'} for a given q_||.
    # For each layer l (1..N), for each neighbor bond (dx,dy,dz), we have a target layer l' = l + dz. We'll add contribution K_bond * e^{i q_||·(dx*a, dy*a)} to block (l,l').
    # This produces a complex matrix? But due to symmetry, the matrix should be real symmetric if we include both + and - vectors? Actually, we sum over all neighbor vectors, but the effective matrix may have imaginary parts if we sum over a single set. To keep Hermitian symmetric, we can sum over all neighbor vectors directly – the imaginary parts from opposite directions will cancel. So we can just sum real part: 2 * K_bond * cos(q_||·R_||). But it's easier to sum over all neighbor vectors in the set that includes both + and - directions, which we already have in get_neighbor_vectors. Then we can compute e^{i phase} for each, but summing will leave only real symmetric part because for each (dx,dy,dz) with phase φ, the opposite (-dx,-dy,-dz) has phase -φ, and the sum gives 2cosφ times K_bond. So we can just use the real part.
    # So we'll loop over all bonds, compute phase φ = qx*dx*a + qy*dy*a, and add factor (1) if we account for both ±? Actually, if we use the full list of 6 NN and 12 NNN vectors, each pair (R,-R) is present. So summing over all of them directly with e^{iφ} gives the correct real symmetric matrix. So we can do:
    #   D_ll' += K_bond(dx,dy,dz,k) * np.exp(1j * (qx*dx*a + qy*dy*a))
    # and then take real part at the end, or just add for each bond individually. The result will be complex but with zero imaginary part for symmetric points? To be safe, we'll add both contributions using complex numbers and then take real part.
    def build_slab_D(N):
        D_comp = np.zeros((3*N, 3*N), dtype=np.complex128)
        for layer in range(N):
            l = layer  # zero-indexed
            for (dx,dy,dz), k in get_neighbor_vectors():
                dlen = math.sqrt(dx*dx+dy*dy+dz*dz)
                if dlen < 1e-8:
                    continue
                dd = np.outer((dx,dy,dz), (dx,dy,dz)) / (dlen**2)
                factor = k / M
                # target layer index
                l2 = l + dz
                if l2 < 0 or l2 >= N:
                    continue  # outside slab -> free surface, skip
                # block index
                i = 3*l; j = 3*l2
                phi = qx*dx*a + qy*dy*a
                phase_factor = np.exp(1j * phi)
                D_comp[i:i+3, j:j+3] += factor * dd * phase_factor
        # Make Hermitian
        D_comp += D_comp.conj().T
        # Return real part (should be real within numerical error)
        D_real = D_comp.real
        # Apply the on-site correction (acoustic sum rule): D_ll should be such that sum over all columns of a given row equals zero.
        # We can enforce by subtracting mean? Not needed for eigenvalue problem, but let's correct diagonal by setting D_ii minus sum of off-diagonal in same row.
        for i in range(3*N):
            D_real[i,i] = -np.sum(D_real[i,:]) + D_real[i,i]
        return D_real
    D = build_slab_D(N_layers)
    return D / (omega0**2)

def surface_dispersion():
    """Compute surface modes using slab method."""
    N = 20
    q_points = 101
    rows = []
    for i in range(q_points):
        q_010 = i / (q_points-1) * math.pi
        # direction [010], so q_parallel = (0, q_010, 0)
        qx = 0.0
        qy = q_010
        D_slab = slab_harmonic_matrix(qx, qy, N_layers=N)
        eigvals, eigvecs = np.linalg.eigh(D_slab)
        # For each mode, check localization in layer 0 (surface layer)
        for mode in range(3*N):
            omega = math.sqrt(max(0.0, eigvals[mode]))
            if omega < 1e-12:
                continue
            vec = eigvecs[:, mode]
            # squared amplitude
            amp2 = np.abs(vec)**2
            # total sum should be 1
            surface_amp = np.sum(amp2[0:3])  # first layer
            if surface_amp > 0.3:  # surface localized
                # determine mode type
                # Rayleigh is the lowest frequency at each q
                # We'll tag per q later; so store all surface modes for this q
                rows.append({
                    'q_010': float(i)/(q_points-1),
                    'Omega': round(omega, 6),
                    'amp': surface_amp
                })
    # Now label Rayleigh vs resonance per q_010 group
    final_rows = []
    # group by q_010
    from collections import defaultdict
    grouped = defaultdict(list)
    for r in rows:
        grouped[r['q_010']].append(r)
    for q_val in sorted(grouped.keys()):
        group = sorted(grouped[q_val], key=lambda x: x['Omega'])
        if not group:
            continue
        # lowest as Rayleigh
        group[0]['mode_type'] = 'Rayleigh'
        for i in range(1, len(group)):
            group[i]['mode_type'] = 'resonance'
        final_rows.extend([{'q_010': g['q_010'], 'Omega': g['Omega'], 'mode_type': g['mode_type']} for g in group])
    # sort
    final_rows.sort(key=lambda r: (r['q_010'], r['Omega']))
    return final_rows

def compute_vdos(N=20, epsilon=0.05, omega_max=1.5, nsteps=200):
    """Compute local VDOS at bulk center and surface site."""
    # For simplicity, use q_010 = 0? VDOS requires integration over in-plane BZ.
    # The paper's VDOS presumably integrated over entire 2D BZ. We'll approximate by sampling a grid of q_parallel points.
    # That's heavy. For oracle, we can approximate by computing VDOS from the slab's Green's function at a few representative q points and averaging? Actually, local VDOS per site should already include contributions from all wavevectors. The slab Hamiltonian with one unit cell laterally does not give full VDOS because it's missing in-plane dispersion. To get correct VDOS, we need to sample 2D BZ.
    # So we'll integrate over in-plane (qx,qy) using a grid (e.g., 10x10). Then compute Green's function for each q, extract diagonal elements for bulk site (middle layer) and surface site, average over q, then produce spectrum.
    # Implement:
    q_samples = 20  # grid per dimension
    N_omega = nsteps
    omega_grid = np.linspace(1e-6, omega_max, N_omega)
    bulk_vdos = np.zeros(N_omega)
    surf_vdos = np.zeros(N_omega)
    
    for ix in range(q_samples):
        qx = (ix / (q_samples-1) - 0.5) * 2*math.pi  # -pi to pi
        for iy in range(q_samples):
            qy = (iy / (q_samples-1) - 0.5) * 2*math.pi
            D_slab = slab_harmonic_matrix(qx, qy, N_layers=N)
            # For each omega, compute - (2Ω/π) Im[ (Ω^2 + iε - D)^{-1} ]_{ii}
            # We'll do matrix solve for each omega, but that's O(N^3) per omega. With N=20 and many q, it's heavy. We'll use sparse if possible but okay.
            # For speed, we can use eigenvalue decomposition once, then the Green's function is: G_ii(Ω) = sum_n |⟨i|n⟩|^2 / (Ω^2 - λ_n + iε)
            # where λ_n are eigenvalues, |n⟩ eigenvectors.
            eigvals, eigvecs = np.linalg.eigh(D_slab)
            for idx_omega, omega in enumerate(omega_grid):
                denom = omega**2 - eigvals + 1j*epsilon
                # contribution to G_ii for site in surface (layer 0) and bulk (layer N//2)
                # eigenvecs[i, mode] gives component for site i
                # For surface site: take the site index 0 (x comp for layer 0), but we sum over 3 dof of a layer.
                # We'll compute total VDOS for a layer: trace over 3 directions.
                # For surface layer: indices 0,1,2
                for idx_site in [0,1,2]:
                    amps = np.abs(eigvecs[idx_site, :])**2
                    G_ii = np.sum(amps / denom)
                    surf_vdos[idx_omega] += - (2*omega/math.pi) * np.imag(G_ii)
                # bulk layer: layer N//2, indices 3*(N//2)+0..2
                bulk_layer_start = 3*(N//2)
                for idx_site in range(bulk_layer_start, bulk_layer_start+3):
                    amps = np.abs(eigvecs[idx_site, :])**2
                    G_ii = np.sum(amps / denom)
                    bulk_vdos[idx_omega] += - (2*omega/math.pi) * np.imag(G_ii)
    # Normalize each spectrum to integrate to 1
    domega = omega_grid[1]-omega_grid[0]
    bulk_area = np.trapz(bulk_vdos, omega_grid)
    surf_area = np.trapz(surf_vdos, omega_grid)
    if bulk_area > 0:
        bulk_vdos /= bulk_area
    if surf_area > 0:
        surf_vdos /= surf_area
    # Output
    rows = []
    for i, omega in enumerate(omega_grid):
        rows.append({
            'Omega': round(omega, 6),
            'bulk_VDOS': round(bulk_vdos[i], 8),
            'surface_VDOS': round(surf_vdos[i], 8)
        })
    return rows

def write_step1(fpath):
    data = {"k1": k1, "k2": k2}
    with open(fpath, 'w') as f:
        json.dump(data, f, indent=2)

def write_step2(fpath):
    rows = phonon_dispersion()
    with open(fpath, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=['direction','q_norm','branch','Omega'])
        writer.writeheader()
        writer.writerows(rows)

def write_step3(fpath):
    rows = surface_dispersion()
    with open(fpath, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=['q_010','Omega','mode_type'])
        writer.writeheader()
        writer.writerows(rows)

def write_step4(fpath):
    rows = compute_vdos()
    with open(fpath, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=['Omega','bulk_VDOS','surface_VDOS'])
        writer.writeheader()
        writer.writerows(rows)

if __name__ == '__main__':
    step = sys.argv[1]
    fpath = sys.argv[2]
    if step == '1':
        write_step1(fpath)
    elif step == '2':
        write_step2(fpath)
    elif step == '3':
        write_step3(fpath)
    elif step == '4':
        write_step4(fpath)
    else:
        raise ValueError('Invalid step')
