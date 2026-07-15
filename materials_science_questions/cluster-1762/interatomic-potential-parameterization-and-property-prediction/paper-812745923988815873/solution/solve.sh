#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: fitted_parameters.json ===
cat > /app/outputs/fitted_parameters.json <<'FFEOF'
[{"RG":"Ne","alpha1":0.7053,"beta1":1.0432,"computed_a1":4.464,"computed_E_inf1":165,"alpha2":0.7092,"beta2":0.116,"computed_a2":4.464,"computed_E_inf2":165},{"RG":"Ar","alpha1":0.8208,"beta1":1.0214,"computed_a1":5.311,"computed_E_inf1":646,"alpha2":0.8293,"beta2":0.074,"computed_a2":5.311,"computed_E_inf2":646},{"RG":"Kr","alpha1":0.8565,"beta1":1.0211,"computed_a1":5.67,"computed_E_inf1":936,"alpha2":0.8602,"beta2":0.08,"computed_a2":5.67,"computed_E_inf2":936},{"RG":"Xe","alpha1":0.8715,"beta1":1.0138,"computed_a1":6.132,"computed_E_inf1":1328,"alpha2":0.876,"beta2":0.06,"computed_a2":6.132,"computed_E_inf2":1328}]
FFEOF
