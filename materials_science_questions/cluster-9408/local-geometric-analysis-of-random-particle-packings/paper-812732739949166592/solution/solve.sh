#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs
python3 -m pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple numpy

# === solve block: transitions.json ===
python3 -c "
import json
data = [
  {'L_over_D': 0.6, 'H_over_D': 1.1, 'phase_A': '1LFO', 'phase_B': '1LEO', 'transition_eta': 0.42},
  {'L_over_D': 0.6, 'H_over_D': 1.1, 'phase_A': '1LEO', 'phase_B': '1LBO', 'transition_eta': 0.79},
  {'L_over_D': 0.3, 'H_over_D': 1.0, 'phase_A': '2L', 'phase_B': '3L', 'transition_eta': 0.54},
  {'L_over_D': 0.3, 'H_over_D': 1.04, 'phase_A': '2L', 'phase_B': '3L', 'transition_eta': 0.52},
  {'L_over_D': 0.3, 'H_over_D': 1.2, 'phase_A': '3L', 'phase_B': '1LBO', 'transition_eta': 0.58},
  {'L_over_D': 0.3, 'H_over_D': 1.2, 'phase_A': '1LBO', 'phase_B': '4L', 'transition_eta': 0.635},
  {'L_over_D': 0.3, 'H_over_D': 1.3, 'phase_A': '3L', 'phase_B': '4L', 'transition_eta': 0.62},
  {'L_over_D': 0.2, 'H_over_D': 1.1, 'phase_A': '4L', 'phase_B': '5L', 'transition_eta': 0.41},
  {'L_over_D': 0.15, 'H_over_D': 0.9, 'phase_A': '5L', 'phase_B': '6L', 'transition_eta': 0.41},
  {'L_over_D': 0.1, 'H_over_D': 0.775, 'phase_A': '5L', 'phase_B': '6L', 'transition_eta': 0.33}
]
with open('/app/outputs/transitions.json', 'w') as f:
    json.dump(data, f, indent=2)
"
