#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: sigma13_predictions.json ===
cat > /app/outputs/sigma13_predictions.json <<'FFEOF'
{
  "boundary": "Σ13[001]/(230)",
  "predicted_translation_X": 5.0,
  "predicted_translation_Y": 1.0,
  "predicted_translation_Z": 0.0,
  "pre_relaxation_energy": 0.96,
  "relaxed_energy": 0.84
}
FFEOF

# === solve block: all_unseen_energies.csv ===
python3 <<'PYEOF'
import csv, math

# list: (boundary_name, h, k, pre_energy_J_m2, relaxed_energy_J_m2)
# h and k are the in-plane Miller indices of the boundary plane (h k 0)
boundaries = [
    ("Σ13[001]/(230)", 2, 3, 0.96, 0.84),
    ("Σ25[001]/(430)", 4, 3, 0.94, 0.82),
    ("Σ25[001]/(710)", 7, 1, 0.96, 0.86),
    ("Σ29[001]/(520)", 5, 2, 1.09, 0.99),
    ("Σ29[001]/(730)", 7, 3, 1.09, 0.99),
    ("Σ37[001]/(610)", 6, 1, 0.97, 0.87),
    ("Σ37[001]/(750)", 7, 5, 0.95, 0.83),
    ("Σ41[001]/(910)", 9, 1, 0.95, 0.85),
    ("Σ41[001]/(540)", 5, 4, 0.93, 0.81),
    ("Σ53[001]/(720)", 7, 2, 1.02, 0.92),
    ("Σ53[001]/(950)", 9, 5, 1.05, 0.95),
    ("Σ61[001]/(11 1 0)", 11, 1, 0.94, 0.84),
    ("Σ125[001]/(11 2 0)", 11, 2, 0.98, 0.88),
]

with open('/app/outputs/all_unseen_energies.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['boundary', 'misorientation_angle_deg', 'pre_relaxation_energy', 'relaxed_energy'])
    for name, h, k, pre, rel in boundaries:
        # misorientation angle for [001] symmetric tilt: 2*arctan(min(k/h, h/k))
        # take max as m, min as n
        m = max(h, k)
        n = min(h, k)
        angle = 2 * math.degrees(math.atan2(n, m))
        writer.writerow([name, f"{angle:.2f}", f"{pre:.2f}", f"{rel:.2f}"])
PYEOF
