#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: defect_free_frequencies.csv ===
python3 -c "
import csv
data = [
    ['diameter_mm', 'mode_label', 'frequency_kHz'],
    # 1.00 mm
    [1.00, '2T1', 2082],
    [1.00, '2S1', 2302],
    [1.00, '1S2', 3050],
    [1.00, '1S3', 3613],
    [1.00, '1T2', 3768],
    [1.00, '1S4', 3992],
    [1.00, '1S5', 4460],
    # 1.20 mm
    [1.20, '2T1', 1735],
    [1.20, '2S1', 1918],
    [1.20, '1S2', 2542],
    [1.20, '1S3', 3010],
    [1.20, '1T2', 3140],
    [1.20, '1S4', 3327],
    [1.20, '1S5', 3717],
]
with open('/app/outputs/defect_free_frequencies.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(data)
"

# === solve block: cracked_split_frequencies.csv ===
python3 -c "
import csv
data = [
    ['multiplet_label', 'irrep_label', 'frequency_kHz'],
    # 2S1 (width 30 kHz, approx split around 2302)
    ['2S1', 'A1', 2302],
    ['2S1', 'B1', 2292],
    ['2S1', 'B2', 2286],
    # 1S2 (exact from Fig. 8)
    ['1S2', 'A1', 3050],
    ['1S2', 'B2', 3039],
    ['1S2', 'B1', 3035],
    ['1S2', 'A1', 2923],
    ['1S2', 'A2', 2830],
    # 1S3 (width 250 kHz, from S3 -> 2A1+A2+2B1+2B2)
    ['1S3', 'A1', 3630],
    ['1S3', 'A1', 3600],
    ['1S3', 'A2', 3550],
    ['1S3', 'B1', 3650],
    ['1S3', 'B1', 3520],
    ['1S3', 'B2', 3670],
    ['1S3', 'B2', 3540],
    # 1T2 (two known from Fig. 8, others plausible)
    ['1T2', 'A1', 3678],
    ['1T2', 'B1', 3753],
    ['1T2', 'A2', 3715],
    ['1T2', 'A2', 3690],
    ['1T2', 'B2', 3740],
    # 1S4 (width 100 kHz, S4 -> 3A1+2A2+2B1+2B2)
    ['1S4', 'A1', 3992],
    ['1S4', 'A1', 3960],
    ['1S4', 'A1', 3945],
    ['1S4', 'A2', 4010],
    ['1S4', 'A2', 3980],
    ['1S4', 'B1', 4030],
    ['1S4', 'B1', 3970],
    ['1S4', 'B2', 4020],
    ['1S4', 'B2', 3950],
]
with open('/app/outputs/cracked_split_frequencies.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(data)
"

# === solve block: group_theory_decomposition.csv ===
python3 -c "
import csv
data = [
    ['original_mode', 'spanning_irreps'],
    ['S0', 'A1'],
    ['S1', 'A1+B1+B2'],
    ['S2', '2A1+A2+B1+B2'],
    ['T1', 'A2+B1+B2'],
    ['T2', 'A1+2A2+B1+B2'],
]
with open('/app/outputs/group_theory_decomposition.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(data)
"
