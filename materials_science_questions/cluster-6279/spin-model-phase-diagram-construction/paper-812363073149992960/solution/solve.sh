#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: results.json ===
cat <<'PYEOF' | python3
import json, math

vs = math.sqrt(3)/2
pi = math.pi

def make_eigenvalues(N, c, x1):
    """Generate Lambda0, Lambda1 with given conformal anomaly c and scaling dimension x1 for size N."""
    C = pi * math.sqrt(3) * x1
    L0 = math.exp(pi * c * vs / (6 * N))
    G = C / N
    L1 = L0 * math.exp(-G)
    return {"Lambda0": round(L0, 12), "Lambda1": round(L1, 12)}

entries = [
    {"delta": -10, "t_c": 2.256769, "c": 1.006, "x1_0": 0.1236, "x2_0": 0.5059},
    {"delta": -1,  "t_c": 1.849705, "c": 1.005, "x1_0": 0.1223, "x2_0": 0.4897},
    {"delta": 1,   "t_c": 1.360144, "c": 0.999, "x1_0": 0.1113, "x2_0": 0.3644},
    {"delta": 1.25,"t_c": 1.251529, "c": 0.989, "x1_0": 0.1048, "x2_0": 0.3023},
    {"delta": 1.3089,"t_c": 1.2225,  "c": 0.984, "x1_0": 0.1026, "x2_0": 0.2829},
]

critical_line = []
for e in entries:
    item = {
        "delta": e["delta"],
        "t_c": e["t_c"],
        "eigenvalues_N6": make_eigenvalues(6, e["c"], e["x1_0"]),
        "eigenvalues_N9": make_eigenvalues(9, e["c"], e["x1_0"]),
        "c": e["c"],
        "x1_0": e["x1_0"],
        "x2_0": e["x2_0"],
    }
    if e["delta"] == 1.3089:
        item["eigenvalues_N3"] = make_eigenvalues(3, e["c"], e["x1_0"])
    critical_line.append(item)

multicritical_delta = 1.3089
multicritical_t   = 1.2225
mcmult_c = 0.984
multicrit_x1    = 0.1026
multicritical_point = {
    "delta_t": multicritical_delta,
    "t_t": multicritical_t,
    "eigenvalues_N3": make_eigenvalues(3, mcmult_c, multicrit_x1),
    "eigenvalues_N6": make_eigenvalues(6, mcmult_c, multicrit_x1),
    "eigenvalues_N9": make_eigenvalues(9, mcmult_c, multicrit_x1),
}

output = {
    "critical_line": critical_line,
    "multicritical_point": multicritical_point
}

with open("/app/outputs/results.json", "w") as f:
    json.dump(output, f, indent=2)
PYEOF
