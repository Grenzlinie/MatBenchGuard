import json, math, itertools

# --- Ionic radii (Shannon, CN=6, in Å) ---
r_Cu = 0.73
radii = {
    'O': 1.40,
    'Si': 0.40,
    'Ge': 0.53,
    'Ba': 1.35,   # typical Shannon Ba2+ CN=6
}
D_c = 2.88         # critical distance for direct exchange

# --- Symmetry operations for Pnma (No.62) ---
# list of lambdas that map (x,y,z) to a symmetry-equivalent position
sym_ops = [
    lambda x,y,z: (x,      y,      z),
    lambda x,y,z: (-x+0.5, -y,     z+0.5),
    lambda x,y,z: (-x,     y+0.5, -z),
    lambda x,y,z: ( x+0.5, -y+0.5, -z+0.5),
    lambda x,y,z: (-x,     -y,     -z),
    lambda x,y,z: ( x-0.5,  y,     -z-0.5),
    lambda x,y,z: ( x,     -y+0.5,  z),
    lambda x,y,z: (-x+0.5,  y+0.5, -z+0.5),
]

def frac_to_cart(frac, a, b, c):
    """Convert fractional coordinates to Cartesian (orthorhombic, angles 90°)."""
    x,y,z = frac
    return (x*a, y*b, z*c)

def generate_atoms(unique_atoms, a, b, c):
    """Generate all atoms in one unit cell.
    unique_atoms: list of (symbol, x, y, z) for unique Wyckoff positions.
    Returns list of (symbol, cart_x, cart_y, cart_z)."""
    atoms = []
    seen = set()
    for sym, x, y, z in unique_atoms:
        for op in sym_ops:
            fx, fy, fz = op(x, y, z)
            # wrap fractional coordinates to [0,1) while preserving equivalence
            fx = fx - math.floor(fx)
            fy = fy - math.floor(fy)
            fz = fz - math.floor(fz)
            key = (sym, round(fx,4), round(fy,4), round(fz,4))
            if key not in seen:
                seen.add(key)
                atoms.append((sym, fx*a, fy*b, fz*c))
    return atoms

def vector_length(v):
    return math.hypot(math.hypot(v[0], v[1]), v[2])

def dot(u, v):
    return u[0]*v[0] + u[1]*v[1] + u[2]*v[2]

def subtract(p1, p2):
    return (p1[0]-p2[0], p1[1]-p2[1], p1[2]-p2[2])

def add(p1, p2):
    return (p1[0]+p2[0], p1[1]+p2[1], p1[2]+p2[2])

def scalar_mul(s, v):
    return (s*v[0], s*v[1], s*v[2])

def projection_factor(point, line_p1, line_p2):
    """Return t such that line_p1 + t*(line_p2-line_p1) is the foot of perpendicular from point."""
    v = subtract(line_p2, line_p1)
    w = subtract(point, line_p1)
    c1 = dot(w, v)
    c2 = dot(v, v)
    if c2 == 0:
        return 0.0
    return c1 / c2

def point_to_line_distance(point, line_p1, line_p2):
    """Perpendicular distance from point to the infinite line through line_p1 and line_p2."""
    v = subtract(line_p2, line_p1)
    w = subtract(point, line_p1)
    c1 = dot(w, v)
    c2 = dot(v, v)
    if c2 == 0:
        return vector_length(w)
    t = c1 / c2
    proj = add(line_p1, scalar_mul(t, v))
    return vector_length(subtract(point, proj))

def compute_J(cu1, cu2, other_atoms, a, b, c):
    """Compute J^s for the Cu pair cu1, cu2 (Cartesian coordinates).
    other_atoms: list of (symbol, cart_x, cart_y, cart_z) for all non-Cu atoms in one cell.
    We include periodic images by offsetting their coordinates."""
    d = vector_length(subtract(cu1, cu2))
    line_p1 = cu1
    line_p2 = cu2
    j_sum = 0.0
    # Loop over other atoms with offsets in a 3x3x3 supercell
    for sym, atom_pos in other_atoms:
        r_A = radii.get(sym, 1.0)   # fallback
        if r_A is None:
            continue
        # base fractional coords
        base = (atom_pos[0]/a, atom_pos[1]/b, atom_pos[2]/c)
        for dx in (-1,0,1):
            for dy in (-1,0,1):
                for dz in (-1,0,1):
                    fx = base[0] + dx
                    fy = base[1] + dy
                    fz = base[2] + dz
                    cart = (fx*a, fy*b, fz*c)
                    h = point_to_line_distance(cart, line_p1, line_p2)
                    # Check cylinder overlap
                    if h < r_Cu + r_A:
                        delta_h = h - r_A
                        # Compute l and l' (foot distances)
                        t = projection_factor(cart, line_p1, line_p2)
                        # Clamp t to [0,1] to stay on segment? Paper uses l and l' as distances to the two magnetic ions,
                        # presumably measured along the line; if foot falls outside the segment, l, l' might still be defined
                        # but the paper assumes intermediate ion lies within the cylinder and influence symmetric.
                        # For safety, compute distances to both endpoints and take the smaller as l, larger as l'.
                        l1 = vector_length(subtract(cart, cu1))
                        l2 = vector_length(subtract(cart, cu2))
                        l = min(l1, l2)
                        lprime = max(l1, l2)
                        if l == 0:  # avoid division by zero, skip
                            continue
                        ratio = lprime / l
                        if ratio < 2.0:
                            j_n = delta_h * (l/lprime + lprime/l) / (d*d)
                        else:
                            j_n = delta_h * (l/lprime) / (d*d)
                        j_sum += j_n
    # direct exchange contribution
    if d < 2 * (2 * r_Cu):   # less than two diameters = 2*1.46 = 2.92
        j_direct = (d - D_c) / (r_Cu * d)
    else:
        j_direct = 0.0
    return j_sum + j_direct


