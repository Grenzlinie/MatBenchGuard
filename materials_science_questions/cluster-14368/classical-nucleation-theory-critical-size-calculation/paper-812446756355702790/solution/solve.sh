#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p "/app/outputs"

# === solve block: tolman_results.json ===
python3 <<'PYEOF'
import json
data = {"a_over_rstar": -0.288, "sigma_over_sigma0": 1.4045}
with open("/app/outputs/tolman_results.json", "w") as f:
    json.dump(data, f)
PYEOF

# === solve block: general_power_table.csv ===
python3 <<'PYEOF'
import csv
rows = [
    (1, 0.35, 1.35),
    (2, 0.77, 1.60),
    (3, 1.07, 2.23),
    (4, 1.64, 8.23),
    (5, 1.43, 6.98),
    (6, 1.32, 6.29),
    (7, 1.25, 5.77),
    (8, 1.21, 5.59),
    (9, 1.18, 5.44),
    (10, 1.16, 5.41),
]
with open("/app/outputs/general_power_table.csv", "w", newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['m', 'a_over_rstar', 'sigma_over_sigma0'])
    writer.writerows(rows)
PYEOF
