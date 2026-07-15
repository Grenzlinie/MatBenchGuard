#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: thermodynamic_functions.csv ===
python3 <<EOFPY
import math, csv

R = 8.314463          # J mol⁻¹ K⁻¹
n_atom = 5.0          # atoms per formula unit (Na3ClO)
theta_D = 350.0       # Debye temperature (K)

def safe_debye_integral(T, theta):
    """Return ∫_0^{θ/T} x⁴ eˣ/(eˣ-1)² dx using a form that avoids overflow."""
    if T <= 0.0:
        return 0.0
    limit = theta / T
    # Integrate only up to min(limit, 50) because the integrand ∝ x⁴ e⁻ˣ decays rapidly.
    max_x = min(limit, 50.0)
    n = 20000                  # fine enough for stable midpoint integration
    dx = max_x / n
    integ = 0.0
    for i in range(n):
        x = (i + 0.5) * dx
        if x == 0.0:
            continue
        ex_neg = math.exp(-x)
        if 1.0 - ex_neg == 0.0:
            continue
        # stable form: x⁴ e⁻ˣ / (1 - e⁻ˣ)²
        term = (x**4) * ex_neg / ((1.0 - ex_neg)**2)
        integ += term * dx
    return integ

# Fine grid (0.1 K steps) for integration
t_fine = [i*0.1 for i in range(0, 6001)]   # 0 K to 600 K
C_V_fine = []
for T in t_fine:
    if T == 0.0:
        C_V_fine.append(0.0)
        continue
    I = safe_debye_integral(T, theta_D)
    C = n_atom * 9.0 * R * (T/theta_D)**3 * I
    C_V_fine.append(C)

# Integrate C_V/T → S and C_V → H using trapezoidal rule
S_fine = [0.0]
H_fine = [0.0]
dT = 0.1
for i in range(1, len(t_fine)):
    # S
    prev_s_integrand = C_V_fine[i-1]/t_fine[i-1] if t_fine[i-1] > 0 else 0.0
    curr_s_integrand = C_V_fine[i]/t_fine[i] if t_fine[i] > 0 else 0.0
    S_val = S_fine[-1] + 0.5*(prev_s_integrand + curr_s_integrand) * dT
    S_fine.append(S_val)
    # H
    H_val = H_fine[-1] + 0.5*(C_V_fine[i-1] + C_V_fine[i]) * dT
    H_fine.append(H_val)

# F = H - T*S
F_fine = [H_fine[i] - t_fine[i]*S_fine[i] for i in range(len(t_fine))]

# Downsample to 101 points (0, 6, 12, ..., 600 K)
temperatures = list(range(0, 601, 6))
rows = [['Temperature (K)', 'C_V (J/mol/K)', 'S (J/mol/K)', 'H (J/mol)', 'F (J/mol)']]
for T in temperatures:
    idx = int(round(T / 0.1))
    rows.append([
        f"{T:.0f}",
        f"{C_V_fine[idx]:.2f}",
        f"{S_fine[idx]:.2f}",
        f"{H_fine[idx]:.2f}",
        f"{F_fine[idx]:.2f}"
    ])

with open('$OUTDIR/thermodynamic_functions.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(rows)
print('Wrote thermodynamic_functions.csv')
EOFPY
