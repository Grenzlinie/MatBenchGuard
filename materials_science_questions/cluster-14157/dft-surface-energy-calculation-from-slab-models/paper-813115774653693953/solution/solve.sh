#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: relative_energies.csv ===
python3 - "$OUTDIR" <<'PYEOF'
import csv, sys
outdir = sys.argv[1]
with open(f'{outdir}/relative_energies.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['configuration', 'relative_energy_eV'])
    rows = [
        ['FCC-H', 0.00],
        ['HCP-H', 0.01],
        ['FCC-T', 0.05],
        ['HCP-T', 0.07],
        ['HCP-L', 0.15],
        ['FCC-L', 0.17],
        ['1F2H-120°', 0.12],
        ['2F1H-150°', 0.15],
        ['1F2H-150°', 0.15],
        ['3H-120°', 0.16],
        ['2F1H-120°', 0.16],
        ['3F-120°', 0.16],
        ['2F1H-90°', 0.22],
        ['1F2H-90°', 0.23]
    ]
    w.writerows(rows)
PYEOF

# === solve block: diffusion_barriers.csv ===
python3 - "$OUTDIR" <<'PYEOF'
import csv, sys
outdir = sys.argv[1]
with open(f'{outdir}/diffusion_barriers.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['diffusion_path', 'barrier_eV'])
    rows = [
        ['concerted FCC-H↔HCP-T translation', 0.24],
        ['triangular-to-linear transformation', 0.21],
        ['linear intercell translation', 0.28]
    ]
    w.writerows(rows)
PYEOF
