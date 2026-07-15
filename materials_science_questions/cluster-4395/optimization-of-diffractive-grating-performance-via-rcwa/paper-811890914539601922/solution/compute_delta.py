import math

# ---------- Marcuvitz-based thin-grid polarizer model ----------
# For an infinitely thin metallic strip grating at the boundary
# between free space (n=1) and a support (n=2.2), with normal incidence.
# Electric field parallel to the strips -> inductive shunt impedance.
# Electric field perpendicular to the strips -> capacitive shunt impedance.
# Using standard simplified forms of the Marcuvitz formulas (p. 280).

def ln_csc(angle):
    """ln(csc(angle)) = -ln(sin(angle))"""
    s = math.sin(angle)
    if s <= 0:
        return float('inf')
    return -math.log(s)

def compute_delta(a_lambda, d_a, n=2.2):
    # X = (a/lambda) * ln(csc(pi*d/(2a)))
    angle = math.pi * d_a / 2.0
    L = ln_csc(angle)
    X = a_lambda * L
    # Avoid numerical singularities for extremely small X
    if X < 1e-15:
        X = 1e-15
    # Phase of transmission coefficient for E parallel (inductive)
    # T_par = 2 / (1+n + 1/Zr) with 1/Zr = -j/X
    # arg(T_par) = arctan(1/((1+n)X))
    phi_par = math.atan2(1.0, (1 + n) * X)
    # Phase of transmission coefficient for E perpendicular (capacitive)
    # Z_cap = -j / (4X)  =>  1/Zr = j * 4X
    # arg(T_perp) = -arctan(4X/(1+n))
    phi_perp = -math.atan2(4.0 * X, 1 + n)
    # Relative phase retardance Delta = arg(T_perp) - arg(T_par)
    return phi_perp - phi_par

# Parameters from the task
d_a_values = [0.2, 0.4, 0.6, 0.8]
n = 2.2
# Logarithmic grid of a/lambda from 0.001 to 1.0 (60 points, >50)
num_points = 60
a_lambda_list = [10 ** (-3.0 + i * 3.0 / (num_points - 1)) for i in range(num_points)]

# Write CSV
out_path = '/app/outputs/delta_vs_a_lambda.csv'
with open(out_path, 'w') as f:
    f.write('a_lambda,d_a,Delta\n')
    for d_a in d_a_values:
        for a_l in a_lambda_list:
            delta = compute_delta(a_l, d_a, n)
            # Full precision output; 15 significant digits is plenty
            f.write(f'{a_l:.15g},{d_a},{delta:.15g}\n')
