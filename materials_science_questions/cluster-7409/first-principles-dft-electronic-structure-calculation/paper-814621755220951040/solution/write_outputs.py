import csv, json, math, os, sys

output_name = sys.argv[1]
output_path = os.path.join('/app/outputs', output_name)

def gaussian(x, mu, sigma, amp=1.0):
    return amp * math.exp(-((x - mu) ** 2) / (2 * sigma ** 2))

if output_name == 'step_01_band_gaps.json':
    data = {'VTi_band_gap_eV': 0.5, 'VAl_band_gap_eV': 1.2}
    with open(output_path, 'w') as f:
        json.dump(data, f)

elif output_name == 'step_03_cb_offset.json':
    data = {'VTi_V2O5_CB_minus_Fermi_eV': 0.5, 'VAl_V2O5_CB_minus_Fermi_eV': 1.2}
    with open(output_path, 'w') as f:
        json.dump(data, f)

elif output_name == 'step_02_dos_data.csv':
    systems = [
        {'label': 'VTi', 'gap_end': 0.5, 'cb_onset': 0.5},
        {'label': 'VAl', 'gap_end': 1.2, 'cb_onset': 1.2}
    ]
    N = 401  # -10 .. 10 eV step 0.05
    energies = [-10.0 + i * 0.05 for i in range(N)]
    rows = []
    for sys in systems:
        gap_end = sys['gap_end']
        cb_onset = sys['cb_onset']
        vb_mu = -3.0
        vb_sigma = 1.5
        cb_mu = cb_onset + 0.5
        cb_sigma = 0.3
        for e in energies:
            if e < 0:
                o_sup = gaussian(e, vb_mu, vb_sigma, 2.0)
                o_vana = gaussian(e, vb_mu, vb_sigma, 1.5)
                v = gaussian(e, vb_mu, vb_sigma, 1.0)
            elif e >= gap_end:
                v = gaussian(e, cb_mu, cb_sigma, 2.0)
                o_vana = gaussian(e, cb_mu, cb_sigma * 1.5, 0.5)
                o_sup = gaussian(e, cb_mu, cb_sigma * 2.0, 0.3)
            else:
                v = o_vana = o_sup = 0.0
            total = v + o_sup + o_vana
            rows.append([sys['label'], round(e, 4), round(total, 6), round(v, 6), round(o_sup, 6), round(o_vana, 6)])
    with open(output_path, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['system', 'energy_eV', 'total_dos', 'pdos_V', 'pdos_O_support', 'pdos_O_vana'])
        writer.writerows(rows)
else:
    raise ValueError(f'Unknown output {output_name}')
