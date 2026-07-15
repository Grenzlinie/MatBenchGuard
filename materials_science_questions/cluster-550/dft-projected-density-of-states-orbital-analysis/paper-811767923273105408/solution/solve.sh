#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
export OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: binding_energies.json ===
cat > "$OUTDIR/binding_energies.json" <<'JSONEOF'
{
  "decorated_1H2_binding_energy_eV": 0.04,
  "max_H2_released": 2,
  "released_1H2_binding_energy_eV": 0.33,
  "released_2H2_binding_energy_per_H2_eV": 0.26
}
JSONEOF

# === solve block: occupation_numbers.json ===
python3 -c "
import json, math
k = 8.617333262145e-5
T1 = 298.0
T2 = 195.0
mu1 = -0.21
mu2 = -0.10
raw_e1 = 0.33
raw_e2 = 0.26
red = 0.75
e1 = raw_e1 * red
e2 = raw_e2 * red
def f(mu, T, e1, e2):
    kT = k * T
    num = 1 * math.exp((mu + e1) / kT) + 2 * math.exp(2 * (mu + e2) / kT)
    den = 1 + math.exp((mu + e1) / kT) + math.exp(2 * (mu + e2) / kT)
    return num / den
f1 = f(mu1, T1, e1, e2)
f2 = f(mu2, T2, e1, e2)
res = {
    'occupation_25C_60atm': round(f1, 4),
    'occupation_minus78C_60atm': round(f2, 4)
}
print(json.dumps(res))
" > /app/outputs/occupation_numbers.json
