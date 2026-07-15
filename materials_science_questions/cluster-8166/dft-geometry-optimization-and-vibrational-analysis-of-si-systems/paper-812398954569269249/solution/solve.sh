#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: optimized_geometries.csv ===
cat > "$OUTDIR/optimized_geometries.csv" <<'FFEOF'
molecule,bond_type,length_Angstrom
SiH4,Si-H,1.434
SiF4,Si-F,1.584
Si(OH)4,Si-O,1.654
Si(OH)4,O-H,0.930
SiO4^4-,Si-O,1.711
Si2O7^6-,Si-O (central),1.769
Si2O7^6-,Si-O (peripheral),1.698
FFEOF

# === solve block: ir_active_frequencies.json ===
cat > "$OUTDIR/ir_active_frequencies.json" <<'FFEOF'
[
  {"molecule": "SiH4", "frequency_cm-1": 2250.0, "relative_intensity": 0.80},
  {"molecule": "SiH4", "frequency_cm-1": 980.0, "relative_intensity": 0.20},
  {"molecule": "SiF4", "frequency_cm-1": 1050.0, "relative_intensity": 0.70},
  {"molecule": "SiF4", "frequency_cm-1": 400.0, "relative_intensity": 0.30},
  {"molecule": "Si(OH)4", "frequency_cm-1": 1067.3, "relative_intensity": 0.50},
  {"molecule": "Si(OH)4", "frequency_cm-1": 1089.1, "relative_intensity": 0.40},
  {"molecule": "Si(OH)4", "frequency_cm-1": 895.4, "relative_intensity": 0.60},
  {"molecule": "Si(OH)4", "frequency_cm-1": 884.8, "relative_intensity": 0.30},
  {"molecule": "Si(OH)4", "frequency_cm-1": 367.2, "relative_intensity": 0.20},
  {"molecule": "Si(OH)4", "frequency_cm-1": 329.4, "relative_intensity": 0.15},
  {"molecule": "SiO4^4-", "frequency_cm-1": 950.0, "relative_intensity": 0.60},
  {"molecule": "SiO4^4-", "frequency_cm-1": 500.0, "relative_intensity": 0.40},
  {"molecule": "Si2O7^6-", "frequency_cm-1": 1100.0, "relative_intensity": 0.80},
  {"molecule": "Si2O7^6-", "frequency_cm-1": 1100.0, "relative_intensity": 0.80},
  {"molecule": "Si2O7^6-", "frequency_cm-1": 600.0, "relative_intensity": 0.40}
]
FFEOF

# === solve finalize ===
echo "All oracle artifacts written."
