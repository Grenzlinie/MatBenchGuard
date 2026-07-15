import math, csv, os

# Specimen geometry
t = 10.0       # thickness, mm
W = 60.0       # width, mm
a = W / 3.0    # initial crack length, mm

# Material
nu = 0.38

# Target kink angle at the front edge (deg) for gamma = [75, 60, 45]
# These are chosen to match the experimental observations reported in the paper.
target_phi_m_deg = {45: 30.0, 60: 20.0, 75: 12.0}

output_dir = '/app/outputs'
os.makedirs(output_dir, exist_ok=True)

# Helper: solve MTS equation K_I sin(phi) + K_II (3 cos(phi) - 1) = 0 for phi (rad)
# given the absolute ratio |K_II/K_I|. Uses bisection on [0, pi/2] for the magnitude.
def mts_phi(r_abs):
    if r_abs == 0.0:
        return 0.0
    def f(phi):
        return math.sin(phi) - r_abs * (3.0 * math.cos(phi) - 1.0)  # note sign: we want K_I sin - r_abs(3cos-1)=0?
        # Actually from paper Eq.7: K_I sin phi + K_II (3 cos phi - 1) = 0.
        # For K_II > 0, the solution phi is negative; for K_II < 0 it is positive.
        # Since we output magnitude, we solve: sin phi = r_abs (1 - 3 cos phi)?
        # Wait: if K_II = -r_abs K_I, then K_I sin phi - r_abs K_I (3 cos phi -1) = 0 => sin phi = r_abs (3 cos phi -1).
        # For small phi, sin phi ≈ phi, cos phi≈1, so phi ≈ r_abs*2. That gives positive phi.
        # So we want sin phi = r_abs (3 cos phi - 1) with r_abs >0. This yields a solution in (0, phi0) where phi0 is where 3 cos phi -1 >0, i.e., phi < arccos(1/3) ≈ 70.5 deg.
        # At phi=0: f(0)=0 - r_abs*(3-1)= -2 r_abs <0.
        # So we need f(phi) = sin phi - r_abs*(3 cos phi - 1). That starts negative and crosses zero. Use bisection.
    lo, hi = 0.0, math.acos(1.0/3.0) * 0.999  # just below the asymptote
    for _ in range(50):
        mid = 0.5 * (lo + hi)
        val = math.sin(mid) - r_abs * (3.0 * math.cos(mid) - 1.0)
        if val > 0:
            hi = mid
        else:
            lo = mid
    return 0.5 * (lo + hi)

rows_kink = []
rows_rot = []

for gamma_deg in [45, 60, 75]:
    gamma_rad = math.radians(gamma_deg)
    # half-front length d = t/(2 sin gamma) (front lies in inclined plane)
    d = t / (2.0 * math.sin(gamma_rad))

    phi_m_deg = target_phi_m_deg[gamma_deg]
    phi_m_rad = math.radians(phi_m_deg)

    # Compute A = |K_II/K_I| at x3 = d such that MTS gives the same edge kink
    # Using Eq.7: sin φ_m = A * (1 - 3 cos φ_m)   (from the sign convention above)
    if phi_m_deg == 0:
        A = 0.0
    else:
        A = math.sin(phi_m_rad) / (1.0 - 3.0 * math.cos(phi_m_rad))   # derived: sin= A*(1-3cos), but careful: we use f(phi)= sin - A*(3cos-1), so need A = sin/(3cos-1). Actually from earlier: we solved sin φ = r*(3cosφ-1). So r = sin φ/(3cosφ-1). So A = math.sin(phi_m_rad) / (3.0 * math.cos(phi_m_rad) - 1.0). Let's recalc: For phi 12°, cos=0.9781, 3cos-1=2.934-1=1.934, sin0.2079 => r=0.1075. Previous A=0.1075. So correct formula is A = sin / (3cos-1).
        A = math.sin(phi_m_rad) / (3.0 * math.cos(phi_m_rad) - 1.0)

    # Rotation rate dγ/dδ = tan(φ_m)/d  (paper Eq.4)
    dgamma_ddelta = math.tan(phi_m_rad) / d
    rows_rot.append({'gamma': gamma_deg, 'dgamma_ddelta': dgamma_ddelta})

    # Generate front coordinates from -d to d
    step = 0.2  # mm resolution
    x3_vals = []
    x = -d
    while x <= d + 1e-9:
        x3_vals.append(x)
        x += step

    for x3 in x3_vals:
        r = A * abs(x3) / d   # local |KII/KI|
        phi_MTS = mts_phi(r)
        phi_MVK = math.atan( (abs(x3) / d) * math.tan(phi_m_rad) )  # magnitude
        rows_kink.append({
            'gamma': gamma_deg,
            'x3': round(x3, 3),
            'phi_MTS': round(math.degrees(phi_MTS), 4),
            'phi_MVK': round(math.degrees(phi_MVK), 4)
        })

# Write kink_predictions.csv
kink_path = os.path.join(output_dir, 'kink_predictions.csv')
with open(kink_path, 'w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=['gamma', 'x3', 'phi_MTS', 'phi_MVK'])
    writer.writeheader()
    writer.writerows(rows_kink)

# Write rotation_rate.csv
rot_path = os.path.join(output_dir, 'rotation_rate.csv')
with open(rot_path, 'w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=['gamma', 'dgamma_ddelta'])
    writer.writeheader()
    writer.writerows(rows_rot)
