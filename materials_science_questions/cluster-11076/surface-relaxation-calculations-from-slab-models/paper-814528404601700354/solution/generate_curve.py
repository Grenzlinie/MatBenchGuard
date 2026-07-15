import sys, math, numpy as np, json

def generate_lattice(lattice_type, max_radius_half):
    points = []
    coords_set = set()
    if lattice_type == 'fcc':
        for i in range(-max_radius_half, max_radius_half+1):
            for j in range(-max_radius_half, max_radius_half+1):
                for k in range(-max_radius_half, max_radius_half+1):
                    if (i+j+k) % 2 == 0:
                        points.append((i,j,k))
                        coords_set.add((i,j,k))
    elif lattice_type == 'bcc':
        for i in range(-max_radius_half, max_radius_half+1):
            for j in range(-max_radius_half, max_radius_half+1):
                for k in range(-max_radius_half, max_radius_half+1):
                    if (i%2 == j%2 == k%2):
                        points.append((i,j,k))
                        coords_set.add((i,j,k))
    return points, coords_set

def get_neighbor_vectors(lattice_type):
    if lattice_type == 'fcc':
        first = [(1,1,0),(1,-1,0),(-1,1,0),(-1,-1,0),
                 (1,0,1),(1,0,-1),(-1,0,1),(-1,0,-1),
                 (0,1,1),(0,1,-1),(0,-1,1),(0,-1,-1)]
        second = [(2,0,0),(-2,0,0),(0,2,0),(0,-2,0),(0,0,2),(0,0,-2)]
    else:  # bcc
        first = [(1,1,1),(1,1,-1),(1,-1,1),(1,-1,-1),
                 (-1,1,1),(-1,1,-1),(-1,-1,1),(-1,-1,-1)]
        second = [(2,0,0),(-2,0,0),(0,2,0),(0,-2,0),(0,0,2),(0,0,-2)]
    return first, second

def build_neighbor_lists(points, coords_set, lattice_type):
    first_vec, second_vec = get_neighbor_vectors(lattice_type)
    idx_map = {pt: i for i,pt in enumerate(points)}
    n = len(points)
    first_neighbors = [[] for _ in range(n)]
    second_neighbors = [[] for _ in range(n)]
    for i, (x,y,z) in enumerate(points):
        for dx,dy,dz in first_vec:
            nb = (x+dx, y+dy, z+dz)
            if nb in coords_set:
                j = idx_map[nb]
                first_neighbors[i].append(j)
        for dx,dy,dz in second_vec:
            nb = (x+dx, y+dy, z+dz)
            if nb in coords_set:
                j = idx_map[nb]
                second_neighbors[i].append(j)
    return first_neighbors, second_neighbors

def bfs_shells(points, first_neighbors):
    from collections import deque
    n = len(points)
    origin_idx = None
    for i, pt in enumerate(points):
        if pt == (0,0,0):
            origin_idx = i
            break
    if origin_idx is None:
        raise ValueError("Origin not in lattice")
    dist = [-1]*n
    q = deque([origin_idx])
    dist[origin_idx] = 0
    while q:
        u = q.popleft()
        for v in first_neighbors[u]:
            if dist[v] == -1:
                dist[v] = dist[u] + 1
                q.append(v)
    return dist

def compute_surface_sums(points, first_neighbors, second_neighbors, lattice_type, max_N):
    shells = bfs_shells(points, first_neighbors)
    dist_sq = [x*x + y*y + z*z for (x,y,z) in points]
    sort_keys = list(range(len(points)))
    sort_keys.sort(key=lambda i: (shells[i], dist_sq[i], points[i][0], points[i][1], points[i][2]))
    
    if lattice_type == 'fcc':
        Z_b, a = 12, 0.08
    else:
        Z_b, a = 8, 0.4
    
    n = len(points)
    weighted_neighbors = [[] for _ in range(n)]
    for i in range(n):
        for j in first_neighbors[i]:
            weighted_neighbors[i].append((j, 1.0))
        for j in second_neighbors[i]:
            weighted_neighbors[i].append((j, a))
    
    added = [False]*n
    Z = [0.0]*n
    surface_sum = [0.0]*(max_N+1)
    current = 0.0
    for idx in range(max_N):
        i = sort_keys[idx]
        Z_i = 0.0
        for (j, w) in weighted_neighbors[i]:
            if added[j]:
                Z_i += w
        Z[i] = Z_i
        if Z_i < 10:
            current += math.sqrt(Z_i / Z_b) - 1
        for (j, w) in weighted_neighbors[i]:
            if added[j]:
                old_Z = Z[j]
                new_Z = old_Z + w
                Z[j] = new_Z
                if old_Z < 10 and new_Z >= 10:
                    current -= (math.sqrt(old_Z / Z_b) - 1)
                elif old_Z < 10 and new_Z < 10:
                    current += (math.sqrt(new_Z / Z_b) - 1) - (math.sqrt(old_Z / Z_b) - 1)
        added[i] = True
        surface_sum[idx+1] = current
    return surface_sum

if __name__ == '__main__':
    output_path = sys.argv[1]
    max_N = 20000
    pts_fcc, coords_fcc = generate_lattice('fcc', 25)
    first_fcc, second_fcc = build_neighbor_lists(pts_fcc, coords_fcc, 'fcc')
    sum_fcc = compute_surface_sums(pts_fcc, first_fcc, second_fcc, 'fcc', max_N)
    pts_bcc, coords_bcc = generate_lattice('bcc', 30)
    first_bcc, second_bcc = build_neighbor_lists(pts_bcc, coords_bcc, 'bcc')
    sum_bcc = compute_surface_sums(pts_bcc, first_bcc, second_bcc, 'bcc', max_N)
    with open(output_path, 'w') as f:
        f.write("N,S\n")
        for N in range(10, max_N+1):
            if N < len(sum_fcc) and N < len(sum_bcc):
                S = (sum_fcc[N] - sum_bcc[N]) / N
                f.write(f"{N},{S:.8f}\n")
