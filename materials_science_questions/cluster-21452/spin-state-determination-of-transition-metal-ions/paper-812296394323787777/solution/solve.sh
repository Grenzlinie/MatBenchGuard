#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: ground_state_complex1.json ===
python3 << 'PYEOF'
import json, itertools
J_wb = -5.3
J_bb = -24.6
states = []
for S_A in range(0, 5):
    for S_B in range(0, 5):
        for S_T in range(abs(S_A - S_B), S_A + S_B + 1):
            energy = -J_wb * (S_T*(S_T+1) - S_A*(S_A+1) - S_B*(S_B+1)) - J_bb * (S_A*(S_A+1))
            states.append((energy, S_T, S_A, S_B))
best = min(states, key=lambda x: x[0])
result = {"S_T": best[1], "S_A": best[2], "S_B": best[3]}
with open("/app/outputs/ground_state_complex1.json", "w") as f:
    json.dump(result, f)
PYEOF

# === solve block: triangle_ground_states.csv ===
python3 << 'PYEOF'
import csv
J_star = -1.0
J_list = [-0.01 - 0.01*i for i in range(1000)]  # J from -0.01 to -10.0
results = []
for J in J_list:
    ground = None
    for S_bc in range(0, 5):
        for S_T in range(abs(2 - S_bc), 2 + S_bc + 1):
            E = -J * (S_T*(S_T+1) - S_bc*(S_bc+1)) - J_star * S_bc*(S_bc+1)
            if ground is None or E < ground[3]:
                ground = (J, S_T, S_bc, E)
    if ground:
        ratio = -J  # J_star = -1, so ratio = J/J_star = -J
        results.append([ratio, ground[1], ground[2], ground[3]])
with open("/app/outputs/triangle_ground_states.csv", "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["ratio", "S_T", "S_bc", "energy"])
    w.writerows(results)
PYEOF

# === solve block: tetranuclear_ground_states.csv ===
python3 /solution/run.py tetranuclear_ground_states.csv
