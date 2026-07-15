#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: bending_gap_results.csv ===
python3 << 'PYEOF'
import csv

# Widths in Å for AGNR (N=10,16,22) and ZGNR (N=6,10,14) as per paper
ag_widths = {
    10: 11.07,   # N=10 -> (10-1)*1.42*sqrt(3)/2 ≈ 11.07
    16: 18.45,   # N=16 -> (15)*... ≈ 18.45
    22: 25.82    # N=22 -> (21)*... ≈ 25.82
}
zg_widths = {
    6:  6.15,   # N=6  -> (5)*1.23
    10: 11.07,
    14: 15.99
}

theta_values = [0.0, 0.02, 0.04, 0.06, 0.08, 0.10]

with open('/app/outputs/bending_gap_results.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['ribbon_type', 'width', 'bend_parameter_Theta', 'computed_band_gap_eV', 'family'])
    # AGNRs (all N=10,16,22 give q=1; (-1)^q = -1; ΔE_g = -10.2 * Θ^2)
    for N, W in ag_widths.items():
        E_g0 = 13.0 / W   # 13 eV·Å / width
        for theta in theta_values:
            delta = -10.2 * theta * theta
            gap = E_g0 + delta
            writer.writerow(['AGNR', f'{W:.2f}', f'{theta:.2f}', f'{gap:.4f}', '1'])
    # ZGNRs
    for N, W in zg_widths.items():
        W_nm = W / 10.0
        theta_crit = W_nm / 200.0
        for theta in theta_values:
            if theta > theta_crit:
                gap = 4.0 * (theta - theta_crit)
            else:
                gap = 0.0
            writer.writerow(['ZGNR', f'{W:.2f}', f'{theta:.2f}', f'{gap:.4f}', ''])
PYEOF
