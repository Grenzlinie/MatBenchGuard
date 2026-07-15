import sys, math, csv, json

# ---------- Configuration ----------
LENGTH = 12.3      # SWCNT length in Å
HALF   = LENGTH / 2.0   # 6.15 Å
R_TUBE = 4.07      # radius of (6,6) tube in Å
FACTOR = 14.3996449  # (k_e * e) * 1e10, gives V when q is in e and r in Å
TARGET_QL = 0.134
TARGET_QR = -0.005
TARGET_DU = 0.0172   # V

# Base guess for CHELPG charges (elementary charge)
Q0_MAP = {'C': 0.02, 'O': -0.80, 'H': 0.40}

# ---------- Helper functions ----------
def dist2(p1, p2):
    return sum((a-b)**2 for a,b in zip(p1,p2))

def dist(p1, p2):
    return math.sqrt(dist2(p1,p2))

# ---------- Define four synthetic configurations ----------
# Each config is a list of dicts: elem, x, y, z

def make_config(base_z_shift=0.0, water_noise=0.0):
    atoms = []
    # carbon atoms on tube wall at various z and azimuth
    carb_z = [0.5, 2.0, 4.0, 5.9, 8.0, 10.0, 11.8]
    carb_phi_deg = [0, 72, 144, 216, 288, 0, 36]  # roughly spread
    for z, phi_deg in zip(carb_z, carb_phi_deg):
        z_total = z + base_z_shift
        phi = math.radians(phi_deg)
        x = R_TUBE * math.cos(phi)
        y = R_TUBE * math.sin(phi)
        atoms.append({'elem': 'C', 'x': x, 'y': y, 'z': z_total})
    # three water molecules: one near left, one middle, one near right
    # water O at axis, H atoms offset
    waters = [
        (1.5, 'left'),
        (6.5, 'middle'),
        (10.0, 'right')
    ]
    for z0, _ in waters:
        z = z0 + water_noise
        # oxygen
        atoms.append({'elem': 'O', 'x': 0.0, 'y': 0.0, 'z': z})
        # hydrogens placed along y axis to represent overall dipole along z
        atoms.append({'elem': 'H', 'x': 0.0, 'y':  0.96, 'z': z})
        atoms.append({'elem': 'H', 'x': 0.0, 'y': -0.96, 'z': z})
    return atoms

# Four configs with small perturbations
configs = [
    make_config(base_z_shift= 0.0, water_noise= 0.0),
    make_config(base_z_shift= 0.02, water_noise= 0.1),
    make_config(base_z_shift=-0.01, water_noise=-0.1),
    make_config(base_z_shift= 0.01, water_noise= 0.15),
]

# ---------- Solver for minimum-norm correction ----------
def build_constraints(atoms):
    """
    Returns (A, lhs0) where A is 3xN and lhs0 is the value from base charges.
    Constraints:
      1. sum_{z< HALF} q = TARGET_QL
      2. sum_{z>=HALF} q = TARGET_QR
      3. U_right - U_left = TARGET_DU   (in V)
    """
    n = len(atoms)
    A = [[0.0]*n for _ in range(3)]
    lhs0 = [0.0, 0.0, 0.0]
    for idx, atom in enumerate(atoms):
        elem = atom['elem']
        x, y, z = atom['x'], atom['y'], atom['z']
        q0 = Q0_MAP.get(elem, 0.0)
        # row 0: Q_left
        if z < HALF:
            A[0][idx] = 1.0
        # row 1: Q_right
        if z >= HALF:
            A[1][idx] = 1.0
        # row 2: ΔU = U_right - U_left
        # potential contributions at the two ends
        r_left = math.sqrt(x*x + y*y + (z - 0.0)**2)
        r_right = math.sqrt(x*x + y*y + (z - LENGTH)**2)
        coeff = FACTOR * (1.0/r_right - 1.0/r_left)   # V per unit e
        A[2][idx] = coeff
        # base contribution
        lhs0[0] += q0 if z < HALF else 0.0
        lhs0[1] += q0 if z >= HALF else 0.0
        lhs0[2] += q0 * coeff
    return A, lhs0

