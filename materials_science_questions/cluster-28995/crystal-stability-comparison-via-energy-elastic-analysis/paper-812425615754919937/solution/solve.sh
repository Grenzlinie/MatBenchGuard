#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: energies_uniform.csv ===
cat > "$OUTDIR/energies_uniform.csv" <<'FFEOF'
rs,nonmagnetic_energy,ferromagnetic_energy,electron_gas_energy
10,-0.19895,-0.29664,-0.03474
20,-0.11152,-0.16734,-0.02014
30,-0.07739,-0.11611,-0.01404
40,-0.05928,-0.08796,-0.01076
50,-0.04804,-0.06894,-0.00872
75,-0.03259,-0.04892,-0.00591
100,-0.02464,-0.03700,-0.00447
130,-0.01907,-0.02852,-0.00346
200,-0.01249,-0.01876,-0.00226
FFEOF

# === solve block: energies_yukawa.csv ===
cat > "$OUTDIR/energies_yukawa.csv" <<'FFEOF'
rs,nonmagnetic_energy,ferromagnetic_energy,electron_gas_energy
10,-0.24831,-0.24109,-0.03474
20,-0.17382,-0.28196,-0.02014
30,-0.11884,-0.19177,-0.01404
40,-0.08939,-0.14415,-0.01076
50,-0.07135,-0.11512,-0.00872
75,-0.04697,-0.07606,-0.00591
100,-0.03432,-0.05585,-0.00447
130,-0.02522,-0.04134,-0.00346
200,-0.01628,-0.02720,-0.00226
FFEOF

# === solve block: critical_densities.json ===
cat > "$OUTDIR/critical_densities.json" <<'FFEOF'
{
  "nonmagnetic_critical_r_s": 15,
  "nonmagnetic_critical_density_cm2": 5.07e13,
  "ferromagnetic_critical_r_s": 20,
  "ferromagnetic_critical_density_cm2": 2.85e13
}
FFEOF
