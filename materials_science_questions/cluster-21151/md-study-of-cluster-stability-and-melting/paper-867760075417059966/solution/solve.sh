#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: quench_events.json ===
python3 -c '
import json, random
random.seed(42)

def generate_outcomes(distribution):
    outcomes = []
    for mode, cnt in distribution:
        outcomes.extend([list(mode) for _ in range(cnt)])
    random.shuffle(outcomes)
    return outcomes

data = []

# N=5
N5_data = [
    (5.25, [([1,2,2], 20)]),
    (5.0,  [([1,2,2], 10), ([1,1,1,2], 10)]),
    (4.9,  [([1,1,1,2], 20)]),
    (4.85, [([1,1,1,2], 10), ([1,1,1,1,1], 10)]),
    (4.79, [([1,1,1,1,1], 19), ([1,2,2], 1)]),
    (4.78, [([1,1,1,1,1], 20)]),
    (4.7,  [([1,1,1,1,1], 20)]),
    (4.5,  [([1,1,1,1,1], 20)]),
]
for b, dist in N5_data:
    outcomes = generate_outcomes(dist)
    data.append({"N": 5, "B_star": b, "outcomes": outcomes})

# N=12
N12_data = [
    (5.25, [([1,1,1,3,3,3], 20)]),
    (5.0,  [([1,1,1,3,3,3], 20)]),
    (4.85, [([1,1,1,3,3,3], 10), ([1]*12, 10)]),
    (4.8,  [([1,1,1,3,3,3], 3), ([1]*12, 17)]),
    (4.775,[([1]*12, 18), ([1,1,1,3,3,3], 2)]),
    (4.76, [([1]*12, 20)]),
    (4.7,  [([1]*12, 20)]),
    (4.5,  [([1]*12, 20)]),
]
for b, dist in N12_data:
    outcomes = generate_outcomes(dist)
    data.append({"N": 12, "B_star": b, "outcomes": outcomes})

# N=15
N15_data = [
    (5.75, [([6,9], 20)]),
    (5.5,  [([6,9], 10), ([2,6,7], 10)]),
    (5.35, [([2,6,7], 20)]),
    (5.1,  [([2,6,7], 10), ([1]*4 + [2]*4 + [3], 10)]),
    (4.8,  [([1]*4 + [2]*4 + [3], 20)]),
    (4.7,  [([1]*4 + [2]*4 + [3], 10), ([1]*15, 10)]),
    (4.65, [([1]*15, 15), ([1]*4 + [2]*4 + [3], 5)]),
    (4.63, [([1]*15, 18), ([1]*4 + [2]*4 + [3], 2)]),
    (4.62, [([1]*15, 20)]),
    (4.5,  [([1]*15, 20)]),
]
for b, dist in N15_data:
    outcomes = generate_outcomes(dist)
    data.append({"N": 15, "B_star": b, "outcomes": outcomes})

print(json.dumps(data, indent=2))
' > "$OUTDIR/quench_events.json"
