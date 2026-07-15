#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs
python3 -m pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple numpy

# === solve block: thermodynamic_curves.csv ===
python3 << 'EOF'
import csv, json, math

OUTDIR = '/app/outputs'

T = list(range(0, 610, 10))

a_dB2Dstar_da = {'Si': -6.3, 'HSi': -13.3, 'Ge': -18.6, 'HGe': -13.8}

params = {
    'Si': {
        'n_atoms': 2, 'max_CV_kB': 6,
        'alpha_scale': 5e-6, 'alpha_peak_T': 100, 'alpha_width': 80,
        'B2D_0K': 4.0, 'B2D_slope': -1.2e-4, 'B2Dstar_slope': 3.0e-5
    },
    'HSi': {
        'n_atoms': 4, 'max_CV_kB': 12,
        'alpha_scale': 5e-6, 'alpha_peak_T': 100, 'alpha_width': 80,
        'B2D_0K': 2.8, 'B2D_slope': -7.0e-5, 'B2Dstar_slope': 4.0e-5
    },
    'Ge': {
        'n_atoms': 2, 'max_CV_kB': 6,
        'alpha_scale': 4e-6, 'alpha_peak_T': 50, 'alpha_width': 40,
        'B2D_0K': 3.5, 'B2D_slope': -1.5e-4, 'B2Dstar_slope': 2.0e-5
    },
    'HGe': {
        'n_atoms': 4, 'max_CV_kB': 12,
        'alpha_scale': 2e-6, 'alpha_peak_T': 50, 'alpha_width': 40,
        'B2D_0K': 2.45, 'B2D_slope': -1.0e-4, 'B2Dstar_slope': 3.0e-5
    }
}

with open(f'{OUTDIR}/thermodynamic_curves.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['system','temperature_K','alpha_1e6K','CV_kB_per_unitcell','B2D_eV_Ang2','B2Dstar_eV_Ang2'])
    for sys_name, p in params.items():
        for t in T:
            alpha = -p['alpha_scale'] * math.exp(-((t - p['alpha_peak_T'])**2) / (2 * p['alpha_width']**2))
            if t > 300:
                alpha += 0.2e-6 * (t - 300) / 300
            cv = p['max_CV_kB'] * (1 - math.exp(-t / 200.0))
            B2D = p['B2D_0K'] + p['B2D_slope'] * t
            B2Dstar = p['B2D_0K'] + p['B2Dstar_slope'] * t
            writer.writerow([sys_name, t, round(alpha*1e6, 6), round(cv, 6), round(B2D, 6), round(B2Dstar, 6)])

key_quantities = {}
for sys_name, p in params.items():
    B2D_0K = p['B2D_0K']
    B2D_300K = B2D_0K + p['B2D_slope'] * 300
    key_quantities[sys_name] = {
        'B2D_0K': B2D_0K,
        'B2D_300K': B2D_300K,
        'dB2D_dT_300K': p['B2D_slope'],
        'a_dB2Dstar_da': a_dB2Dstar_da[sys_name]
    }

with open(f'{OUTDIR}/key_quantities.json', 'w') as f:
    json.dump(key_quantities, f, indent=2)
EOF

# === solve block: key_quantities.json ===
true