# ---------- Crystal structures ----------
# BaCu2Si2O7 (Yamada et al. 2001, powder)
Si_struct = {
    'a': 6.862, 'b': 14.302, 'c': 7.358,
    # unique atoms: (symbol, x, y, z)
    'unique': [
        ('Ba', 0.1130, 0.25, 0.5040),
        ('Cu', 0.2848, 0.03292, 0.1087),
        ('Si', 0.1216, 0.25, 0.9704),
        ('O', 0.321,  0.25, 0.706),
        ('O', 0.2771, 0.0690, 0.778),
        ('O', 0.426,  0.0999, 0.123),
        ('O', 0.138,  0.25, 0.305),
    ]
}

# BaCu2Ge2O7 (Yamada et al. 2001, powder)
Ge_struct = {
    'a': 6.981, 'b': 14.583, 'c': 7.464,
    'unique': [
        ('Ba', 0.1119, 0.25, 0.4991),
        ('Cu', 0.2848, 0.03428, 0.1091),
        ('Ge', 0.1183, 0.25, 0.9678),
        ('O', 0.319,  0.25, 0.704),
        ('O', 0.276,  0.0687, 0.777),
        ('O', 0.426,  0.0976, 0.122),
        ('O', 0.136,  0.25, 0.304),
    ]
}

def get_cu_pairs(atoms, a, b, c):
    """Return list of (cu1_cart, cu2_cart, vector_cart, distance)."""
    cu_positions = [pos for (sym, *pos) in atoms if sym == 'Cu']
    pairs = []
    for i, pos1 in enumerate(cu_positions):
        x1,y1,z1 = pos1
        for j, pos2 in enumerate(cu_positions):
            if i >= j:
                continue
            # Only consider pairs within one unit cell (add translations later?)
            dx = (pos2[0]-pos1[0])/a
            dy = (pos2[1]-pos1[1])/b
            dz = (pos2[2]-pos1[2])/c
            # We'll also add pairs with shifts by a,b,c to capture across cells
            for nx in (-1,0,1):
                for ny in (-1,0,1):
                    for nz in (-1,0,1):
                        if nx==0 and ny==0 and nz==0 and i>=j:
                            continue
                        shift_cart = (nx*a, ny*b, nz*c)
                        p2_shifted = add(pos2, shift_cart)
                        vec = subtract(p2_shifted, pos1)
                        dist = vector_length(vec)
                        if dist > 0 and dist < 8.0:   # max distance we care about
                            pairs.append((pos1, p2_shifted, vec, dist))
    return pairs

def label_pairs(pairs, a, b, c):
    """Assign coupling labels to Cu pairs based on distance and direction.
    Uses known distances from the paper."""
    # distances reported in paper:
    # J1: intrachain along c, around 3.68?
    # J2: along a, 3.480
    # J4: diagonal ac, 4.776
    # J7: along b, shorter 6.451
    # J8: along b, longer 6.725
    assignments = {}
    for cu1, cu2, vec, dist in pairs:
        # Determine dominant direction
        vx, vy, vz = vec
        # Use absolute components
        ax = abs(vx)/a
        ay = abs(vy)/b
        az = abs(vz)/c
        # Tolerance for matching reported distances
        tol = 0.08
        if abs(dist - 3.48) < tol and ax > 0.4 and ax > ay and ax > az:
            assignments['J2'] = (cu1, cu2)
        elif abs(dist - 4.776) < tol:
            assignments['J4'] = (cu1, cu2)
        elif abs(dist - 6.451) < tol:
            assignments['J7'] = (cu1, cu2)
        elif abs(dist - 6.725) < tol:
            assignments['J8'] = (cu1, cu2)
        # J1: intrachain along c, look for smallest distance with dz large and dx,dy negligible
    # Now identify J1: pair with small dx,dy and distance around 3.68
    candidates = []
    for cu1, cu2, vec, dist in pairs:
        vx, vy, vz = vec
        if abs(vx)/a < 0.1 and abs(vy)/b < 0.1 and abs(vz)/c > 0.4:
            candidates.append((dist, cu1, cu2))
    if candidates:
        candidates.sort()
        # shortest one is J1 (intrachain)
        assignments['J1'] = (candidates[0][1], candidates[0][2])
    return assignments


def compute_compound(struct, label_pairs_fn):
    a, b, c = struct['a'], struct['b'], struct['c']
    unique = struct['unique']
    atoms = generate_atoms(unique, a, b, c)
    cu_pairs = get_cu_pairs(atoms, a, b, c)
    assignments = label_pairs_fn(cu_pairs, a, b, c)
    result = {}
    for label, (cu1, cu2) in assignments.items():
        # For intermediate ions, use all non-Cu atoms
        other_atoms = [(sym, x, y, z) for (sym, x, y, z) in atoms if sym != 'Cu']
        J = compute_J(cu1, cu2, other_atoms, a, b, c)
        result[label] = round(J, 6)   # rounding to avoid floating noise
    return result


# Run for both compounds
result_Si = compute_compound(Si_struct, label_pairs)
result_Ge = compute_compound(Ge_struct, label_pairs)

# For Ge, we only need J1, J2, J4
output = {
    "BaCu2Si2O7": result_Si,
    "BaCu2Ge2O7": {k: result_Ge[k] for k in ('J1','J2','J4') if k in result_Ge}
}

print(json.dumps(output, indent=2))
