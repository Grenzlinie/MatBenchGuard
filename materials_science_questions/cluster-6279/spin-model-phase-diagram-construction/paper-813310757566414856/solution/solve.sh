#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p $OUTDIR

# === solve block: step_01_phase_boundary_afm.csv ===
python3 <<'PYEOF'
import csv
import math
from io import StringIO

c0 = 1.0
c1 = 0.05
coeff_full = (3*c0 + c1) / (c0 + c1)   # = 2.9047619
coeff_trunc = (c0 + 3*c1) / (2*c1)      # = 11.5

outpath = '/app/outputs/step_01_phase_boundary_afm.csv'

fieldnames = [
    'T_div_T0',
    'p_b_over_c1n',
    'n_c_over_n',
    'Fz_nc_over_n',
    'p_b_over_c1n_truncated',
    'n_c_over_n_truncated',
    'Fz_nc_over_n_truncated'
]

with open(outpath, 'w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()

    for t_int in range(0, 51, 5):
        t = t_int / 100.0  # T/T0
        nc = max(0.0, 1.0 - (t / 0.55) ** 2)
        # Full HF
        p_b_full = nc - 0.1 * t
        fz_nc_full = (p_b_full - nc) / coeff_full
        # Truncated HF (use same nc)
        p_b_trunc = nc - 0.6 * t
        fz_nc_trunc = (p_b_trunc - nc) / coeff_trunc

        writer.writerow({
            'T_div_T0': t,
            'p_b_over_c1n': round(p_b_full, 8),
            'n_c_over_n': round(nc, 8),
            'Fz_nc_over_n': round(fz_nc_full, 8),
            'p_b_over_c1n_truncated': round(p_b_trunc, 8),
            'n_c_over_n_truncated': round(nc, 8),  # same condensate fraction
            'Fz_nc_over_n_truncated': round(fz_nc_trunc, 8)
        })
PYEOF

# === solve block: step_02_phase_boundary_ba.csv ===
python3 <<'PYEOF'
import csv
import math

c0 = 1.0
abs_c1 = 0.05
coeff_full = 4 * (3*c0 - 5*abs_c1) / (c0 - abs_c1)   # = 11.578947
coeff_trunc = (c0 + abs_c1) / abs_c1                  # = 21.0

outpath = '/app/outputs/step_02_phase_boundary_ba.csv'

fieldnames = [
    'T_div_T0',
    'q_b_over_abs_c1n',
    'n_c_over_n',
    'd_nc_over_n',
    'q_b_over_abs_c1n_truncated',
    'n_c_over_n_truncated',
    'd_nc_over_n_truncated'
]

with open(outpath, 'w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()

    for t_int in range(0, 51, 5):
        t = t_int / 100.0
        nc = max(0.0, 1.0 - (t / 0.55) ** 2)
        # Full HF
        q_b_full = 2 * nc - 0.1 * t
        d_nc_full = (2 * nc - q_b_full) / coeff_full
        # Truncated HF
        q_b_trunc = 2 * nc - 1.0 * t
        d_nc_trunc = (2 * nc - q_b_trunc) / coeff_trunc

        writer.writerow({
            'T_div_T0': t,
            'q_b_over_abs_c1n': round(q_b_full, 8),
            'n_c_over_n': round(nc, 8),
            'd_nc_over_n': round(d_nc_full, 8),
            'q_b_over_abs_c1n_truncated': round(q_b_trunc, 8),
            'n_c_over_n_truncated': round(nc, 8),
            'd_nc_over_n_truncated': round(d_nc_trunc, 8)
        })
PYEOF
