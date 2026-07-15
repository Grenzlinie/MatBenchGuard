#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: step_01_energy_absorption.csv ===
cat > /app/outputs/step_01_energy_absorption.csv <<'FFEOF'
beam_voltage_kV,energy_absorbed_pct
62,6.1
80,3.2
100,1.8
120,1.2
140,0.9
160,0.7
180,0.6
200,0.5
FFEOF

# === solve block: step_02_simulated_mpp_trend.csv ===
python3 << 'PYEOF'
absorb = {62:6.1, 80:3.2, 100:1.8, 120:1.2, 140:0.9, 160:0.7, 180:0.6, 200:0.5}
base = absorb[62]
with open('/app/outputs/step_02_simulated_mpp_trend.csv', 'w') as f:
    f.write('beam_voltage_kV,simulated_mpp_nW\n')
    for kv in sorted(absorb):
        mpp = 97.8 * absorb[kv] / base
        f.write(f'{kv},{mpp}\n')
PYEOF
