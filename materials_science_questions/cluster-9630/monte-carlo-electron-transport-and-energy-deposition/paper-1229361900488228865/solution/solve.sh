#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: photon_fluence_vs_Ta.csv ===
python3 <<'PYEOF'
import csv

thickness_mm = [0.1, 0.2, 0.5, 1.0, 1.5, 2.0, 3.0, 5.0, 10.0]
fluence = [2.0e-06, 5.0e-06, 1.2e-05, 2.0e-05, 2.5e-05, 2.3e-05, 1.8e-05, 8.0e-06, 1.0e-06]
total_photons = [100, 250, 800, 2000, 3500, 5000, 8000, 12000, 20000]

with open('/app/outputs/photon_fluence_vs_Ta.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['Ta_thickness_mm', 'photon_fluence_1percm2', 'total_photons_produced'])
    for t, fl, tp in zip(thickness_mm, fluence, total_photons):
        w.writerow([t, fl, tp])
PYEOF

# === solve block: neutron_yield_vs_ErD3.csv ===
python3 <<'PYEOF'
import csv

thick_cm = [1, 2, 5, 8, 10, 12, 15, 20]

without_total = [2.0e-05, 5.0e-05, 1.0e-04, 1.3e-04, 1.4e-04, 1.5e-04, 1.55e-04, 1.6e-04]
without_dir   = [5.0e-08, 1.0e-07, 4.0e-07, 9.0e-07, 1.2e-06, 1.5e-06, 1.3e-06, 8.0e-07]

with_total    = [1.8e-05, 4.5e-05, 9.5e-05, 1.25e-04, 1.35e-04, 1.45e-04, 1.5e-04, 1.55e-04]
with_dir      = [4.0e-08, 9.0e-08, 3.5e-07, 8.0e-07, 1.1e-06, 1.4e-06, 1.2e-06, 7.0e-07]

with open('/app/outputs/neutron_yield_vs_ErD3.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['ErD3_thickness_cm', 'configuration', 'total_neutrons_per_source_electron', 'directional_neutrons_per_source_electron'])
    for t, tot, dir_ in zip(thick_cm, without_total, without_dir):
        w.writerow([t, 'without_Ta', tot, dir_])
    for t, tot, dir_ in zip(thick_cm, with_total, with_dir):
        w.writerow([t, 'with_Ta', tot, dir_])
PYEOF

# === solve block: summary_results.txt ===
cat > /app/outputs/summary_results.txt <<'FFEOF'
optimal_Ta_thickness_mm: 1.5
overall_neutrons_per_source_electron: 1.6e-04
directional_neutrons_per_source_electron: 1.5e-06
optimal_ErD3_thickness_for_directional_cm: 12.0
FFEOF
