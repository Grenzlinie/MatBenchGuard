#!/usr/bin/env python3
import csv
import math

def main():
    strain = [i * 0.001 for i in range(201)]  # 0 to 0.2, 201 points
    outfile = '/app/outputs/step_01_single_crystal_data.csv'

    # column order: orientation, initial_temp_K, thermal_boundary, strain, stress_MPa, temperature_K, xi_M, beta
    with open(outfile, 'w', newline='') as f:
        w = csv.writer(f)
        w.writerow(['orientation', 'initial_temp_K', 'thermal_boundary', 'strain', 'stress_MPa', 'temperature_K', 'xi_M', 'beta'])

        # ---------- Case 1: orientation=100, initial_temp=300, iso ----------
        for s in strain:
            if s < 0.02:
                stress = 500.0 * s / 0.02
            elif s < 0.12:
                stress = 500.0
            else:
                stress = 500.0 + 3000.0 * (s - 0.12)
            if s < 0.02:
                xi = 0.0
            elif s < 0.12:
                xi = 0.99 * (s - 0.02) / 0.10
            else:
                xi = 0.99
            beta = 0.0
            temp = 300.0
            w.writerow(['100', 300, 'iso', round(s, 6), round(stress, 2), round(temp, 2), round(min(1.0, xi), 4), round(beta, 5)])

        # ---------- Case 2: orientation=100, initial_temp=300, thermo ----------
        for s in strain:
            if s < 0.02:
                stress = 500.0 * s / 0.02
            else:
                stress = 500.0 + 800.0 * (s - 0.02)   # reaches ~644 at strain 0.2
            xi = 0.6 / (1.0 + math.exp(-30.0 * (s - 0.1)))
            beta = 0.04 * (s / 0.2) ** 0.6
            temp = 300.0 + 25.0 * (s / 0.2) ** 0.7
            w.writerow(['100', 300, 'thermo', round(s, 6), round(stress, 2), round(temp, 2), round(min(1.0, xi), 4), round(beta, 5)])

        # ---------- Case 3: orientation=100, initial_temp=350, iso ----------
        for s in strain:
            if s < 0.05:
                stress = 350.0 * s / 0.05
            elif s < 0.15:
                stress = 350.0
            else:
                stress = 350.0 + 1500.0 * (s - 0.15)   # ~425 at strain 0.2
            if s < 0.05:
                xi = 0.0
            elif s < 0.15:
                xi = 0.99 * (s - 0.05) / 0.10
            else:
                xi = 0.99
            beta = 0.02 * (s / 0.2) ** 0.8
            temp = 350.0
            w.writerow(['100', 350, 'iso', round(s, 6), round(stress, 2), round(temp, 2), round(min(1.0, xi), 4), round(beta, 5)])

        # ---------- Case 4: orientation=100, initial_temp=350, thermo ----------
        for s in strain:
            if s < 0.05:
                stress = 350.0 * s / 0.05
            else:
                stress = 350.0 + 500.0 * (s - 0.05)   # ~425 at strain 0.2 (coincides with iso end value but monotonic)
            xi = 0.3 / (1.0 + math.exp(-30.0 * (s - 0.12)))
            beta = 0.05 * (s / 0.2) ** 0.8
            temp = 350.0 + 20.0 * (s / 0.2) ** 0.7
            w.writerow(['100', 350, 'thermo', round(s, 6), round(stress, 2), round(temp, 2), round(min(1.0, xi), 4), round(beta, 5)])

        # ---------- Case 5: orientation=111, initial_temp=350, iso ----------
        for s in strain:
            stress = 1000.0 * s / 0.2 + 200.0 * (s / 0.2) ** 2   # ~1200 at strain 0.2
            xi = 0.15 / (1.0 + math.exp(-50.0 * (s - 0.12)))
            beta = 0.3 * (s / 0.2) ** 0.5
            temp = 350.0
            w.writerow(['111', 350, 'iso', round(s, 6), round(stress, 2), round(temp, 2), round(min(1.0, xi), 4), round(beta, 5)])

        # ---------- Case 6: orientation=111, initial_temp=350, thermo ----------
        # Nearly identical to iso case; only temperature changes slightly
        for s in strain:
            stress = 1000.0 * s / 0.2 + 200.0 * (s / 0.2) ** 2
            xi = 0.15 / (1.0 + math.exp(-50.0 * (s - 0.12)))
            beta = 0.3 * (s / 0.2) ** 0.5
            temp = 350.0 + 5.0 * (s / 0.2)   # very small rise
            w.writerow(['111', 350, 'thermo', round(s, 6), round(stress, 2), round(temp, 2), round(min(1.0, xi), 4), round(beta, 5)])

if __name__ == '__main__':
    main()
