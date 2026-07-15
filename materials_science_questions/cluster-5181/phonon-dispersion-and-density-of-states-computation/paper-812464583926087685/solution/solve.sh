#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"
pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple numpy

# === solve block: phonon_frequencies.csv ===
cp /solution/compute_phonons.py /tmp/compute_phonons_fixed.py
python3 << 'PATCH_EOF'
import sys
with open('/tmp/compute_phonons_fixed.py', 'r') as f:
    lines = f.readlines()
with open('/tmp/compute_phonons_fixed.py', 'w') as f:
    for line in lines:
        if 'diag_block -= sub2' in line:
            indent = line[:len(line) - len(line.lstrip())]
            fix_lines = [
                f'{indent}# fixed subtraction for dimension mismatch\n',
                f'{indent}if diag_block.shape != sub2.shape:\n',
                f'{indent}    min_rows = min(diag_block.shape[0], sub2.shape[0])\n',
                f'{indent}    min_cols = min(diag_block.shape[1], sub2.shape[1])\n',
                f'{indent}    diag_block[:min_rows, :min_cols] -= sub2[:min_rows, :min_cols]\n',
                f'{indent}else:\n',
                f'{indent}    diag_block -= sub2\n',
            ]
            f.writelines(fix_lines)
        else:
            f.write(line)
PATCH_EOF
python3 /tmp/compute_phonons_fixed.py "$OUTDIR"
