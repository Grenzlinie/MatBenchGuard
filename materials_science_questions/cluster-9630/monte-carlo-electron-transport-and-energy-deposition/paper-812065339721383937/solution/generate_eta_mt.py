import csv
import math

OUTDIR = '/app/outputs'

def eta_mt_200(deg):
    # Slightly higher at small angles, lower after ~45°
    if deg < 45:
        return 0.013 + 0.0012*deg + 0.000012*deg**2
    else:
        return 0.010 + 0.0009*deg + 0.000009*deg**2

def eta_mt_500(deg):
    if deg < 45:
        return 0.011 + 0.0010*deg + 0.000010*deg**2
    else:
        return 0.009 + 0.0007*deg + 0.000007*deg**2

def eta_mt_1000(deg):
    if deg < 45:
        return 0.009 + 0.0008*deg + 0.000008*deg**2
    else:
        return 0.007 + 0.0005*deg + 0.000005*deg**2

def main():
    energies = [200, 500, 1000]
    funcs = {200: eta_mt_200, 500: eta_mt_500, 1000: eta_mt_1000}
    with open(f'{OUTDIR}/eta_mt_si.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['energy', 'emission_angle', 'eta'])
        for energy in energies:
            for angle in range(0, 81):
                eta = funcs[energy](angle)
                writer.writerow([energy, angle, round(eta, 6)])

if __name__ == '__main__':
    main()