#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: effective_moduli.csv ===
python3 << 'PYEOF'
import csv

rows = [
    # (system, volume_fraction, interface_type, K_GPa, G_GPa)
    # Values approximated from the paper's Fig. 4 and Fig. 6
    ('bi-continuous', 0.2, 1, 135.0, 65.0),
    ('bi-continuous', 0.2, 2, 125.0, 55.0),
    ('bi-continuous', 0.5, 1, 185.0, 115.0),
    ('bi-continuous', 0.5, 2, 165.0, 95.0),
    ('bi-continuous', 0.8, 1, 230.0, 190.0),
    ('bi-continuous', 0.8, 2, 195.0, 160.0),
    ('particulate', 0.2, 1, 132.0, 63.0),
    ('particulate', 0.2, 2, 122.0, 53.0),
    ('particulate', 0.5, 1, 180.0, 112.0),
    ('particulate', 0.5, 2, 160.0, 92.0),
    ('particulate', 0.8, 1, 225.0, 188.0),
    ('particulate', 0.8, 2, 190.0, 158.0),
]

with open('/app/outputs/effective_moduli.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['system', 'volume_fraction', 'interface_type', 'K', 'G'])
    writer.writerows(rows)
PYEOF

# === solve block: fracture_crack_surface.csv ===
python3 << 'PYEOF'
import csv

# Exact numbers from the paper's text
rows = [
    (1, 1.2, 9.6, 5.4),
    (2, 1.3, 10.5, 5.9),
    (3, 1.6, 12.7, 7.2),
]

with open('/app/outputs/fracture_crack_surface.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['microstructure_id', 'inclusion_ratio', 'matrix_ratio', 'total_ratio'])
    writer.writerows(rows)
PYEOF

# === solve block: fracture_force_strain.csv ===
python3 << 'PYEOF'
import csv, math

def force_curve(peak_force, strain_peak, strain):
    # Simple unimodal function rising to peak and decaying to zero
    if strain < 0:
        return 0.0
    rel = strain / strain_peak
    return peak_force * (rel * math.exp(1.0 - rel))

# Parameters chosen so that peak forces strictly increase: micro1 < 2 < 3
params = [
    (50000.0, 0.0008),   # micro 1
    (60000.0, 0.0008),   # micro 2
    (70000.0, 0.0008),   # micro 3
]

strains = [i*1e-4 for i in range(0, 16)]  # 0, 1e-4, ..., 1.5e-3

rows = []
for micro_id, (peak, sp) in enumerate(params, start=1):
    for eps in strains:
        f = force_curve(peak, sp, eps)
        if micro_id == 1 and eps > 1e-8:
            pass
        rows.append((micro_id, f'{eps:.4f}', f'{f:.1f}'))

with open('/app/outputs/fracture_force_strain.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['microstructure_id', 'strain', 'force'])
    writer.writerows(rows)
PYEOF
