import csv
import sys
import math

# ========== Reference data from the paper ==========

# System sizes
N_VALUES = [24, 36, 48, 60, 72, 84, 96]

# Specific heat data: mu, A, alpha_nu, T_c
SPECIFIC_HEAT_PARAMS = [
    ( -1.5 , 0.2, 0.528, 0.12),
    ( -1.35, 0.2, 0.921, 0.16),
    ( -1.14, 0.5, 1.065, 0.189),   # Theta=1/4
    ( -1.0 , 0.3, 1.13,  0.182),
    ( -0.94, 0.3, 1.67,  0.181),
    ( -0.93, 0.3, 1.26,  0.180),
    ( -0.75, 0.2, 0.529, 0.187),   # Theta=1/3
]

# Susceptibility data: mu, B, gamma_nu, T_c
SUSCEPTIBILITY_PARAMS = [
    ( -1.5 , 0.1, 1.5,   0.12),
    ( -1.35, 0.1, 1.6,   0.16),
    ( -1.14, 0.1, 1.763, 0.189),
    ( -1.0 , 0.1, 1.8,   0.182),
    ( -0.94, 0.1, 1.9,   0.181),
    ( -0.93, 0.1, 1.85,  0.180),
    ( -0.75, 0.1, 1.540, 0.187),
]

# Phase diagram points: (T, Theta, mu, boundary_type)
# Special points
PHASE_DIAGRAM_POINTS = [
    # Tricritical points
    (0.07, 0.21, -1.62, "tricritical"),   # P_tr^A
    (0.189, 0.25, -1.14, "tricritical"),  # P_tr^B
    (0.185, 0.327, -0.78, "tricritical"), # P_tr^D
    # Eutectic point
    (0.158, 0.292, -0.85, "eutectic"),    # P_eut
    # Critical point
    (0.187, 0.33333, -0.75, "critical"),  # P_c^D

    # Region A coexistence boundaries (left branch with lattice gas, right branch with p(2x2))
    (0.01, 0.15, -1.8, "coexistence_left"),
    (0.04, 0.18, -1.7, "coexistence_left"),
    (0.07, 0.21, -1.62, "coexistence_left"),
    (0.01, 0.25, -1.62, "coexistence_right"),
    (0.04, 0.23, -1.62, "coexistence_right"),

    # Critical line from P_tr^A to P_tr^B (boundary between p(2x2) and disordered)
    (0.10, 0.22, -1.4, "critical"),
    (0.14, 0.235, -1.25, "critical"),

    # Region C coexistence: left boundary (contact with p(2x2)) and right boundary (contact with sqrt3)
    (0.01, 0.25, -1.14, "coexistence_left"),
    (0.08, 0.27, -1.0, "coexistence_left"),
    (0.12, 0.282, -0.9, "coexistence_left"),
    (0.01, 0.33, -0.75, "coexistence_right"),
    (0.08, 0.31, -0.80, "coexistence_right"),
    (0.12, 0.30, -0.83, "coexistence_right"),

    # Region E1 (coexistence of p(2x2) and disordered) boundaries
    (0.16, 0.28, -0.82, "coexistence_left"),
    (0.18, 0.26, -0.95, "coexistence_left"),
    (0.189, 0.20, -1.2, "coexistence_right"),
    (0.18, 0.15, -1.3, "coexistence_right"),

    # Region E2 (coexistence of sqrt3 and disordered) boundaries
    (0.16, 0.31, -0.78, "coexistence_right"),
    (0.18, 0.315, -0.77, "coexistence_right"),
    # Critical line from P_tr^D to P_c^D
    (0.186, 0.33, -0.76, "critical"),
    (0.1865, 0.3316, -0.755, "critical"),
]

# =================== File writers ===================

def write_specific_heat_maxima(output_path):
    with open(output_path, 'w', newline='') as f:
        w = csv.writer(f)
        w.writerow(['N','mu','T_c','c_max'])
        for mu, A, alpha, T_c in SPECIFIC_HEAT_PARAMS:
            for N in N_VALUES:
                c_max = A * (N ** alpha)
                w.writerow([N, mu, T_c, round(c_max, 4)])

def write_susceptibility_maxima(output_path):
    with open(output_path, 'w', newline='') as f:
        w = csv.writer(f)
        w.writerow(['N','mu','T_c','chi_max'])
        for mu, B, gamma, T_c in SUSCEPTIBILITY_PARAMS:
            for N in N_VALUES:
                chi_max = B * (N ** gamma)
                w.writerow([N, mu, T_c, round(chi_max, 4)])

def write_phase_diagram_points(output_path):
    with open(output_path, 'w', newline='') as f:
        w = csv.writer(f)
        w.writerow(['T','Theta','mu','boundary_type'])
        for T, Theta, mu, btype in PHASE_DIAGRAM_POINTS:
            w.writerow([T, Theta, mu, btype])

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: generate_csv.py <specific_heat|susceptibility|phase_diagram> <output_path>")
        sys.exit(1)
    kind = sys.argv[1]
    out = sys.argv[2]
    if kind == 'specific_heat':
        write_specific_heat_maxima(out)
    elif kind == 'susceptibility':
        write_susceptibility_maxima(out)
    elif kind == 'phase_diagram':
        write_phase_diagram_points(out)
    else:
        print(f"Unknown kind: {kind}")
        sys.exit(1)
