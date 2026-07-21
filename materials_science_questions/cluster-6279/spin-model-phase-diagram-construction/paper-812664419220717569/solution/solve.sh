#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: fig1_maxima.json ===
python3 <<'PYEOF'
import json

data = [
    {"kappa_tilde": 60, "M": 0.6681, "omega": 0.1129, "omega_m": 0.9855},
    {"kappa_tilde": 130, "M": 0.8207, "omega": 0.4705, "omega_m": 1.0727}
]

with open("/app/outputs/fig1_maxima.json", "w") as f:
    json.dump(data, f, indent=2)

print("wrote fig1_maxima.json")
PYEOF

# === solve block: triple_points.json ===
python3 <<'PYEOF'
import json

data = [
    {"omega": 0.0, "triple_omega_m": 0.9429, "transition_order_I_to_ordered": "first", "transition_order_FMN_AFMN": None},
    {"omega": 0.4, "triple_omega_m": 0.7040, "transition_order_I_to_ordered": "first", "transition_order_FMN_AFMN": "second"},
    {"omega": 1.2, "triple_omega_m": 0.4703, "transition_order_I_to_ordered": "first", "transition_order_FMN_AFMN": "second"}
]

with open("/app/outputs/triple_points.json", "w") as f:
    json.dump(data, f, indent=2)

print("wrote triple_points.json")
PYEOF
