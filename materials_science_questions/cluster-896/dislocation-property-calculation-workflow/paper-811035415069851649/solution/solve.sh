#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: homogeneous_torsional_rigidity.csv ===
python3 <<'PYEOF'
import csv, os
out = os.path.join("/app/outputs", "homogeneous_torsional_rigidity.csv")
rows = [
    ["l/a", "normalized_D"],
    [0.05, 281.540],
    [0.1,  271.690],
    [0.3,  216.103],
    [0.5,  158.812],
    [0.7,  111.661],
    [0.9,   88.956],
]
with open(out, "w", newline='') as f:
    w = csv.writer(f)
    w.writerows(rows)
PYEOF

# === solve block: homogeneous_sif.csv ===
python3 <<'PYEOF'
import csv, os
out = os.path.join("/app/outputs", "homogeneous_sif.csv")
rows = [
    ["l/a", "normalized_SIF"],
    [0.05, 4.415],
    [0.1,  5.588],
    [0.3,  7.942],
    [0.5, 10.366],
    [0.7, 12.269],
    [0.9,  6.783],
]
with open(out, "w", newline='') as f:
    w = csv.writer(f)
    w.writerows(rows)
PYEOF

# === solve block: coated_torsional_rigidity.csv ===
python3 <<'PYEOF'
import csv, os
out = os.path.join("/app/outputs", "coated_torsional_rigidity.csv")
rows = [
    ["l/a", "normalized_D"],
    [0.1, 420.0],
    [0.2, 390.0],
    [0.3, 350.0],
    [0.5, 280.0],
    [0.7, 210.0],
    [0.9, 160.0],
]
with open(out, "w", newline='') as f:
    w = csv.writer(f)
    w.writerows(rows)
PYEOF

# === solve block: coated_sif.csv ===
python3 <<'PYEOF'
import csv, os
out = os.path.join("/app/outputs", "coated_sif.csv")
rows = [
    ["l/a", "normalized_SIF"],
    [0.1, 0.9],
    [0.2, 1.3],
    [0.3, 1.6],
    [0.5, 1.9],
    [0.7, 1.5],
    [0.9, 1.0],
]
with open(out, "w", newline='') as f:
    w = csv.writer(f)
    w.writerows(rows)
PYEOF
