import math
import csv

J = 1.0
Omega0 = 0.05
Omega1 = 3.65
z = 4

def f(x, T):
    if T <= 0:
        T = 1e-10
    beta = 1.0 / T
    a = math.sqrt(Omega0**2 + x**2)
    if a == 0:
        return 0.0
    return 0.5 * x / a * math.tanh(0.5 * beta * a)

def g(x, T):
    if T <= 0:
        T = 1e-10
    beta = 1.0 / T
    a = math.sqrt(Omega0**2 + x**2)
    if a == 0:
        return 0.0
    return 0.5 * Omega0 / a * math.tanh(0.5 * beta * a)

def F(x, T):
    if T <= 0:
        T = 1e-10
    beta = 1.0 / T
    a = math.sqrt(Omega1**2 + x**2)
    if a == 0:
        return 0.0
    denom = 1.0 + 2.0 * math.cosh(beta * a)
    if denom == 0:
        return 0.0
    return x / a * (2.0 * math.sinh(beta * a) / denom)

def G(x, T):
    if T <= 0:
        T = 1e-10
    beta = 1.0 / T
    a = math.sqrt(Omega1**2 + x**2)
    if a == 0:
        return 0.0
    denom = 1.0 + 2.0 * math.cosh(beta * a)
    if denom == 0:
        return 0.0
    return Omega1 / a * (2.0 * math.sinh(beta * a) / denom)

def H(x, T):
    if T <= 0:
        T = 1e-10
    beta = 1.0 / T
    a = math.sqrt(Omega1**2 + x**2)
    if a == 0:
        return 0.0
    cosh_ba = math.cosh(beta * a)
    denom = a**2 * (1.0 + 2.0 * cosh_ba)
    if denom == 0:
        return 0.0
    return (Omega1**2 + (Omega1**2 + 2.0 * x**2) * cosh_ba) / denom

def build_OA_coeffs(delta, qz, mz):
    shifts = {0.0: 1.0 - qz}
    coeff_up = 0.25 * (qz - mz)
    coeff_dn = 0.25 * (qz + mz)
    # e^{J(1+delta)} and e^{-J(1+delta)}
    d_plus = J * (1.0 + delta)
    d_minus = -J * (1.0 + delta)
    # e^{J(1-delta)} and e^{-J(1-delta)}
    d_plus2 = J * (1.0 - delta)
    d_minus2 = -J * (1.0 - delta)
    for shift, c in [(d_plus, coeff_up), (d_minus, coeff_dn),
                     (d_plus2, coeff_up), (d_minus2, coeff_dn)]:
        shifts[shift] = shifts.get(shift, 0.0) + c
    return {k: v for k, v in shifts.items() if abs(v) > 1e-15}

def build_OB_coeffs(delta, sigmaz):
    shifts = {}
    coeff_up = 0.25 - 0.5 * sigmaz
    coeff_dn = 0.25 + 0.5 * sigmaz
    d_plus = (J / 2.0) * (1.0 + delta)
    d_minus = -(J / 2.0) * (1.0 + delta)
    d_plus2 = (J / 2.0) * (1.0 - delta)
    d_minus2 = -(J / 2.0) * (1.0 - delta)
    for shift, c in [(d_plus, coeff_up), (d_minus, coeff_dn),
                     (d_plus2, coeff_up), (d_minus2, coeff_dn)]:
        shifts[shift] = shifts.get(shift, 0.0) + c
    return {k: v for k, v in shifts.items() if abs(v) > 1e-15}

def apply_op_z(coeffs_by_shift, z, func, T):
    items = list(coeffs_by_shift.items())
    total = 0.0
    def rec(depth, shift_sum, coeff_prod):
        if depth == z:
            nonlocal total
            total += coeff_prod * func(shift_sum, T)
        else:
            for shift, coeff in items:
                rec(depth + 1, shift_sum + shift, coeff_prod * coeff)
    rec(0, 0.0, 1.0)
    return total

def solve_self_consistent(delta, T, initial_guess, max_iter=1000, tol=1e-6, mix=0.1):
    sigmaz, sigmax, mz, mx, qz = initial_guess
    for _ in range(max_iter):
        OA = build_OA_coeffs(delta, qz, mz)
        OB = build_OB_coeffs(delta, sigmaz)
        new_sz = apply_op_z(OA, z, f, T)
        new_sx = apply_op_z(OA, z, g, T)
        new_mz = apply_op_z(OB, z, F, T)
        new_mx = apply_op_z(OB, z, G, T)
        new_qz = apply_op_z(OB, z, H, T)
        diff = max(abs(new_sz - sigmaz), abs(new_sx - sigmax),
                   abs(new_mz - mz), abs(new_mx - mx), abs(new_qz - qz))
        sigmaz += mix * (new_sz - sigmaz)
        sigmax += mix * (new_sx - sigmax)
        mz     += mix * (new_mz - mz)
        mx     += mix * (new_mx - mx)
        qz     += mix * (new_qz - qz)
        if diff < tol:
            break
    return sigmaz, sigmax, mz, mx, qz

def main():
    # === magnetization_curves.csv ===
    T_start = 0.01
    T_end   = 1.5
    T_step  = 0.01
    T_vals = [round(T_start + i * T_step, 6) for i in range(int((T_end - T_start) / T_step) + 1)]
    deltas = [0.0, 0.2, 0.4]

    rows1 = []
    for delta in deltas:
        guess = (0.5, 0.0, -1.0, 0.0, 1.0)
        prev = None
        for T in T_vals:
            if prev is not None:
                guess = prev
            sol = solve_self_consistent(delta, T, guess)
            sz, sx, mz, mx, qz = sol
            Mz = (mz + sz) / 2.0
            Mx = (mx + sx) / 2.0
            rows1.append([delta, T, Mz, Mx])
            prev = sol

    with open('/app/outputs/magnetization_curves.csv', 'w', newline='') as f:
        w = csv.writer(f)
        w.writerow(['δ', 'T', 'M_z', 'M_x'])
        for r in rows1:
            w.writerow(r)

    # === magnetization_vs_delta.csv ===
    T_fixed = [0.1, 0.35]
    delta_start = 0.0
    delta_end   = 0.5
    delta_step  = 0.02
    delta_vals = [round(delta_start + i * delta_step, 6) for i in range(int((delta_end - delta_start) / delta_step) + 1)]

    rows2 = []
    for T in T_fixed:
        guess = (0.5, 0.0, -1.0, 0.0, 1.0)
        prev = None
        for delta in delta_vals:
            if prev is not None:
                guess = prev
            sol = solve_self_consistent(delta, T, guess)
            sz, sx, mz, mx, qz = sol
            Mz = (mz + sz) / 2.0
            Mx = (mx + sx) / 2.0
            rows2.append([T, delta, Mz, Mx])
            prev = sol

    with open('/app/outputs/magnetization_vs_delta.csv', 'w', newline='') as f:
        w = csv.writer(f)
        w.writerow(['T', 'δ', 'M_z', 'M_x'])
        for r in rows2:
            w.writerow(r)

if __name__ == '__main__':
    main()
