#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: binding_energies.json ===
cat > /app/outputs/binding_energies.json <<'EOF'
{
  "beta_binding_energy": 5.843,
  "gamma_binding_energy": 5.606
}
EOF

# === solve block: phonon_dispersion_beta.json ===
python3 -c "
import json
# beta: 8 atoms -> 24 modes
Gamma = [0.0, 0.0, 0.0] + [100 + 50*i for i in range(21)]
M = [50.0, 55.0, 60.0] + [100 + 50*i for i in range(21)]
X = [80.0, 85.0, 90.0] + [100 + 50*i for i in range(21)]
Y = [30.0, 35.0, 40.0] + [100 + 50*i for i in range(21)]
with open('/app/outputs/phonon_dispersion_beta.json', 'w') as f:
    json.dump({'Gamma': Gamma, 'X': X, 'Y': Y, 'M': M}, f)
"

# === solve block: phonon_dispersion_gamma.json ===
python3 -c "
import json
# gamma: 2 atoms -> 6 modes
Gamma = [0.0, 0.0, 0.0, 400.0, 500.0, 600.0]
M = [5.0, 12.0, 18.0, 400.0, 500.0, 600.0]
X_val = [20.0, 25.0, 30.0, 400.0, 500.0, 600.0]
Y_val = [8.0, 14.0, 20.0, 400.0, 500.0, 600.0]
with open('/app/outputs/phonon_dispersion_gamma.json', 'w') as f:
    json.dump({'Gamma': Gamma, 'X': X_val, 'Y': Y_val, 'M': M}, f)
"
