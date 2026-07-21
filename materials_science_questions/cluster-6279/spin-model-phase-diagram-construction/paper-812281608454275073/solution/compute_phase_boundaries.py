import csv
import math

# Parameters (dimensionless)
A_gamma = 0.6
A3 = 0.6
A5 = 0.8
A8 = 1.5
Q_L_sq = 0.2
Q = 0.5
c0 = 3.0 + math.sqrt(6.0)  # 3+√6 ≈ 5.449

# Mapping functions

def D0_from_B2(B2):
    return 2.0 * B2**2 * (B2 - Q_L_sq)

def D_l_from_B2(B2, Q_l_sq):
    diff = B2 - Q_l_sq
    return diff * diff * (Q_l_sq + 2.0 * (B2 - Q_L_sq))

# Thermodynamic potentials (minimized)

def phi_IC(A):
    t = 1.0 + 12.0 * A_gamma**2 * A
    return -(1.0 / (216.0 * A_gamma**4)) * (t**1.5 - (1.0 + 18.0 * A_gamma**2 * A))

def phi_0_1(A, D0):
    t = 1.0 + 10.8 * A_gamma**2 * (A - D0)
    return -(1.0 / (0.54 * 216.0 * A_gamma**4)) * (t**1.5 - (1.0 + 16.2 * A_gamma**2 * (A - D0)))

def phi_1_3(A, D3):
    # Quartic potential (sextic terms cancel because A_gamma = A3)
    if A >= D3:
        return -0.25 * (A - D3)**2
    return 0.0

def phi_m_l(A, D_l, l, A_l):
    t = 1.0 + 12.0 * A_gamma**2 * (A - D_l)
    first = -(1.0 / (216.0 * A_gamma**4)) * (t**1.5 - (1.0 + 18.0 * A_gamma**2 * (A - D_l)))
    inner = (A_l / (6.0 * A_gamma**2)) * (math.sqrt(t) - 1.0)
    second = -(1.0 / (2.0 * A_l)) * (inner**l)
    return first + second

# Bisection solver

def solve_root(f, a, b, max_iter=60):
    fa = f(a)
    fb = f(b)
    for _ in range(max_iter):
        m = (a + b) / 2.0
        fm = f(m)
        if fm == 0.0 or (b - a) < 1e-12:
            return m
        if fa * fm < 0.0:
            b = m
            fb = fm
        else:
            a = m
            fa = fm
    return (a + b) / 2.0

# Boundary solvers

def IC_C01_boundary(D0):
    def f(A):
        return phi_IC(A) - phi_0_1(A, D0)
    # bracket: A in [max(0, D0-0.01), D0+0.2]
    a = max(0.0, D0 - 0.01)
    b = D0 + 0.2
    return solve_root(f, a, b)

def IC_C13_boundary(D3):
    def f(A):
        return phi_IC(A) - phi_1_3(A, D3)
    a = max(0.0, D3 - 0.01)
    b = D3 + 0.2
    return solve_root(f, a, b)

def IC_C2l_from_Dl(D_l, l, A_l):
    # Invert weak-anisotropy IC–C_{m/l} boundary: D_l = f^{l-1}
    exponent = l - 1
    f_val = D_l ** (1.0 / exponent) if D_l > 0 else 0.0
    x = 1.0 + (6.0 * A_gamma**2 / A_l) * f_val
    A = (x**2 - 1.0) / (12.0 * A_gamma**2)
    return max(A, 0.0)

def C25_C13_boundary(D3, D5):
    # equality of weak-anisotropy terms: D3 - f3(A) = D5 - f5(A)
    def eq(A):
        t = 1.0 + 12.0 * A_gamma**2 * A
        x = math.sqrt(t)
        f3 = ((A3 / (6.0 * A_gamma**2)) * (x - 1.0)) ** 2
        f5 = ((A5 / (6.0 * A_gamma**2)) * (x - 1.0)) ** 4
        return D3 - f3 - (D5 - f5)
    a = 0.0
    b = 0.5
    return solve_root(eq, a, b)

