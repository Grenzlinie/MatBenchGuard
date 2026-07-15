#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
set -euo pipefail
OUTDIR="${OUTDIR:-/app/outputs}"
mkdir -p "$OUTDIR"
python3 -m pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple numpy

# === solve block: properties.json ===
python3 -c "
import json
phases = [
    {
        'phase_name': 'V',
        'space_group': 'Im‑3m',
        'Cij': [241.333, 149.333, 27.8],
        'B': 180.0,
        'G': 34.0,
        'E': 96.0,
        'v': 0.411,
        'Hv': 0.0
    },
    {
        'phase_name': 'V2C',
        'space_group': 'Pbcn',
        'Cij': [400, 383, 414, 110, 130, 135, 182, 120, 189],
        'B': 242,
        'G': 121,
        'E': 311,
        'v': 0.286,
        'Hv': 11.7
    },
    {
        'phase_name': 'V4C3',
        'space_group': 'R‑3m',
        'Cij': [537, 154, 206, 0.0, 480, 148],
        'B': 299,
        'G': 162,
        'E': 412,
        'v': 0.271,
        'Hv': 16.2
    },
    {
        'phase_name': 'P31‑V6C5',
        'space_group': 'P31',
        'Cij': [456, 114, 130, 0.0, 0.0, 474, 189],
        'B': 237,
        'G': 176,
        'E': 423,
        'v': 0.202,
        'Hv': 26.1
    },
    {
        'phase_name': 'V8C7',
        'space_group': 'P4_332',
        'Cij': [663, 122, 203],
        'B': 243,
        'G': 180,
        'E': 433,
        'v': 0.203,
        'Hv': 26.4
    },
    {
        'phase_name': 'VC',
        'space_group': 'Fm‑3m',
        'Cij': [615, 154, 178],
        'B': 302,
        'G': 228,
        'E': 546,
        'v': 0.198,
        'Hv': 31.5
    }
]
with open('$OUTDIR/properties.json', 'w') as f:
    json.dump({'phases': phases}, f, indent=2)
"
