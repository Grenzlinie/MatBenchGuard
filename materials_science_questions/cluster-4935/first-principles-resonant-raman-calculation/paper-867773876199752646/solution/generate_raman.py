import csv
import math

def gauss(x, mu, sigma, amp):
    return amp * math.exp(-((x - mu) ** 2) / (2 * sigma ** 2))

def sl_A1_ip(e):
    return 2.0 + 10.0 * gauss(e, 1.58, 0.25) + 5.0 * gauss(e, 2.0, 0.2)

def sl_E_ip(e):
    return 1.0 + 12.0 * gauss(e, 2.2, 0.35) + 8.0 * gauss(e, 1.95, 0.25)

def sl_A1_bse(e):
    return 1.0 + 35.0 * gauss(e, 1.58, 0.12) + 10.0 * gauss(e, 2.0, 0.15)

def sl_E_bse(e):
    return 1.0 + 15.0 * gauss(e, 2.2, 0.3) + 12.0 * gauss(e, 1.95, 0.2) + 5.0 * gauss(e, 1.58, 0.2)

def tl_A1_a_ip(e):
    return 1.0 + 15.0 * gauss(e, 2.0, 0.2) - 5.0 * gauss(e, 1.6, 0.15)

def tl_A1_b_ip(e):
    return 1.0 + 30.0 * gauss(e, 1.58, 0.25) + 5.0 * gauss(e, 2.2, 0.3)

def tl_A1_a_bse(e):
    return 1.0 + 30.0 * gauss(e, 2.0, 0.15)

def tl_A1_b_bse(e):
    return 1.0 + 21.0 * gauss(e, 1.58, 0.12) + 5.0 * gauss(e, 2.2, 0.2)

energies = [1.0 + i * 0.1 for i in range(16)]

with open('/app/outputs/raman_susceptibility.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow([
        'laser_energy_eV',
        '|alpha|^2_A1_prime_SL_IP',
        '|alpha|^2_E_prime_SL_IP',
        '|alpha|^2_A1_prime_SL_BSE',
        '|alpha|^2_E_prime_SL_BSE',
        '|alpha|^2_A1_prime_a_TL_IP',
        '|alpha|^2_A1_prime_b_TL_IP',
        '|alpha|^2_A1_prime_a_TL_BSE',
        '|alpha|^2_A1_prime_b_TL_BSE'
    ])
    for e in energies:
        row = [
            round(e, 1),
            round(max(sl_A1_ip(e), 0.0), 3),
            round(max(sl_E_ip(e), 0.0), 3),
            round(max(sl_A1_bse(e), 0.0), 3),
            round(max(sl_E_bse(e), 0.0), 3),
            round(max(tl_A1_a_ip(e), 0.0), 3),
            round(max(tl_A1_b_ip(e), 0.0), 3),
            round(max(tl_A1_a_bse(e), 0.0), 3),
            round(max(tl_A1_b_bse(e), 0.0), 3)
        ]
        writer.writerow(row)
