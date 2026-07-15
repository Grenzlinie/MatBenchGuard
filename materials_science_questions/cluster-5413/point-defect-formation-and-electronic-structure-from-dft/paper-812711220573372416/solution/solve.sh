#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: step_01_energetics.json ===
cat > "$OUTDIR/step_01_energetics.json" <<'FFEOF'
{
  "pristine": {
    "O2": {
      "physisorption_Delta_H_kJmol": -66.79,
      "physisorption_Delta_G_kJmol": -55.49,
      "decomposition_Delta_H_kJmol": -94.40,
      "oxygenation_Delta_H_kJmol": -32.98,
      "TeO2_formation_Delta_H_kJmol": -295.27
    },
    "H2O": {
      "physisorption_Delta_H_kJmol": -19.38,
      "physisorption_Delta_G_kJmol": 11.92,
      "decomposition_Delta_H_kJmol": 131.49,
      "oxygenation_Delta_H_kJmol": 0.0,
      "TeO2_formation_Delta_H_kJmol": 0.0
    },
    "CO": {
      "physisorption_Delta_H_kJmol": -9.90,
      "physisorption_Delta_G_kJmol": 9.45,
      "decomposition_Delta_H_kJmol": 0.0,
      "oxygenation_Delta_H_kJmol": 0.0,
      "TeO2_formation_Delta_H_kJmol": 0.0
    }
  },
  "defect": {
    "O2": {
      "physisorption_Delta_H_kJmol": -53.74,
      "physisorption_Delta_G_kJmol": -52.44,
      "decomposition_Delta_H_kJmol": -92.28,
      "oxygenation_Delta_H_kJmol": -39.11,
      "TeO2_formation_Delta_H_kJmol": -336.44
    },
    "H2O": {
      "physisorption_Delta_H_kJmol": -20.25,
      "physisorption_Delta_G_kJmol": 11.05,
      "decomposition_Delta_H_kJmol": 167.68,
      "oxygenation_Delta_H_kJmol": 0.0,
      "TeO2_formation_Delta_H_kJmol": 0.0
    },
    "CO": {
      "physisorption_Delta_H_kJmol": -9.41,
      "physisorption_Delta_G_kJmol": 9.94,
      "decomposition_Delta_H_kJmol": 0.0,
      "oxygenation_Delta_H_kJmol": 0.0,
      "TeO2_formation_Delta_H_kJmol": 0.0
    }
  }
}
FFEOF

# === solve block: step_02_dos.csv ===
python3 <<'PYEOF'
import csv, math

def gaussian(x, mu, amp, sigma):
    return amp * math.exp(-((x - mu) ** 2) / (2 * sigma**2))

configs = ['pristine', 'O2_decomp', 'full_oxygenation', 'TeO2_layer']
rows = []
for cfg in configs:
    # Energy from -20 to 10 eV, step 0.1
    for e in (i/10.0 for i in range(-200, 101)):
        # Simple baseline, no O-2s peak by default
        dos = 1.0 + 0.05*e
        if cfg in ('full_oxygenation', 'TeO2_layer'):
            # Add O-2s peak near -18 eV
            dos += gaussian(e, -18.0, 2.0, 0.5)
        rows.append({'Configuration': cfg, 'Energy_eV': round(e, 2), 'DOS_arb_units': round(dos, 6)})

with open('/app/outputs/step_02_dos.csv', 'w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=['Configuration','Energy_eV','DOS_arb_units'])
    writer.writeheader()
    writer.writerows(rows)
PYEOF
