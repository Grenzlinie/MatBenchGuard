import csv
import sys
import math

mode = sys.argv[1]
output_file = sys.argv[2]

d = 100/29
z_list = [(d/2 + i*d) for i in range(29)] + [105.0]
z_list = [round(z, 2) for z in z_list]

if mode == 'energy':
    gammas = [0, 1, 2, 3]
    proton_scales = [500, 200, 50, 15]
    proton_z0 = 10.0
    electron_centers = [35, 30, 25, 20]
    electron_amps = [200, 80, 40, 15]
    electron_sigma = 12.0
    elec_exp_scale = [10, 5, 2, 1]
    elec_exp_z0 = 8.0

    with open(output_file, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['altitude_km','e_gamma0','e_gamma1','e_gamma2','e_gamma3',
                         'p_gamma0','p_gamma1','p_gamma2','p_gamma3'])
        for z in z_list:
            p_row = []
            e_row = []
            for i, gamma in enumerate(gammas):
                p_val = proton_scales[i] * math.exp(-z / proton_z0)
                p_row.append(round(p_val, 2))
                e_gauss = electron_amps[i] * math.exp(-(z - electron_centers[i])**2 / (2 * electron_sigma**2))
                e_exp = elec_exp_scale[i] * math.exp(-z / elec_exp_z0)
                e_val = e_gauss + e_exp
                e_row.append(round(e_val, 2))
            writer.writerow([z] + e_row + p_row)

elif mode == 'oct':
    proton_amp = 8000
    electron_amp = 2500
    peak_alt = 55
    sigma_p = 15.0
    sigma_e = 10.0
    with open(output_file, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['altitude_km','proton_rate','electron_rate','total_rate'])
        for z in z_list:
            p_rate = proton_amp * math.exp(-(z - peak_alt)**2 / (2 * sigma_p**2)) * max(0, 1 - 0.5*z/100) + 100 * math.exp(-z/20)
            e_rate = electron_amp * math.exp(-(z - peak_alt)**2 / (2 * sigma_e**2)) + 10 * math.exp(-z/10)
            total = p_rate + e_rate
            writer.writerow([z, round(p_rate,2), round(e_rate,2), round(total,2)])

elif mode == 'jun':
    electron_amp_j = 10000
    proton_amp_j = 4000
    peak_alt_e = 70
    peak_alt_p = 55
    sigma_e = 12.0
    sigma_p = 18.0
    with open(output_file, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['altitude_km','proton_rate','electron_rate','total_rate'])
        for z in z_list:
            p_rate_j = proton_amp_j * math.exp(-(z - peak_alt_p)**2 / (2 * sigma_p**2)) * max(0, 1 - 0.3*z/100) + 80 * math.exp(-z/25)
            e_rate_j = electron_amp_j * math.exp(-(z - peak_alt_e)**2 / (2 * sigma_e**2)) + 20 * math.exp(-z/15)
            total = p_rate_j + e_rate_j
            writer.writerow([z, round(p_rate_j,2), round(e_rate_j,2), round(total,2)])
