#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: binding_energies.json ===
cat > "$OUTDIR/binding_energies.json" <<'EOF'
{
  "B_H_binding_energy_eV": 2.7,
  "B_B_binding_energy_eV": 0.7,
  "B2H1_binding_energy_eV": 3.3,
  "B2H2_binding_energy_eV": 4.8
}
EOF

# === solve block: vibrational_frequencies.csv ===
cat > "$OUTDIR/vibrational_frequencies.csv" <<'EOF'
defect,isotope,mode_frequency_cm-1
B1H1,11BH,2657
B1H1,11BD,1965
B1H1,10BH,2668
B1H1,10BD,1984
B2H1_neutral,11BH11B,2739
B2H1_neutral,10BH11B,2746
EOF
