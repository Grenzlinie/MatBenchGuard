#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: thermal_conductivity.json ===
python3 -c "
import json, sys
outdir = sys.argv[1]
data = {'temperature_K': [300, 900], 'kappa_l_W_mK': [1.82, 0.60]}
with open(f'{outdir}/thermal_conductivity.json', 'w') as f:
    json.dump(data, f)
" "$OUTDIR"

# === solve block: phonon_group_velocities.json ===
python3 -c "
import json, sys
outdir = sys.argv[1]
data = {'TA_mean_m_s': 1433, 'LA_mean_m_s': 2374}
with open(f'{outdir}/phonon_group_velocities.json', 'w') as f:
    json.dump(data, f)
" "$OUTDIR"

# === solve block: ZT_n_type.json ===
python3 -c "
import json, sys
outdir = sys.argv[1]
data = {'ZT_max': 1.9, 'carrier_concentration_cm-3': 4.2e18, 'temperature_K': 900}
with open(f'{outdir}/ZT_n_type.json', 'w') as f:
    json.dump(data, f)
" "$OUTDIR"
