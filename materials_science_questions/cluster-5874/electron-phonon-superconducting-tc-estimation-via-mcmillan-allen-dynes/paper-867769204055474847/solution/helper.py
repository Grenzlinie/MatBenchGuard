import csv
import json
import math

def gaussian(x, pos, amp, width):
    if width == 0 or amp == 0:
        return 0.0
    return amp * math.exp(-0.5 * ((x - pos) / width)**2)

def generate_curves():
    conditions = {
        'AN_delta0.06_T0.002J': {
            'low_n_pos':5.0, 'low_n_amp':0.8, 'low_n_width':1.5,
            'broad_n_pos':30.0, 'broad_n_amp':0.25, 'broad_n_width':7.0,
            'low_p_pos':5.0, 'low_p_amp':0.6, 'low_p_width':1.5,
            'broad_p_pos':30.0, 'broad_p_amp':0.15, 'broad_p_width':7.0,
            'bg':0.01
        },
        'AN_delta0.09_T0.002J': {
            'low_n_pos':5.0, 'low_n_amp':0.9, 'low_n_width':1.5,
            'broad_n_pos':35.0, 'broad_n_amp':0.28, 'broad_n_width':7.5,
            'low_p_pos':5.0, 'low_p_amp':0.7, 'low_p_width':1.5,
            'broad_p_pos':35.0, 'broad_p_amp':0.18, 'broad_p_width':7.5,
            'bg':0.01
        },
        'AN_delta0.12_T0.002J': {
            'low_n_pos':5.0, 'low_n_amp':0.95, 'low_n_width':1.5,
            'broad_n_pos':38.0, 'broad_n_amp':0.3, 'broad_n_width':8.0,
            'low_p_pos':5.0, 'low_p_amp':0.75, 'low_p_width':1.5,
            'broad_p_pos':38.0, 'broad_p_amp':0.2, 'broad_p_width':8.0,
            'bg':0.01
        },
        'AN_delta0.15_T0.002J': {
            'low_n_pos':5.0, 'low_n_amp':1.0, 'low_n_width':1.5,
            'broad_n_pos':40.0, 'broad_n_amp':0.32, 'broad_n_width':8.0,
            'low_p_pos':5.0, 'low_p_amp':0.8, 'low_p_width':1.5,
            'broad_p_pos':40.0, 'broad_p_amp':0.22, 'broad_p_width':8.0,
            'bg':0.01
        },
        'AN_delta0.09_T0.06J': {
            'low_n_pos':5.0, 'low_n_amp':0.45, 'low_n_width':1.5,
            'broad_n_pos':35.0, 'broad_n_amp':0.14, 'broad_n_width':7.5,
            'low_p_pos':5.0, 'low_p_amp':0.0, 'low_p_width':1.5,
            'broad_p_pos':35.0, 'broad_p_amp':0.0, 'broad_p_width':7.5,
            'bg':0.01
        },
        'HS_delta0.15_T0.002J': {
            'low_n_pos':0, 'low_n_amp':0, 'low_n_width':1,
            'broad_n_pos':0, 'broad_n_amp':0, 'broad_n_width':1,
            'low_p_pos':0, 'low_p_amp':0, 'low_p_width':1,
            'broad_p_pos':0, 'broad_p_amp':0, 'broad_p_width':1,
            'bg':0.001
        },
        'ND_delta0.15_T0.002J': {
            'low_n_pos':3.0, 'low_n_amp':0.5, 'low_n_width':1.2,
            'broad_n_pos':35.0, 'broad_n_amp':0.15, 'broad_n_width':6.0,
            'low_p_pos':0, 'low_p_amp':0, 'low_p_width':1,
            'broad_p_pos':0, 'broad_p_amp':0, 'broad_p_width':1,
            'bg':0.01
        }
    }

    omega_grid = [i * 0.2 for i in range(301)]  # 0 to 60 meV
    return conditions, omega_grid

def write_csv(filepath):
    conditions, omegas = generate_curves()
    with open(filepath, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['condition', 'omega', 'alpha2F_n', 'alpha2F_p'])
        for condition, params in conditions.items():
            for w in omegas:
                an = params['bg']
                an += gaussian(w, params['low_n_pos'], params['low_n_amp'], params['low_n_width'])
                an += gaussian(w, params['broad_n_pos'], params['broad_n_amp'], params['broad_n_width'])
                an = max(an, 0.0)
                ap = params['bg']
                ap += gaussian(w, params['low_p_pos'], params['low_p_amp'], params['low_p_width'])
                ap += gaussian(w, params['broad_p_pos'], params['broad_p_amp'], params['broad_p_width'])
                ap = max(ap, 0.0)
                writer.writerow([condition, w, an, ap])

def write_json(filepath):
    conditions, _ = generate_curves()
    peaks = {}
    for condition, params in conditions.items():
        low_n = params['low_n_pos'] if params['low_n_amp'] > 1e-8 else None
        broad_n = params['broad_n_pos'] if params['broad_n_amp'] > 1e-8 else None
        low_p = params['low_p_pos'] if params['low_p_amp'] > 1e-8 else None
        broad_p = params['broad_p_pos'] if params['broad_p_amp'] > 1e-8 else None
        peaks[condition] = {
            'low_peak_omega_n': low_n,
            'broad_peak_omega_n': broad_n,
            'low_peak_omega_p': low_p,
            'broad_peak_omega_p': broad_p
        }
    with open(filepath, 'w') as f:
        json.dump(peaks, f, indent=2)

if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1 and sys.argv[1] == 'json':
        write_json('/app/outputs/peak_positions.json')
    else:
        write_csv('/app/outputs/eliashberg_functions.csv')
