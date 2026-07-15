#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: step_01_shear_vs_strain.csv ===
python3 <<'PYEOF'
import csv

with open('/app/outputs/step_01_shear_vs_strain.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['material', 'true_strain', 'slip_system', 'normalized_shear'])
    # Parameters for rational saturating function: normalized_shear = scale * strain / (strain + c)
    params = {
        ('Ti', 'Prism_a'):   (2.0, 0.08),
        ('Ti', 'Pyr1_a'):    (0.6, 0.08),
        ('Ti', 'Pyr1_ca'):   (0.8, 0.08),
        ('MPEA','Prism_a'):  (1.6, 0.08),
        ('MPEA','Pyr1_a'):   (2.0, 0.08),
        ('MPEA','Pyr1_ca'):  (1.6, 0.08),
    }
    strains = [0.0] + [round(0.01 * i, 4) for i in range(1, 16)]  # 0.0 .. 0.15
    for (mat, ssys), (scale, c) in params.items():
        for s in strains:
            val = round(scale * s / (s + c), 6) if s != 0 else 0.0
            w.writerow([mat, s, ssys, val])
PYEOF

# === solve block: step_02_shear_at_strain_0.08.csv ===
python3 <<'PYEOF'
import csv

with open('/app/outputs/step_02_shear_at_strain_0.08.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['material', 'slip_system', 'normalized_shear'])
    strain = 0.08
    params = {
        ('Ti', 'Prism_a'):   (2.0, 0.08),
        ('Ti', 'Pyr1_a'):    (0.6, 0.08),
        ('Ti', 'Pyr1_ca'):   (0.8, 0.08),
        ('MPEA','Prism_a'):  (1.6, 0.08),
        ('MPEA','Pyr1_a'):   (2.0, 0.08),
        ('MPEA','Pyr1_ca'):  (1.6, 0.08),
    }
    for (mat, ssys), (scale, c) in params.items():
        val = round(scale * strain / (strain + c), 6)
        w.writerow([mat, ssys, val])
PYEOF