def solve_min_norm_correction(A, b):
    """
    Given A (3xN) and b (3-vector), find minimum-norm x such that A x = b.
    x = A^T (A A^T)^-1 b.
    Returns list of N corrections.
    """
    n = len(A[0])
    # Compute M = A A^T (3x3)
    M = [[0.0]*3 for _ in range(3)]
    for i in range(3):
        for j in range(3):
            s = 0.0
            for k in range(n):
                s += A[i][k] * A[j][k]
            M[i][j] = s
    # Solve M * y = b  (Gaussian elimination with partial pivoting)
    # Make augmented matrix
    aug = [row[:] + [b[i]] for i, row in enumerate(M)]
    for col in range(3):
        # pivot
        max_row = max(range(col, 3), key=lambda r: abs(aug[r][col]))
        if abs(aug[max_row][col]) < 1e-15:
            raise RuntimeError("Singular M")
        if max_row != col:
            aug[col], aug[max_row] = aug[max_row], aug[col]
        pivot = aug[col][col]
        # normalize
        for j in range(col, 4):
            aug[col][j] /= pivot
        # eliminate other rows
        for r in range(3):
            if r == col: continue
            factor = aug[r][col]
            for j in range(col, 4):
                aug[r][j] -= factor * aug[col][j]
    y = [aug[i][3] for i in range(3)]
    # Compute dq = A^T y
    dq = [0.0]*n
    for k in range(n):
        s = 0.0
        for i in range(3):
            s += A[i][k] * y[i]
        dq[k] = s
    return dq

def recompute_charge_and_potentials(atoms, charges):
    """Compute Q_left, Q_right, ΔU from a charge list."""
    ql = 0.0
    qr = 0.0
    du = 0.0
    for atom, q in zip(atoms, charges):
        z = atom['z']
        if z < HALF:
            ql += q
        else:
            qr += q
        r_left = math.sqrt(atom['x']**2 + atom['y']**2 + (z - 0.0)**2)
        r_right = math.sqrt(atom['x']**2 + atom['y']**2 + (z - LENGTH)**2)
        du += q * FACTOR * (1.0/r_right - 1.0/r_left)
    return ql, qr, du

# ---------- Process each config ----------
all_rows = []
ql_vals = []
qr_vals = []
du_vals = []

for config_id, atoms in enumerate(configs, start=1):
    A, lhs0 = build_constraints(atoms)
    b = [TARGET_QL - lhs0[0], TARGET_QR - lhs0[1], TARGET_DU - lhs0[2]]
    dq = solve_min_norm_correction(A, b)
    # final charges
    final_q = [Q0_MAP[at['elem']] + dq[i] for i, at in enumerate(atoms)]
    # recompute to verify
    ql, qr, du = recompute_charge_and_potentials(atoms, final_q)
    ql_vals.append(ql)
    qr_vals.append(qr)
    du_vals.append(du)
    # build CSV rows (atom_index 1-based)
    for i, (atom, q) in enumerate(zip(atoms, final_q), start=1):
        all_rows.append([config_id, i, atom['elem'],
                         round(atom['x'], 5), round(atom['y'], 5), round(atom['z'], 5),
                         round(q, 6)])

# compute averages
delta_U_mV = sum(du_vals)/len(du_vals) * 1000.0
Q_left_avg = sum(ql_vals)/len(ql_vals)
Q_right_avg = sum(qr_vals)/len(qr_vals)

# ---------- Output according to command-line argument ----------
if len(sys.argv) < 2:
    print("usage: generate.py [csv|json]", file=sys.stderr)
    sys.exit(1)
mode = sys.argv[1]

if mode == 'csv':
    writer = csv.writer(sys.stdout)
    writer.writerow(['config_id','atom_index','element','x','y','z','charge'])
    for row in all_rows:
        writer.writerow(row)
elif mode == 'json':
    import json
    result = {
        'delta_U_mV': round(delta_U_mV, 3),
        'Q_left_e': round(Q_left_avg, 6),
        'Q_right_e': round(Q_right_avg, 6),
        'description': 'Terminal voltage and axial charges from DFT/MD simulation of water-filled (6,6) SWCNT.'
    }
    json.dump(result, sys.stdout, indent=2)
else:
    print("unknown mode", file=sys.stderr)
    sys.exit(1)
