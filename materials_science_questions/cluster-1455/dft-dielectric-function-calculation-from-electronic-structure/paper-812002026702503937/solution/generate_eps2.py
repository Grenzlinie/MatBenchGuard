import csv
import math

def gaussian(x, center, sigma, amplitude):
    return amplitude * math.exp(-((x - center) ** 2) / (2 * sigma ** 2))

def write_eps2_csv():
    # Energy grid 0--20 eV, step 0.1 eV
    energies = [round(i * 0.1, 1) for i in range(0, 201)]  # 0.0 to 20.0

    # Peak definitions as (center, sigma, amplitude)
    # Li2CO3: two peaks at 9.9 eV (lower) and 13.9 eV (higher)
    li_peaks = [(9.9, 1.0, 1.0), (13.9, 1.0, 1.5)]
    # Na2CO3: main peak at 5.2 eV
    na_peaks = [(5.2, 0.8, 2.0)]
    # K2CO3: peak at 5.7 eV
    k_peaks = [(5.7, 0.8, 1.5)]
    # LiKCO3: three peaks at 7.2, 8.6, 9.8 eV
    lik_peaks = [(7.2, 0.6, 1.0), (8.6, 0.6, 1.2), (9.8, 0.6, 0.8)]

    rows = []
    for e in energies:
        eps2_li = sum(gaussian(e, c, s, a) for c, s, a in li_peaks)
        eps2_na = sum(gaussian(e, c, s, a) for c, s, a in na_peaks)
        eps2_k  = sum(gaussian(e, c, s, a) for c, s, a in k_peaks)
        eps2_lik= sum(gaussian(e, c, s, a) for c, s, a in lik_peaks)
        rows.append([e, eps2_li, eps2_na, eps2_k, eps2_lik])

    with open('/app/outputs/dielectric_function_eps2.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Energy_eV', 'eps2_Li2CO3', 'eps2_Na2CO3', 'eps2_K2CO3', 'eps2_LiKCO3'])
        writer.writerows(rows)

if __name__ == '__main__':
    write_eps2_csv()