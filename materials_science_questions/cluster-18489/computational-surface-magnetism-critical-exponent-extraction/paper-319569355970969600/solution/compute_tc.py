#!/usr/bin/env python3
import sys
import numpy as np

def det_A(T, geometry, Sc, Ss, J1_div_J, delta_s):
    J = 1.0
    J1 = J1_div_J * J
    Js = J * (1.0 + delta_s)
    k = 1.0
    if geometry == 'nanowire':
        A = np.zeros((4, 4))
        # row 0 (type 1)
        A[0, 0] = (3 * Sc * k * T) / (Sc + 1) - 2 * J
        A[0, 1] = -6 * J
        # row 1 (type 2)
        A[1, 0] = -J
        A[1, 1] = (3 * Sc * k * T) / (Sc + 1) - 4 * J
        A[1, 2] = -2 * J1
        A[1, 3] = -J1
        # row 2 (type 3)
        A[2, 1] = -2 * J1
        A[2, 2] = (3 * Ss * k * T) / (Ss + 1) - 2 * Js
        A[2, 3] = -2 * Js
        # row 3 (type 4)
        A[3, 1] = -J1
        A[3, 2] = -2 * Js
        A[3, 3] = (3 * Ss * k * T) / (Ss + 1) - 2 * Js
    else:  # nanotube
        A = np.zeros((3, 3))
        # row 0 (type 2)
        A[0, 0] = (3 * Sc * k * T) / (Sc + 1) - 4 * J
        A[0, 1] = -2 * J1
        A[0, 2] = -J1
        # row 1 (type 3)
        A[1, 0] = -2 * J1
        A[1, 1] = (3 * Ss * k * T) / (Ss + 1) - 2 * Js
        A[1, 2] = -2 * Js
        # row 2 (type 4)
        A[2, 0] = -J1
        A[2, 1] = -2 * Js
        A[2, 2] = (3 * Ss * k * T) / (Ss + 1) - 2 * Js
    return np.linalg.det(A)

def find_Tc(geometry, Sc, Ss, J1_div_J, delta_s, tol=1e-9):
    f = lambda T: det_A(T, geometry, Sc, Ss, J1_div_J, delta_s)
    T_low = 0.0
    f_low = f(T_low)
    T_high = 1.0
    for _ in range(50):
        if f_low * f(T_high) < 0:
            break
        T_high *= 2
    else:
        raise ValueError(f"No sign change found for {geometry}, Sc={Sc}, Ss={Ss}, J1/J={J1_div_J}, delta_s={delta_s}")
    # bisection
    for _ in range(100):
        T_mid = (T_low + T_high) / 2
        f_mid = f(T_mid)
        if f_mid == 0 or (T_high - T_low) / 2 < tol:
            return T_mid
        if f_low * f_mid < 0:
            T_high = T_mid
        else:
            T_low = T_mid
            f_low = f_mid
    return (T_low + T_high) / 2

def main():
    if len(sys.argv) != 2:
        print("Usage: compute_tc.py <output_csv>")
        sys.exit(1)
    output = sys.argv[1]
    geometries = ["nanowire", "nanotube"]
    param_sets = [
        (0.5, 1.0, 1.0),   # Sc, Ss, J1_div_J
        (0.5, 0.5, 1.0),
        (0.5, 1.0, 1.5),
    ]
    delta_values = [0.0, 0.5, 1.0]
    rows = []
    for Sc, Ss, J1_div in param_sets:
        for delta in delta_values:
            for geo in geometries:
                Tc = find_Tc(geo, Sc, Ss, J1_div, delta)
                rows.append((geo, Sc, Ss, J1_div, delta, Tc))
    with open(output, 'w') as f:
        f.write("geometry,Sc,Ss,J1_div_J,delta_s,Tc\n")
        for geo, Sc, Ss, J1_div, delta, Tc in rows:
            f.write(f"{geo},{Sc},{Ss},{J1_div},{delta},{Tc:.6f}\n")

if __name__ == "__main__":
    main()