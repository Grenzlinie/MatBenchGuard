import csv
import math

OUTDIR = '/app/outputs'

def eta_na_200(deg):
    # Approximate Fig.3(a): monotonic increase
    return 0.012 + 0.001*deg + 0.00001*deg**2

def eta_na_500(deg):
    return 0.010 + 0.0008*deg + 0.000008*deg**2

def eta_na_1000(deg):
    return 0.008 + 0.0006*deg + 0.000006*deg**2

def main():
    energies = [200, 500, 1000]
    funcs = {200: eta_na_200, 500: eta_na_500, 1000: eta_na_1000}
    with open(f'{OUTDIR}/eta_na_si.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['energy', 'emission_angle', 'eta'])
        for energy in energies:
            for angle in range(0, 81):  # 0 to 80 deg
                eta = funcs[energy](angle)
                writer.writerow([energy, angle, round(eta, 6)])

if __name__ == '__main__':
    main()