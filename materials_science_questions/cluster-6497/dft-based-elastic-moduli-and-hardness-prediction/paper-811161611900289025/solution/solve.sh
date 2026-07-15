#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: step_01_fitted_parameters.csv ===
python3 <<'PYEOF'
import csv
out = '/app/outputs/step_01_fitted_parameters.csv'
with open(out, 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['Group', 'm', 'C'])
    for g, m, c in [
        ('sp3', -3.60, 0.525),
        ('spd', -4.25, 0.174),
        ('3d',  -5.14, 0.151),
        ('4d',  -7.27, 0.020),
        ('5d4f', -8.24, 0.007),
    ]:
        w.writerow([g, m, c])
PYEOF

# === solve block: step_02_predicted_B.csv ===
python3 <<PYEOF
import csv, math, os

outdir = os.environ.get('OUTDIR', '/app/outputs')

fitted_params = {
    'sp3':  {'m': -3.60, 'C': 0.525},
    'spd':  {'m': -4.25, 'C': 0.174},
    '3d':   {'m': -5.14, 'C': 0.151},
    '4d':   {'m': -7.27, 'C': 0.020},
    '5d4f': {'m': -8.24, 'C': 0.007},
}

compounds = [
    ('CaO',    0.2405, '3d',   1, 1),
    ('SrO',    0.258,  '4d',   1, 1),
    ('BaO',    0.2762, '5d4f', 1, 1),
    ('CoO',    0.2133, '3d',   1, 1),
    ('MnO',    0.223,  'spd',  1, 1),
    ('FeO',    0.214,  '3d',   1, 1),
    ('NiO',    0.2084, '3d',   1, 1),
    ('ZnO',    0.2001, 'spd',  1, 1),
    ('EuO',    0.2572, '5d4f', 1, 1),
    ('Sc2O3',  0.2134, '3d',   2, 3),
]

outfile = os.path.join(outdir, 'step_02_predicted_B.csv')
with open(outfile, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Compound', 'Predicted_B_GPa'])
    for name, d, metal_group, x, y in compounds:
        C_A = fitted_params[metal_group]['C']
        m_A = fitted_params[metal_group]['m']
        C_B = fitted_params['sp3']['C']
        m_B = fitted_params['sp3']['m']
        z = x / (x + y)
        C_AB = (C_A ** z) * (C_B ** (1 - z))
        pos_m_A = -m_A
        pos_m_B = -m_B
        m_AB_pos = (pos_m_A ** z) * (pos_m_B ** (1 - z))
        B = C_AB * (d ** (-m_AB_pos))
        writer.writerow([name, f'{B:.1f}'])
PYEOF
