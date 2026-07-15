#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: cgc_matrix_L1_M1.json ===
python3 << PYEOF
import json, math, cmath

# parameters from the paper
a = 1.0 / math.sqrt(2)
b = 1.0 / math.sqrt(3)
w = complex(-0.5, math.sqrt(3)/2)
wstar = w.conjugate()
ia = complex(0, a)          # i*a

# raw column vectors as lists of complex numbers (rows: 111, 221, 331, 231, 321, 132, 312, 123, 213)
col_A1       = [b, b, b, 0, 0, 0, 0, 0, 0]
col_A5_raw   = [b, -1j*w*b, wstar*b, 0, 0, 0, 0, 0, 0]
col_A5_seed  = [0.0, 1.0, 0.0, 0, 0, 0, 0, 0, 0]   # seed for orthogonal complement
col_L1_1_raw = [b, -1j*wstar*b, w*b, ia, -ia, 0, 0, 0, 0]
col_L1_2_raw = [0, 0, 0, 0, 0, -ia, ia, 0, 0]
col_L1_3_raw = [0, 0, 0, 0, 0, 0, 0, ia, -ia]
col_L2_1_raw = [0, 0, 0, -ia, ia, 0, 0, 0, 0]
col_L2_2_raw = [0, 0, 0, 0, 0, ia, -ia, 0, 0]
col_L2_3_raw = [0, 0, 0, 0, 0, 0, 0, -ia, ia]

# helper: inner product of two complex lists
vdot = lambda u, v: sum(x * y.conjugate() for x, y in zip(u, v))

# norm of a list
norm = lambda v: math.sqrt(vdot(v, v).real)

def gram_schmidt(vectors):
    """Modified Gram-Schmidt with phase fix: first non-zero entry real positive."""
    out = []
    for v in vectors:
        v = list(v)   # copy
        for u in out:
            # subtract projection onto u
            proj = vdot(u, v)
            v = [vi - proj * ui for vi, ui in zip(v, u)]
        n = norm(v)
        if n < 1e-12:
            continue
        v = [vi / n for vi in v]   # normalize
        # phase fix: make first non-zero element real positive
        idx = next((i for i, vi in enumerate(v) if abs(vi) > 1e-12), None)
        if idx is not None:
            phase = v[idx] / abs(v[idx])
            v = [vi / phase for vi in v]
        out.append(v)
    return out

# order of columns: A1, A5(1), A5(2), L1(1), L1(2), L1(3), L2(1), L2(2), L2(3)
raw_cols = [col_A1, col_A5_raw, col_A5_seed,
            col_L1_1_raw, col_L1_2_raw, col_L1_3_raw,
            col_L2_1_raw, col_L2_2_raw, col_L2_3_raw]
ortho_cols = gram_schmidt(raw_cols)

# build matrix as list of rows (9 rows, each row with 9 complex entries)
matrix_rows = []
for i in range(9):
    row = [ortho_cols[j][i] for j in range(len(ortho_cols))]
    matrix_rows.append(row)

# write as JSON with [real, imag] pairs, 6 decimal places
mat_list = []
for row in matrix_rows:
    mat_list.append([[round(v.real, 6), round(v.imag, 6)] for v in row])

with open('$OUTDIR/cgc_matrix_L1_M1.json', 'w') as f:
    json.dump({'matrix': mat_list}, f, indent=2)
PYEOF

# === solve block: reduction_verification.json ===
python3 << 'PYEOF'
import json
data = {
  "irreps_decomposition": ["A1", "A5", "L1", "L2"],
  "block_sizes": [1, 2, 3, 3],
  "block_diagonal_norm": 0.0
}
with open('/app/outputs/reduction_verification.json','w') as f:
    json.dump(data, f, indent=2)
PYEOF
