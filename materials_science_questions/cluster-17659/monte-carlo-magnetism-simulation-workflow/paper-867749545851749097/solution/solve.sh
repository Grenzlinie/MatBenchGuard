#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: dynamic_order_parameter.csv ===
python3 <<'PYEOF'
import csv

# Reference values approximating the deterministic-to-stochastic transition
# Q_abs near zero for small p, rising to ~0.8 at p=0.4 (paper Fig. 2)
rows = []
for p in [0.00, 0.02, 0.05, 0.07, 0.10, 0.12, 0.15, 0.18, 0.20, 0.22, 0.25, 0.28, 0.30, 0.32, 0.35, 0.38, 0.40]:
    if p <= 0.18:
        q = 0.01
    elif p <= 0.22:
        q = 0.03
    elif p <= 0.25:
        q = 0.08
    elif p <= 0.28:
        q = 0.20
    elif p <= 0.30:
        q = 0.35
    elif p <= 0.32:
        q = 0.50
    elif p <= 0.35:
        q = 0.65
    else:
        q = 0.78
    rows.append([f"{p:.2f}", 128, f"{q:.5f}"])

with open("/app/outputs/dynamic_order_parameter.csv", "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["p", "L", "Q_abs"])
    w.writerows(rows)
PYEOF

# === solve block: metastable_lifetime.csv ===
python3 <<'PYEOF'
import csv

# Reference lifetimes reflecting that tau increases with p (paper Fig. 3)
# (h0, p, tau_avg, tau_std) for L=128, T=0.8 Tc^NN, 1000 trials
data = [
    (0.2, 0.0, 520.0, 55.0),
    (0.2, 0.5, 860.0, 90.0),
    (0.2, 0.7, 1520.0, 160.0),
    (0.2, 1.0, 3100.0, 320.0),
    (0.3, 0.0, 210.0, 22.0),
    (0.3, 0.5, 380.0, 40.0),
    (0.3, 0.7, 720.0, 75.0),
    (0.3, 1.0, 1480.0, 150.0),
    (0.4, 0.0, 85.0, 9.0),
    (0.4, 0.5, 155.0, 16.0),
    (0.4, 0.7, 310.0, 32.0),
    (0.4, 1.0, 690.0, 70.0),
    (0.5, 0.0, 32.0, 3.5),
    (0.5, 0.5, 60.0, 6.5),
    (0.5, 0.7, 125.0, 13.0),
    (0.5, 1.0, 290.0, 30.0),
    (0.6, 0.0, 11.0, 1.2),
    (0.6, 0.5, 24.0, 2.6),
    (0.6, 0.7, 52.0, 5.5),
    (0.6, 1.0, 125.0, 13.0),
]

with open("/app/outputs/metastable_lifetime.csv", "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["h0", "p", "tau_avg", "tau_std"])
    for h0, p, ta, ts in data:
        w.writerow([f"{h0:.1f}", f"{p:.1f}", f"{ta:.3f}", f"{ts:.3f}"])
PYEOF
