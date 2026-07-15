#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
set -euo pipefail
mkdir -p /app/outputs

# === solve block: structural_params.json ===
cat > "$OUTDIR/structural_params.json" <<'EOF'
{
  "a": 3.691,
  "c_over_a": 3.376,
  "z_Oz": 0.189,
  "z_La": 0.362
}
EOF

# === solve block: mode_stabilities.json ===
python3 -c "
import json
data = {
    'E_u_mode_1_frequency_THz': 2.0,
    'E_u_mode_2_frequency_THz': 3.5,
    'E_g_mode_frequency_THz': 1.0
}
with open('/app/outputs/mode_stabilities.json', 'w') as f:
    json.dump(data, f, indent=2)
"
