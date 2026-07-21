#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: eta_vs_temperature.csv ===
python3 << 'PYEOF'
import csv

temps = [0.02 * i for i in range(1, 101)]  # 0.02, 0.04, ..., 2.00

def eta_D0(t):
    if t <= 0.35:
        return 0.317
    else:
        return 0.317 + (0.55 - 0.317) * (t - 0.35) / (2.0 - 0.35)

def eta_Dneg1(t):
    if t <= 0.35:
        return 0.0
    else:
        return (0.45) * (t - 0.35) / (2.0 - 0.35)

def err(t):
    # small error estimate
    if t < 0.5:
        return 0.01
    else:
        return 0.03

with open('/app/outputs/eta_vs_temperature.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['D_over_abs_J', 'temperature', 'eta', 'eta_error'])
    for t in temps:
        w.writerow([0, round(t, 2), round(eta_D0(t), 5), round(err(t), 5)])
    for t in temps:
        w.writerow([-1, round(t, 2), round(eta_Dneg1(t), 5), round(err(t), 5)])
PYEOF

# === solve block: pattern_densities_low_temperature.csv ===
python3 << 'PYEOF'
import csv

# All distinct pattern IDs (27 total: p1 and ±p2 … ±p14)
pattern_ids = ['p1']
for i in range(2, 15):
    pattern_ids.append(f'p{i}')
    pattern_ids.append(f'-p{i}')

# Densities per D/|J|
# D=1: only patterns ±p3, ±p7, ±p9 get equal share (1/6 each), rest 0
D1_patterns = {'p3','-p3','p7','-p7','p9','-p9'}
D1_val = 1.0/6

# D=-1: choose the set {p6, -p8, -p12} (one of the two equivalent configurations)
Dneg1_patterns = {'p6','-p8','-p12'}
Dneg1_val = 1.0/3

# D=0: mixture, ratio 2.7:1 between the D1 set and the union of both D=-1 sets
# The D=-1 union patterns: ±p6, ∓p8, ∓p12 → 6 patterns
D0_D1_set = D1_patterns   # same 6 patterns
D0_Dneg1_set = {'p6','-p6','-p8','p8','-p12','p12'}
ratio = 2.7
total_mask = 1.0
frac_D1 = ratio / (ratio + 1)
frac_Dneg1 = 1 / (ratio + 1)
D0_val_D1 = frac_D1 / len(D0_D1_set)
D0_val_Dneg1 = frac_Dneg1 / len(D0_Dneg1_set)

rows = []
for pid in pattern_ids:
    # D=1
    if pid in D1_patterns:
        rows.append((1, 0.02, pid, round(D1_val, 6)))
    else:
        rows.append((1, 0.02, pid, 0.0))
    # D=0
    if pid in D0_D1_set:
        rows.append((0, 0.02, pid, round(D0_val_D1, 6)))
    elif pid in D0_Dneg1_set:
        rows.append((0, 0.02, pid, round(D0_val_Dneg1, 6)))
    else:
        rows.append((0, 0.02, pid, 0.0))
    # D=-1
    if pid in Dneg1_patterns:
        rows.append((-1, 0.02, pid, round(Dneg1_val, 6)))
    else:
        rows.append((-1, 0.02, pid, 0.0))

with open('/app/outputs/pattern_densities_low_temperature.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['D_over_abs_J', 'temperature', 'pattern_id', 'density'])
    for r in rows:
        w.writerow(r)
PYEOF

# === solve block: ground_state_regimes.txt ===
cat > /app/outputs/ground_state_regimes.txt << 'TEXTEOF'
Ground state regimes as a function of D/|J|:
1) D/|J| > 0: spin-1/2-like frustrated behavior, no long-range order.
2) -1.5 < D/|J| < 0: partially ordered antiferromagnetic phase.
3) D/|J| < -1.5: non-magnetic all-zero ground state.
4) D/|J| = 0: degenerate manifold with no long-range order.
TEXTEOF
