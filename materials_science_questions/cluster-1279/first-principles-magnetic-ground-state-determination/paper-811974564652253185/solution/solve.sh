#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: stability_table.json ===
# stability_table.json
cat > "$OUTDIR/stability_table.json" << 'EOF'
{
  "n=3": {"delta_E": 2.0, "stable_config": "FM"},
  "n=4": {"delta_E": -4.0, "stable_config": "AFM"},
  "n=5": {"delta_E": -10.0, "stable_config": "AFM"},
  "n=6": {"delta_E": -6.0, "stable_config": "AFM"},
  "n=7": {"delta_E": -2.0, "stable_config": "AFM"}
}
EOF

# === solve block: delta_N_curves_n5.json ===
# delta_N_curves_n5.json
python3 << 'PYEOF'
import json, math

def gauss(x, mu, sigma, amp):
    return amp * math.exp(-0.5 * ((x - mu) / sigma) ** 2)

energy = [e/100.0 for e in range(-50, 51, 2)]  # -0.50 to 0.50 eV step 0.02
# Fe_sp: mild increase across range (AFM has slightly more sp states overall)
Fe_sp = [[e, 0.02 + 0.01*e] for e in energy]
# Fe_d: a small surplus of AFM states at low E (d-band shift) with a shallow bump
Fe_d = [[e, -0.1 + 0.12*e + gauss(e, -0.15, 0.1, 0.1)] for e in energy]
# Cr_sp: sharp peak around -0.3 eV simulating sp–d hybridization surplus
Cr_sp = [[e, 0.0 + gauss(e, -0.30, 0.08, 0.25) + 0.01*e] for e in energy]
# Cr_d: peak at same energy due to sp–d hybridization, plus d-band features
Cr_d = [[e, -0.05 + 0.05*e + gauss(e, -0.30, 0.12, 0.15)] for e in energy]

result = {
    "Fe_sp": Fe_sp,
    "Fe_d": Fe_d,
    "Cr_sp": Cr_sp,
    "Cr_d": Cr_d
}
with open('/app/outputs/delta_N_curves_n5.json', 'w') as f:
    json.dump(result, f, indent=2)
PYEOF

# === solve finalize ===
echo "Oracle artifacts written."
