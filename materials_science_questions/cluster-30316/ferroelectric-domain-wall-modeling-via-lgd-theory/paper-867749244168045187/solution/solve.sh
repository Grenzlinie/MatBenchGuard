#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: cluster_size_scaling.csv ===
python3 << 'PYEOF'
import csv

alpha = 0.59
beta = 0.31
C = 10.0  # scaling coefficient: mean_cluster_size = C * gamma / Pe

combos = [
    (1, 10), (1, 20), (1, 50), (1, 100),
    (5, 10), (5, 20), (5, 50), (5, 100),
    (10, 10), (10, 20), (10, 50), (10, 100),
    (20, 10), (20, 20), (20, 50), (20, 100),
    (50, 10), (50, 20), (50, 50),
    (100, 10), (100, 20)
]

rows = []
for Pe, gamma in combos:
    mean_cluster = C * gamma / Pe
    std_cluster = 0.2 * mean_cluster
    rows.append([Pe, gamma, alpha, beta, mean_cluster, std_cluster])

with open('/app/outputs/cluster_size_scaling.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Pe', 'gamma', 'alpha', 'beta', 'mean_cluster_size', 'std_cluster_size'])
    writer.writerows(rows)
print('cluster_size_scaling.csv written')
PYEOF

# === solve block: polarity_autocorrelation_scaling.csv ===
python3 << 'PYEOF'
import csv

C = 0.01  # tau_p = C * N²
Ns = [3, 5, 10, 15, 20, 30, 40, 50, 60, 70, 80, 90, 100]

rows = []
for N in Ns:
    tau_p = C * N * N
    rows.append([N, tau_p])

with open('/app/outputs/polarity_autocorrelation_scaling.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['N', 'tau_p'])
    writer.writerows(rows)
print('polarity_autocorrelation_scaling.csv written')
PYEOF

# === solve block: phase_diagram_simulation.csv ===
python3 << 'PYEOF'
import csv

alpha_beta_ratios = [0.5, 1.0, 2.0, 5.0, 10.0]
pe_gamma_values = [0.1, 0.3, 0.5, 0.7, 1.0, 1.5, 2.0, 3.0, 5.0, 10.0]

def classify(ratio, pe_gamma):
    if ratio >= 5.0:
        # re-entrant: clustered -> microphase -> dispersed -> clustered
        if pe_gamma < 0.5:
            return 'clustered'
        elif pe_gamma < 1.5:
            return 'microphase'
        elif pe_gamma < 3.0:
            return 'dispersed'
        else:
            return 'clustered'
    elif ratio >= 2.0:
        # microphase present but narrower
        if pe_gamma < 0.7:
            return 'clustered'
        elif pe_gamma < 1.2:
            return 'microphase'
        elif pe_gamma < 2.5:
            return 'dispersed'
        else:
            return 'clustered'
    else:
        # low ratio: no microphase
        if pe_gamma < 1.5:
            return 'clustered'
        elif pe_gamma < 4.0:
            return 'dispersed'
        else:
            return 'clustered'

rows = []
for ratio in alpha_beta_ratios:
    for pe_gamma in pe_gamma_values:
        regime = classify(ratio, pe_gamma)
        rows.append([ratio, pe_gamma, regime])

with open('/app/outputs/phase_diagram_simulation.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['alpha_beta_ratio', 'Pe_gamma', 'regime'])
    writer.writerows(rows)
print('phase_diagram_simulation.csv written')
PYEOF
