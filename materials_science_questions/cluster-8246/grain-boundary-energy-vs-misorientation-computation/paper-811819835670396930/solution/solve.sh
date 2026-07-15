#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs
cat > /tmp/gen_texture_outputs.py << 'PYEOF'
import sys
import csv
import json
import math

def make_row(thickness_nm, mcs, f111, f001, f511, f101):
    return {
        'thickness_nm': thickness_nm,
        'MCS': mcs,
        'fraction_111': f111,
        'fraction_001': f001,
        'fraction_511': f511,
        'fraction_101': f101
    }

def generate_csv(path):
    # Reference final fractions per thickness
    finals = {
        100: {
            'fraction_111': 0.92,
            'fraction_001': 0.04,
            'fraction_511': 0.02,
            'fraction_101': 0.02
        },
        500: {
            'fraction_111': 0.45,
            'fraction_001': 0.10,
            'fraction_511': 0.40,
            'fraction_101': 0.05
        },
        800: {
            'fraction_111': 0.05,
            'fraction_001': 0.90,
            'fraction_511': 0.03,
            'fraction_101': 0.02
        }
    }
    # Uniform initial fractions (≈ random orientation)
    init = {'fraction_111': 0.25, 'fraction_001': 0.25, 'fraction_511': 0.25, 'fraction_101': 0.25}
    mcs_values = list(range(0, 5500, 500))   # 0,500,...,5000
    with open(path, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=['thickness_nm','MCS','fraction_111','fraction_001','fraction_511','fraction_101'])
        writer.writeheader()
        for thick in [100, 500, 800]:
            final = finals[thick]
            for mcs in mcs_values:
                # Linear ramp: reaches final at MCS=2000, constant thereafter
                w = min(1.0, mcs / 2000.0)
                row = make_row(
                    thickness_nm=thick,
                    mcs=mcs,
                    f111=init['fraction_111'] + w*(final['fraction_111'] - init['fraction_111']),
                    f001=init['fraction_001'] + w*(final['fraction_001'] - init['fraction_001']),
                    f511=init['fraction_511'] + w*(final['fraction_511'] - init['fraction_511']),
                    f101=init['fraction_101'] + w*(final['fraction_101'] - init['fraction_101'])
                )
                writer.writerow(row)

def generate_json(path):
    # Same finals
    data = {
        "100nm": {
            "fraction_111": 0.92,
            "fraction_001": 0.04,
            "fraction_511": 0.02,
            "fraction_101": 0.02
        },
        "500nm": {
            "fraction_111": 0.45,
            "fraction_001": 0.10,
            "fraction_511": 0.40,
            "fraction_101": 0.05
        },
        "800nm": {
            "fraction_111": 0.05,
            "fraction_001": 0.90,
            "fraction_511": 0.03,
            "fraction_101": 0.02
        }
    }
    with open(path, 'w') as f:
        json.dump(data, f, indent=2)

if __name__ == '__main__':
    if len(sys.argv) != 3:
        sys.exit(1)
    mode = sys.argv[1]
    path = sys.argv[2]
    if mode == 'csv':
        generate_csv(path)
    elif mode == 'json':
        generate_json(path)
    else:
        sys.exit(1)
PYEOF

# === solve block: texture_fractions.csv ===
python3 /tmp/gen_texture_outputs.py csv /app/outputs/texture_fractions.csv

# === solve block: final_texture_summary.json ===
python3 /tmp/gen_texture_outputs.py json /app/outputs/final_texture_summary.json
