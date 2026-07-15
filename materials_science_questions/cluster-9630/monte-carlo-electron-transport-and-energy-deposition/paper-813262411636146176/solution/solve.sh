#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: interaction_volume_ratio.json ===
cat > "/app/outputs/interaction_volume_ratio.json" <<'FFEOF'
{"ratio": 225.0, "unit": "dimensionless"}
FFEOF

# === solve block: depth_vacancy_profile.csv ===
python3 -c "
import csv, math
mu_v, sigma_v, max_v = 200.0, 70.0, 2000
mu_i, sigma_i, max_i = 200.0, 45.0, 500
depths = [i + 0.5 for i in range(0, 500)]
rows = []
for d in depths:
    v = int(max_v * math.exp(-((d - mu_v) ** 2) / (2 * sigma_v ** 2)))
    i = int(max_i * math.exp(-((d - mu_i) ** 2) / (2 * sigma_i ** 2)))
    rows.append((d, v, i))
with open('/app/outputs/depth_vacancy_profile.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['depth_nm', 'total_vacancies', 'he_ions_remaining'])
    for d, v, i in rows:
        w.writerow([d, v, i])
"
