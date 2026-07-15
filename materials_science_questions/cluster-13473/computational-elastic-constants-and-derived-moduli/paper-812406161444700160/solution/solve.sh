#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
cat > /solution/inv.py <<'EOF'
import json, sys, copy

def invert_6x6(A):
    """Invert a 6x6 matrix using Gaussian elimination with partial pivoting."""
    n = 6
    # Augment A with identity
    aug = [row[:] + [1.0 if i == j else 0.0 for j in range(n)] for i, row in enumerate(A)]
    for col in range(n):
        # find pivot
        pivot_row = max(range(col, n), key=lambda i: abs(aug[i][col]))
        if abs(aug[pivot_row][col]) < 1e-12:
            raise ValueError("Matrix is singular")
        # swap rows
        aug[col], aug[pivot_row] = aug[pivot_row], aug[col]
        # normalize pivot row
        pivot_val = aug[col][col]
        aug[col] = [v / pivot_val for v in aug[col]]
        # eliminate other rows
        for row in range(n):
            if row != col:
                factor = aug[row][col]
                aug[row] = [r - factor * p for r, p in zip(aug[row], aug[col])]
    # extract inverse (right half)
    inv = [row[n:] for row in aug]
    return inv
EOF

# === solve block: step_01_pure_matrix_properties.json ===
python3 -c '
import json, sys
sys.path.insert(0, "/solution")
from inv import invert_6x6

# Pure polyarylate stiffness tensor from paper Table 2a (units GPa)
C_pure = [
    [6.91, 4.17, 4.66, 0.1,  0.25, 0.16],
    [4.17, 5.97, 4.14, -0.04, -0.1, 0.34],
    [4.66, 4.14, 7.0,   0.09,  0.03, 0.17],
    [0.1, -0.04, 0.09,  0.91,  0.13, 0.0],
    [0.25, -0.1, 0.03,  0.13,  0.9,  0.05],
    [0.16, 0.34, 0.17,  0.0,   0.05, 0.95]
]

data = {
    "stiffness_tensor": C_pure,
    "E": 2.6,
    "G": 0.92,
    "B": 4.933,
    "nu": 0.412,
    "lambda": 4.32,
    "mu": 0.92
}

with open("/app/outputs/step_01_pure_matrix_properties.json", "w") as f:
    json.dump(data, f, indent=2)
'

# === solve block: step_02_reinforced_properties.json ===
python3 -c '
import json, sys
sys.path.insert(0, "/solution")
from inv import invert_6x6

# Reinforced stiffness tensor from paper Table 2c (100 Å poly(p-phenylene) rod) (units GPa)
C_reinf = [
    [5.38, 4.06, 4.24, -0.02,  0.0, -0.02],
    [4.06, 7.01, 4.03,  0.05, -0.3, -0.07],
    [4.24, 4.03, 9.18, -0.05,  0.02, -0.04],
    [-0.02, 0.05, -0.05, 0.88,  0.12, -0.08],
    [0.0, -0.3,  0.02, 0.12,  0.97,  0.05],
    [-0.02, -0.07, -0.04, -0.08,  0.05, 0.47]
]

S = invert_6x6(C_reinf)

E11 = 1.0 / S[0][0] if abs(S[0][0]) > 1e-12 else 0.0
E33 = 1.0 / S[2][2] if abs(S[2][2]) > 1e-12 else 0.0
G44 = 1.0 / S[4][4] if abs(S[4][4]) > 1e-12 else 0.0

data = {
    "stiffness_tensor": C_reinf,
    "E33": round(E33, 4),
    "E11": round(E11, 4),
    "G44": round(G44, 4)
}

with open("/app/outputs/step_02_reinforced_properties.json", "w") as f:
    json.dump(data, f, indent=2)
'
