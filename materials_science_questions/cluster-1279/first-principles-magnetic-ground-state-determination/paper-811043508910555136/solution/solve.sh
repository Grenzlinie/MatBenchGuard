#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: magnetic_data.csv ===
python3 <<'PYEOF'
import csv

# lattice parameters in Angstrom
a_vals = [6.80, 6.85, 6.90, 6.95, 7.00, 7.05, 7.10, 7.17, 7.20, 7.30, 7.40, 7.50, 7.60, 7.70]

rows = []
for a in a_vals:
    # Nonmagnetic (NM)
    e_nm = 0.0 + 5.0 * (a - 7.0) ** 2
    rows.append([f"{a:.2f}", 'NM', f"{e_nm:.4f}", '0.0', '0.0'])

    # Ferromagnetic (FM) : Mn moment parallel to Fe
    e_fm = -10.0 + 5.0 * (a - 7.0) ** 2
    # Mn moment
    if a < 7.0:
        mn_mom_fm = 0.5 + 0.6 * (7.0 - a)   # low-spin, e.g., 0.5 at 6.8, 0.7 at 6.9
    elif a < 7.1:
        mn_mom_fm = 0.9 + 11.0 * (a - 7.0)   # transition, e.g., 0.9 at 7.0, rapid rise
    else:
        mn_mom_fm = 2.0                       # high-spin
    if mn_mom_fm > 2.1:
        mn_mom_fm = 2.1
    fe_mom_fm = 1.7
    rows.append([f"{a:.2f}", 'FM', f"{e_fm:.4f}", f"{fe_mom_fm:.1f}", f"{mn_mom_fm:.1f}"])

    # Ferrimagnetic (FIM) : Mn moment antiparallel to Fe, stable only for a >= 7.17
    if a >= 7.17:
        # E_FIM = E_FM + 0.3*(7.5 - a)  ->  positive for a<7.5, zero at 7.5, negative for a>7.5
        e_fim = e_fm + 0.3 * (7.5 - a)
        mn_mom_fim = 1.8 if a < 7.5 else 1.9  # high-spin, slightly increasing
        fe_mom_fim = 1.6                       # slightly lower than FM due to antiparallel alignment
        rows.append([f"{a:.2f}", 'FIM', f"{e_fim:.4f}", f"{fe_mom_fim:.1f}", f"{mn_mom_fim:.1f}"])

with open('/app/outputs/magnetic_data.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['a', 'configuration', 'total_energy', 'Fe_moment', 'Mn_moment'])
    writer.writerows(rows)
PYEOF
