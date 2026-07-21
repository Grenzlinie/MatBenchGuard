#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: magnetic_couplings.json ===
python3 << 'EOF'
import sys, io, contextlib
with open('/solution/calc_J.py') as f:
    lines = f.readlines()
new_lines = []
for line in lines:
    if 'for sym, atom_pos in other_atoms:' in line:
        indent = line[:len(line) - len(line.lstrip())]
        new_lines.append(f'{indent}for entry in other_atoms:\n')
        new_lines.append(f'{indent}    sym = entry[0]\n')
        new_lines.append(f'{indent}    atom_pos = entry[1:]\n')
    else:
        new_lines.append(line)
with open('/tmp/calc_J_fixed.py', 'w') as f:
    f.writelines(new_lines)
EOF
python3 /tmp/calc_J_fixed.py > $OUTDIR/magnetic_couplings.json
