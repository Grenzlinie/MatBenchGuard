#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: step_01_multiplicities.json ===
cat <<'EOF' > "$OUTDIR/step_01_multiplicities.json"
{
  "n1": 8,
  "n2": 4,
  "n3": 4,
  "n4": 8
}
EOF

# === solve block: step_02_symmetry_modes.json ===
python3 <<'PYEOF' > "$OUTDIR/step_02_symmetry_modes.json"
import json, math, sys
sqrt2 = math.sqrt(2)
def make_vec(pairs):
    v = [0.0]*24
    for i1, s1, i2, s2 in pairs:
        v[i1] = s1 / sqrt2
        v[i2] = s2 / sqrt2
    return v

M1 = []
for p in [
    [(0,1,3,-1)],
    [(2,1,5,1)],
    [(6,1,9,-1)],
    [(8,1,11,1)],
    [(12,1,15,-1)],
    [(14,1,17,1)],
    [(18,1,21,-1)],
    [(20,1,23,1)]
]:
    M1.append(make_vec(p))

M2 = []
for p in [
    [(1,1,4,1)],
    [(7,1,10,1)],
    [(13,1,16,1)],
    [(19,1,22,1)]
]:
    M2.append(make_vec(p))

M3 = []
for p in [
    [(1,1,4,-1)],
    [(7,1,10,-1)],
    [(13,1,16,-1)],
    [(19,1,22,-1)]
]:
    M3.append(make_vec(p))

M4 = []
for p in [
    [(0,1,3,1)],
    [(2,1,5,-1)],
    [(6,1,9,1)],
    [(8,1,11,-1)],
    [(12,1,15,1)],
    [(14,1,17,-1)],
    [(18,1,21,1)],
    [(20,1,23,-1)]
]:
    M4.append(make_vec(p))

data = {"M1": M1, "M2": M2, "M3": M3, "M4": M4}
json.dump(data, sys.stdout)
PYEOF
