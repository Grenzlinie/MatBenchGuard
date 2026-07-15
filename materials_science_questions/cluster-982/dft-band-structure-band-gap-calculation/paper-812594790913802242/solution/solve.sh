#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: step_01_band_gap.json ===
# Write electronic band gap (repaired: python3 no‑network writer)
python3 -c "
import json
with open('$OUTDIR/step_01_band_gap.json', 'w') as f:
    json.dump({'Eg': 2.28}, f)
"

# === solve block: step_02_effective_couplings.json ===
# Write effective transfer integrals
cat > "$OUTDIR/step_02_effective_couplings.json" <<'FFEOF'
[
  {"channel": "P", "V_eff_h": -13.00, "V_eff_e": 0.4},
  {"channel": "T1", "V_eff_h": -4.6, "V_eff_e": 10.9},
  {"channel": "T2", "V_eff_h": -4.6, "V_eff_e": 10.9}
]
FFEOF

# === solve block: step_03_anisotropic_mobilities.json ===
# Write maximum anisotropic mobilities
cat > "$OUTDIR/step_03_anisotropic_mobilities.json" <<'FFEOF'
{
  "mu_h_max": 0.0889,
  "mu_e_max": 0.0152
}
FFEOF
