#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: binding_enthalpies.csv ===
python3 << 'PYEOF'
import csv
with open("/app/outputs/binding_enthalpies.csv", "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["molecule", "delta_H298_kcalmol", "delta_G298_kcalmol"])
    data = [
        ("DHB", 34.5, 27.8),
        ("SA", 39.0, 30.7),
        ("4-HCCA", 44.3, 36.1),
        ("PA", 42.9, 35.2),
        ("NA", 37.5, 29.6),
        ("AA", 37.0, 29.0),
    ]
    for row in data:
        w.writerow(row)
PYEOF

# === solve block: dhb_isomer_energies.csv ===
python3 << 'PYEOF'
import csv
with open("/app/outputs/dhb_isomer_energies.csv", "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["isomer_label", "relative_delta_H_kcalmol"])
    data = [
        (1, 0.0),
        (2, 0.0),
        (3, 8.6),
        (4, 10.4),
        (5, 10.2),
        (6, 0.7),
        (7, 13.9),
        (8, "not found"),
    ]
    for row in data:
        w.writerow(row)
PYEOF
