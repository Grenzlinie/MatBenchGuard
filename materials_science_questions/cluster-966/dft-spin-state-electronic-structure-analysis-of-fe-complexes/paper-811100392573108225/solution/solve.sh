#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail

python3 -m pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple numpy
mkdir -p /app/outputs

# === solve block: calculated_results.json ===
python3 <<'PYTHON_EOF'
import json, math
import numpy as np

beta = 0.5
Dq = 500.0

# Diagonal entries (free-ion term energies * beta)
diag = [
    35100 * beta,
    52100 * beta,
    32000 * beta
]

sqrt5 = math.sqrt(5)
# Off-diagonal couplings
off13 = -4 * sqrt5 * Dq
off23 = -2 * sqrt5 * Dq

# Build symmetric 3x3 matrix
mat = np.array([
    [diag[0], 0,       off13],
    [0,       diag[1], off23],
    [off13,   off23,   diag[2]]
])

eigenvalues = np.linalg.eigvalsh(mat)
quartet_energy = float(np.min(eigenvalues))

delta = -10 * Dq

result = {
    "beta": beta,
    "Dq": Dq,
    "quartet_energy_cm-1": quartet_energy,
    "delta_cm-1": delta
}

with open("/app/outputs/calculated_results.json", "w") as f:
    json.dump(result, f, indent=2)
PYTHON_EOF
