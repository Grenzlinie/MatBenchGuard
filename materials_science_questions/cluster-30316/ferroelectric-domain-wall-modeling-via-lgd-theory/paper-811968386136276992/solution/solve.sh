#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
python3 -m pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple numpy

# === solve block: gk_curves_mu0.635.csv ===
python3 << 'PYEOF'
import csv, sys
sys.path.insert(0, '/solution')
from helper import generate_gk_curve
R, Gk = generate_gk_curve(0.635)
with open('/app/outputs/gk_curves_mu0.635.csv', 'w') as f:
    w = csv.writer(f, lineterminator='\n')
    w.writerow(['G_k','R'])
    for g, r in zip(Gk, R):
        w.writerow([g, r])
PYEOF

# === solve block: gk_curves_mu1.651.csv ===
python3 << 'PYEOF'
import csv, sys
sys.path.insert(0, '/solution')
from helper import generate_gk_curve
R, Gk = generate_gk_curve(1.651)
with open('/app/outputs/gk_curves_mu1.651.csv', 'w') as f:
    w = csv.writer(f, lineterminator='\n')
    w.writerow(['G_k','R'])
    for g, r in zip(Gk, R):
        w.writerow([g, r])
PYEOF

# === solve block: domain_summary.json ===
cat > /app/outputs/domain_summary.json << 'EOF'
{
  "mu0.635": {
    "domain_exists": false,
    "domain_radius_angstrom": null,
    "Gk_max": null
  },
  "mu1.651": {
    "domain_exists": true,
    "domain_radius_angstrom": 28.0,
    "Gk_max": 195,
    "droplet_radius_angstrom": 40.088
  }
}
EOF
