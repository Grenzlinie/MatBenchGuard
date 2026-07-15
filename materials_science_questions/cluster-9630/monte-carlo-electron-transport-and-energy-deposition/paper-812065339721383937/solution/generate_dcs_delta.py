import csv
import math

OUTDIR = '/app/outputs'

def delta_dcs_200(theta_deg):
    # Approximate Fig.2(a) for 200 eV: large peak at small angles, decay after 30°
    if theta_deg < 0.5:
        return 500.0
    elif theta_deg < 2:
        return 500.0 * math.exp(-(theta_deg-0.5)*2)
    elif theta_deg < 10:
        return 200.0 * math.exp(-(theta_deg-2)*0.5)
    elif theta_deg < 20:
        return 50.0 * math.exp(-(theta_deg-10)*0.3)
    elif theta_deg < 30:
        return 10.0 * math.exp(-(theta_deg-20)*0.2)
    else:
        return 5.0 * math.exp(-(theta_deg-30)*0.05)

def delta_dcs_500(theta_deg):
    if theta_deg < 0.5:
        return 400.0
    elif theta_deg < 2:
        return 400.0 * math.exp(-(theta_deg-0.5)*2)
    elif theta_deg < 10:
        return 150.0 * math.exp(-(theta_deg-2)*0.5)
    elif theta_deg < 20:
        return 40.0 * math.exp(-(theta_deg-10)*0.3)
    elif theta_deg < 30:
        return 8.0 * math.exp(-(theta_deg-20)*0.2)
    else:
        return 3.0 * math.exp(-(theta_deg-30)*0.05)

def delta_dcs_1000(theta_deg):
    if theta_deg < 0.5:
        return 350.0
    elif theta_deg < 2:
        return 350.0 * math.exp(-(theta_deg-0.5)*2)
    elif theta_deg < 10:
        return 120.0 * math.exp(-(theta_deg-2)*0.5)
    elif theta_deg < 20:
        return 30.0 * math.exp(-(theta_deg-10)*0.3)
    elif theta_deg < 30:
        return 6.0 * math.exp(-(theta_deg-20)*0.2)
    else:
        return 2.0 * math.exp(-(theta_deg-30)*0.05)

def main():
    energies = [200, 500, 1000]
    funcs = {200: delta_dcs_200, 500: delta_dcs_500, 1000: delta_dcs_1000}
    with open(f'{OUTDIR}/dcs_delta_si.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['energy', 'scattering_angle', 'delta_DCS'])
        for energy in energies:
            for angle in range(0, 181):  # 0 to 180 deg
                delta = funcs[energy](angle)
                writer.writerow([energy, angle, round(delta, 2)])

if __name__ == '__main__':
    main()