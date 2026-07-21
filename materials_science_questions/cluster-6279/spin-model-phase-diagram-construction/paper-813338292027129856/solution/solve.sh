#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: ground_states.csv ===
python3 <<'PYEOF'
import csv

gamma = 1.0

def compute_ground(c_a, c_b, c_ab, B, N_a, N_b):
    best_E = float('inf')
    best = (0,0,0)
    N_a = int(N_a)
    N_b = int(N_b)
    for S_a in range(N_a+1):
        for S_b in range(N_b+1):
            for S in range(abs(S_a - S_b), S_a + S_b + 1):
                E = (c_a - c_ab)*S_a*(S_a+1)/2.0 + (c_b - c_ab)*S_b*(S_b+1)/2.0 + c_ab*S*(S+1)/2.0 - gamma*B*S
                if E < best_E - 1e-12:
                    best_E = E
                    best = (S_a, S_b, S)
    return best

points = [
    # c_ab = 0
    (-2, -2, 0, 1, 10, 10),
    (-2, 0, 0, 1, 10, 10),
    (-2, 2, 0, 1, 10, 10),
    (0, -2, 0, 1, 10, 10),
    (0, 0, 0, 1, 10, 10),
    (0, 2, 0, 1, 10, 10),
    (2, -2, 0, 1, 10, 10),
    (2, 0, 0, 1, 10, 10),
    (2, 2, 0, 1, 10, 10),
    # c_ab < 0
    (-2, -2, -1, 1, 10, 10),
    (-2, 0, -1, 1, 10, 10),
    (-2, 0.5, -1, 1, 10, 10),
    (-2, 2, -1, 1, 10, 10),
    (0, -2, -1, 1, 10, 10),
    (0, 0, -1, 1, 10, 10),
    (0.5, -2, -1, 1, 10, 10),
    (2, -2, -1, 1, 10, 10),
    # 0 < c_ab <= 2*gamma*B
    (0.5, 0.5, 1, 1, 10, 10),
    (2, 2, 1, 1, 10, 10),
    (0.5, 2, 1, 1, 10, 10),
    (2, 0.5, 1, 1, 10, 10),
    (3, 3, 1, 1, 10, 10),
    # c_ab > 2*gamma*B
    (2, 2, 5, 1, 5, 5),
    (8, 8, 5, 1, 5, 5),
    # varying B
    (1, 1, 0, 0.5, 10, 10),
    (1, 1, 0, 2.0, 10, 10),
]

with open('/app/outputs/ground_states.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['c_a', 'c_b', 'c_ab', 'B', 'N_a', 'N_b', 'S_a', 'S_b', 'S'])
    for (c_a, c_b, c_ab, B, N_a, N_b) in points:
        S_a, S_b, S = compute_ground(c_a, c_b, c_ab, B, N_a, N_b)
        w.writerow([c_a, c_b, c_ab, B, N_a, N_b, S_a, S_b, S])
PYEOF
