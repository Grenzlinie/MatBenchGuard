#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: incorporation_ratios.json ===
python3 << 'PYEOF'
import json, math

J_total = 100000.0         # total Hg flux, atoms/s
N_sites = 900              # 30x30 surface
J_per_site = J_total / N_sites
R_24 = 18000.0
R_26 = 762.0
R_27 = 150.0

p24 = J_per_site / R_24
p26 = J_per_site / R_26
p27 = J_per_site / R_27
ratio_26_24 = p26 / p24    # = R_24 / R_26
ratio_27_24 = p27 / p24    # = R_24 / R_27

result = {
    "p_Hg_24": p24,
    "p_Hg_26": p26,
    "p_Hg_27": p27,
    "ratio_26_24": ratio_26_24,
    "ratio_27_24": ratio_27_24
}

with open("/app/outputs/incorporation_ratios.json", "w") as f:
    json.dump(result, f, indent=2)
PYEOF
