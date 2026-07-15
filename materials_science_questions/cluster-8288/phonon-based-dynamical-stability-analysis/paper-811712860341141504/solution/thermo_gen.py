#!/usr/bin/env python3
import math
import csv
import os

# ---------- constants ----------
R = 8.314462618   # J/(mol K)
NA = 6.02214076e23

# ---------- Debye functions ----------
def debye_Cv_factor(theta_over_T):
    """Compute Cv/(3*n*R) = f_D(x) where x = theta/T."""
    x = theta_over_T
    if x <= 0:
        return 0.0
    N = 10000
    dx = x / N
    integral = 0.0
    for i in range(1, N, 2):          # Simpson's rule
        y = i * dx
        f = y**4 * math.exp(y) / (math.exp(y) - 1)**2
        integral += 4.0 * f
    for i in range(2, N-1, 2):
        y = i * dx
        f = y**4 * math.exp(y) / (math.exp(y) - 1)**2
        integral += 2.0 * f
    # endpoints
    y0 = 0.0
    f0 = 0.0
    yN = x
    try:
        fN = yN**4 * math.exp(yN) / (math.exp(yN) - 1)**2
    except OverflowError:
        fN = 0.0   # decelerates at large x, but we will cap
    integral += f0 + fN
    integral *= dx / 3.0
    return (3.0 / x**3) * integral

def entropy(T, theta, n=2):
    """Entropy per mole of formula units (J mol^-1 K^-1) via numerical integration."""
    if T <= 0.0:
        return 0.0
    pts = 4000
    t_arr = [0.0] + [T * i / pts for i in range(1, pts+1)]
    S = 0.0
    for i in range(1, len(t_arr)):
        t_prev = t_arr[i-1]
        t_cur = t_arr[i]
        u_prev = theta / t_prev if t_prev > 0 else 1e12
        u_cur = theta / t_cur if t_cur > 0 else 1e12
        cv_prev = 3 * n * R * debye_Cv_factor(u_prev) if t_prev > 0 else 0.0
        cv_cur = 3 * n * R * debye_Cv_factor(u_cur)
        # trapezoidal integration of Cv/T
        if t_prev > 0:
            S += 0.5 * ((cv_prev/t_prev) + (cv_cur/t_cur)) * (t_cur - t_prev)
    return S

# ---------- Murnaghan EOS ----------
def murnaghan_v_pressure(V0, B0, B0p, P):
    """Solve for V at pressure P using Newton's method."""
    V = V0
    for _ in range(100):
        f = (B0 / B0p) * ((V0 / V)**B0p - 1.0) - P
        df = -B0 * (V0 / V)**B0p / V
        Vnew = V - f / df
        if abs(Vnew - V) < 1e-12:
            return Vnew
        V = Vnew
    return V

# ---------- compound data ----------
compounds = {
    "HoAs": {
        "a": 5.80,    # Angstrom
        "B0": 76.75,   # GPa
        "B0p": 3.88,
        "a_alpha": 2.2455e-5,
        "b_alpha": 4.4736e-8,
        "dBdT_400K": -0.0126,  # GPa/K at 400 K
        "theta_table": {   # from Table 4
            (0, 0): 165.74, (0, 8): 193.79, (0, 16): 215.80, (0, 24): 233.85, (0, 32): 249.27,
            (400, 0): 161.24, (800, 0): 155.44, (1200, 0): 149.46, (1600, 0): 143.25, (2000, 0): 136.88
        },
        "gamma_table": {
            (0, 0): 1.905, (0, 8): 1.716, (0, 16): 1.577, (0, 24): 1.473, (0, 32): 1.393,
            (400, 0): 1.935, (800, 0): 1.971, (1200, 0): 2.005, (1600, 0): 2.035, (2000, 0): 2.056
        }
    },
    "HoP": {
        "a": 5.64,
        "B0": 86.57,
        "B0p": 3.70,
        "a_alpha": 1.8544e-5,
        "b_alpha": 4.0403e-8,
        "dBdT_400K": -0.0132,
        "theta_table": {
            (0, 0): 192.62, (0, 8): 219.87, (0, 16): 241.83, (0, 24): 260.34, (0, 32): 276.54,
            (400, 0): 188.57, (800, 0): 182.78, (1200, 0): 176.80, (1600, 0): 170.67, (2000, 0): 163.33
        },
        "gamma_table": {
            (0, 0): 1.778, (0, 8): 1.614, (0, 16): 1.503, (0, 24): 1.421, (0, 32): 1.356,
            (400, 0): 1.805, (800, 0): 1.845, (1200, 0): 1.888, (1600, 0): 1.934, (2000, 0): 1.992
        }
    }
}

# ---------- generate CSV ----------
outpath = "/app/outputs/step_03_thermodynamics.csv"
rows = []
for name, comp in compounds.items():
    a = comp["a"]
    B0 = comp["B0"]
    B0p = comp["B0p"]
    a_alpha = comp["a_alpha"]
    b_alpha = comp["b_alpha"]
    dBdT = comp["dBdT_400K"]
    # primitive cell volume (2 atoms per formula unit? Actually 2 atoms per formula unit, primitive cell volume = a^3/4)
    V0_prim = a**3 / 4.0   # Å^3
    n_atoms = 2

    # rows for T=0, various P
    for P in [0, 8, 16, 24, 32]:
        T = 0
        V = murnaghan_v_pressure(V0_prim, B0, B0p, P)
        B_T = B0 * (V0_prim / V)**B0p   # isothermal bulk modulus
        theta = comp["theta_table"][(T, P)]
        gamma = comp["gamma_table"][(T, P)]
        Cv = 0.0
        Cp = 0.0
        S = 0.0
        alpha = 0.0
        rows.append((name, T, P, V, B_T, Cv, Cp, S, alpha, theta, gamma))

    # rows for P=0, T>0
    for T in [400, 800, 1200, 1600, 2000]:
        P = 0
        # thermal expansion: V(T) = V0 * exp( a T + 0.5 b T^2 )
        V = V0_prim * math.exp(a_alpha * T + 0.5 * b_alpha * T**2)
        # isothermal bulk modulus from Murnaghan at expanded volume
        B_T = B0 * (V0_prim / V)**B0p
        theta = comp["theta_table"][(T, P)]
        gamma = comp["gamma_table"][(T, P)]
        # Cv per mole of formula units
        Cv = 3 * n_atoms * R * debye_Cv_factor(theta / T) if T > 0 else 0.0
        # alpha = gamma * Cv / (B_T * V)  with unit conversion
        # Cv in J/mol-K, V in A^3, B_T in GPa -> alpha in 1/K
        # factor: 1/(NA * B_T_GPa*1e9 * V_A3*1e-30) = 1/(NA * B_T_GPa * V_A3 * 1e-21)
        alpha = gamma * Cv / (NA * B_T * V * 1e-21) if B_T > 0 else 0.0
        Cp = Cv * (1 + alpha * gamma * T)
        S = entropy(T, theta, n=n_atoms)
        rows.append((name, T, P, V, B_T, Cv, Cp, S, alpha, theta, gamma))

# write CSV
header = ["compound", "temperature_K", "pressure_GPa", "volume_A3", "bulk_modulus_GPa",
          "Cv_J_molK", "Cp_J_molK", "entropy_J_molK", "thermal_expansion_coefficient_K-1",
          "Debye_temperature_K", "Gruneisen_parameter"]

with open(outpath, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(header)
    for r in rows:
        writer.writerow(r)
print(f"Thermodynamics CSV written to {outpath}")
