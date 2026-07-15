import sys, math, csv, json, os

# Physical constants
kB = 8.617333262145e-5  # eV/K

# Reference Arrhenius parameters
params = {
    'Pd': {'D0': 4.8e-3, 'U': 0.245},
    'Nb': {'D0': 7.5e-4, 'U': 0.101}
}

# Temperatures for which D_s is reported
temperatures = {
    'Pd': [600, 700, 800, 900, 1000],
    'Nb': [600, 800, 1000]
}

outdir = '/app/outputs'

def generate_csv():
    path = os.path.join(outdir, 'diffusion_constants.csv')
    with open(path, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['system', 'temperature_K', 'D_cm2_per_s'])
        for system in ['Pd', 'Nb']:
            D0 = params[system]['D0']
            U  = params[system]['U']
            for T in temperatures[system]:
                D = D0 * math.exp(-U / (kB * T))
                writer.writerow([system, T, D])

def generate_json():
    path = os.path.join(outdir, 'arrhenius_params.json')
    data = {}
    for system in ['Pd', 'Nb']:
        data[system] = {
            'U': params[system]['U'],
            'D0': params[system]['D0']
        }
    with open(path, 'w') as f:
        json.dump(data, f)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        sys.exit(1)
    cmd = sys.argv[1]
    if cmd == 'csv':
        generate_csv()
    elif cmd == 'json':
        generate_json()
    else:
        sys.exit(1)
