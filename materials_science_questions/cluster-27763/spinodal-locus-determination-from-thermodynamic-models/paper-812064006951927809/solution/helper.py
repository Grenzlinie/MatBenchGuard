import csv
import math

def vinet_pressure(V, V0, B0, B0p):
    if V <= 0 or V0 <= 0:
        return 0.0
    x = (V / V0) ** (1.0/3.0)
    eta = 1.5 * (B0p - 1.0)
    if x <= 0:
        return 0.0
    return 3.0 * B0 * ( (1.0 - x) / (x**2) ) * math.exp(eta * (1.0 - x))

def write_eos_parameters(path):
    data = [
        ["fcc", 16.58, 75.80, 4.61, 24.22, -10.87],
        ["bcc", 17.10, 63.25, 4.72, 26.08, -10.71],
        ["hcp", 16.74, 70.62, 4.44, 25.12, -11.09],
        ["sc", 20.25, 56.50, 4.56, 30.07, -8.64],
        ["spinel", 27.71, 37.70, 4.43, 41.60, -5.93],
        ["gra-e1", 24.67, 43.77, 4.25, 37.64, -7.16],
        ["gra-e", 20.68, 57.78, 3.74, 32.32, -9.92],
    ]
    with open(path, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["lattice", "V0_ang3", "B0_GPa", "B0_prime", "Vsp_ang3", "psp_GPa"])
        for row in data:
            w.writerow(row)

def write_elastic_constants_sc(path):
    # SC EOS parameters: V0=20.25, B0=56.5, B0p=4.56
    # Rows: volume_A3, pressure_GPa, C11_GPa, C12_GPa, C44_GPa, B_GPa, C11_minus_C12_abs_GPa
    sc_rows = [
        (18.0, 66.5, 51.5, -18.0, 56.5, 15.0),          # below eq vol, p>0
        (20.25, 66.5, 51.5, -15.0, 56.5, 15.0),         # V0, p=0
        (27.0,  14.666667, 22.666667, -10.0, 20.0, 8.0), # ~unstable
        (35.0,  -5.0, 15.0, -2.0, 1.666667, 20.0),      # intermediate
        (43.67, -23.333333, -3.333333, 5.0, -10.0, 20.0) # Vexp
    ]
    with open(path, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["volume_A3", "pressure_GPa", "C11_GPa", "C12_GPa", "C44_GPa", "B_GPa", "C11_minus_C12_abs_GPa"])
        for vol, c11, c12, c44, B, c_diff in sc_rows:
            p = vinet_pressure(vol, 20.25, 56.5, 4.56)
            w.writerow([vol, round(p, 4), c11, c12, c44, B, c_diff])

def write_elastic_constants_grae1(path):
    # From Table 3: volume, p, C11, C12, C33, C44, C13
    grae1_rows = [
        (20.81, 10.627, 80.3, 141.5, 154.2, -9.1, 38.8),
        (22.43, 5.097, 73.0, 102.5, 139.4, -15.9, 22.0),
        (24.67, 0.0, 74.2, 53.7, 137.7, -19.8, -2.5),
        (26.85, -3.080, 57.3, 25.9, 98.3, -15.0, 0.5),
        (28.76, -4.813, 54.5, 15.8, 68.5, -10.4, -1.8),
        (37.34, -7.161, 20.4, 8.1, -19.1, 0.6, 0.2),
    ]
    with open(path, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["volume_A3", "pressure_GPa", "C11_GPa", "C12_GPa", "C33_GPa", "C44_GPa", "C13_GPa"])
        for row in grae1_rows:
            w.writerow(row)

def write_critical_points(path):
    # From Table 4, Laplacian values converted from 10^{-3} scale to e/bohr^5
    rows = [
        # lattice, cp_type, x, y, z, rho, laplacian
        ("fcc", "BP", 0.0, 0.25, 0.25, 2.96, -0.49e-3),
        ("fcc", "RP", 0.282, 0.282, 0.282, 2.82, float("nan")),
        ("fcc", "CP", 0.25, 0.25, 0.25, 2.81, float("nan")),
        ("fcc", "CP", 0.0, 0.0, 0.5, 1.76, float("nan")),
        ("sc", "BP", 0.0, 0.0, 0.5, 3.09, -12.3e-3),
        ("sc", "RP", 0.0, 0.5, 0.5, 1.74, float("nan")),
        ("sc", "CP", 0.5, 0.5, 0.5, 0.815, float("nan")),
        ("spinel", "BP", 0.125, 0.125, 0.525, 3.55, -4.54e-3),
        ("spinel", "RP", 0.341, 0.341, 0.341, 3.33, float("nan")),
        ("spinel", "RP", 0.0, 0.25, 0.25, 0.193, float("nan")),
        ("spinel", "CP", 0.375, 0.375, 0.375, 3.25, float("nan")),
        ("spinel", "CP", 0.125, 0.125, 0.125, 0.0489, float("nan")),
        ("gra-e1", "BP", 0.0, 0.5, 0.5, 3.62, -22.3e-3),
        ("gra-e1", "BP", 1.0/3.0, 2.0/3.0, 0.0, 2.85, -7.53e-3),
        ("gra-e1", "RP", 0.5, 0.5, 0.0, 1.92, float("nan")),
        ("gra-e1", "RP", 0.0, 0.0, 0.5, 0.262, float("nan")),
        ("gra-e1", "CP", 0.0, 0.0, 0.0, 0.115, float("nan")),
        ("gra-a", "BP", 1.0/6.0, 1.0/3.0, 1.0/3.0, 3.86, -26.3e-3),
        ("gra-a", "BP", 0.0, 0.0, 0.5, 3.26, -8.19e-3),
        ("gra-a", "RP", 1.0/3.0, 1.0/6.0, 1.0/6.0, 1.11, float("nan")),
        ("gra-a", "CP", 2.0/3.0, 1.0/3.0, 1.0/3.0, 0.349, float("nan")),
    ]
    with open(path, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["lattice", "cp_type", "x", "y", "z", "rho_e_per_bohr3", "laplacian_e_per_bohr5"])
        for row in rows:
            w.writerow(row)
