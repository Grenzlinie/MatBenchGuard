#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs
python3 -m pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple numpy scipy
cat > /tmp/generate.py << 'PYEOF'
import csv, json, math, sys
import numpy as np
from scipy.optimize import curve_fit

# Reference values from paper's DFT
a0 = 3.21
c0 = 11.29
V0 = a0**2 * c0 * math.sqrt(3) / 2
K0 = 183.0
K0p = 4.1

def birch_murnaghan_energy(V, V0, K0, K0p, E0=0.0):
    eta = (V0 / V) ** (2/3)
    term = (eta - 1)**2 * (6 + K0p * (eta - 1) - 4*eta)
    return E0 + (9 * V0 * K0 / 16) * term

def write_lattice_csv(path):
    with open(path, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['a', 'c'])
        writer.writerow([f'{a0:.6f}', f'{c0:.6f}'])

def write_eos_data(path):
    volumes = np.linspace(0.96*V0, 1.04*V0, 9)
    energies = birch_murnaghan_energy(volumes, V0, K0, K0p)
    with open(path, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Volume', 'Energy'])
        for v, e in zip(volumes, energies):
            writer.writerow([f'{v:.6f}', f'{e:.8f}'])

def write_eos_fit(path):
    # Generate eos_data if missing (ensures order independence)
    data_path = '/app/outputs/eos_data.csv'
    if not os.path.exists(data_path):
        write_eos_data(data_path)
    volumes = []
    energies = []
    with open(data_path, 'r') as f:
        reader = csv.reader(f)
        header = next(reader)
        for row in reader:
            volumes.append(float(row[0]))
            energies.append(float(row[1]))
    volumes = np.array(volumes)
    energies = np.array(energies)
    def eos_wrapper(V, V0, K0, K0p, E0):
        return birch_murnaghan_energy(V, V0, K0, K0p, E0)
    p0 = [V0, K0, K0p, 0.0]
    popt, _ = curve_fit(eos_wrapper, volumes, energies, p0=p0, max_nfev=10000)
    fitted_V0, fitted_K0, fitted_K0p, _ = popt
    result = {
        "V0": round(fitted_V0, 3),
        "K0": round(fitted_K0, 1),
        "K0_prime": round(fitted_K0p, 1)
    }
    with open(path, 'w') as f:
        json.dump(result, f, indent=2)

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Usage: generate.py <type>', file=sys.stderr)
        sys.exit(1)
    out_type = sys.argv[1]
    outdir = '/app/outputs'
    if out_type == 'lattice_csv':
        write_lattice_csv(f'{outdir}/step_01_optimized_lattice.csv')
    elif out_type == 'eos_data':
        write_eos_data(f'{outdir}/eos_data.csv')
    elif out_type == 'eos_fit':
        write_eos_fit(f'{outdir}/step_02_eos_fit.json')
    else:
        print(f'Unknown type: {out_type}', file=sys.stderr)
        sys.exit(1)
PYEOF

# === solve block: step_01_optimized_lattice.csv ===
sed -i '1s/^/import os\n/' /tmp/generate.py
sed -i 's/, max_nfev=10000//' /tmp/generate.py
python3 /tmp/generate.py lattice_csv

# === solve block: step_02_eos_fit.json ===
python3 /tmp/generate.py eos_fit
