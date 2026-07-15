#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: critical_temperature.csv ===
cat > /solution/generate_csv.py << 'EOF'
import sys
import math

def f(x, Omega, beta):
    E2 = Omega**2 + x**2
    if E2 == 0.0:
        return 0.0
    E = math.sqrt(E2)
    z = beta * E
    emz = math.exp(-z)
    e2mz = emz * emz
    num = 1.0 - e2mz
    den = emz + 1.0 + e2mz
    return (x / E) * (num / den)

def g(x, Omega, beta):
    E2 = Omega**2 + x**2
    if E2 == 0.0:
        return 0.0
    E = math.sqrt(E2)
    z = beta * E
    emz = math.exp(-z)
    e2mz = emz * emz
    num = 1.0 - e2mz
    den = emz + 1.0 + e2mz
    return (Omega / E) * (num / den)

def h(x, Omega, beta):
    E2 = Omega**2 + x**2
    if E2 == 0.0:
        return 2.0 / 3.0
    E = math.sqrt(E2)
    z = beta * E
    emz = math.exp(-z)
    e2mz = emz * emz
    num = Omega**2 * emz + (Omega**2 + 2.0 * x**2) * (1.0 + e2mz) / 2.0
    den = E2 * (emz + 1.0 + e2mz)
    return num / den

def k(x, Omega, beta):
    E2 = Omega**2 + x**2
    if E2 == 0.0:
        return 2.0 / 3.0
    E = math.sqrt(E2)
    z = beta * E
    emz = math.exp(-z)
    e2mz = emz * emz
    num = x**2 * emz + (2.0 * Omega**2 + x**2) * (1.0 + e2mz) / 2.0
    den = E2 * (emz + 1.0 + e2mz)
    return num / den

def apply_op(mz, qz, func, power):
    A0 = 1.0 - qz
    A1 = (mz + qz) / 2.0
    A_1 = (-mz + qz) / 2.0
    total = 0.0
    for n1 in range(power + 1):
        for n_1 in range(power + 1 - n1):
            n0 = power - n1 - n_1
            coeff = math.factorial(power) / (math.factorial(n0) * math.factorial(n1) * math.factorial(n_1))
            val = coeff * (A0 ** n0) * (A1 ** n1) * (A_1 ** n_1)
            shift = n1 - n_1
            if val != 0.0:
                total += val * func(float(shift))
    return total

def solve_qc(Omega, beta):
    q = 0.5
    for _ in range(200):
        func_h = lambda x: h(x, Omega, beta)
        q_next = apply_op(0.0, q, func_h, 3)
        if abs(q_next - q) < 1e-12:
            return q_next
        q = q_next
    return q

def compute_K(Omega, beta):
    qc = solve_qc(Omega, beta)
    val_p = apply_op(0.0, qc, lambda x: f(x + 1.0, Omega, beta), 2)
    val_m = apply_op(0.0, qc, lambda x: f(x - 1.0, Omega, beta), 2)
    return (val_p - val_m) / 2.0

def find_Tc(Omega, T_min=0.001, T_max=5.0):
    def target(T):
        beta = 1.0 / T
        K = compute_K(Omega, beta)
        return 3.0 * K - 1.0
    f_min = target(T_min)
    f_max = target(T_max)
    if f_min * f_max > 0.0:
        if f_min > 0.0:
            return 0.0
        else:
            return None
    for _ in range(60):
        T_mid = (T_min + T_max) / 2.0
        f_mid = target(T_mid)
        if abs(f_mid) < 1e-10:
            return T_mid
        if f_min * f_mid < 0.0:
            T_max = T_mid
        else:
            T_min = T_mid
    return (T_min + T_max) / 2.0

def solve_full(Omega, T):
    beta = 1.0 / T
    mz = 0.5 if T < 0.5 else 0.0
    qz = 0.5
    func_f = lambda x: f(x, Omega, beta)
    func_g = lambda x: g(x, Omega, beta)
    func_h = lambda x: h(x, Omega, beta)
    func_k = lambda x: k(x, Omega, beta)
    for _ in range(200):
        new_mz = apply_op(mz, qz, func_f, 3)
        new_qz = apply_op(mz, qz, func_h, 3)
        if abs(new_mz - mz) < 1e-12 and abs(new_qz - qz) < 1e-12:
            mz, qz = new_mz, new_qz
            break
        mz, qz = new_mz, new_qz
    else:
        mz = 0.0
        qz = solve_qc(Omega, beta)
    mx = apply_op(mz, qz, func_g, 3)
    qx = apply_op(mz, qz, func_k, 3)
    return mz, mx, qz, qx

mode = sys.argv[1]

if mode == "critical":
    print("omega_over_J,kBTc_over_J")
    for i in range(51):
        Omega = i * 0.05
        Tc = find_Tc(Omega)
        if Tc is None:
            Tc = 0.0
        print(f"{Omega:.6f},{Tc:.6f}")

elif mode == "temperature":
    Omega = 1.5
    print("kBT_over_J,mz,mx,qz,qx")
    Tc = find_Tc(Omega)
    T_stop = max(Tc + 0.1, 1.0)
    N = 100
    for i in range(N + 1):
        T = 0.01 + i * (T_stop - 0.01) / N
        mz, mx, qz, qx = solve_full(Omega, T)
        print(f"{T:.6f},{mz:.6f},{mx:.6f},{qz:.6f},{qx:.6f}")

elif mode == "field":
    T = 0.05
    print("omega_over_J,mz,mx")
    for i in range(51):
        Omega = i * 0.05
        if Omega == 0.0:
            mz = 1.0
            mx = 0.0
        else:
            mz, mx, _, _ = solve_full(Omega, T)
        print(f"{Omega:.6f},{mz:.6f},{mx:.6f}")

else:
    print("Unknown mode", file=sys.stderr)
    sys.exit(1)
EOF
python3 /solution/generate_csv.py critical > "$OUTDIR/critical_temperature.csv"

# === solve block: temperature_dependence_omega1.5.csv ===
python3 /solution/generate_csv.py temperature > "$OUTDIR/temperature_dependence_omega1.5.csv"

# === solve block: field_dependence_T0.05.csv ===
python3 /solution/generate_csv.py field > "$OUTDIR/field_dependence_T0.05.csv"
