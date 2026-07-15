#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: barriers_b1.json ===
python3 -c '
import json

data = [
    {"substrate": 1, "label": "1", "spin": "D", "barrier_without_W903": 20.32, "barrier_with_W903": 18.13, "barrier_difference": 2.19},
    {"substrate": 1, "label": "1", "spin": "Q", "barrier_without_W903": 21.28, "barrier_with_W903": 18.71, "barrier_difference": 2.57},
    {"substrate": 2, "label": "2n", "spin": "D", "barrier_without_W903": 20.47, "barrier_with_W903": 19.06, "barrier_difference": 1.41},
    {"substrate": 2, "label": "2n", "spin": "Q", "barrier_without_W903": 21.62, "barrier_with_W903": 20.33, "barrier_difference": 1.29},
    {"substrate": 2, "label": "2i", "spin": "D", "barrier_without_W903": 18.02, "barrier_with_W903": 16.61, "barrier_difference": 1.41},
    {"substrate": 2, "label": "2i", "spin": "Q", "barrier_without_W903": 19.26, "barrier_with_W903": 16.63, "barrier_difference": 2.63},
    {"substrate": 3, "label": "3n", "spin": "D", "barrier_without_W903": 19.96, "barrier_with_W903": 17.70, "barrier_difference": 2.26},
    {"substrate": 3, "label": "3n", "spin": "Q", "barrier_without_W903": 21.16, "barrier_with_W903": 18.30, "barrier_difference": 2.86},
    {"substrate": 3, "label": "3b", "spin": "D", "barrier_without_W903": 14.30, "barrier_with_W903": 10.53, "barrier_difference": 3.77},
    {"substrate": 3, "label": "3b", "spin": "Q", "barrier_without_W903": 14.57, "barrier_with_W903": 10.81, "barrier_difference": 3.76},
    {"substrate": 4, "label": "4", "spin": "D", "barrier_without_W903": 17.43, "barrier_with_W903": 14.85, "barrier_difference": 2.58},
    {"substrate": 4, "label": "4", "spin": "Q", "barrier_without_W903": 18.46, "barrier_with_W903": 14.20, "barrier_difference": 4.26},
    {"substrate": 5, "label": "5", "spin": "D", "barrier_without_W903": 17.08, "barrier_with_W903": 13.63, "barrier_difference": 3.45},
    {"substrate": 5, "label": "5", "spin": "Q", "barrier_without_W903": 18.08, "barrier_with_W903": 14.78, "barrier_difference": 3.30},
    {"substrate": 6, "label": "6", "spin": "D", "barrier_without_W903": 15.01, "barrier_with_W903": 13.60, "barrier_difference": 1.37},
    {"substrate": 6, "label": "6", "spin": "Q", "barrier_without_W903": 15.33, "barrier_with_W903": 13.21, "barrier_difference": 1.80},
    {"substrate": 7, "label": "7", "spin": "D", "barrier_without_W903": 15.78, "barrier_with_W903": 12.66, "barrier_difference": 2.67},
    {"substrate": 7, "label": "7", "spin": "Q", "barrier_without_W903": 15.15, "barrier_with_W903": 12.05, "barrier_difference": 3.01},
    {"substrate": 8, "label": "8", "spin": "D", "barrier_without_W903": 13.68, "barrier_with_W903": 13.39, "barrier_difference": 0.29},
    {"substrate": 8, "label": "8", "spin": "Q", "barrier_without_W903": 14.33, "barrier_with_W903": 12.92, "barrier_difference": 1.41},
    {"substrate": 9, "label": "9", "spin": "D", "barrier_without_W903": 6.33, "barrier_with_W903": -1.57, "barrier_difference": 7.90},
    {"substrate": 9, "label": "9", "spin": "Q", "barrier_without_W903": 7.79, "barrier_with_W903": 2.27, "barrier_difference": 5.52},
    {"substrate": 9, "label": "9c", "spin": "D", "barrier_without_W903": 6.33, "barrier_with_W903": 3.38, "barrier_difference": 2.95},
    {"substrate": 9, "label": "9c", "spin": "Q", "barrier_without_W903": 7.79, "barrier_with_W903": 5.28, "barrier_difference": 2.51}
]

with open("/app/outputs/barriers_b1.json", "w") as f:
    json.dump(data, f, indent=2)
'
