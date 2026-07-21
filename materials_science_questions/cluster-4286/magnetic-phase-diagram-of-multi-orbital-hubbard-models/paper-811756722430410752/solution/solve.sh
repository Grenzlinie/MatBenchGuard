#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
python3 -m pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple numpy

# === solve block: effective_U.csv ===
python3 -m pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple scipy
python3 /solution/solve_helper.py --task single_layer --output "$OUTDIR/effective_U.csv"

# === solve block: af_order_and_charge.csv ===
python3 -m pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple numpy
python3 /solution/solve_helper.py --task multilayer --output /tmp/temp_af.csv
python3 -c "
import csv
rows = []
with open('/tmp/temp_af.csv', newline='') as f:
    reader = csv.DictReader(f)
    fieldnames = reader.fieldnames[:]
    for row in reader:
        doping = float(row['doping'])
        y = float(row['y'])
        # compute n_IP and n_OP from doping and y
        # using: average doping delta = (2*delta_OP + delta_IP)/3, y = delta_IP - delta_OP
        # => delta_IP = average_delta + (2/3)*y, n_IP = 1 - delta_IP, n_OP = n_IP + y
        delta_ip = doping + 2.0 * y / 3.0
        n_ip = 1.0 - delta_ip
        n_op = n_ip + y
        row['n_OP'] = f'{n_op:.6f}'
        row['n_IP'] = f'{n_ip:.6f}'
        rows.append(row)
    with open('/app/outputs/af_order_and_charge.csv', 'w', newline='') as out:
        writer = csv.DictWriter(out, fieldnames=fieldnames + ['n_OP', 'n_IP'])
        writer.writeheader()
        writer.writerows(rows)
"
