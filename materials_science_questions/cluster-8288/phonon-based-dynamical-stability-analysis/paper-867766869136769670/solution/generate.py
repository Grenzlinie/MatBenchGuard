#!/usr/bin/env python3
"""Hidden oracle: write synthetic transport artifacts for 2D Na."""
import sys
import json
import csv
import math

def write_resistivity_csv():
    # Paper's fitted parameters
    A = 2.9e-8       # K^-4
    B = 3.3e-3       # K^-1
    rho_300 = 2.0    # µΩ·cm (plausible absolute value)

    # Generate temperature points from 5 K to 300 K, with finer spacing near crossover
    temps = list(range(10, 51, 2)) + list(range(55, 101, 5)) + list(range(110, 301, 10))
    rows = []
    for T in temps:
        # Low‑T regime: ρ/ρ₃₀₀ = A·T⁴
        # High‑T regime: ρ/ρ₃₀₀ = B·T
        # Use a smooth transition near 50 K to avoid a sharp kink
        T_cross = 50.0
        if T <= T_cross:
            rho_norm = A * T**4
        else:
            rho_norm = B * T
        # At the exact crossover, both formulas would give similar value; no special handling needed.
        rho_abs = rho_norm * rho_300
        rows.append([T, round(rho_abs, 6), round(rho_norm, 10)])

    with open('/app/outputs/resistivity_temperature.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['T_K', 'rho_abs_microOhm_cm', 'rho_normalized'])
        writer.writerows(rows)

def write_fitted_parameters():
    params = {
        "A_K_minus4": 2.9e-8,
        "B_K_minus1": 3.3e-3,
        "Theta_BG_K": 50.0
    }
    with open('/app/outputs/fitted_parameters.json', 'w') as f:
        json.dump(params, f, indent=2)

def write_lorenz_number():
    lorenz = 2.41e-8
    with open('/app/outputs/lorenz_number_300K.txt', 'w') as f:
        f.write(f"{lorenz}\n")

def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: generate.py <output_basename>")
    target = sys.argv[1]
    if target == 'resistivity_temperature.csv':
        write_resistivity_csv()
    elif target == 'fitted_parameters.json':
        write_fitted_parameters()
    elif target == 'lorenz_number_300K.txt':
        write_lorenz_number()
    else:
        sys.exit(f"Unknown target: {target}")

if __name__ == '__main__':
    main()
