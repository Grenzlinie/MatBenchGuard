#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p $OUTDIR

# === solve block: geometric_parameters.json ===
python3 << 'PYEOF'
import json

hf_lengths = {
    'P1-O1': 1.599, 'P1-O2': 1.598, 'P1-O3': 1.489, 'P1-O4': 1.477,
    'N1-C5': 1.336, 'N1-C1': 1.349, 'N2-C5': 1.320, 'C1-C2': 1.351,
    'C2-C3': 1.415, 'C3-C4': 1.356, 'C4-C5': 1.422, 'O3-N1': 2.607,
    'O4-N2': 2.752, 'N1-H7': 1.049, 'N2-H8': 1.022, 'N2-H9': 0.992
}
hf_angles = {
    'O3-P1-O4': 117.5, 'O3-P1-O1': 107.3, 'O4-P1-O1': 110.0,
    'O3-P1-O2': 109.1, 'O4-P1-O2': 108.5, 'O1-P1-O2': 103.7,
    'C2-C1-N1': 121.8, 'C1-C2-C3': 117.1, 'C4-C3-C2': 121.1,
    'C3-C4-C5': 119.5, 'C5-N1-C1': 122.8, 'N2-C5-N1': 119.7,
    'N2-C5-C4': 122.6, 'N1-C5-C4': 117.7, 'N1-H7-O3': 174.1,
    'N1-H8-O4': 175.7
}

b3lyp_lengths = {
    'P1-O1': 1.633, 'P1-O2': 1.631, 'P1-O3': 1.521, 'P1-O4': 1.505,
    'N1-C5': 1.360, 'N1-C1': 1.352, 'N2-C5': 1.335, 'C1-C2': 1.370,
    'C2-C3': 1.411, 'C3-C4': 1.373, 'C4-C5': 1.422, 'O3-N1': 2.558,
    'O4-N2': 2.703, 'N1-H7': 1.102, 'N2-H8': 1.050, 'N2-H9': 1.007
}
b3lyp_angles = {
    'O3-P1-O4': 118.3, 'O3-P1-O1': 106.0, 'O4-P1-O1': 110.7,
    'O3-P1-O2': 109.2, 'O4-P1-O2': 107.8, 'O1-P1-O2': 103.9,
    'C2-C1-N1': 121.8, 'C1-C2-C3': 117.6, 'C4-C3-C2': 120.7,
    'C3-C4-C5': 119.9, 'C5-N1-C1': 122.4, 'N2-C5-N1': 119.3,
    'N2-C5-C4': 123.2, 'N1-C5-C4': 117.6, 'N1-H7-O3': 174.7,
    'N1-H8-O4': 177.1
}

data = {
    'hf': {'bond_lengths': hf_lengths, 'bond_angles': hf_angles},
    'b3lyp': {'bond_lengths': b3lyp_lengths, 'bond_angles': b3lyp_angles}
}
with open('/app/outputs/geometric_parameters.json', 'w') as f:
    json.dump(data, f, indent=2)
PYEOF

# === solve block: scaled_frequencies.json ===
python3 << 'PYEOF'
import json

hf_raw = [3501,3499,3273,2843,2829,2819,2799,2785,2369,1662,1656,1623,1529,1458,1401,1339,1273,1207,1173,1121,1097,1064,1056,1034,996,983,977,971,965,949,857,830,816,811,791,751,714,603,537,509,504,491,460,419,413,403,382,346,259,210,193,169,124,89,83,40,32]
b3lyp_raw = [3683,3680,3520,3094,3078,3069,3051,2785,2060,1662,1656,1617,1528,1481,1427,1358,1307,1257,1161,1145,1123,1115,1046,1042,1015,987,970,966,950,936,862,836,828,815,777,746,709,616,547,515,490,466,463,417,411,402,390,340,259,223,194,181,141,102,86,38,29]

data = {
    'hf': sorted(hf_raw),
    'b3lyp': sorted(b3lyp_raw)
}
with open('/app/outputs/scaled_frequencies.json', 'w') as f:
    json.dump(data, f)
PYEOF
