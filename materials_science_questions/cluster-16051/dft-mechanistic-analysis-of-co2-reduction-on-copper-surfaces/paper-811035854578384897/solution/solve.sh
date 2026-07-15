#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: pmf_data.csv ===
python3 << 'EOF'
import csv

r_vals = [1.8, 2.125, 2.45, 2.775, 3.1, 3.425, 3.75, 4.075, 4.4, 4.725, 5.05, 5.375, 5.7, 6.025, 6.35, 6.675, 7.0]

# PMF functions for each scenario and RSNO
def pmf_1rsno_cysno(r):
    if r <= 2.0:
        return 0.0
    elif r <= 3.0:
        return (r - 2.0) * 0.5
    else:
        return 0.5

def pmf_1rsno_gsno(r):
    if r <= 2.0:
        return 0.0
    elif r <= 3.0:
        return (r - 2.0) * 0.4
    else:
        return 0.4

def pmf_2rsno_cysno(r):
    if r <= 2.0:
        return 0.0
    elif r <= 3.5:
        return (r - 2.0) * 15.0 / 1.5
    else:
        return 15.0

def pmf_2rsno_gsno(r):
    if r <= 2.0:
        return 0.0
    elif r <= 2.8:
        return (r - 2.0) * 1.2 / 0.8
    else:
        return 1.2

def pmf_rsno2_cysno(r):
    return pmf_1rsno_cysno(r)

def pmf_rsno2_gsno(r):
    return pmf_1rsno_gsno(r)

with open('/app/outputs/pmf_data.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['scenario', 'RSNO', 'r_CuS', 'PMF'])
    for r in r_vals:
        w.writerow(['1RSNO', 'CysNO', r, pmf_1rsno_cysno(r)])
        w.writerow(['1RSNO', 'GSNO', r, pmf_1rsno_gsno(r)])
        w.writerow(['2RSNO', 'CysNO', r, pmf_2rsno_cysno(r)])
        w.writerow(['2RSNO', 'GSNO', r, pmf_2rsno_gsno(r)])
        w.writerow(['RSNO2', 'CysNO', r, pmf_rsno2_cysno(r)])
        w.writerow(['RSNO2', 'GSNO', r, pmf_rsno2_gsno(r)])
EOF

# === solve block: barriers.csv ===
python3 << 'EOF'
import csv

barriers = [
    ('1RSNO', 'CysNO', 0.0),
    ('1RSNO', 'GSNO', 0.0),
    ('2RSNO', 'CysNO', 15.0),
    ('2RSNO', 'GSNO', 0.0),
    ('RSNO2', 'CysNO', 0.0),
    ('RSNO2', 'GSNO', 0.0),
]

with open('/app/outputs/barriers.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['scenario', 'RSNO', 'barrier_height'])
    w.writerows(barriers)
EOF