def C13_C01_boundary(D0, D3):
    # small‑A quadratic (11), with (A_γ²-A3²)=0
    def eq(A):
        term = 0.9 * c0 * A_gamma**2 * (A - D0)**2
        return term - A + c0 * D0 - (c0 - 1.0) * D3
    a = max(0.0, D0, D3) - 0.01
    b = max(D0, D3) + 0.5
    return solve_root(eq, a, b)

# Generate boundary points

def main():
    # Grid of B²
    B2_vals = [0.201 + i * (0.35 - 0.201) / 299 for i in range(300)]  # ~0.201..0.35
    
    # Compute D0, D3, D5 for each B²
    points_ic01 = []
    points_ic13 = []
    points_ic25 = []
    points_c25c13 = []
    points_c13c01 = []
    
    Q_l_sq_3 = (1.0 / 3.0 / 0.5) ** 2   # 4/9 ≈ 0.4444
    Q_l_sq_5 = (2.0 / 5.0 / 0.5) ** 2   # 0.64
    
    for B2 in B2_vals:
        D0 = D0_from_B2(B2)
        D3 = D_l_from_B2(B2, Q_l_sq_3)
        D5 = D_l_from_B2(B2, Q_l_sq_5)
        
        # IC–C0/1
        try:
            A = IC_C01_boundary(D0)
            if 0 <= A <= 0.5:
                points_ic01.append((D0, A))
        except Exception:
            pass
        
        # IC–C1/3
        try:
            A = IC_C13_boundary(D3)
            if 0 <= A <= 0.5:
                points_ic13.append((D0, A))
        except Exception:
            pass
        
        # IC–C2/5 (weak anisotropy)
        try:
            if D5 > 0:
                A = IC_C2l_from_Dl(D5, 5, A5)
                if 0 <= A <= 0.5:
                    points_ic25.append((D0, A))
        except Exception:
            pass
        
        # C2/5–C1/3
        try:
            A = C25_C13_boundary(D3, D5)
            if 0.0 <= A <= 0.5:
                points_c25c13.append((D0, A))
        except Exception:
            pass
        
        # C1/3–C0/1 (small‑A)
        try:
            A = C13_C01_boundary(D0, D3)
            if 0.0 <= A <= 0.5:
                points_c13c01.append((D0, A))
        except Exception:
            pass
    
    # Trivial boundaries: C–IC (A=0) and C–C0/1 (A=D0)
    points_c_ic = [(d, 0.0) for d in [0.0, 0.005, 0.01, 0.015, 0.02, 0.025, 0.03] if d >= 0]
    points_c_c01 = [(d, d) for d in [0.0, 0.005, 0.01, 0.015, 0.02, 0.025, 0.03] if d >= 0]
    
    # Write CSV
    with open("/app/outputs/phase_boundaries_d0_a.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["phase_pair", "D0", "A"])
        
        for D0, A in points_ic01:
            writer.writerow(["IC-C0/1", f"{D0:.6f}", f"{A:.6f}"])
        for D0, A in points_ic13:
            writer.writerow(["IC-C1/3", f"{D0:.6f}", f"{A:.6f}"])
        for D0, A in points_ic25:
            writer.writerow(["IC-C2/5", f"{D0:.6f}", f"{A:.6f}"])
        for D0, A in points_c25c13:
            writer.writerow(["C2/5-C1/3", f"{D0:.6f}", f"{A:.6f}"])
        for D0, A in points_c13c01:
            writer.writerow(["C1/3-C0/1", f"{D0:.6f}", f"{A:.6f}"])
        for D0, A in points_c_ic:
            writer.writerow(["C-IC", f"{D0:.6f}", f"{A:.6f}"])
        for D0, A in points_c_c01:
            writer.writerow(["C-C0/1", f"{D0:.6f}", f"{A:.6f}"])

if __name__ == "__main__":
    main()