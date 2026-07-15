#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
set -euo pipefail
mkdir -p /app/outputs

# === solve block: angular_transmission_SPG.csv ===
cat > /tmp/gen_spg.py << 'PYEOF'
import math
sigma = 9.5 / math.sqrt(2*math.log(2))
with open('/app/outputs/angular_transmission_SPG.csv', 'w') as f:
    f.write('angle_deg,transmission' + chr(10))
    for theta_deg in range(0, 31, 2):
        trans = math.exp(-theta_deg**2 / (2.0 * sigma**2))
        f.write(str(theta_deg) + ',' + format(trans, '.6f') + chr(10))
PYEOF
python3 /tmp/gen_spg.py

# === solve block: angular_transmission_bi-atomic.csv ===
cat > /tmp/gen_bi.py << 'PYEOF'
import math
sigma = 17.0 / math.sqrt(2*math.log(2))
with open('/app/outputs/angular_transmission_bi-atomic.csv', 'w') as f:
    f.write('angle_deg,transmission' + chr(10))
    for theta_deg in range(0, 31, 2):
        trans = math.exp(-theta_deg**2 / (2.0 * sigma**2))
        f.write(str(theta_deg) + ',' + format(trans, '.6f') + chr(10))
PYEOF
python3 /tmp/gen_bi.py
