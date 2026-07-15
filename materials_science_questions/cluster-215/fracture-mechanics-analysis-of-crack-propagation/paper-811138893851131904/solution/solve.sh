#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: transition_strain_rates.csv ===
python3 << 'PYEOF'
import csv, math

K_Ic = 0.1
f = 0.015

# Material/temperature configurations
configs = [
    # (material, temperature_C, B, mu)
    ('fresh',  -10, 4.3e-7,  0.5),
    ('saline', -10, 5.1e-6,  0.5),
    ('fresh',  -40, 3.345e-8, 0.8),
]

# Grain sizes in mm (cover the typical range from the paper)
d_mm_vals = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0]

# Confinement ratios: only values that keep the denominator positive.
# mu=0.5 → limit ~0.333; mu=0.8 → limit ~0.111
R_vals = {
    ('fresh',  -10): [0.0, 0.1, 0.2],
    ('saline', -10): [0.0, 0.1, 0.2],
    ('fresh',  -40): [0.0, 0.05, 0.1],
}

rows = []
for mat, temp, B, mu in configs:
    for d_mm in d_mm_vals:
        d_m = d_mm / 1000.0          # convert mm → m
        for R in R_vals[(mat, temp)]:
            denom = math.sqrt(1 + mu*mu) - mu - R * (mu + math.sqrt(1 + mu*mu))
            if denom <= 0:
                continue  # skip non‑physical entries
            eps_t = B * (K_Ic**3) / (f * (d_m**1.5) * denom)
            cond_id = f"{mat}_{temp}C_d{d_mm}_R{R}"
            rows.append([cond_id, d_mm, R, mat, float(temp), eps_t])

with open('/app/outputs/transition_strain_rates.csv', 'w', newline='') as fh:
    w = csv.writer(fh)
    w.writerow(['condition_id', 'd_mm', 'R', 'material', 'temperature_C', 'epsilon_t_1_per_s'])
    w.writerows(rows)
PYEOF
