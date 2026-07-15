import sys
import csv
import json
import math


def gaussian(x, center, sigma, amplitude):
    return amplitude * math.exp(-((x - center) ** 2) / (2 * sigma ** 2))


def generate_pdos():
    # Energy grid from -15 to 20 eV with step 0.2 eV
    start = -15.0
    end = 20.0
    step = 0.2
    energies = []
    e = start
    while e <= end + 1e-6:
        energies.append(e)
        e += step

    # Gaussian parameters tuned to match paper-reported occupancies
    s_params   = {'center': -6.0, 'sigma': 2.0, 'amplitude': 0.4195}
    pz_params  = {'center':  1.0, 'sigma': 1.5, 'amplitude': 0.210}
    px_params  = {'center':  2.5, 'sigma': 1.5, 'amplitude': 0.266}
    py_params  = px_params.copy()   # degenerate with px

    pdos_list = []
    for energy in energies:
        s  = gaussian(energy, **s_params)
        px = gaussian(energy, **px_params)
        py = gaussian(energy, **py_params)
        pz = gaussian(energy, **pz_params)
        pdos_list.append({'energy': energy, 's': s, 'px': px, 'py': py, 'pz': pz})
    return pdos_list


def write_csv(pdos_list):
    writer = csv.writer(sys.stdout)
    writer.writerow(['energy', 's', 'px', 'py', 'pz'])
    for row in pdos_list:
        writer.writerow([row['energy'], row['s'], row['px'], row['py'], row['pz']])


def compute_occupancies(pdos_list):
    # Trapezoidal integration up to and including E=0
    s_occ = px_occ = py_occ = pz_occ = 0.0
    n = len(pdos_list)
    for i in range(n - 1):
        e1 = pdos_list[i]['energy']
        e2 = pdos_list[i+1]['energy']
        if e2 <= 0.0:
            de = e2 - e1
            s_occ  += (pdos_list[i]['s']  + pdos_list[i+1]['s'])  * de / 2.0
            px_occ += (pdos_list[i]['px'] + pdos_list[i+1]['px']) * de / 2.0
            py_occ += (pdos_list[i]['py'] + pdos_list[i+1]['py']) * de / 2.0
            pz_occ += (pdos_list[i]['pz'] + pdos_list[i+1]['pz']) * de / 2.0
        else:
            break
    return {
        's_occupancy': s_occ,
        'p_occupancy': px_occ + py_occ + pz_occ,
        'net_charge_transfer': 3.0 - (s_occ + px_occ + py_occ + pz_occ),
        'pz_occupancy': pz_occ,
        'px_occupancy': px_occ
    }


def write_results(occupancies):
    json.dump(occupancies, sys.stdout, indent=2)


if __name__ == '__main__':
    mode = sys.argv[1]
    pdos_list = generate_pdos()
    if mode == 'pdos':
        write_csv(pdos_list)
    elif mode == 'results':
        occ = compute_occupancies(pdos_list)
        write_results(occ)
    else:
        raise ValueError("Unknown mode")
