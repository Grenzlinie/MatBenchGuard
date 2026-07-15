import sys
import math
import csv
import json

e = 4.8032047e-10
hbar = 1.054571817e-27
c = 2.99792458e10
kB = 1.380649e-16
me = 9.10938356e-28
eV_to_erg = 1.602176634e-12

m_e = 0.023 * me
m_h = 0.4 * me
E_g_eV = 0.354
T = 300.0
chi_inf = 12.3
kBT_eV = 8.617333262e-5 * T

E_g_erg = E_g_eV * eV_to_erg

fac = e**2 * math.sqrt(m_e) / (c * math.sqrt(chi_inf) * hbar**2 * math.sqrt(E_g_erg))

def N_c():
    h = 2 * math.pi * hbar
    Nc = 2 * (2 * math.pi * m_e * kB * T / (h**2))**1.5
    return Nc

def epsilon_c(n_cm3):
    Nc = N_c()
    if n_cm3 <= 0:
        return 0.0
    eps_erg = kB * T * math.log(n_cm3 / Nc)
    return eps_erg / eV_to_erg

def compute_alpha_for_doping(n, energies_eV):
    eps_c_eV = epsilon_c(n)
    alpha = []
    for E in energies_eV:
        if E < E_g_eV:
            alpha.append(0.0)
            continue
        heavy_term1 = math.sqrt(2) * math.sqrt(E * (E - E_g_eV))
        arg_h = (E - E_g_eV) / kBT_eV * (1 - (m_e/m_h) * (E / E_g_eV)) - eps_c_eV / kBT_eV
        if arg_h > 700:
            f_n_h = 0.0
        elif arg_h < -700:
            f_n_h = 1.0
        else:
            f_n_h = 1.0 / (1.0 + math.exp(arg_h))
        heavy_contrib = heavy_term1 * (1 - f_n_h)

        light_term2 = (1.0/(6*math.sqrt(2))) * math.sqrt(E**2 - E_g_eV**2) * (2*E_g_eV**2/E**2 + 1)
        arg_l = (E - E_g_eV) / (2 * kBT_eV) - eps_c_eV / kBT_eV
        if arg_l > 700:
            f_n_l = 0.0
        elif arg_l < -700:
            f_n_l = 1.0
        else:
            f_n_l = 1.0 / (math.exp(arg_l) + 1.0)
        light_contrib = light_term2 * (1 - f_n_l)

        curly = heavy_contrib + light_contrib
        alpha_val = fac * curly
        alpha.append(max(alpha_val, 0.0))
    return alpha

def find_edge(energies, alphas, target=100.0):
    for i in range(len(alphas)-1):
        if alphas[i] <= target and alphas[i+1] >= target:
            t = (target - alphas[i]) / (alphas[i+1] - alphas[i])
            edge = energies[i] + t * (energies[i+1] - energies[i])
            return edge
    if alphas[0] > target:
        return energies[0]
    else:
        return energies[-1]

def main():
    if '--output-csv' in sys.argv:
        outpath = sys.argv[sys.argv.index('--output-csv')+1]
        energies = [0.3 + i*0.001 for i in range(301)]
        alpha_n2 = compute_alpha_for_doping(2e18, energies)
        alpha_n5 = compute_alpha_for_doping(5e18, energies)
        with open(outpath, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['photon_energy_eV', 'alpha_n2e18_cm_minus1', 'alpha_n5e18_cm_minus1'])
            for e, a2, a5 in zip(energies, alpha_n2, alpha_n5):
                writer.writerow([e, a2, a5])
        print("CSV written")
    elif '--output-json' in sys.argv:
        outpath = sys.argv[sys.argv.index('--output-json')+1]
        csv_path = '/app/outputs/absorption_spectra.csv'
        energies = []
        alpha_n2 = []
        alpha_n5 = []
        with open(csv_path, 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                energies.append(float(row['photon_energy_eV']))
                alpha_n2.append(float(row['alpha_n2e18_cm_minus1']))
                alpha_n5.append(float(row['alpha_n5e18_cm_minus1']))
        edge_n2 = find_edge(energies, alpha_n2)
        edge_n5 = find_edge(energies, alpha_n5)
        data = {"n2e18_edge_eV": edge_n2, "n5e18_edge_eV": edge_n5}
        with open(outpath, 'w') as f:
            json.dump(data, f, indent=2)
        print("JSON written")
    else:
        print("Usage: ... --output-csv <file> or --output-json <file>")

if __name__ == "__main__":
    main()
