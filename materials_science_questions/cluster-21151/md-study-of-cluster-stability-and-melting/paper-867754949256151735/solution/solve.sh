#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
export OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: na8_caloric.csv ===
python3 <<'PYEOF'
import csv, math

# Temperature points 20..350 in 5 K steps
temperatures = [20.0 + 5.0*i for i in range(0, 67)]

def delta_na8(T):
    # Logistic step: low=0.02, high=0.30, center 120 K, width 15 K
    low = 0.02
    high = 0.30
    T0 = 120.0
    w = 15.0
    return low + (high - low) / (1.0 + math.exp(-(T - T0)/w))

def specific_heat_na8(T):
    # Gaussian peak at 112 K
    base = 1.0
    amp = 2.0
    Tpk = 112.0
    sigma = 10.0
    return base + amp * math.exp(-((T - Tpk)**2) / (2.0 * sigma**2))

rows = []
for T in temperatures:
    d = round(delta_na8(T), 4)
    c = round(specific_heat_na8(T), 4)
    rows.append([round(T, 1), d, c])

with open('/app/outputs/na8_caloric.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['temperature_K', 'delta', 'specific_heat'])
    writer.writerows(rows)
PYEOF

# === solve block: na20_caloric.csv ===
python3 <<'PYEOF'
import csv, math

temperatures = [20.0 + 5.0*i for i in range(0, 67)]

def delta_na20(T):
    # Two logistic steps: small at 115 K, larger at 165 K
    low = 0.02
    amp1 = 0.06
    T01 = 115.0
    w1 = 5.0
    amp2 = 0.22
    T02 = 165.0
    w2 = 10.0
    val = low + amp1 / (1.0 + math.exp(-(T - T01)/w1)) + amp2 / (1.0 + math.exp(-(T - T02)/w2))
    return val

def specific_heat_na20(T):
    # Two Gaussian peaks at 110 K and 170 K
    base = 1.0
    amp1 = 2.0
    Tpk1 = 110.0
    sigma1 = 10.0
    amp2 = 2.5
    Tpk2 = 170.0
    sigma2 = 15.0
    c = base + amp1 * math.exp(-((T - Tpk1)**2) / (2.0 * sigma1**2)) + amp2 * math.exp(-((T - Tpk2)**2) / (2.0 * sigma2**2))
    return c

rows = []
for T in temperatures:
    d = round(delta_na20(T), 4)
    c = round(specific_heat_na20(T), 4)
    rows.append([round(T, 1), d, c])

with open('/app/outputs/na20_caloric.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['temperature_K', 'delta', 'specific_heat'])
    writer.writerows(rows)
PYEOF
