import numpy as np
import csv
import os

np.random.seed(42)

R_large = 1.0
n_cells = 2  # number of unit cells per dimension

def generate_fcc_positions(n, L_unit):
    """Return list of large sphere centers in box from (0,0,0) to (n*L_unit, n*L_unit, n*L_unit)."""
    positions = []
    offsets = np.array([[0,0,0],
                        [L_unit/2, L_unit/2, 0],
                        [L_unit/2, 0, L_unit/2],
                        [0, L_unit/2, L_unit/2]])
    for i in range(n):
        for j in range(n):
            for k in range(n):
                base = np.array([i*L_unit, j*L_unit, k*L_unit])
                for off in offsets:
                    pos = base + off
                    positions.append(pos)
    return positions

def run_simulation(diameter_ratio, large_volume_fraction):
    r_small = R_large / diameter_ratio
    V_large = 4/3 * np.pi * R_large**3
    # L_unit based on volume fraction of large particles
    L_unit = (4 * V_large / large_volume_fraction) ** (1/3)
    L_box = n_cells * L_unit
    
    # Place large particles
    large_centers = generate_fcc_positions(n_cells, L_unit)
    large_radii = [R_large] * len(large_centers)
    
    small_centers = []
    small_radii = []
    
    max_attempts = 500
    attempt = 0
    
    # Prepare arrays for vectorized distance checks
    centers = np.array(large_centers)  # shape (N,3)
    radii = np.array(large_radii, dtype=float)
    
    tol = 1e-4
    
    while attempt < max_attempts:
        # Random (x,y) within box
        x = np.random.uniform(0, L_box)
        y = np.random.uniform(0, L_box)
        
        # Drop
        dx = x - centers[:,0]
        dy = y - centers[:,1]
        d_sq = dx*dx + dy*dy
        r_sum = radii + r_small
        mask = d_sq <= r_sum**2
        if not np.any(mask):
            z_first = r_small
        else:
            z_cands = centers[mask,2] + np.sqrt(r_sum[mask]**2 - d_sq[mask])
            z_first = max(z_cands.max(), r_small)
        
        pos = np.array([x, y, z_first])
        
        # Quick overlap check
        dist_vec = np.linalg.norm(pos - centers, axis=1) - (radii + r_small)
        if np.any(dist_vec < -1e-3):
            attempt += 1
            continue
        
        # Determine initial contacts count
        contacts_initial = 0
        if abs(z_first - r_small) < tol:
            contacts_initial += 1
        near = np.abs(dist_vec) < tol
        contacts_initial += near.sum()
        
        best_pos = pos.copy()
        best_z = z_first
        best_contacts = contacts_initial
        
        # Monte Carlo search for lower z with more contacts
        for trial in range(30):
            perturb_x = np.random.uniform(-0.3, 0.3) * r_small
            perturb_y = np.random.uniform(-0.3, 0.3) * r_small
            nx = x + perturb_x
            ny = y + perturb_y
            if nx < 0 or nx > L_box or ny < 0 or ny > L_box:
                continue
            
            # Re-drop
            dx_t = nx - centers[:,0]
            dy_t = ny - centers[:,1]
            d_sq_t = dx_t*dx_t + dy_t*dy_t
            mask_t = d_sq_t <= r_sum**2
            if not np.any(mask_t):
                nz = r_small
            else:
                nz_cands = centers[mask_t,2] + np.sqrt(r_sum[mask_t]**2 - d_sq_t[mask_t])
                nz = max(nz_cands.max(), r_small)
            npos = np.array([nx, ny, nz])
            
            # Overlap check
            dist_vec_t = np.linalg.norm(npos - centers, axis=1) - (radii + r_small)
            if np.any(dist_vec_t < -1e-3):
                continue
            
            # Count contacts
            n_contacts = 0
            if abs(nz - r_small) < tol:
                n_contacts += 1
            n_contacts += (np.abs(dist_vec_t) < tol).sum()
            
            if nz < best_z - 1e-4 or (abs(nz - best_z) < tol and n_contacts > best_contacts):
                best_pos = npos
                best_z = nz
                best_contacts = n_contacts
        
        # Accept if at least 2 contacts (some stability)
        if best_contacts >= 2:
            # add to small particles
            centers = np.vstack([centers, best_pos])
            radii = np.append(radii, r_small)
        attempt += 1
    
    # All particles
    all_centers = centers
    all_radii = radii
    N = len(all_centers)
    
    # Coordination number
    coord_sum = 0
    for i in range(N):
        pos_i = all_centers[i]
        r_i = all_radii[i]
        dists = np.linalg.norm(all_centers - pos_i, axis=1)
        # exclude self, contact when distance approx equal to sum of radii
        mask = (np.abs(dists - (r_i + all_radii)) < tol) & (np.arange(N) != i)
        coord_sum += mask.sum()
    avg_coord = coord_sum / N if N > 0 else 0.0
    
    # Voidness
    total_particle_vol = np.sum(4/3 * np.pi * all_radii**3)
    voidness = 1.0 - total_particle_vol / (L_box**3)
    
    return avg_coord, voidness, N

def main():
    # Parameter grid covering the conditions studied in the paper
    diameter_ratios = [3, 5, 7, 10]
    large_volume_fractions = [0.2, 0.3, 0.35, 0.4, 0.5, 0.6]
    
    rows = []
    for dr in diameter_ratios:
        for lvf in large_volume_fractions:
            coord, void, n_total = run_simulation(dr, lvf)
            rows.append({
                'diameter_ratio': dr,
                'large_volume_fraction': lvf,
                'coordination_number': round(coord, 4),
                'voidness': round(void, 4)
            })
    
    outdir = '/app/outputs'
    os.makedirs(outdir, exist_ok=True)
    outpath = os.path.join(outdir, 'packing_results.csv')
    with open(outpath, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=['diameter_ratio','large_volume_fraction','coordination_number','voidness'])
        writer.writeheader()
        writer.writerows(rows)

if __name__ == '__main__':
    main()
