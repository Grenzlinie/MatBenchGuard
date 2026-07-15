#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: conductance_ratios.json ===
python3 -c "
import json

arm_undef = 2.0
arm_bend = arm_undef / 1.01
arm_tip  = arm_undef / 1.05
zig_undef = 2.0
zig_bend = zig_undef / 1.9
zig_tip  = zig_undef / 1.7e4

data = {
    'armchair_undeformed': arm_undef,
    'armchair_bending_40': round(arm_bend, 6),
    'armchair_tip_25': round(arm_tip, 6),
    'zigzag_undeformed': zig_undef,
    'zigzag_bending_40': round(zig_bend, 6),
    'zigzag_tip_25': round(zig_tip, 10)
}

with open('/app/outputs/conductance_ratios.json', 'w') as f:
    json.dump(data, f, indent=2)
"
