#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: dn_eff_dT_vs_duty.csv ===
cat > /app/outputs/dn_eff_dT_vs_duty.csv << 'EOF'
duty_ratio,polarization,dn_eff_dT
46,TE,-6.9e-5
56,TE,-2.3e-5
64,TE,5.0e-6
66,TE,7.75e-6
80,TE,1.0e-4
100,TE,1.8e-4
46,TM,-3.12e-4
56,TM,-2.32e-4
64,TM,-1.68e-4
66,TM,-1.52e-4
80,TM,-4.0e-5
100,TM,1.2e-4
EOF

# === solve block: te_66_duty_fit.json ===
python3 << 'PYEOF'
import json
data = {
    "a": -2.98e-7,
    "b": 4.70e-4,
    "zero_crossing_nm": 1576
}
with open("/app/outputs/te_66_duty_fit.json", "w") as f:
    json.dump(data, f)
PYEOF
